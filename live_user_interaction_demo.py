#!/usr/bin/env python3
"""
🌍 AI Travel Platform - Live User Interaction Demo
Experience how the platform interacts with users
"""

import os
import sys
import time
from datetime import datetime

def typing_effect(text, delay=0.03):
    """Simulate typing effect for more realistic interaction"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_platform_intro():
    """Show platform introduction"""
    print("🌟" * 30)
    print("🌍 AI TRAVEL PLATFORM - LIVE DEMO")
    print("🌟" * 30)
    print()
    print("Welcome to your AI Travel Assistant!")
    print("I'm here to help you plan amazing trips around the world.")
    print()
    print("✨ What I can do for you:")
    print("• 🎯 Create personalized travel itineraries")
    print("• 🏨 Find perfect hotels and accommodations")
    print("• 🍽️ Recommend amazing restaurants")
    print("• ✈️ Search for flights and transport")
    print("• 💰 Optimize your travel budget")
    print("• 🌍 Provide local insights and cultural tips")
    print()

def simulate_user_interaction():
    """Simulate realistic user interaction with the AI"""
    
    scenarios = [
        {
            "user": "I want to plan a romantic trip to Paris for 5 days",
            "ai_response": """🗼 Paris - The City of Love! Perfect choice for a romantic getaway.

🔍 Let me create a romantic 5-day itinerary for you:

📅 Day 1: Arrival & Eiffel Tower
   • Check into a romantic hotel (Le Meurice recommended)
   • Evening: Eiffel Tower sunset viewing
   • Dinner: Jules Verne restaurant (in the Eiffel Tower)

📅 Day 2: Art & Culture
   • Morning: Louvre Museum (Mona Lisa & Venus de Milo)
   • Afternoon: Stroll along Seine River
   • Evening: Romantic dinner cruise

📅 Day 3: Montmartre & Sacré-Cœur
   • Morning: Explore artistic Montmartre district
   • Lunch: Café des Deux Moulins (Amélie filming location)
   • Evening: Sunset at Sacré-Cœur Basilica

📅 Day 4: Gardens & Shopping
   • Morning: Luxembourg Gardens picnic
   • Afternoon: Champs-Élysées shopping
   • Evening: Opera show at Palais Garnier

📅 Day 5: Hidden Gems
   • Morning: Île Saint-Louis exploration
   • Afternoon: Musée Rodin gardens
   • Farewell dinner: Le Comptoir du Relais

💰 Estimated Budget: $2,500 per couple
🏨 Recommended Hotel: Le Meurice (luxury) or Hotel des Grands Boulevards (boutique)
✈️ Best time to book: 2-3 months in advance"""
        },
        {
            "user": "I'm on a tight budget, can you suggest a cheap trip to Thailand?",
            "ai_response": """🇹🇭 Thailand - Amazing value for budget travelers! 

💰 BUDGET-FRIENDLY THAILAND ITINERARY (7 days):

📍 Bangkok (3 days) - Budget: $30-40/day
   • Stay: Khao San Road hostels ($8-12/night)
   • Must-see: Grand Palace, Wat Pho Temple (FREE!)
   • Food: Street food paradise ($1-3 per meal)
   • Transport: BTS Skytrain day pass ($4)

📍 Chiang Mai (2 days) - Budget: $25-35/day
   • Stay: Old City guesthouses ($10-15/night)
   • Activities: Temple hopping, night markets
   • Food: Khao Soi noodles ($2), mango sticky rice ($1)

📍 Phuket Beach (2 days) - Budget: $35-50/day
   • Stay: Patong Beach hostels ($12-18/night)
   • Beach: Kata Beach (FREE!)
   • Food: Beach BBQ seafood ($5-8)

💡 MONEY-SAVING TIPS:
   • Fly during shoulder season (May-June)
   • Use local buses instead of taxis
   • Eat at local food courts
   • Book hostels with kitchen facilities
   • Take advantage of free temple visits

🎯 Total estimated cost: $500-700 for 7 days (including flights from US)
✈️ Best booking sites: Skyscanner, Hostelworld, Agoda"""
        },
        {
            "user": "I need help planning a business trip to Tokyo",
            "ai_response": """🏢 Tokyo Business Trip - Professional and efficient!

📋 BUSINESS-FOCUSED TOKYO ITINERARY:

🏨 RECOMMENDED BUSINESS HOTELS:
   • The Ritz-Carlton Tokyo (Roppongi) - $400-600/night
   • Palace Hotel Tokyo (Marunouchi) - $300-500/night
   • Park Hyatt Tokyo (Shinjuku) - $350-550/night

🚇 TRANSPORTATION:
   • Narita Express to city center (1 hour)
   • JR Yamanote Line for business districts
   • Tokyo Metro 24-hour pass ($8)

🏢 BUSINESS DISTRICTS:
   • Marunouchi: Financial center, close to Tokyo Station
   • Shibuya: Tech companies, modern offices
   • Roppongi: International business, embassies

🍽️ BUSINESS DINING:
   • Sushi: Sukiyabashi Jiro (world-famous)
   • Kaiseki: Kikunoi (traditional fine dining)
   • Teppanyaki: Kawamura (premium beef)
   • Business lunch: Ginza district restaurants

📱 BUSINESS ETIQUETTE TIPS:
   • Always bow when greeting
   • Exchange business cards with both hands
   • Remove shoes when entering traditional restaurants
   • Punctuality is crucial (arrive 10 minutes early)

🎯 AFTER-HOURS NETWORKING:
   • Ginza bars for client entertainment
   • Robot Restaurant show (unique experience)
   • Karaoke boxes for team building

💰 Estimated budget: $250-400/day (including accommodation)
📞 Need help with specific arrangements? I can assist with bookings!"""
        }
    ]
    
    print("🎪 Let's see how I interact with different types of travelers:")
    print("=" * 60)
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n📚 SCENARIO {i}:")
        print("=" * 20)
        
        # Show user input
        print(f"👤 User: {scenario['user']}")
        print()
        
        # Show AI thinking
        print("🤖 AI Agent: ", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print(" Let me help you with that!")
        print()
        
        # Show AI response
        print("🤖 AI Agent Response:")
        print(scenario['ai_response'])
        
        if i < len(scenarios):
            input("\n⏎ Press Enter to see the next scenario...")

def interactive_chat_mode():
    """Allow real user interaction"""
    print("\n🎪 INTERACTIVE CHAT MODE")
    print("=" * 30)
    print("Now it's your turn! Ask me anything about travel planning.")
    print("I'll respond as your AI Travel Assistant.")
    print("(Type 'quit' to exit)")
    print()
    
    while True:
        user_input = input("👤 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("🤖 AI Agent: Safe travels! I'm here whenever you need travel planning help! 👋")
            break
        
        if not user_input:
            continue
        
        # Simulate AI processing
        print("🤖 AI Agent: ", end="")
        for _ in range(2):
            print(".", end="", flush=True)
            time.sleep(0.3)
        print(" ")
        
        # Generate contextual response
        response = generate_ai_response(user_input)
        typing_effect(response, 0.02)
        print()

def generate_ai_response(user_input):
    """Generate contextual AI response based on user input"""
    user_lower = user_input.lower()
    
    if "budget" in user_lower or "cheap" in user_lower:
        return "💰 I specialize in budget travel! Let me find you amazing deals and cost-effective options. What's your target budget and destination?"
    
    elif "romantic" in user_lower or "honeymoon" in user_lower:
        return "💕 How romantic! I'll help you plan the perfect romantic getaway. Are you thinking beaches, mountains, or cultural cities?"
    
    elif "business" in user_lower or "work" in user_lower:
        return "🏢 I'll help you plan an efficient business trip. Which city are you traveling to, and do you need help with hotels near business districts?"
    
    elif "family" in user_lower or "kids" in user_lower:
        return "👨‍👩‍👧‍👦 Family travel is wonderful! I'll suggest kid-friendly destinations and activities. How many children and what ages?"
    
    elif "solo" in user_lower or "alone" in user_lower:
        return "🚶‍♀️ Solo travel is amazing for self-discovery! I'll recommend safe destinations and solo-friendly activities. Any particular interests?"
    
    elif "adventure" in user_lower or "hiking" in user_lower:
        return "🏔️ Adventure awaits! I can suggest thrilling destinations with hiking, climbing, or extreme sports. What's your experience level?"
    
    elif any(country in user_lower for country in ["japan", "tokyo", "kyoto"]):
        return "🇯🇵 Japan is incredible! From Tokyo's modern energy to Kyoto's traditional charm. Are you interested in culture, food, or nature?"
    
    elif any(country in user_lower for country in ["paris", "france", "europe"]):
        return "🇫🇷 Bonjour! Europe has so much to offer. Interested in art, history, cuisine, or maybe a multi-city tour?"
    
    elif any(country in user_lower for country in ["thailand", "bali", "asia"]):
        return "🌴 Southeast Asia is a traveler's paradise! Great food, beautiful beaches, and rich culture. Beach relaxation or cultural exploration?"
    
    elif "hotel" in user_lower or "accommodation" in user_lower:
        return "🏨 I'll help you find the perfect place to stay! Are you looking for luxury, boutique, budget-friendly, or something unique?"
    
    elif "flight" in user_lower or "airplane" in user_lower:
        return "✈️ Let me help you find the best flights! Where are you flying from and to? Any date preferences?"
    
    elif "food" in user_lower or "restaurant" in user_lower:
        return "🍽️ I'm a foodie too! I can recommend amazing restaurants and local dishes. Any dietary restrictions or cuisine preferences?"
    
    else:
        return "🤔 That sounds like an interesting travel request! Could you tell me more about your destination preferences, budget, and travel style so I can give you the best recommendations?"

def show_platform_features():
    """Show detailed platform features"""
    print("\n🔧 PLATFORM FEATURES SHOWCASE")
    print("=" * 40)
    
    features = [
        ("🧠 AI-Powered Recommendations", "Uses advanced AI to understand your preferences and suggest personalized travel options"),
        ("🌍 Global Database", "Access to thousands of destinations, hotels, restaurants, and attractions worldwide"),
        ("💰 Budget Optimization", "Smart budget planning to get the most value from your travel spending"),
        ("📅 Itinerary Planning", "Day-by-day detailed itineraries with optimal timing and logistics"),
        ("🏨 Accommodation Finder", "From budget hostels to luxury resorts, find the perfect place to stay"),
        ("🍽️ Restaurant Recommendations", "Local cuisine gems and fine dining options based on your taste"),
        ("✈️ Flight Integration", "Search and compare flights from multiple airlines and booking sites"),
        ("📱 Mobile Friendly", "Access your travel plans from anywhere, anytime"),
        ("🌐 Multi-language Support", "Platform available in 50+ languages with cultural context"),
        ("👥 Group Travel", "Coordinate group trips with shared planning and split billing")
    ]
    
    for feature, description in features:
        print(f"\n{feature}")
        print(f"   → {description}")
        time.sleep(0.5)

def main():
    """Main demo function"""
    try:
        show_platform_intro()
        time.sleep(2)
        
        print("\n🎯 DEMO OPTIONS:")
        print("1. See AI interaction scenarios")
        print("2. Try interactive chat mode")
        print("3. View platform features")
        print("4. All of the above")
        
        choice = input("\nWhat would you like to see? (1-4): ").strip()
        
        if choice == '1':
            simulate_user_interaction()
        elif choice == '2':
            interactive_chat_mode()
        elif choice == '3':
            show_platform_features()
        elif choice == '4':
            simulate_user_interaction()
            show_platform_features()
            interactive_chat_mode()
        else:
            print("🤖 Let me show you everything!")
            simulate_user_interaction()
            show_platform_features()
            interactive_chat_mode()
        
        print("\n🎉 Thank you for experiencing the AI Travel Platform!")
        print("This demo shows how the platform intelligently responds to different travel needs.")
        print("The actual platform integrates with real APIs for live data and bookings.")
        
    except KeyboardInterrupt:
        print("\n\n👋 Demo ended. Thanks for trying the AI Travel Platform!")
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
        print("The platform is still under development, but you can see its potential!")

if __name__ == "__main__":
    main()
