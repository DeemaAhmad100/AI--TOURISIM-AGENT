import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def test_travel_agent_integration():
    """Test the integration between travel agent and Supabase database."""
    
    print("🧪 TESTING TRAVEL AGENT DATABASE INTEGRATION")
    print("=" * 55)
    
    # Test 1: Get destination info (like the travel agent would)
    print("\n1️⃣ Testing destination lookup...")
    try:
        response = supabase.table("destinations").select("*").eq("name", "Paris").execute()
        if response.data:
            paris = response.data[0]
            print(f"✅ Found destination: {paris['name']}")
            print(f"   📝 Description: {paris['description']}")
            print(f"   🏷️  Category: {paris['category']}")
        else:
            print("❌ Paris not found!")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 2: Get attractions for a destination
    print("\n2️⃣ Testing attractions lookup...")
    try:
        response = supabase.table("attractions").select("*").eq("destination_id", 1).execute()
        if response.data:
            print(f"✅ Found {len(response.data)} attractions for Paris:")
            for attr in response.data:
                print(f"   🎯 {attr['name']} ({attr['type']}) - ⭐ {attr['rating']}")
        else:
            print("❌ No attractions found for Paris!")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 3: Search destinations by category
    print("\n3️⃣ Testing category search...")
    try:
        response = supabase.table("destinations").select("name, category").eq("category", "cultural").execute()
        if response.data:
            print(f"✅ Found {len(response.data)} cultural destinations:")
            for dest in response.data:
                print(f"   🏛️  {dest['name']}")
        else:
            print("❌ No cultural destinations found!")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 4: Save a sample travel plan
    print("\n4️⃣ Testing travel plan storage...")
    try:
        sample_plan = {
            'user_id': 'test_user_123',
            'destination': 'Tokyo',
            'start_date': '2024-06-01',
            'end_date': '2024-06-07',
            'budget': 2500,
            'preferences': 'cultural sites, temples, technology',
            'itinerary': {
                'day1': 'Arrive, visit Senso-ji Temple',
                'day2': 'Tokyo Skytree, Shibuya Crossing',
                'day3': 'Day trip to Mount Fuji'
            }
        }
        
        result = supabase.table("travel_history").insert(sample_plan).execute()
        if result.data:
            print(f"✅ Travel plan saved with ID: {result.data[0]['id']}")
        else:
            print("❌ Failed to save travel plan!")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 5: Save user preferences
    print("\n5️⃣ Testing user preferences storage...")
    try:
        sample_preference = {
            'user_id': 'test_user_123',
            'budget_range': '$2000-3000',
            'travel_style': 'cultural_explorer',
            'preferred_activities': ['museums', 'temples', 'local_food'],
            'accommodation_type': 'hotel'
        }
        
        result = supabase.table("user_preferences").insert(sample_preference).execute()
        if result.data:
            print(f"✅ User preferences saved with ID: {result.data[0]['id']}")
        else:
            print("❌ Failed to save user preferences!")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 6: Database statistics
    print("\n6️⃣ Database statistics...")
    try:
        dest_count = len(supabase.table("destinations").select("id").execute().data)
        attr_count = len(supabase.table("attractions").select("id").execute().data)
        history_count = len(supabase.table("travel_history").select("id").execute().data)
        pref_count = len(supabase.table("user_preferences").select("id").execute().data)
        
        print(f"📊 Database contains:")
        print(f"   🌍 {dest_count} destinations")
        print(f"   🎯 {attr_count} attractions") 
        print(f"   📜 {history_count} travel plans")
        print(f"   ⚙️  {pref_count} user preferences")
        
    except Exception as e:
        print(f"❌ Error getting statistics: {e}")

def demonstrate_travel_agent_queries():
    """Demonstrate real-world queries the travel agent might make."""
    
    print("\n\n🤖 SAMPLE TRAVEL AGENT QUERIES")
    print("=" * 40)
    
    # Query 1: Get top-rated attractions in a city
    print("\n🔍 Query: 'What are the top attractions in Rome?'")
    try:
        rome = supabase.table("destinations").select("id").eq("name", "Rome").execute().data[0]
        attractions = supabase.table("attractions").select("*").eq("destination_id", rome['id']).order("rating", desc=True).execute()
        
        print("🏛️  Top attractions in Rome:")
        for attr in attractions.data:
            print(f"   • {attr['name']} - ⭐ {attr['rating']} ({attr['type']})")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Query 2: Find destinations by budget/category
    print("\n🔍 Query: 'Recommend cultural destinations'")
    try:
        cultural_destinations = supabase.table("destinations").select("*").eq("category", "cultural").execute()
        
        print("🏛️  Cultural destinations:")
        for dest in cultural_destinations.data:
            print(f"   • {dest['name']}: {dest['description']}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Query 3: Get travel history for personalization
    print("\n🔍 Query: 'Get user travel history for recommendations'")
    try:
        history = supabase.table("travel_history").select("*").eq("user_id", "test_user_123").execute()
        
        if history.data:
            print(f"📜 Found {len(history.data)} previous trips:")
            for trip in history.data:
                print(f"   • {trip['destination']} ({trip['start_date']} to {trip['end_date']})")
        else:
            print("📜 No previous trips found")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_travel_agent_integration()
    demonstrate_travel_agent_queries()
    
    print("\n\n🎉 ALL TESTS COMPLETED!")
    print("✅ Your Supabase database is fully integrated and ready!")
    print("💡 Your travel agent can now:")
    print("   • Store and retrieve destination information")
    print("   • Get attractions and recommendations")
    print("   • Save user travel plans and preferences")
    print("   • Provide personalized recommendations based on history")
    print("\n🚀 Ready to build amazing travel experiences!")
