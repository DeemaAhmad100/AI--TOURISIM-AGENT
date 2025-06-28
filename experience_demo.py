#!/usr/bin/env python3
"""
🌍 AI Travel Platform - Live Experience Demo
Interactive experience with real AI travel planning
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import json
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

# Add the current directory to the Python path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

def get_user_input():
    """Get travel preferences from user"""
    print("\n🎯 Let's plan your dream trip!")
    print("=" * 40)
    
    destination = input("🌍 Where would you like to go? (e.g., Tokyo, Paris, New York): ").strip()
    
    try:
        duration = int(input("📅 How many days? (e.g., 5): ").strip())
    except ValueError:
        duration = 5
        print(f"Using default duration: {duration} days")
    
    try:
        budget = int(input("💰 What's your budget in USD? (e.g., 2000): ").strip())
    except ValueError:
        budget = 2000
        print(f"Using default budget: ${budget}")
    
    travel_style = input("🎨 Travel style? (adventure/cultural/relaxation/luxury) [cultural]: ").strip().lower()
    if not travel_style:
        travel_style = "cultural"
    
    group_size = input("👥 How many travelers? (e.g., 2) [1]: ").strip()
    try:
        group_size = int(group_size) if group_size else 1
    except ValueError:
        group_size = 1
    
    return {
        "destination": destination,
        "duration": duration,
        "budget": budget,
        "travel_style": travel_style,
        "group_size": group_size
    }

def generate_ai_travel_plan(preferences):
    """Generate AI-powered travel plan"""
    print(f"\n🤖 AI is planning your {preferences['duration']}-day trip to {preferences['destination']}...")
    print("🔄 This may take a moment...")
    
    try:
        from enhanced_travel_platform import SmartTravelAssistant
        
        # Initialize the AI assistant
        assistant = SmartTravelAssistant()
        
        # Create travel query
        query = f"""
        Plan a {preferences['duration']}-day {preferences['travel_style']} trip to {preferences['destination']} 
        for {preferences['group_size']} traveler(s) with a budget of ${preferences['budget']}.
        
        Include:
        - Best time to visit
        - Must-see attractions
        - Day-by-day itinerary
        - Hotel recommendations with prices
        - Restaurant suggestions
        - Transportation options
        - Budget breakdown
        - Local tips and cultural insights
        """
        
        # Get AI recommendations (this will use the real AI)
        plan = assistant.plan_trip(
            destination=preferences['destination'],
            duration=preferences['duration'],
            budget=preferences['budget'],
            preferences={
                "travel_style": preferences['travel_style'],
                "group_size": preferences['group_size']
            }
        )
        
        return plan
        
    except Exception as e:
        print(f"⚠️ AI planning encountered an issue: {e}")
        print("🔄 Generating simulated plan...")
        
        # Fallback simulated plan
        return generate_simulated_plan(preferences)

def generate_simulated_plan(preferences):
    """Generate a realistic simulated travel plan"""
    dest = preferences['destination']
    days = preferences['duration']
    budget = preferences['budget']
    style = preferences['travel_style']
    
    # Simulated AI response
    plan = {
        "destination": dest,
        "duration": days,
        "travel_style": style,
        "best_time": "Spring and Fall for most destinations",
        "overview": f"A carefully curated {days}-day {style} experience in {dest}",
        "daily_itinerary": [],
        "hotels": [
            {
                "name": f"Premium Hotel {dest}",
                "rating": 4.5,
                "price_per_night": budget // days // 2,
                "amenities": ["WiFi", "Breakfast", "Gym", "Pool"]
            },
            {
                "name": f"Boutique Inn {dest}",
                "rating": 4.2,
                "price_per_night": (budget // days // 2) - 50,
                "amenities": ["WiFi", "Local Character", "Central Location"]
            }
        ],
        "restaurants": [
            {
                "name": f"Local Cuisine House",
                "type": "Traditional",
                "price_range": "$$",
                "specialty": f"Authentic {dest} flavors"
            },
            {
                "name": f"Modern Bistro",
                "type": "Contemporary",
                "price_range": "$$$",
                "specialty": "Fusion cuisine"
            }
        ],
        "budget_breakdown": {
            "accommodation": budget * 0.4,
            "food": budget * 0.3,
            "activities": budget * 0.2,
            "transportation": budget * 0.1
        },
        "local_tips": [
            f"Best way to get around {dest} is usually public transport",
            "Try local markets for authentic food experiences",
            "Book popular attractions in advance",
            "Learn a few basic phrases in the local language"
        ]
    }
    
    # Generate daily itinerary
    sample_activities = [
        "Explore historic city center",
        "Visit famous landmarks",
        "Museum and cultural sites",
        "Local market tour",
        "Walking tour of neighborhoods",
        "Day trip to nearby attractions",
        "Shopping and souvenirs",
        "Sunset viewing point"
    ]
    
    for day in range(1, days + 1):
        activities = sample_activities[:3] if day <= len(sample_activities) else sample_activities[-3:]
        plan["daily_itinerary"].append({
            "day": day,
            "theme": f"Day {day} - {style.title()} Experience",
            "activities": activities
        })
    
    return plan

def display_travel_plan(plan, preferences):
    """Display the travel plan in a beautiful format"""
    print("\n" + "=" * 60)
    print("🎉 YOUR PERSONALIZED TRAVEL PLAN")
    print("=" * 60)
    
    print(f"\n📍 DESTINATION: {plan.get('destination', preferences['destination'])}")
    print(f"📅 DURATION: {plan.get('duration', preferences['duration'])} days")
    print(f"💰 BUDGET: ${preferences['budget']}")
    print(f"🎨 STYLE: {plan.get('travel_style', preferences['travel_style']).title()}")
    
    if 'overview' in plan:
        print(f"\n📝 OVERVIEW:")
        print(f"   {plan['overview']}")
    
    if 'best_time' in plan:
        print(f"\n🌤️ BEST TIME TO VISIT:")
        print(f"   {plan['best_time']}")
    
    # Daily Itinerary
    if 'daily_itinerary' in plan:
        print(f"\n📅 DAILY ITINERARY:")
        print("-" * 40)
        for day_plan in plan['daily_itinerary']:
            theme = day_plan.get('theme', f'Day {day_plan["day"]}')
            print(f"\n   Day {day_plan['day']}: {theme}")
            for activity in day_plan.get('activities', []):
                print(f"      • {activity}")
    
    # Hotels
    if 'hotels' in plan:
        print(f"\n🏨 RECOMMENDED HOTELS:")
        print("-" * 40)
        for hotel in plan['hotels']:
            print(f"   • {hotel['name']} (⭐{hotel['rating']})")
            print(f"     ${hotel['price_per_night']}/night")
            print(f"     Amenities: {', '.join(hotel['amenities'])}")
            print()
    
    # Restaurants
    if 'restaurants' in plan:
        print(f"🍽️ RESTAURANT RECOMMENDATIONS:")
        print("-" * 40)
        for restaurant in plan['restaurants']:
            print(f"   • {restaurant['name']} ({restaurant['price_range']})")
            print(f"     {restaurant['type']} - {restaurant['specialty']}")
            print()
    
    # Budget Breakdown
    if 'budget_breakdown' in plan:
        print(f"💰 BUDGET BREAKDOWN:")
        print("-" * 40)
        for category, amount in plan['budget_breakdown'].items():
            percentage = (amount / preferences['budget']) * 100
            print(f"   • {category.title()}: ${amount:.0f} ({percentage:.0f}%)")
    
    # Local Tips
    if 'local_tips' in plan:
        print(f"\n💡 LOCAL TIPS:")
        print("-" * 40)
        for tip in plan['local_tips']:
            print(f"   • {tip}")
    
    print("\n" + "=" * 60)

def demonstrate_booking():
    """Demonstrate the booking functionality"""
    print("\n💳 BOOKING DEMONSTRATION")
    print("=" * 40)
    
    choice = input("\nWould you like to see the booking process? (y/n) [n]: ").strip().lower()
    
    if choice == 'y':
        try:
            from booking_system.booking_manager import BookingManager
            
            booking_manager = BookingManager()
            
            print("✅ Booking system initialized")
            print("🔄 Processing mock booking...")
            
            # Simulate booking process
            booking_details = {
                "user_id": f"user_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "trip_id": f"trip_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "status": "confirmed",
                "total_amount": 1500.00,
                "currency": "USD"
            }
            
            print(f"📝 Booking ID: {booking_details['trip_id']}")
            print(f"👤 User ID: {booking_details['user_id']}")
            print(f"💰 Total: ${booking_details['total_amount']}")
            print(f"✅ Status: {booking_details['status'].title()}")
            
            print("\n📧 Confirmation email would be sent")
            print("📱 SMS notification would be sent")
            print("📄 PDF itinerary would be generated")
            
        except Exception as e:
            print(f"⚠️ Booking demo error: {e}")
            print("💡 This is normal - some features require additional setup")

def main():
    """Main experience function"""
    print("🚀 Welcome to the AI Travel Platform Experience!")
    print("🌍 Let's create your personalized travel plan")
    print("⏰", datetime.now().strftime("%B %d, %Y - %I:%M %p"))
    
    # Get user preferences
    preferences = get_user_input()
    
    # Generate AI travel plan
    plan = generate_ai_travel_plan(preferences)
    
    # Display the plan
    display_travel_plan(plan, preferences)
    
    # Demonstrate booking
    demonstrate_booking()
    
    print(f"\n🎉 Experience complete!")
    print(f"🌐 Visit the web interface at: http://localhost:8501")
    print(f"📱 Full features available in the Streamlit app")
    print(f"✈️ Happy travels!")

if __name__ == "__main__":
    main()
