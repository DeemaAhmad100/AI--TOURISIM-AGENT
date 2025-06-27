"""
🌟 COMPLETE AI TRAVEL AGENT WITH INTENT DETECTION 🌟
Full integration demonstration with interactive chat interface
"""

import os
import sys
from dotenv import load_dotenv
from supabase import create_client, Client
from enhanced_travel_agent import SmartTravelAgent

def main_demo():
    """Complete demonstration of the AI Travel Agent system"""
    
    print("🎉" * 25)
    print("🌍 AI TRAVEL AGENT - COMPLETE SYSTEM DEMO 🌍")
    print("🎉" * 25)
    
    print("\n✅ SYSTEM CAPABILITIES OVERVIEW:")
    print("=" * 50)
    print("🧠 Intent Detection using Sentence Transformers")
    print("🗄️  Database Integration with Supabase")
    print("🎯 Smart Query Processing")
    print("💬 Interactive Chat Interface")
    print("📊 Real-time Confidence Scoring")
    print("🔍 Intelligent Destination Search")
    print("💰 Budget Analysis and Planning")
    print("🎪 Activity Recommendations")
    print("📅 Trip Planning Assistance")
    print("🌤️  Weather and Seasonal Advice")
    print("🚗 Transportation Guidance")
    print("🏨 Accommodation Suggestions")
    print("🏛️  Cultural Information")
    
    print("\n🎯 INTENT CATEGORIES SUPPORTED:")
    print("=" * 40)
    intent_descriptions = {
        "destination_search": "Finding and recommending travel destinations",
        "budget_planning": "Cost analysis and budget-friendly options",
        "activity_recommendations": "Attractions, museums, restaurants, etc.",
        "trip_planning": "Itinerary creation and trip organization",
        "weather_information": "Seasonal advice and weather guidance",
        "transportation": "Travel methods and logistics",
        "accommodation": "Hotels, hostels, vacation rentals",
        "cultural_information": "Local customs and cultural tips"
    }
    
    for intent, description in intent_descriptions.items():
        print(f"• {intent.replace('_', ' ').title()}: {description}")
    
    print("\n🚀 DEMO OPTIONS:")
    print("=" * 30)
    print("1️⃣ Quick Test - Pre-defined queries")
    print("2️⃣ Interactive Chat - Talk with the agent")
    print("3️⃣ Intent Analysis - Test specific queries")
    print("4️⃣ Database Exploration - View available data")
    print("5️⃣ Exit")
    
    while True:
        try:
            choice = input("\n🔥 Choose an option (1-5): ").strip()
            
            if choice == "1":
                quick_test_demo()
            elif choice == "2":
                interactive_chat_demo()
            elif choice == "3":
                intent_analysis_demo()
            elif choice == "4":
                database_exploration_demo()
            elif choice == "5":
                print("\n🌟 Thank you for exploring the AI Travel Agent! 🌟")
                break
            else:
                print("❌ Please choose a valid option (1-5)")
                
        except KeyboardInterrupt:
            print("\n\n🌟 Thank you for exploring the AI Travel Agent! 🌟")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def quick_test_demo():
    """Quick demonstration with pre-defined queries"""
    
    print("\n🧪 QUICK TEST DEMONSTRATION")
    print("=" * 40)
    
    agent = SmartTravelAgent()
    
    test_scenarios = [
        {
            "query": "Find me romantic destinations in Europe for my honeymoon",
            "expectation": "Should detect 'destination_search' and return European romantic destinations"
        },
        {
            "query": "I have a budget of $50 per day, where can I travel?",
            "expectation": "Should detect 'budget_planning' and show budget-friendly destinations"
        },
        {
            "query": "What are the best museums to visit in the world?",
            "expectation": "Should detect 'activity_recommendations' and show museum attractions"
        },
        {
            "query": "Help me plan a 10-day trip to Japan",
            "expectation": "Should detect 'trip_planning' and offer planning assistance"
        },
        {
            "query": "Tell me about local customs in Thailand",
            "expectation": "Should detect 'cultural_information' and provide cultural tips"
        }
    ]
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n🔍 Test {i}: {scenario['query']}")
        print(f"💭 Expected: {scenario['expectation']}")
        print("-" * 50)
        
        result = agent.process_user_query(scenario['query'])
        agent._display_response(result)
        
        input("\n⏸️  Press Enter to continue to next test...")

def interactive_chat_demo():
    """Interactive chat demonstration"""
    
    print("\n💬 INTERACTIVE CHAT DEMONSTRATION")
    print("=" * 40)
    print("Now you can chat directly with the AI Travel Agent!")
    print("Try asking about destinations, budgets, activities, etc.")
    print("The agent will detect your intent and provide intelligent responses.")
    
    agent = SmartTravelAgent()
    agent.chat_interface()

def intent_analysis_demo():
    """Detailed intent analysis demonstration"""
    
    print("\n🔬 INTENT ANALYSIS DEMONSTRATION")
    print("=" * 40)
    
    agent = SmartTravelAgent()
    
    print("Enter queries to see detailed intent analysis:")
    print("Type 'back' to return to main menu")
    
    while True:
        try:
            query = input("\n🔍 Enter your query: ").strip()
            
            if query.lower() == 'back':
                break
            
            if not query:
                continue
            
            # Get detailed analysis
            result = agent.process_user_query(query)
            
            print(f"\n📊 DETAILED ANALYSIS:")
            print("-" * 30)
            print(f"Query: '{query}'")
            print(f"Detected Intent: {result['detected_intent']}")
            print(f"Confidence Score: {result['confidence']:.3f}")
            
            # Get all intent suggestions for comparison
            suggestions = agent.intent_detector.get_intent_suggestions(query, top_k=5)
            
            print(f"\n🎯 ALL INTENT SCORES:")
            for intent, score in suggestions:
                confidence_level = "🔥 High" if score > 0.6 else "🟡 Medium" if score > 0.4 else "🔹 Low"
                print(f"   {intent.replace('_', ' ').title()}: {score:.3f} {confidence_level}")
            
            print(f"\n💬 Agent Response: {result['response']['message']}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def database_exploration_demo():
    """Explore the database content"""
    
    print("\n🗄️  DATABASE EXPLORATION")
    print("=" * 30)
    
    # Load environment variables
    load_dotenv()
    
    try:
        # Initialize Supabase client
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        supabase = create_client(supabase_url, supabase_key)
        
        print("\n📍 DESTINATIONS TABLE:")
        destinations = supabase.table("destinations").select("name, country, continent, average_cost_per_day").execute()
        for dest in destinations.data:
            print(f"   • {dest['name']}, {dest['country']} ({dest['continent']}) - ${dest['average_cost_per_day']}/day")
        
        print(f"\n🎯 ATTRACTIONS TABLE (Top 10 by rating):")
        attractions = supabase.table("attractions").select("name, type, rating").order("rating", desc=True).limit(10).execute()
        for attr in attractions.data:
            print(f"   • {attr['name']} ({attr['type']}) - ⭐ {attr['rating']}")
        
        print(f"\n📊 DATABASE STATISTICS:")
        dest_count = len(destinations.data)
        attr_count = len(supabase.table("attractions").select("id").execute().data)
        history_count = len(supabase.table("travel_history").select("id").execute().data)
        pref_count = len(supabase.table("user_preferences").select("id").execute().data)
        
        print(f"   📍 Destinations: {dest_count}")
        print(f"   🎯 Attractions: {attr_count}")
        print(f"   📜 Travel History Records: {history_count}")
        print(f"   ⚙️  User Preferences: {pref_count}")
        
    except Exception as e:
        print(f"❌ Database connection error: {e}")
    
    input("\n⏸️  Press Enter to return to main menu...")

def show_system_architecture():
    """Display system architecture overview"""
    
    print("\n🏗️  SYSTEM ARCHITECTURE")
    print("=" * 30)
    print("""
    User Query
        ↓
    Intent Detection (Sentence Transformers)
        ↓
    Query Processing & Intent Classification
        ↓
    Database Query (Supabase)
        ↓
    Intelligent Response Generation
        ↓
    Formatted Output to User
    
    📚 Technology Stack:
    • Sentence Transformers (all-MiniLM-L6-v2)
    • Scikit-learn (Cosine Similarity)
    • Supabase (Database)
    • Python (Backend Logic)
    • NumPy (Mathematical Operations)
    """)

if __name__ == "__main__":
    try:
        main_demo()
    except Exception as e:
        print(f"\n❌ System Error: {e}")
        print("Please ensure all dependencies are installed and environment is configured.")
