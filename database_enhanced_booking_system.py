"""
🎫 Database Enhanced Booking System
Comprehensive booking management system for the AI Travel Platform
Handles flights, hotels, restaurants, car rentals, and travel packages with database integration
"""

import os
import json
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum
import stripe
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class BookingStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    FAILED = "failed"

class BookingType(Enum):
    FLIGHT = "flight"
    HOTEL = "hotel"
    RESTAURANT = "restaurant"
    CAR_RENTAL = "car_rental"
    PACKAGE = "package"

@dataclass
class BookingRequest:
    """Booking request data structure"""
    booking_type: BookingType
    user_id: str
    item_id: str
    details: Dict
    total_amount: float
    currency: str = "USD"
    special_requests: List[str] = None
    group_booking_id: Optional[str] = None

@dataclass
class BookingConfirmation:
    """Booking confirmation data structure"""
    booking_id: str
    confirmation_number: str
    status: BookingStatus
    booking_details: Dict
    payment_details: Dict
    created_at: datetime
    expires_at: Optional[datetime] = None

class DatabaseEnhancedBookingSystem:
    """
    🎫 Comprehensive Database Enhanced Booking System
    
    Features:
    - Multi-service booking (flights, hotels, restaurants, car rentals, packages)
    - Database integration with Supabase
    - Payment processing with Stripe
    - Real-time availability checking
    - Booking modifications and cancellations
    - Automated confirmations and notifications
    """
    
    def __init__(self):
        """Initialize the enhanced booking system"""
        print("🎫 Initializing Database Enhanced Booking System...")
        
        # Initialize Supabase client
        self.supabase = self._init_supabase()
        
        # Initialize Stripe for payments
        self._init_stripe()
        
        print("✅ Database Enhanced Booking System ready!")
    
    def _init_supabase(self) -> Client:
        """Initialize Supabase client"""
        try:
            supabase_url = os.getenv("SUPABASE_URL")
            supabase_key = os.getenv("SUPABASE_KEY")
            
            if not supabase_url or not supabase_key:
                raise ValueError("Supabase credentials missing in .env file")
            
            return create_client(supabase_url, supabase_key)
        except Exception as e:
            print(f"❌ Error initializing Supabase: {e}")
            return None
    
    def _init_stripe(self):
        """Initialize Stripe for payment processing"""
        try:
            stripe_key = os.getenv("STRIPE_SECRET_KEY")
            if stripe_key:
                stripe.api_key = stripe_key
                print("✅ Stripe initialized")
            else:
                print("⚠️ Stripe key not found. Payment features will be limited.")
        except Exception as e:
            print(f"❌ Error initializing Stripe: {e}")

    # === MAIN BOOKING METHODS ===
    
    def create_booking(self, booking_request: BookingRequest) -> BookingConfirmation:
        """Create a new booking in the main bookings table"""
        try:
            # Validate booking request
            validation = self._validate_booking_request(booking_request)
            if not validation["valid"]:
                raise ValueError(validation["error"])
            
            # Check availability
            availability = self._check_availability(booking_request)
            if not availability["available"]:
                raise ValueError(f"Not available: {availability.get('reason', 'Unknown reason')}")
            
            # Calculate final pricing
            pricing = self._calculate_pricing(booking_request)
            
            # Generate unique identifiers
            booking_id = str(uuid.uuid4())
            confirmation_number = self._generate_confirmation_number()
            
            # Prepare booking data
            booking_data = {
                "id": booking_id,
                "confirmation_number": confirmation_number,
                "booking_type": booking_request.booking_type.value,
                "user_id": booking_request.user_id,
                "item_id": booking_request.item_id,
                "total_amount": pricing["final_amount"],
                "currency": booking_request.currency,
                "status": BookingStatus.PENDING.value,
                "payment_status": "pending",
                "details": booking_request.details,
                "pricing_breakdown": pricing,
                "special_requests": booking_request.special_requests or [],
                "group_booking_id": booking_request.group_booking_id,
                "expires_at": (datetime.now() + timedelta(hours=24)).isoformat(),
                "created_at": datetime.now().isoformat()
            }
            
            # Insert into bookings table
            if self.supabase:
                result = self.supabase.table("bookings").insert(booking_data).execute()
                
                if result.data:
                    booking_record = result.data[0]
                    
                    return BookingConfirmation(
                        booking_id=booking_record["id"],
                        confirmation_number=booking_record["confirmation_number"],
                        status=BookingStatus(booking_record["status"]),
                        booking_details=booking_record["details"],
                        payment_details={"status": "pending", "amount": pricing["final_amount"]},
                        created_at=datetime.fromisoformat(booking_record["created_at"])
                    )
                else:
                    raise Exception("Failed to create booking record")
            else:
                # Fallback for demo mode
                return BookingConfirmation(
                    booking_id=booking_id,
                    confirmation_number=confirmation_number,
                    status=BookingStatus.PENDING,
                    booking_details=booking_request.details,
                    payment_details={"status": "pending", "amount": pricing["final_amount"]},
                    created_at=datetime.now()
                )
                
        except Exception as e:
            print(f"❌ Error creating booking: {e}")
            raise

    def process_payment(self, booking_id: str, payment_method_id: str, 
                       customer_details: Dict) -> Dict:
        """Process payment for a booking"""
        try:
            print(f"💳 Processing payment for booking {booking_id}...")
            
            # Get booking details
            booking = self._get_booking_by_id(booking_id)
            if not booking:
                raise ValueError("Booking not found")
            
            if booking["status"] != BookingStatus.PENDING.value:
                raise ValueError(f"Cannot process payment for booking with status: {booking['status']}")
            
            # Create Stripe payment intent
            if stripe.api_key:
                payment_intent = stripe.PaymentIntent.create(
                    amount=int(booking["total_amount"] * 100),  # Convert to cents
                    currency=booking["currency"].lower(),
                    payment_method=payment_method_id,
                    customer=self._get_or_create_stripe_customer(customer_details),
                    confirmation_method='manual',
                    confirm=True,
                    metadata={
                        'booking_id': booking_id,
                        'confirmation_number': booking["confirmation_number"]
                    }
                )
                
                if payment_intent.status == 'succeeded':
                    # Update booking status
                    self._update_booking_status(booking_id, BookingStatus.CONFIRMED)
                    
                    # Send confirmation
                    self._send_booking_confirmation(booking)
                    
                    # Update inventory if needed
                    self._update_inventory(booking)
                    
                    return {
                        "success": True,
                        "payment_intent_id": payment_intent.id,
                        "status": "confirmed",
                        "message": "Payment processed successfully!"
                    }
                else:
                    # Update booking status to failed
                    self._update_booking_status(booking_id, BookingStatus.FAILED)
                    
                    return {
                        "success": False,
                        "status": "failed",
                        "message": "Payment failed. Please try again."
                    }
            else:
                # Demo mode - simulate successful payment
                self._update_booking_status(booking_id, BookingStatus.CONFIRMED)
                return {
                    "success": True,
                    "payment_intent_id": "demo_payment_123",
                    "status": "confirmed",
                    "message": "Payment processed successfully! (Demo Mode)"
                }
                
        except Exception as e:
            print(f"❌ Error processing payment: {e}")
            # Update booking status to failed
            self._update_booking_status(booking_id, BookingStatus.FAILED)
            return {"success": False, "error": str(e)}
    
    def cancel_booking(self, booking_id: str, reason: str = None) -> Dict:
        """Cancel a booking"""
        try:
            print(f"❌ Cancelling booking {booking_id}...")
            
            # Get booking details
            booking = self._get_booking_by_id(booking_id)
            if not booking:
                raise ValueError("Booking not found")
            
            # Check if cancellation is allowed
            if not self._can_cancel_booking(booking):
                raise ValueError("Booking cannot be cancelled at this time")
            
            # Process refund if payment was made
            refund_result = None
            if booking["status"] == BookingStatus.CONFIRMED.value:
                refund_result = self._process_refund(booking, reason)
            
            # Update booking status
            self._update_booking_status(booking_id, BookingStatus.CANCELLED)
            
            # Update inventory
            self._restore_inventory(booking)
            
            # Send cancellation confirmation
            self._send_cancellation_confirmation(booking, reason)
            
            return {
                "success": True,
                "message": "Booking cancelled successfully",
                "refund_details": refund_result
            }
            
        except Exception as e:
            print(f"❌ Error cancelling booking: {e}")
            return {"success": False, "error": str(e)}
    
    # === HOTEL BOOKING ===
    
    def book_hotel(self, user_id: str, hotel_id: str, check_in: str, check_out: str,
                  room_type: str, guests: int, special_requests: List[str] = None) -> BookingConfirmation:
        """Book a hotel"""
        try:
            print(f"🏨 Booking hotel {hotel_id} for user {user_id}...")
            
            # Get hotel details from database
            hotel = self._get_hotel_details(hotel_id)
            if not hotel:
                raise ValueError("Hotel not found")
            
            # Calculate number of nights and total price
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
            nights = (check_out_date - check_in_date).days
            
            if nights <= 0:
                raise ValueError("Check-out date must be after check-in date")
            
            base_price = float(hotel.get("price_per_night", hotel.get("price", 100)))
            total_price = base_price * nights
            
            booking_request = BookingRequest(
                booking_type=BookingType.HOTEL,
                user_id=user_id,
                item_id=hotel_id,
                details={
                    "hotel": hotel,
                    "check_in": check_in,
                    "check_out": check_out,
                    "nights": nights,
                    "room_type": room_type,
                    "guests": guests,
                    "customer_details": {
                        "guest_count": guests,
                        "room_preferences": room_type
                    }
                },
                total_amount=total_price,
                special_requests=special_requests
            )
            
            return self.create_booking(booking_request)
            
        except Exception as e:
            print(f"❌ Error booking hotel: {e}")
            raise
    
    # === RESTAURANT BOOKING ===
    
    def book_restaurant(self, user_id: str, restaurant_id: str, date_time: str,
                       party_size: int, special_requests: List[str] = None) -> BookingConfirmation:
        """Book a restaurant"""
        try:
            print(f"🍽️ Booking restaurant {restaurant_id} for user {user_id}...")
            
            # Get restaurant details
            restaurant = self._get_restaurant_details(restaurant_id)
            if not restaurant:
                raise ValueError("Restaurant not found")
            
            # Restaurant bookings might be free or have a deposit
            deposit_amount = restaurant.get("deposit_per_person", 0) * party_size
            
            booking_request = BookingRequest(
                booking_type=BookingType.RESTAURANT,
                user_id=user_id,
                item_id=restaurant_id,
                details={
                    "restaurant": restaurant,
                    "date_time": date_time,
                    "party_size": party_size,
                    "customer_details": {
                        "party_size": party_size,
                        "dining_preferences": special_requests or []
                    }
                },
                total_amount=deposit_amount,
                special_requests=special_requests
            )
            
            return self.create_booking(booking_request)
            
        except Exception as e:
            print(f"❌ Error booking restaurant: {e}")
            raise
    
    # === PACKAGE BOOKING ===
    
    def book_travel_package(self, user_id: str, package_id: str, travelers: List[Dict],
                          travel_date: str, special_requests: List[str] = None) -> BookingConfirmation:
        """Book a complete travel package"""
        try:
            print(f"📦 Booking travel package {package_id} for user {user_id}...")
            
            # Get package details
            package = self._get_package_details(package_id)
            if not package:
                raise ValueError("Package not found")
            
            # Calculate total price based on number of travelers
            base_price = float(package.get("total_price", package.get("price", 500)))
            total_price = base_price * len(travelers)
            
            booking_request = BookingRequest(
                booking_type=BookingType.PACKAGE,
                user_id=user_id,
                item_id=package_id,
                details={
                    "package": package,
                    "travelers": travelers,
                    "travel_date": travel_date,
                    "total_travelers": len(travelers),
                    "customer_details": {
                        "traveler_count": len(travelers),
                        "travel_preferences": special_requests or []
                    }
                },
                total_amount=total_price,
                special_requests=special_requests
            )
            
            return self.create_booking(booking_request)
            
        except Exception as e:
            print(f"❌ Error booking package: {e}")
            raise
    
    # === BOOKING MANAGEMENT ===
    
    def get_user_bookings(self, user_id: str, status: BookingStatus = None) -> List[Dict]:
        """Get all bookings for a user"""
        try:
            if not self.supabase:
                return []
                
            query = self.supabase.table("bookings").select("*").eq("user_id", user_id)
            
            if status:
                query = query.eq("status", status.value)
            
            result = query.order("created_at", desc=True).execute()
            return result.data
            
        except Exception as e:
            print(f"❌ Error getting user bookings: {e}")
            return []
    
    def get_booking_details(self, booking_id: str) -> Dict:
        """Get detailed booking information"""
        try:
            booking = self._get_booking_by_id(booking_id)
            if not booking:
                return None
            
            # Enhance with additional details based on booking type
            if booking["booking_type"] == BookingType.HOTEL.value:
                booking["hotel_details"] = self._get_hotel_details(booking["item_id"])
            elif booking["booking_type"] == BookingType.RESTAURANT.value:
                booking["restaurant_details"] = self._get_restaurant_details(booking["item_id"])
            elif booking["booking_type"] == BookingType.PACKAGE.value:
                booking["package_details"] = self._get_package_details(booking["item_id"])
            
            return booking
            
        except Exception as e:
            print(f"❌ Error getting booking details: {e}")
            return None
    
    def modify_booking(self, booking_id: str, modifications: Dict) -> Dict:
        """Modify an existing booking"""
        try:
            print(f"✏️ Modifying booking {booking_id}...")
            
            # Get current booking
            booking = self._get_booking_by_id(booking_id)
            if not booking:
                raise ValueError("Booking not found")
            
            # Check if modification is allowed
            if not self._can_modify_booking(booking):
                raise ValueError("Booking cannot be modified at this time")
            
            # Calculate price difference
            price_difference = self._calculate_modification_cost(booking, modifications)
            
            # Update booking details
            updated_details = booking["details"].copy()
            updated_details.update(modifications)
            
            # Update in database
            if self.supabase:
                update_data = {
                    "details": updated_details,
                    "total_amount": booking["total_amount"] + price_difference,
                    "modified_at": datetime.now().isoformat()
                }
                
                self.supabase.table("bookings").update(update_data).eq("id", booking_id).execute()
            
            # Process additional payment if needed
            payment_result = None
            if price_difference > 0:
                payment_result = {"additional_payment_required": price_difference}
            elif price_difference < 0:
                payment_result = {"refund_amount": abs(price_difference)}
            
            return {
                "success": True,
                "message": "Booking modified successfully",
                "price_difference": price_difference,
                "payment_details": payment_result
            }
            
        except Exception as e:
            print(f"❌ Error modifying booking: {e}")
            return {"success": False, "error": str(e)}
    
    # === HELPER METHODS ===
    
    def _validate_booking_request(self, request: BookingRequest) -> Dict:
        """Validate booking request"""
        try:
            # Basic validation
            if not request.user_id:
                return {"valid": False, "error": "User ID is required"}
            
            if not request.item_id:
                return {"valid": False, "error": "Item ID is required"}
            
            if request.total_amount <= 0:
                return {"valid": False, "error": "Amount must be greater than 0"}
            
            # Type-specific validation
            if request.booking_type == BookingType.HOTEL:
                if "check_in" not in request.details or "check_out" not in request.details:
                    return {"valid": False, "error": "Check-in and check-out dates are required for hotel booking"}
            
            return {"valid": True}
            
        except Exception as e:
            return {"valid": False, "error": str(e)}
    
    def _check_availability(self, request: BookingRequest) -> Dict:
        """Check if the requested booking is available"""
        try:
            # This would implement real availability checking
            # For now, assuming everything is available
            return {"available": True}
            
        except Exception as e:
            return {"available": False, "reason": str(e)}
    
    def _calculate_pricing(self, request: BookingRequest) -> Dict:
        """Calculate final pricing including fees and taxes"""
        try:
            base_amount = request.total_amount
            
            # Add service fees (2% of total)
            service_fee = base_amount * 0.02
            
            # Add taxes (varies by booking type)
            tax_rate = {
                BookingType.FLIGHT: 0.08,
                BookingType.HOTEL: 0.12,
                BookingType.RESTAURANT: 0.06,
                BookingType.CAR_RENTAL: 0.10,
                BookingType.PACKAGE: 0.09
            }.get(request.booking_type, 0.08)
            
            tax_amount = base_amount * tax_rate
            final_amount = base_amount + service_fee + tax_amount
            
            return {
                "base_amount": base_amount,
                "service_fee": service_fee,
                "tax_amount": tax_amount,
                "final_amount": final_amount
            }
            
        except Exception as e:
            print(f"❌ Error calculating pricing: {e}")
            return {"final_amount": request.total_amount}
    
    def _generate_confirmation_number(self) -> str:
        """Generate a unique confirmation number"""
        import random
        import string
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    
    def _get_booking_by_id(self, booking_id: str) -> Dict:
        """Get booking by ID"""
        try:
            if not self.supabase:
                return None
                
            result = self.supabase.table("bookings").select("*").eq("id", booking_id).execute()
            return result.data[0] if result.data else None
        except Exception as e:
            print(f"❌ Error getting booking: {e}")
            return None
    
    def _update_booking_status(self, booking_id: str, status: BookingStatus):
        """Update booking status"""
        try:
            if self.supabase:
                self.supabase.table("bookings").update({
                    "status": status.value,
                    "updated_at": datetime.now().isoformat()
                }).eq("id", booking_id).execute()
        except Exception as e:
            print(f"❌ Error updating booking status: {e}")
    
    def _get_hotel_details(self, hotel_id: str) -> Dict:
        """Get hotel details from database"""
        try:
            if not self.supabase:
                return None
                
            result = self.supabase.table("hotels").select("*").eq("id", hotel_id).execute()
            return result.data[0] if result.data else None
        except Exception as e:
            print(f"❌ Error getting hotel details: {e}")
            return None
    
    def _get_restaurant_details(self, restaurant_id: str) -> Dict:
        """Get restaurant details"""
        try:
            if not self.supabase:
                return None
                
            result = self.supabase.table("restaurants").select("*").eq("id", restaurant_id).execute()
            return result.data[0] if result.data else None
        except Exception as e:
            print(f"❌ Error getting restaurant details: {e}")
            return None
    
    def _get_package_details(self, package_id: str) -> Dict:
        """Get package details"""
        try:
            if not self.supabase:
                return None
                
            result = self.supabase.table("travel_packages").select("*").eq("id", package_id).execute()
            return result.data[0] if result.data else None
        except Exception as e:
            print(f"❌ Error getting package details: {e}")
            return None
    
    def _get_or_create_stripe_customer(self, customer_details: Dict) -> str:
        """Get or create Stripe customer"""
        try:
            if not stripe.api_key:
                return None
                
            # Check if customer already exists
            customers = stripe.Customer.list(email=customer_details["email"])
            
            if customers.data:
                return customers.data[0].id
            else:
                # Create new customer
                customer = stripe.Customer.create(
                    email=customer_details["email"],
                    name=customer_details.get("name"),
                    phone=customer_details.get("phone")
                )
                return customer.id
        except Exception as e:
            print(f"❌ Error with Stripe customer: {e}")
            return None
    
    def _send_booking_confirmation(self, booking: Dict):
        """Send booking confirmation email/SMS"""
        try:
            # This would integrate with email/SMS service
            print(f"📧 Sending confirmation for booking {booking['confirmation_number']}")
            # Implementation would go here
        except Exception as e:
            print(f"❌ Error sending confirmation: {e}")
    
    def _send_cancellation_confirmation(self, booking: Dict, reason: str):
        """Send cancellation confirmation"""
        try:
            print(f"📧 Sending cancellation confirmation for booking {booking['confirmation_number']}")
            # Implementation would go here
        except Exception as e:
            print(f"❌ Error sending cancellation confirmation: {e}")
    
    def _update_inventory(self, booking: Dict):
        """Update inventory after booking"""
        try:
            # This would update availability in respective tables
            print(f"📦 Updating inventory for {booking['booking_type']}")
            # Implementation would go here
        except Exception as e:
            print(f"❌ Error updating inventory: {e}")
    
    def _restore_inventory(self, booking: Dict):
        """Restore inventory after cancellation"""
        try:
            print(f"📦 Restoring inventory for {booking['booking_type']}")
            # Implementation would go here
        except Exception as e:
            print(f"❌ Error restoring inventory: {e}")
    
    def _can_cancel_booking(self, booking: Dict) -> bool:
        """Check if booking can be cancelled"""
        try:
            # Basic cancellation policy - can cancel if not within 24 hours of travel
            booking_date = datetime.fromisoformat(booking["created_at"])
            return datetime.now() < booking_date + timedelta(hours=24)
        except Exception as e:
            return False
    
    def _can_modify_booking(self, booking: Dict) -> bool:
        """Check if booking can be modified"""
        return self._can_cancel_booking(booking)  # Same policy for now
    
    def _process_refund(self, booking: Dict, reason: str) -> Dict:
        """Process refund for cancelled booking"""
        try:
            # This would implement actual refund processing
            return {
                "refund_amount": booking["total_amount"],
                "processing_time": "3-5 business days",
                "reason": reason
            }
        except Exception as e:
            return {"error": str(e)}
    
    def _calculate_modification_cost(self, booking: Dict, modifications: Dict) -> float:
        """Calculate cost of modifications"""
        try:
            # This would implement complex modification pricing logic
            return 0.0  # Simplified for now
        except Exception as e:
            return 0.0

# === DEMO FUNCTION ===

def demo_enhanced_booking_system():
    """Demonstrate the enhanced booking system capabilities"""
    print("\n🎫 DATABASE ENHANCED BOOKING SYSTEM DEMO")
    print("=" * 60)
    
    # Initialize booking system
    booking_system = DatabaseEnhancedBookingSystem()
    
    # Demo hotel booking
    print("\n🏨 Demo Hotel Booking...")
    try:
        hotel_booking = booking_system.book_hotel(
            user_id="demo_user_001",
            hotel_id="1",  # Assuming we have hotel with ID 1
            check_in="2025-08-01",
            check_out="2025-08-05",
            room_type="Deluxe",
            guests=2,
            special_requests=["Ocean view", "Late checkout"]
        )
        print(f"✅ Hotel booking created: {hotel_booking.confirmation_number}")
    except Exception as e:
        print(f"⚠️ Hotel booking demo: {e}")
    
    # Demo restaurant booking
    print("\n🍽️ Demo Restaurant Booking...")
    try:
        restaurant_booking = booking_system.book_restaurant(
            user_id="demo_user_001",
            restaurant_id="1",  # Assuming we have restaurant with ID 1
            date_time="2025-08-02 19:30",
            party_size=4,
            special_requests=["Window table", "Anniversary celebration"]
        )
        print(f"✅ Restaurant booking created: {restaurant_booking.confirmation_number}")
    except Exception as e:
        print(f"⚠️ Restaurant booking demo: {e}")
    
    print("✅ Enhanced booking system demo completed!")

if __name__ == "__main__":
    demo_enhanced_booking_system()
