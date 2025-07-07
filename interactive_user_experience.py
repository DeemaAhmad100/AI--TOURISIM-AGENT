#!/usr/bin/env python3
"""
🌍 AI Travel Platform - Interactive User Experience Demo
Run this to experience how the platform works and interact with users
"""

import os
import sys
import time
from datetime import datetime
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

def typing_effect(text, delay=0.02):
    """Simulate typing effect for more realistic interaction"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_welcome_screen():
    """Show welcome screen with platform introduction"""
    print("\n" + "🌟" * 50)
    print("🌍 AI TRAVEL PLATFORM - INTERACTIVE EXPERIENCE")
    print("🌟" * 50)
    print()
    typing_effect("Welcome to your AI-powered travel companion! 🚀")
    print()
    typing_effect("I'm your personal travel assistant, ready to help you plan amazing trips.")
    print()
    print("✨ What I can do for you:")
    print("• 🎯 Create personalized travel itineraries")
    print("• 🏨 Find perfect accommodations") 
    print("• 🍽️ Recommend amazing restaurants")
    print("• ✈️ Search flights and transportation")
    print("• 💰 Optimize your travel budget")
    print("• 🌍 Provide local insights and cultural tips")
    print("• 👥 Coordinate group travel")
    print("• 🌐 Support 50+ languages")
    print()

def get_user_profile():
    """Get user profile information"""
    print("📋 Let's get to know you better!")
    print("-" * 30)
    
    name = input("🧑‍💼 What's your name? ").strip()
    if not name:
        name = "Traveler"
    
    print(f"\nHello {name}! Nice to meet you! 👋")
    
    # Get travel preferences
    print("\n🎯 What type of traveler are you?")
    print("1. 🏝️ Leisure & Relaxation")
    print("2. 🎒 Adventure & Exploration")
    print("3. 🏛️ Culture & History")
    print("4. 🍽️ Food & Culinary")
    print("5. 💼 Business Travel")
    print("6. 👨‍👩‍👧‍👦 Family Travel")
    
    traveler_type = input("Select your type (1-6): ").strip()
    
    types = {
        '1': '🏝️ Leisure & Relaxation',
        '2': '🎒 Adventure & Exploration', 
        '3': '🏛️ Culture & History',
        '4': '🍽️ Food & Culinary',
        '5': '💼 Business Travel',
        '6': '👨‍👩‍👧‍👦 Family Travel'
    }
    
    selected_type = types.get(traveler_type, '🎒 Adventure & Exploration')
    
    print(f"\n✅ Great! You're a {selected_type} traveler!")
    
    return {
        'name': name,
        'traveler_type': selected_type,
        'preferences': []
    }

def travel_planning_demo(user_profile):
    """Interactive travel planning demonstration"""
    print(f"\n🎯 Let's plan your next adventure, {user_profile['name']}!")
    print("-" * 40)
    
    # Get destination
    destination = input("🌍 Where would you like to travel? ").strip()
    if not destination:
        destination = "Tokyo, Japan"
        print(f"Great choice! Let's explore {destination}!")
    
    # Get duration
    print("\n📅 How long is your trip?")
    print("1. Weekend (2-3 days)")
    print("2. Week (5-7 days)")
    print("3. Extended (10+ days)")
    
    duration_choice = input("Select duration (1-3): ").strip()
    duration_map = {
        '1': '3 days',
        '2': '7 days', 
        '3': '14 days'
    }
    duration = duration_map.get(duration_choice, '7 days')
    
    # Get budget
    print("\n💰 What's your budget range?")
    print("1. 💵 Budget-friendly ($500-1000)")
    print("2. 💸 Mid-range ($1000-3000)")
    print("3. 💎 Luxury ($3000+)")
    
    budget_choice = input("Select budget (1-3): ").strip()
    budget_map = {
        '1': '💵 Budget-friendly',
        '2': '💸 Mid-range',
        '3': '💎 Luxury'
    }
    budget = budget_map.get(budget_choice, '💸 Mid-range')
    
    # Generate itinerary
    print(f"\n🔄 Creating your personalized {duration} itinerary for {destination}...")
    print("🤖 AI Agent: Analyzing your preferences...")
    time.sleep(2)
    
    generate_sample_itinerary(destination, duration, budget, user_profile)

def generate_sample_itinerary(destination, duration, budget, user_profile):
    """Generate a sample itinerary based on user inputs"""
    print(f"\n🎉 Here's your personalized {duration} itinerary for {destination}!")
    print("=" * 60)
    
    # Sample itinerary based on destination
    if "tokyo" in destination.lower() or "japan" in destination.lower():
        show_tokyo_itinerary(duration, budget)
    elif "paris" in destination.lower() or "france" in destination.lower():
        show_paris_itinerary(duration, budget)
    elif "new york" in destination.lower() or "nyc" in destination.lower():
        show_nyc_itinerary(duration, budget)
    else:
        show_generic_itinerary(destination, duration, budget)
    
    # Show additional features
    print("\n🌟 Additional Features Available:")
    print("• 📱 Mobile app with offline maps")
    print("• 🔔 Real-time travel alerts")
    print("• 💬 24/7 AI travel support")
    print("• 📊 Budget tracking")
    print("• 🌍 Cultural etiquette guide")
    print("• 👥 Group travel coordination")

def show_tokyo_itinerary(duration, budget):
    """Show sample Tokyo itinerary"""
    print("🗾 TOKYO ADVENTURE ITINERARY")
    print("-" * 30)
    
    print("📅 Day 1: Traditional Tokyo")
    print("   🌅 Morning: Visit Senso-ji Temple")
    print("   🍜 Lunch: Authentic ramen in Asakusa")
    print("   🏯 Afternoon: Imperial Palace East Gardens")
    print("   🌃 Evening: Tokyo Skytree observation deck")
    
    print("\n📅 Day 2: Modern Tokyo")
    print("   🛍️ Morning: Shibuya crossing & shopping")
    print("   🍱 Lunch: Sushi at Tsukiji Outer Market")
    print("   🎮 Afternoon: TeamLab Borderless")
    print("   🍻 Evening: Izakaya experience in Shinjuku")
    
    print("\n📅 Day 3: Culture & Nature")
    print("   🌸 Morning: Meiji Shrine")
    print("   🎭 Lunch: Harajuku street food")
    print("   🎨 Afternoon: Ueno Museums")
    print("   🎌 Evening: Traditional kaiseki dinner")
    
    if "14 days" in duration:
        print("\n📅 Days 4-14: Extended exploration...")
        print("   🏔️ Day trip to Mt. Fuji")
        print("   🦌 Nara deer park visit")
        print("   🏮 Kyoto temples and gardens")
        print("   🍣 Osaka food tour")
    
    print(f"\n💰 Estimated Budget: {budget}")
    print("🏨 Accommodation: Traditional ryokan + modern hotel")
    print("🚄 Transportation: JR Pass included")

def show_paris_itinerary(duration, budget):
    """Show sample Paris itinerary"""
    print("🗼 PARIS ROMANTIC GETAWAY")
    print("-" * 30)
    
    print("📅 Day 1: Classic Paris")
    print("   🗼 Morning: Eiffel Tower visit")
    print("   🥐 Lunch: Café de Flore")
    print("   🎨 Afternoon: Louvre Museum")
    print("   🌹 Evening: Seine River cruise")
    
    print("📅 Day 2: Montmartre & Arts")
    print("   ⛪ Morning: Sacré-Cœur Basilica")
    print("   🎨 Lunch: Artist quarter exploration")
    print("   🏛️ Afternoon: Musée d'Orsay")
    print("   🍷 Evening: Wine tasting in Marais")

def show_nyc_itinerary(duration, budget):
    """Show sample NYC itinerary"""
    print("🏙️ NEW YORK CITY HIGHLIGHTS")
    print("-" * 30)
    
    print("📅 Day 1: Manhattan Icons")
    print("   🗽 Morning: Statue of Liberty")
    print("   🍕 Lunch: Authentic NY pizza")
    print("   🌳 Afternoon: Central Park")
    print("   🎭 Evening: Broadway show")

def show_generic_itinerary(destination, duration, budget):
    """Show generic itinerary template"""
    print(f"✈️ {destination.upper()} ADVENTURE")
    print("-" * 30)
    
    print("📅 Day 1: Arrival & Exploration")
    print("   🏨 Check into accommodation")
    print("   🍽️ Local cuisine tasting")
    print("   🚶 Walking tour of main attractions")
    
    print("📅 Day 2: Cultural Immersion")
    print("   🏛️ Visit museums and historical sites")
    print("   🛍️ Local markets and shopping")
    print("   🎪 Evening entertainment")

def advanced_features_demo():
    """Demonstrate advanced features"""
    print("\n🚀 ADVANCED FEATURES DEMONSTRATION")
    print("=" * 40)
    
    print("🤖 AI Agent Collaboration:")
    print("   • Travel Planner: Creates itineraries")
    print("   • Budget Optimizer: Finds best deals")
    print("   • Cultural Guide: Provides local insights")
    print("   • Safety Advisor: Ensures secure travel")
    
    print("\n👥 Group Travel Features:")
    print("   • Create travel groups")
    print("   • Collaborative planning")
    print("   • Split expenses")
    print("   • Group voting on activities")
    
    print("\n🌐 Multilingual Support:")
    print("   • 50+ languages supported")
    print("   • Cultural context awareness")
    print("   • Local etiquette guides")
    print("   • Region-specific recommendations")
    
    print("\n💡 Smart Features:")
    print("   • Real-time price monitoring")
    print("   • Weather-based recommendations")
    print("   • Crowd-sourced reviews")
    print("   • AI-powered personalization")

def interactive_chat_demo():
    """Interactive chat with AI travel assistant"""
    print("\n💬 CHAT WITH YOUR AI TRAVEL ASSISTANT")
    print("=" * 40)
    print("Ask me anything about travel! (Type 'exit' to return)")
    print()
    
    while True:
        user_input = input("🧑‍💼 You: ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'back']:
            break
            
        if not user_input:
            continue
            
        # Simulate AI response based on keywords
        print("🤖 AI Assistant:", end=" ")
        time.sleep(1)
        
        if any(word in user_input.lower() for word in ['hotel', 'accommodation', 'stay']):
            typing_effect("I'd be happy to help you find the perfect accommodation! What's your destination and budget range?")
        elif any(word in user_input.lower() for word in ['flight', 'airline', 'fly']):
            typing_effect("Great! I can help you find flights. What are your departure and destination cities?")
        elif any(word in user_input.lower() for word in ['restaurant', 'food', 'eat']):
            typing_effect("Food is one of the best parts of travel! What type of cuisine are you interested in?")
        elif any(word in user_input.lower() for word in ['budget', 'cost', 'price']):
            typing_effect("Budget planning is crucial! I can help you optimize costs and find the best deals.")
        elif any(word in user_input.lower() for word in ['culture', 'custom', 'etiquette']):
            typing_effect("Cultural awareness makes travel more meaningful! I can provide local customs and etiquette tips.")
        else:
            typing_effect("That's an interesting question! Let me help you with that travel-related query.")
        
        print()

def main():
    """Main demo function"""
    show_welcome_screen()
    
    while True:
        print("\n🎮 What would you like to do?")
        print("1. 🎯 Plan a New Trip")
        print("2. 💬 Chat with AI Assistant")
        print("3. 🚀 See Advanced Features")
        print("4. 🔧 Setup & Configuration")
        print("5. 📊 Platform Status")
        print("6. 🚪 Exit")
        
        choice = input("\nSelect option (1-6): ").strip()
        
        if choice == '1':
            user_profile = get_user_profile()
            travel_planning_demo(user_profile)
        elif choice == '2':
            interactive_chat_demo()
        elif choice == '3':
            advanced_features_demo()
        elif choice == '4':
            run_setup_demo()
        elif choice == '5':
            show_platform_status()
        elif choice == '6':
            print("\n👋 Thank you for trying the AI Travel Platform!")
            print("Have amazing travels! 🌍✈️")
            break
        else:
            print("❌ Invalid option. Please try again.")

def run_setup_demo():
    """Run the setup demonstration"""
    print("\n🔧 SETUP & CONFIGURATION")
    print("=" * 30)
    
    print("Running interactive setup demo...")
    os.system("python interactive_setup.py")

def show_platform_status():
    """Show current platform status"""
    print("\n📊 PLATFORM STATUS")
    print("=" * 20)
    
    print("✅ Core Features: Ready")
    print("✅ AI Agents: Active")
    print("✅ Database: Connected")
    print("🔄 Enhanced Features: Configurable")
    print("🌐 Multilingual: Available")
    print("👥 Group Travel: Ready")
    
    print("\n🎯 Quick Actions:")
    print("• Run: python interactive_setup.py")
    print("• Verify: python verify_setup.py")
    print("• Test: python comprehensive_test.py")

if __name__ == "__main__":
    main()
