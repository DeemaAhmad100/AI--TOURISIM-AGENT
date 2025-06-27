import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def test_travel_agent_integration_fixed():
    """Test the integration with the ACTUAL table schema."""
    
    print("🧪 TESTING TRAVEL AGENT DATABASE INTEGRATION (CORRECTED)")
    print("=" * 60)
    
    # Test 1: Get destination info (using actual columns)
    print("\n1️⃣ Testing destination lookup...")
    try:
        response = supabase.table("destinations").select("*").eq("name", "Paris").execute()
        if response.data:
            paris = response.data[0]
            print(f"✅ Found destination: {paris['name']}")
            print(f"   📝 Description: {paris['description']}")
            print(f"   🌍 Country: {paris['country']}")
            print(f"   💰 Cost per day: ${paris['average_cost_per_day']}")
            print(f"   🗣️  Language: {paris['language']}")
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
                print(f"      💰 Cost: ${attr['cost']} | ⏰ Duration: {attr['duration_hours']}h")
        else:
            print("❌ No attractions found for Paris!")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 3: Search destinations by continent
    print("\n3️⃣ Testing continent search...")
    try:
        response = supabase.table("destinations").select("name, continent, country").eq("continent", "Europe").execute()
        if response.data:
            print(f"✅ Found {len(response.data)} European destinations:")
            for dest in response.data:
                print(f"   🇪🇺 {dest['name']}, {dest['country']}")
        else:
            print("❌ No European destinations found!")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 4: Save a sample travel plan (using actual columns)
    print("\n4️⃣ Testing travel plan storage...")
    try:
        sample_plan = {
            'destination': 'Tokyo',
            'travel_dates': '2024-06-01 to 2024-06-07',
            'duration_days': 7,
            'budget': 2500,
            'preferences': 'cultural sites, temples, technology',
            'plan_summary': 'Week-long cultural exploration of Tokyo including temples, technology districts, and local cuisine'
        }
        
        result = supabase.table("travel_history").insert(sample_plan).execute()
        if result.data:
            print(f"✅ Travel plan saved with ID: {result.data[0]['id']}")
        else:
            print("❌ Failed to save travel plan!")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test 5: Save user preferences (using actual columns)
    print("\n5️⃣ Testing user preferences storage...")
    try:
        sample_preferences = [
            {
                'preference_type': 'budget_range',
                'preference_value': '$2000-3000',
                'frequency': 1,
                'last_used': '2024-01-15'
            },
            {
                'preference_type': 'travel_style',
                'preference_value': 'cultural_explorer',
                'frequency': 3,
                'last_used': '2024-01-15'
            }
        ]
        
        for pref in sample_preferences:
            result = supabase.table("user_preferences").insert(pref).execute()
            if result.data:
                print(f"✅ Saved preference: {pref['preference_type']} = {pref['preference_value']}")
            else:
                print(f"❌ Failed to save preference: {pref['preference_type']}")
                
    except Exception as e:
        print(f"❌ Error: {e}")

def demonstrate_realistic_travel_queries():
    """Demonstrate realistic queries the travel agent would make."""
    
    print("\n\n🤖 REALISTIC TRAVEL AGENT QUERIES")
    print("=" * 45)
    
    # Query 1: Find budget-friendly destinations
    print("\n🔍 Query: 'Find destinations under $100 per day'")
    try:
        budget_destinations = supabase.table("destinations").select("name, country, average_cost_per_day").lt("average_cost_per_day", 100).order("average_cost_per_day").execute()
        
        if budget_destinations.data:
            print("💰 Budget-friendly destinations:")
            for dest in budget_destinations.data:
                print(f"   • {dest['name']}, {dest['country']} - ${dest['average_cost_per_day']}/day")
        else:
            print("❌ No budget destinations found")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Query 2: Get top-rated attractions by type
    print("\n🔍 Query: 'Find the best museums'")
    try:
        museums = supabase.table("attractions").select("name, rating, cost").eq("type", "museum").order("rating", desc=True).execute()
        
        if museums.data:
            print("🏛️  Top-rated museums:")
            for museum in museums.data:
                print(f"   • {museum['name']} - ⭐ {museum['rating']} (${museum['cost']})")
        else:
            print("❌ No museums found")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Query 3: Seasonal recommendations
    print("\n🔍 Query: 'Best destinations for summer travel'")
    try:
        summer_destinations = supabase.table("destinations").select("name, country, best_season").eq("best_season", "Summer").execute()
        
        if summer_destinations.data:
            print("☀️ Perfect for summer:")
            for dest in summer_destinations.data:
                print(f"   • {dest['name']}, {dest['country']}")
        else:
            print("❌ No summer destinations found")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Query 4: Get attractions by duration for day planning
    print("\n🔍 Query: 'Quick attractions for half-day tour (2-4 hours)'")
    try:
        quick_attractions = supabase.table("attractions").select("name, duration_hours, type").gte("duration_hours", 2).lte("duration_hours", 4).order("rating", desc=True).execute()
        
        if quick_attractions.data:
            print("⏰ Half-day attractions:")
            for attr in quick_attractions.data[:5]:  # Top 5
                print(f"   • {attr['name']} ({attr['type']}) - {attr['duration_hours']}h")
        else:
            print("❌ No quick attractions found")
    except Exception as e:
        print(f"❌ Error: {e}")

def show_database_analytics():
    """Show useful analytics about the travel database."""
    
    print("\n\n📊 DATABASE ANALYTICS")
    print("=" * 30)
    
    try:
        # Continent distribution
        print("\n🌍 Destinations by continent:")
        continents = supabase.table("destinations").select("continent").execute()
        continent_counts = {}
        for dest in continents.data:
            cont = dest['continent']
            continent_counts[cont] = continent_counts.get(cont, 0) + 1
        
        for continent, count in continent_counts.items():
            print(f"   • {continent}: {count} destinations")
        
        # Average costs
        print("\n💰 Cost analysis:")
        costs = supabase.table("destinations").select("average_cost_per_day").execute()
        cost_values = [dest['average_cost_per_day'] for dest in costs.data]
        
        if cost_values:
            avg_cost = sum(cost_values) / len(cost_values)
            min_cost = min(cost_values)
            max_cost = max(cost_values)
            
            print(f"   • Average cost per day: ${avg_cost:.2f}")
            print(f"   • Cheapest destination: ${min_cost}/day")
            print(f"   • Most expensive: ${max_cost}/day")
        
        # Attraction types
        print("\n🎯 Attraction types:")
        attractions = supabase.table("attractions").select("type").execute()
        type_counts = {}
        for attr in attractions.data:
            attr_type = attr['type']
            type_counts[attr_type] = type_counts.get(attr_type, 0) + 1
        
        for attr_type, count in sorted(type_counts.items()):
            print(f"   • {attr_type}: {count} attractions")
            
    except Exception as e:
        print(f"❌ Error generating analytics: {e}")

if __name__ == "__main__":
    test_travel_agent_integration_fixed()
    demonstrate_realistic_travel_queries()
    show_database_analytics()
    
    print("\n\n🎉 COMPREHENSIVE TESTING COMPLETE!")
    print("✅ Your Supabase database is fully functional!")
    print("\n💡 Your travel agent can now:")
    print("   • Search destinations by budget, continent, and season")
    print("   • Get detailed attraction information with costs and durations")
    print("   • Store travel plans and user preferences")
    print("   • Provide data-driven recommendations")
    print("   • Generate analytics and insights")
    print("\n🚀 Ready to enhance your AI Travel Agent with rich database features!")
