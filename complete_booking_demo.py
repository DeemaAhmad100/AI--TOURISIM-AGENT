#!/usr/bin/env python3
"""
🌍 AI Travel Platform - Complete Booking System Demo
Demonstrates the full end-to-end booking experience with pre-paid packages
"""

import os
import sys
import time
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class UserProfile:
    """User profile for personalized recommendations"""
    user_id: str
    name: str
    age: int
    interests: List[str]
    travel_style: str
    budget_range: str
    dietary_restrictions: List[str]
    accessibility_needs: List[str]
    preferred_airlines: List[str]
    language_preferences: List[str]

@dataclass
class TravelPackage:
    """Complete travel package"""
    package_id: str
    destination: str
    duration: int
    departure_date: str
    return_date: str
    
    # Core Components
    flights: Dict[str, Any]
    hotels: Dict[str, Any]
    restaurants: List[Dict[str, Any]]
    activities: List[Dict[str, Any]]
    transportation: Dict[str, Any]
    
    # Pricing
    total_price: float
    deposit_required: float
    savings: float
    
    # Additional Services
    travel_insurance: Dict[str, Any]
    visa_assistance: bool
    emergency_support: Dict[str, Any]
    travel_guide_pdf: str

def clear_screen():
    """Clear the screen for better presentation"""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_print(text, delay=0.02):
    """Print text with typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_welcome():
    """Show welcome screen"""
    clear_screen()
    print("🌟" * 70)
    print("🌍 AI TRAVEL PLATFORM - COMPLETE BOOKING SYSTEM DEMO")
    print("🌟" * 70)
    print()
    typing_print("Welcome to the future of travel booking! 🚀")
    print()
    print("✨ What makes our packages special:")
    print("• 🎯 100% Personalized based on your profile")
    print("• 💰 Pre-paid all-inclusive packages")
    print("• 🏨 Curated hotels matching your preferences")
    print("• 🍽️ Restaurant recommendations for your taste")
    print("• 🎭 Activities aligned with your interests")
    print("• 🚗 Complete transportation solutions")
    print("• 🛡️ Travel insurance and emergency support")
    print("• 📱 24/7 concierge service")
    print()

def create_user_profile():
    """Simulate user profile creation"""
    print("👤 USER PROFILE CREATION")
    print("=" * 50)
    print()
    
    print("Let's create your personalized travel profile...")
    print()
    
    # Simulate user input
    profile_data = {
        "name": "Sarah Johnson",
        "age": 28,
        "interests": ["culture", "food", "art", "history"],
        "travel_style": "mid-luxury",
        "budget_range": "$3000-5000",
        "dietary_restrictions": ["vegetarian"],
        "accessibility_needs": [],
        "preferred_airlines": ["Emirates", "Qatar Airways"],
        "language_preferences": ["English", "Spanish"]
    }
    
    print("📋 Profile Information:")
    for key, value in profile_data.items():
        if isinstance(value, list):
            value_str = ", ".join(value) if value else "None"
        else:
            value_str = str(value)
        print(f"   • {key.replace('_', ' ').title()}: {value_str}")
    
    print()
    print("✅ Profile created successfully!")
    
    return UserProfile(
        user_id="user_001",
        name=profile_data["name"],
        age=profile_data["age"],
        interests=profile_data["interests"],
        travel_style=profile_data["travel_style"],
        budget_range=profile_data["budget_range"],
        dietary_restrictions=profile_data["dietary_restrictions"],
        accessibility_needs=profile_data["accessibility_needs"],
        preferred_airlines=profile_data["preferred_airlines"],
        language_preferences=profile_data["language_preferences"]
    )

def generate_travel_package(user_profile: UserProfile):
    """Generate a comprehensive travel package"""
    print("🤖 AI PACKAGE GENERATION")
    print("=" * 50)
    print()
    
    print("🎯 Analyzing your preferences...")
    time.sleep(1)
    print("🔍 Searching best flights...")
    time.sleep(1)
    print("🏨 Finding perfect hotels...")
    time.sleep(1)
    print("🍽️ Curating restaurant recommendations...")
    time.sleep(1)
    print("🎭 Planning exciting activities...")
    time.sleep(1)
    print("📋 Optimizing itinerary...")
    time.sleep(1)
    
    print()
    typing_print("✨ Your personalized package is ready!")
    print()
    
    # Create sample package
    package = TravelPackage(
        package_id="PKG_001_ROME_7D",
        destination="Rome, Italy",
        duration=7,
        departure_date="2025-09-15",
        return_date="2025-09-22",
        
        flights={
            "outbound": {
                "airline": "Emirates",
                "flight_number": "EK91",
                "departure": "2025-09-15 14:30",
                "arrival": "2025-09-15 20:45",
                "class": "Business",
                "price": 2100
            },
            "return": {
                "airline": "Emirates", 
                "flight_number": "EK92",
                "departure": "2025-09-22 10:15",
                "arrival": "2025-09-22 18:30",
                "class": "Business",
                "price": 2100
            }
        },
        
        hotels={
            "name": "Hotel Artemide",
            "location": "Via Nazionale, Rome",
            "category": "4-star boutique",
            "room_type": "Superior Double Room",
            "nights": 7,
            "price_per_night": 180,
            "total_price": 1260,
            "amenities": ["Free WiFi", "Breakfast included", "Rooftop terrace", "Spa"]
        },
        
        restaurants=[
            {
                "name": "La Pergola",
                "cuisine": "Italian Fine Dining",
                "michelin_stars": 3,
                "specialties": ["Vegetarian tasting menu", "Roman classics"],
                "reservation": "Included in package"
            },
            {
                "name": "Checchino dal 1887",
                "cuisine": "Traditional Roman",
                "specialties": ["Vegetarian Roman dishes", "Historic atmosphere"],
                "reservation": "Included in package"
            },
            {
                "name": "Glass Hostaria",
                "cuisine": "Modern Italian",
                "specialties": ["Creative vegetarian options", "Wine pairings"],
                "reservation": "Included in package"
            }
        ],
        
        activities=[
            {
                "day": 1,
                "activity": "Vatican Museums & Sistine Chapel",
                "type": "Cultural/Art",
                "duration": "4 hours",
                "included": "Skip-the-line tickets + expert guide"
            },
            {
                "day": 2,
                "activity": "Colosseum & Roman Forum",
                "type": "Historical",
                "duration": "3 hours", 
                "included": "VIP access + historian guide"
            },
            {
                "day": 3,
                "activity": "Cooking Class in Trastevere",
                "type": "Culinary/Cultural",
                "duration": "4 hours",
                "included": "Vegetarian menu + market tour"
            },
            {
                "day": 4,
                "activity": "Villa Borghese & Galleria Borghese",
                "type": "Art/Nature",
                "duration": "Half day",
                "included": "Gallery tickets + park bike rental"
            }
        ],
        
        transportation={
            "airport_transfers": "Private luxury car",
            "city_transport": "7-day Roma Pass",
            "inter_city": "High-speed train to Florence (day trip)",
            "total_cost": 450
        },
        
        total_price=4500,
        deposit_required=900,  # 20%
        savings=650,
        
        travel_insurance={
            "provider": "AIG Travel Guard",
            "coverage": "Comprehensive",
            "medical_limit": "$100,000",
            "cancellation": "100% coverage",
            "cost": "Included"
        },
        
        visa_assistance=True,
        
        emergency_support={
            "24_7_hotline": "+1-800-TRAVEL",
            "local_contact": "+39-06-1234-5678",
            "concierge_service": "Available via app",
            "medical_assistance": "Included"
        },
        
        travel_guide_pdf="rome_personalized_guide.pdf"
    )
    
    return package

def display_package_details(package: TravelPackage):
    """Display complete package details"""
    print("📦 YOUR COMPLETE TRAVEL PACKAGE")
    print("=" * 60)
    print()
    
    # Header
    print(f"🌍 Destination: {package.destination}")
    print(f"📅 Duration: {package.duration} days ({package.departure_date} to {package.return_date})")
    print(f"💰 Total Price: ${package.total_price:,}")
    print(f"💵 Deposit Required: ${package.deposit_required:,} (remaining ${package.total_price - package.deposit_required:,})")
    print(f"🎉 You Save: ${package.savings:,} compared to booking separately!")
    print()
    
    # Flights
    print("✈️ FLIGHTS (Business Class)")
    print("-" * 30)
    outbound = package.flights["outbound"]
    return_flight = package.flights["return"]
    print(f"🛫 Outbound: {outbound['airline']} {outbound['flight_number']}")
    print(f"   Departure: {outbound['departure']}")
    print(f"   Arrival: {outbound['arrival']}")
    print(f"🛬 Return: {return_flight['airline']} {return_flight['flight_number']}")
    print(f"   Departure: {return_flight['departure']}")
    print(f"   Arrival: {return_flight['arrival']}")
    print(f"💰 Flight Total: ${outbound['price'] + return_flight['price']:,}")
    print()
    
    # Hotels
    print("🏨 ACCOMMODATION")
    print("-" * 30)
    hotel = package.hotels
    print(f"🏛️ Hotel: {hotel['name']}")
    print(f"📍 Location: {hotel['location']}")
    print(f"⭐ Category: {hotel['category']}")
    print(f"🛏️ Room: {hotel['room_type']}")
    print(f"🌙 Nights: {hotel['nights']} nights")
    print(f"💰 Hotel Total: ${hotel['total_price']:,} (${hotel['price_per_night']}/night)")
    print(f"🎁 Amenities: {', '.join(hotel['amenities'])}")
    print()
    
    # Restaurants
    print("🍽️ CURATED DINING EXPERIENCES")
    print("-" * 30)
    for restaurant in package.restaurants:
        stars = "⭐" * restaurant.get('michelin_stars', 0)
        print(f"🍴 {restaurant['name']} {stars}")
        print(f"   Cuisine: {restaurant['cuisine']}")
        print(f"   Specialties: {', '.join(restaurant['specialties'])}")
        print(f"   Status: {restaurant['reservation']}")
        print()
    
    # Activities
    print("🎭 PLANNED ACTIVITIES & EXPERIENCES")
    print("-" * 30)
    for activity in package.activities:
        print(f"📅 Day {activity['day']}: {activity['activity']}")
        print(f"   Type: {activity['type']} | Duration: {activity['duration']}")
        print(f"   Included: {activity['included']}")
        print()
    
    # Transportation
    print("🚗 TRANSPORTATION")
    print("-" * 30)
    transport = package.transportation
    print(f"🚖 Airport Transfers: {transport['airport_transfers']}")
    print(f"🚇 City Transport: {transport['city_transport']}")
    print(f"🚄 Inter-city Travel: {transport['inter_city']}")
    print(f"💰 Transport Total: ${transport['total_cost']:,}")
    print()
    
    # Additional Services
    print("🛡️ ADDITIONAL SERVICES INCLUDED")
    print("-" * 30)
    insurance = package.travel_insurance
    emergency = package.emergency_support
    print(f"🛡️ Travel Insurance: {insurance['provider']} - {insurance['coverage']}")
    print(f"   Medical Coverage: {insurance['medical_limit']}")
    print(f"   Cancellation: {insurance['cancellation']}")
    print(f"📋 Visa Assistance: {'✅ Included' if package.visa_assistance else '❌ Not needed'}")
    print(f"🆘 24/7 Emergency Support: {emergency['24_7_hotline']}")
    print(f"📱 Concierge Service: {emergency['concierge_service']}")
    print(f"📖 Personalized Travel Guide: {package.travel_guide_pdf}")
    print()

def simulate_booking_process(package: TravelPackage):
    """Simulate the booking and payment process"""
    print("💳 BOOKING & PAYMENT PROCESS")
    print("=" * 50)
    print()
    
    print("🔒 Secure Payment Processing...")
    print()
    
    # Payment options
    print("💰 PAYMENT OPTIONS:")
    print("1. 💳 Pay Full Amount: $4,500 (5% discount = $4,275)")
    print("2. 📊 Payment Plan: $900 deposit + 3 monthly payments of $1,200")
    print("3. 🏦 Bank Transfer: $4,500 (2% discount = $4,410)")
    print()
    
    print("Selected: Option 1 - Pay Full Amount with 5% discount")
    print("Final Amount: $4,275")
    print()
    
    # Simulate payment processing
    print("Processing payment...")
    time.sleep(2)
    print("✅ Payment successful!")
    print()
    
    # Booking confirmation
    booking_id = f"BK{datetime.now().strftime('%Y%m%d%H%M%S')}"
    print("📧 BOOKING CONFIRMATION")
    print("-" * 30)
    print(f"🎫 Booking ID: {booking_id}")
    print(f"📅 Booking Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"👤 Traveler: Sarah Johnson")
    print(f"🌍 Destination: {package.destination}")
    print(f"📊 Status: CONFIRMED & PAID")
    print()
    
    print("📱 WHAT HAPPENS NEXT:")
    print("• Flight tickets will be issued within 24 hours")
    print("• Hotel confirmation sent to your email")
    print("• Restaurant reservations confirmed")
    print("• Activity tickets delivered to your app")
    print("• Personalized travel guide emailed within 48 hours")
    print("• Travel insurance policy documents sent")
    print("• Pre-departure checklist sent 2 weeks before travel")
    print()
    
    return booking_id

def show_post_booking_services():
    """Show post-booking services"""
    print("🎯 POST-BOOKING SERVICES")
    print("=" * 50)
    print()
    
    print("📱 YOUR TRAVEL APP FEATURES:")
    print("• Real-time flight updates")
    print("• Digital itinerary with maps")
    print("• Instant chat with local concierge")
    print("• Restaurant reservation management")
    print("• Activity ticket storage")
    print("• Emergency contact buttons")
    print("• Local recommendations based on your location")
    print("• Photo sharing with your travel group")
    print()
    
    print("🔔 AUTOMATIC NOTIFICATIONS:")
    print("• Flight check-in reminders")
    print("• Weather updates for your destination")
    print("• Local event notifications")
    print("• Restaurant reservation reminders")
    print("• Activity meeting point alerts")
    print("• Transportation pickup notifications")
    print()
    
    print("🛠️ MODIFICATION OPTIONS:")
    print("• Change dates (subject to availability)")
    print("• Upgrade flights or hotels")
    print("• Add extra activities")
    print("• Extend your stay")
    print("• Add travel companions")
    print("• Request special arrangements")
    print()

def main():
    """Main demo function"""
    try:
        show_welcome()
        input("Press Enter to start the complete booking demo...")
        
        while True:
            clear_screen()
            print("🎮 AI TRAVEL PLATFORM - COMPLETE BOOKING DEMO")
            print("=" * 60)
            print("Experience the full end-to-end booking process:")
            print()
            print("1. 👤 Create User Profile")
            print("2. 🤖 Generate AI Travel Package")
            print("3. 📦 View Complete Package Details")
            print("4. 💳 Complete Booking & Payment")
            print("5. 🎯 Post-Booking Services")
            print("6. 🎪 Full Demo (All Steps)")
            print("7. 🚪 Exit")
            print()
            
            choice = input("Select option (1-7): ").strip()
            
            clear_screen()
            
            if choice == '1':
                user_profile = create_user_profile()
                input("\nPress Enter to continue...")
                
            elif choice == '2':
                if 'user_profile' not in locals():
                    user_profile = create_user_profile()
                    print()
                package = generate_travel_package(user_profile)
                input("\nPress Enter to continue...")
                
            elif choice == '3':
                if 'package' not in locals():
                    if 'user_profile' not in locals():
                        user_profile = create_user_profile()
                        print()
                    package = generate_travel_package(user_profile)
                    print()
                display_package_details(package)
                input("\nPress Enter to continue...")
                
            elif choice == '4':
                if 'package' not in locals():
                    if 'user_profile' not in locals():
                        user_profile = create_user_profile()
                        print()
                    package = generate_travel_package(user_profile)
                    print()
                booking_id = simulate_booking_process(package)
                input("\nPress Enter to continue...")
                
            elif choice == '5':
                show_post_booking_services()
                input("\nPress Enter to continue...")
                
            elif choice == '6':
                # Full demo
                user_profile = create_user_profile()
                input("\nPress Enter to continue...")
                clear_screen()
                
                package = generate_travel_package(user_profile)
                input("\nPress Enter to continue...")
                clear_screen()
                
                display_package_details(package)
                input("\nPress Enter to continue...")
                clear_screen()
                
                booking_id = simulate_booking_process(package)
                input("\nPress Enter to continue...")
                clear_screen()
                
                show_post_booking_services()
                input("\nPress Enter to continue...")
                
            elif choice == '7':
                clear_screen()
                print("🌟" * 60)
                print("Thank you for exploring the AI Travel Platform!")
                print("🌟" * 60)
                print()
                print("🚀 Ready to start your real booking?")
                print("• Web Interface: streamlit run ui/streamlit_ui.py")
                print("• Full Platform: python src/core/platform_core.py")
                print("• Setup Guide: python interactive_setup.py")
                print()
                print("🌍 Your next adventure awaits! ✈️")
                break
            else:
                print("❌ Invalid option. Please try again.")
                time.sleep(2)
                continue
            
    except KeyboardInterrupt:
        print("\n\n👋 Demo ended. Thanks for exploring the AI Travel Platform!")
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
        print("The platform is ready for use!")

if __name__ == "__main__":
    main()
