"""
🛠️ Booking Tools for CrewAI Agents
Specialized booking tools for flight, hotel, restaurant, and car rental bookings
"""

import sys
import os
from pathlib import Path

# Add the project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

try:
    from crewai import tool
except ImportError:
    def tool(name=None, description=None):
        def decorator(func):
            func._tool_name = name or func.__name__
            func._tool_description = description or func.__doc__
            return func
        return decorator

import json
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv

# Import booking system components
try:
    from src.booking_system.booking_manager import (
        BookingManager, BookingRequest, BookingType, BookingStatus
    )
    BOOKING_SYSTEM_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Booking system not available: {e}")
    BOOKING_SYSTEM_AVAILABLE = False

load_dotenv()

# Initialize booking manager
if BOOKING_SYSTEM_AVAILABLE:
    booking_manager = BookingManager()
else:
    booking_manager = None

@tool
def create_booking_tool(booking_data: str) -> str:
    """
    Create a new booking for flights, hotels, restaurants, or car rentals.
    
    Args:
        booking_data (str): JSON string containing booking details:
            {
                "booking_type": "flight|hotel|restaurant|car_rental",
                "user_id": "user_identifier",
                "item_id": "item_to_book",
                "details": {
                    "dates": "travel_dates",
                    "guests": "number_of_guests",
                    "preferences": "special_preferences"
                },
                "total_amount": 150.00,
                "currency": "USD",
                "special_requests": ["vegetarian_meal", "window_seat"]
            }
        
    Returns:
        str: Booking confirmation details or error message
    """
    if not booking_manager:
        return "❌ Booking system not available. Please check configuration."
    
    try:
        # Parse booking data
        booking_info = json.loads(booking_data)
        
        # Validate required fields
        required_fields = ["booking_type", "user_id", "item_id", "details", "total_amount"]
        for field in required_fields:
            if field not in booking_info:
                return f"❌ Missing required field: {field}"
        
        # Create booking request
        booking_request = BookingRequest(
            booking_type=BookingType(booking_info["booking_type"]),
            user_id=booking_info["user_id"],
            item_id=booking_info["item_id"],
            details=booking_info["details"],
            total_amount=float(booking_info["total_amount"]),
            currency=booking_info.get("currency", "USD"),
            special_requests=booking_info.get("special_requests", []),
            group_booking_id=booking_info.get("group_booking_id")
        )
        
        # Create booking
        result = booking_manager.create_booking(booking_request)
        
        if result.success:
            return f"✅ Booking created successfully!\n" \
                   f"Booking ID: {result.booking_id}\n" \
                   f"Confirmation Number: {result.confirmation_number}\n" \
                   f"Status: {result.status}\n" \
                   f"Total Amount: ${result.total_amount} {result.currency}"
        else:
            return f"❌ Booking failed: {result.error_message}"
            
    except json.JSONDecodeError:
        return "❌ Invalid JSON format in booking data"
    except ValueError as e:
        return f"❌ Invalid booking type: {e}"
    except Exception as e:
        return f"❌ Booking creation failed: {str(e)}"

@tool
def payment_processing_tool(payment_data: str) -> str:
    """
    Process payment for a booking using Stripe or other payment methods.
    
    Args:
        payment_data (str): JSON string containing payment details:
            {
                "booking_id": "booking_identifier",
                "payment_method": "card|paypal|apple_pay",
                "amount": 150.00,
                "currency": "USD",
                "customer_info": {
                    "name": "John Doe",
                    "email": "john@example.com"
                },
                "payment_details": {
                    "card_token": "stripe_card_token"
                }
            }
        
    Returns:
        str: Payment confirmation details or error message
    """
    if not booking_manager:
        return "❌ Payment system not available. Please check configuration."
    
    try:
        # Parse payment data
        payment_info = json.loads(payment_data)
        
        # Validate required fields
        required_fields = ["booking_id", "payment_method", "amount"]
        for field in required_fields:
            if field not in payment_info:
                return f"❌ Missing required field: {field}"
        
        # Process payment
        result = booking_manager.process_payment(
            booking_id=payment_info["booking_id"],
            payment_method=payment_info["payment_method"],
            amount=float(payment_info["amount"]),
            currency=payment_info.get("currency", "USD"),
            customer_info=payment_info.get("customer_info", {}),
            payment_details=payment_info.get("payment_details", {})
        )
        
        if result.success:
            return f"✅ Payment processed successfully!\n" \
                   f"Payment ID: {result.payment_id}\n" \
                   f"Transaction ID: {result.transaction_id}\n" \
                   f"Amount: ${result.amount} {result.currency}\n" \
                   f"Status: {result.status}"
        else:
            return f"❌ Payment failed: {result.error_message}"
            
    except json.JSONDecodeError:
        return "❌ Invalid JSON format in payment data"
    except Exception as e:
        return f"❌ Payment processing failed: {str(e)}"

@tool
def booking_confirmation_tool(booking_id: str) -> str:
    """
    Send booking confirmation to customer via email and SMS.
    
    Args:
        booking_id (str): Unique booking identifier
        
    Returns:
        str: Confirmation status and details
    """
    if not booking_manager:
        return "❌ Booking system not available. Please check configuration."
    
    try:
        # Get booking details
        booking = booking_manager.get_booking(booking_id)
        
        if not booking:
            return f"❌ Booking not found: {booking_id}"
        
        # Send confirmation
        result = booking_manager.send_confirmation(booking_id)
        
        if result.success:
            return f"✅ Confirmation sent successfully!\n" \
                   f"Booking ID: {booking_id}\n" \
                   f"Confirmation Number: {booking.confirmation_number}\n" \
                   f"Email sent to: {booking.customer_email}\n" \
                   f"SMS sent to: {booking.customer_phone}\n" \
                   f"Confirmation details: {booking.details}"
        else:
            return f"❌ Confirmation failed: {result.error_message}"
            
    except Exception as e:
        return f"❌ Confirmation processing failed: {str(e)}"

@tool
def cancellation_tool(cancellation_data: str) -> str:
    """
    Cancel an existing booking and process refund if applicable.
    
    Args:
        cancellation_data (str): JSON string containing cancellation details:
            {
                "booking_id": "booking_identifier",
                "reason": "customer_request|weather|emergency",
                "refund_requested": true,
                "cancellation_fee_accepted": true
            }
        
    Returns:
        str: Cancellation confirmation and refund details
    """
    if not booking_manager:
        return "❌ Booking system not available. Please check configuration."
    
    try:
        # Parse cancellation data
        cancellation_info = json.loads(cancellation_data)
        
        # Validate required fields
        if "booking_id" not in cancellation_info:
            return "❌ Missing required field: booking_id"
        
        booking_id = cancellation_info["booking_id"]
        reason = cancellation_info.get("reason", "customer_request")
        refund_requested = cancellation_info.get("refund_requested", False)
        
        # Get booking details first
        booking = booking_manager.get_booking(booking_id)
        
        if not booking:
            return f"❌ Booking not found: {booking_id}"
        
        if booking.status == BookingStatus.CANCELLED:
            return f"❌ Booking already cancelled: {booking_id}"
        
        # Process cancellation
        result = booking_manager.cancel_booking(
            booking_id=booking_id,
            reason=reason,
            refund_requested=refund_requested
        )
        
        if result.success:
            refund_info = ""
            if refund_requested and result.refund_amount:
                refund_info = f"\n💰 Refund processed: ${result.refund_amount} {result.currency}"
                if result.cancellation_fee:
                    refund_info += f"\n⚠️ Cancellation fee: ${result.cancellation_fee}"
            
            return f"✅ Booking cancelled successfully!\n" \
                   f"Booking ID: {booking_id}\n" \
                   f"Cancellation Number: {result.cancellation_number}\n" \
                   f"Reason: {reason}\n" \
                   f"Status: CANCELLED{refund_info}"
        else:
            return f"❌ Cancellation failed: {result.error_message}"
            
    except json.JSONDecodeError:
        return "❌ Invalid JSON format in cancellation data"
    except Exception as e:
        return f"❌ Cancellation processing failed: {str(e)}"

@tool
def get_booking_status_tool(booking_id: str) -> str:
    """
    Get current status and details of a booking.
    
    Args:
        booking_id (str): Unique booking identifier
        
    Returns:
        str: Current booking status and details
    """
    if not booking_manager:
        return "❌ Booking system not available. Please check configuration."
    
    try:
        booking = booking_manager.get_booking(booking_id)
        
        if not booking:
            return f"❌ Booking not found: {booking_id}"
        
        return f"📋 Booking Status:\n" \
               f"Booking ID: {booking_id}\n" \
               f"Confirmation Number: {booking.confirmation_number}\n" \
               f"Type: {booking.booking_type.value}\n" \
               f"Status: {booking.status.value}\n" \
               f"Total Amount: ${booking.total_amount} {booking.currency}\n" \
               f"Created: {booking.created_at}\n" \
               f"Details: {json.dumps(booking.details, indent=2)}"
        
    except Exception as e:
        return f"❌ Status check failed: {str(e)}"

@tool
def modify_booking_tool(modification_data: str) -> str:
    """
    Modify an existing booking (dates, preferences, etc.).
    
    Args:
        modification_data (str): JSON string containing modification details:
            {
                "booking_id": "booking_identifier",
                "modifications": {
                    "dates": "new_dates",
                    "guests": "new_guest_count",
                    "preferences": "new_preferences"
                },
                "price_difference": 25.00
            }
        
    Returns:
        str: Modification confirmation and any price changes
    """
    if not booking_manager:
        return "❌ Booking system not available. Please check configuration."
    
    try:
        # Parse modification data
        modification_info = json.loads(modification_data)
        
        # Validate required fields
        required_fields = ["booking_id", "modifications"]
        for field in required_fields:
            if field not in modification_info:
                return f"❌ Missing required field: {field}"
        
        booking_id = modification_info["booking_id"]
        modifications = modification_info["modifications"]
        price_difference = modification_info.get("price_difference", 0.0)
        
        # Process modification
        result = booking_manager.modify_booking(
            booking_id=booking_id,
            modifications=modifications,
            price_difference=price_difference
        )
        
        if result.success:
            price_info = ""
            if price_difference != 0:
                if price_difference > 0:
                    price_info = f"\n💰 Additional charge: ${price_difference}"
                else:
                    price_info = f"\n💰 Refund: ${abs(price_difference)}"
            
            return f"✅ Booking modified successfully!\n" \
                   f"Booking ID: {booking_id}\n" \
                   f"Modification ID: {result.modification_id}\n" \
                   f"Changes: {json.dumps(modifications, indent=2)}{price_info}"
        else:
            return f"❌ Modification failed: {result.error_message}"
            
    except json.JSONDecodeError:
        return "❌ Invalid JSON format in modification data"
    except Exception as e:
        return f"❌ Modification processing failed: {str(e)}"

# Export all booking tools
def get_booking_tools():
    """Get all available booking tools"""
    return [
        create_booking_tool,
        payment_processing_tool,
        booking_confirmation_tool,
        cancellation_tool,
        get_booking_status_tool,
        modify_booking_tool
    ]

# Tool availability status
def check_booking_tools_availability():
    """Check if booking tools are available"""
    return {
        "booking_system": BOOKING_SYSTEM_AVAILABLE,
        "tools_count": len(get_booking_tools()),
        "status": "✅ Available" if BOOKING_SYSTEM_AVAILABLE else "❌ Not Available"
    }

__all__ = [
    "create_booking_tool",
    "payment_processing_tool", 
    "booking_confirmation_tool",
    "cancellation_tool",
    "get_booking_status_tool",
    "modify_booking_tool",
    "get_booking_tools",
    "check_booking_tools_availability"
]
