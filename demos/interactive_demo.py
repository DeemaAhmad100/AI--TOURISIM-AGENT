#!/usr/bin/env python3
"""
🌍 AI Travel Assistant - Interactive Demo
Demonstration of the travel platform features
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the current directory to the Python path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

def demo_travel_assistant():
    """Demo the travel assistant functionality"""
    print("🌍 AI Travel Assistant Demo")
    print("=" * 40)
    
    try:
        from enhanced_travel_platform import SmartTravelAssistant, UserProfile
        
        print("✅ Successfully imported travel platform modules")
        
        # Create a travel assistant instance
        assistant = SmartTravelAssistant()
        print("✅ Travel assistant initialized")
        
        # Demo user profile
        profile = UserProfile(
            user_id="demo_user_001",
            name="Demo User",
            email="demo@example.com",
            preferences={
                "budget_range": [1000, 3000],
                "preferred_destinations": ["Europe", "Asia"],
                "travel_style": "cultural",
                "accommodation_type": "hotel"
            }
        )
        print("✅ User profile created")
        
        # Demo travel query
        destination = "Paris, France"
        duration = 5
        budget = 2000
        
        print(f"\n🎯 Planning a {duration}-day trip to {destination} with budget ${budget}")
        print("-" * 50)
        
        # Generate travel recommendations
        print("🔍 Generating AI-powered travel recommendations...")
        
        # Simulate the assistant recommendations
        recommendations = {
            "destination_info": {
                "name": "Paris, France",
                "best_time": "April-June, September-October", 
                "weather": "Mild temperatures, perfect for sightseeing",
                "highlights": ["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Champs-Élysées"]
            },
            "suggested_itinerary": [
                {"day": 1, "activities": ["Arrive in Paris", "Check into hotel", "Evening Seine cruise"]},
                {"day": 2, "activities": ["Visit Louvre Museum", "Walk along Champs-Élysées", "Dinner in Montmartre"]},
                {"day": 3, "activities": ["Climb Eiffel Tower", "Explore Latin Quarter", "Visit Notre-Dame"]},
                {"day": 4, "activities": ["Day trip to Versailles", "Return to Paris for shopping"]},
                {"day": 5, "activities": ["Visit Musée d'Orsay", "Last-minute shopping", "Departure"]}
            ],
            "hotels": [
                {"name": "Hotel Le Marais", "price": "$150/night", "rating": 4.2, "location": "Central Paris"},
                {"name": "Boutique Hotel Montparnasse", "price": "$180/night", "rating": 4.5, "location": "Montparnasse"},
                {"name": "Palace Hotel Champs-Élysées", "price": "$280/night", "rating": 4.8, "location": "Champs-Élysées"}
            ],
            "restaurants": [
                {"name": "Le Comptoir du Relais", "cuisine": "French Bistro", "price": "$$", "specialty": "Traditional French"},
                {"name": "L'As du Fallafel", "cuisine": "Middle Eastern", "price": "$", "specialty": "Best falafel in Marais"},
                {"name": "Pierre Hermé", "cuisine": "Pastry", "price": "$", "specialty": "World-famous macarons"}
            ],
            "estimated_costs": {
                "accommodation": "$150-280/night",
                "meals": "$50-100/day",
                "activities": "$30-50/day",
                "total_estimated": f"${budget-300}-{budget+500}"
            }
        }
        
        print("✅ Recommendations generated!")
        
        # Display recommendations
        print(f"\n📍 Destination: {recommendations['destination_info']['name']}")
        print(f"🌤️  Best time to visit: {recommendations['destination_info']['best_time']}")
        print(f"🌡️  Weather: {recommendations['destination_info']['weather']}")
        
        print(f"\n🗺️  Must-see attractions:")
        for highlight in recommendations['destination_info']['highlights']:
            print(f"   • {highlight}")
            
        print(f"\n📅 Suggested {duration}-day itinerary:")
        for day_plan in recommendations['suggested_itinerary']:
            print(f"   Day {day_plan['day']}: {', '.join(day_plan['activities'])}")
            
        print(f"\n🏨 Recommended hotels:")
        for hotel in recommendations['hotels']:
            print(f"   • {hotel['name']} - {hotel['price']} (⭐{hotel['rating']}) in {hotel['location']}")
            
        print(f"\n🍽️  Restaurant recommendations:")
        for restaurant in recommendations['restaurants']:
            print(f"   • {restaurant['name']} - {restaurant['cuisine']} ({restaurant['price']}) - {restaurant['specialty']}")
            
        print(f"\n💰 Estimated costs:")
        for cost_type, amount in recommendations['estimated_costs'].items():
            if cost_type != "total_estimated":
                print(f"   • {cost_type.replace('_', ' ').title()}: {amount}")
        print(f"   • Total estimated: {recommendations['estimated_costs']['total_estimated']}")
        
        print(f"\n🎉 Trip planning complete!")
        print("📝 Additional features available:")
        features = [
            "📄 Generate detailed PDF itinerary",
            "💳 Book hotels and flights",
            "💰 Set up price tracking alerts", 
            "📅 Sync with your calendar",
            "👥 Share with travel companions",
            "🔔 Get real-time notifications"
        ]
        
        for feature in features:
            print(f"   {feature}")
            
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Some modules may not be fully implemented yet.")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 There might be missing dependencies or configuration issues.")

def demo_booking_system():
    """Demo the booking system"""
    print("\n" + "=" * 40)
    print("💳 Booking System Demo")
    print("=" * 40)
    
    try:
        from booking_system.booking_manager import BookingManager
        
        booking_manager = BookingManager()
        print("✅ Booking system initialized")
        
        # Demo booking details
        booking_details = {
            "user_id": "demo_user_001",
            "trip_id": "paris_trip_2025",
            "flights": {
                "outbound": "NYC to CDG - $650",
                "return": "CDG to NYC - $650"
            },
            "hotels": {
                "name": "Hotel Le Marais",
                "nights": 5,
                "price_per_night": 150,
                "total": 750
            },
            "total_amount": 2050,
            "payment_method": "credit_card"
        }
        
        print(f"💼 Processing booking for Paris trip:")
        print(f"   ✈️  Flights: {booking_details['flights']['outbound']}")
        print(f"   🏨 Hotel: {booking_details['hotels']['name']} for {booking_details['hotels']['nights']} nights")
        print(f"   💰 Total amount: ${booking_details['total_amount']}")
        
        print("✅ Booking processed successfully!")
        print("📧 Confirmation email sent")
        print("📱 SMS notification sent")
        
    except ImportError:
        print("💡 Booking system module not fully implemented yet")
    except Exception as e:
        print(f"❌ Booking error: {e}")

def main():
    """Main demo function"""
    print("🚀 Starting AI Travel Platform Demo")
    print("Version: Enhanced Edition")
    print("Date:", "June 29, 2025")
    print()
    
    # Run travel assistant demo
    demo_travel_assistant()
    
    # Run booking system demo  
    demo_booking_system()
    
    print("\n" + "=" * 40)
    print("🎉 Demo completed!")
    print("🌐 To run the full web interface:")
    print("   streamlit run main_app.py")
    print("📱 Access at: http://localhost:8501")
    print("Happy travels! ✈️🌍")

if __name__ == "__main__":
    main()
