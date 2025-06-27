"""
📊 DEMO DATA VIEWER - Complete Database Overview
View all the demo data in your AI Travel Agent database
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client
import json

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def show_destinations():
    """Display all destinations with full details"""
    print("📍 DESTINATIONS TABLE - Complete Data:")
    print("=" * 60)
    
    destinations = supabase.table("destinations").select("*").execute()
    
    for i, dest in enumerate(destinations.data, 1):
        print(f"\n{i}. {dest['name']}, {dest['country']}")
        print(f"   🌍 Continent: {dest['continent']}")
        print(f"   💰 Cost: ${dest['average_cost_per_day']}/day")
        print(f"   🌡️  Best Season: {dest['best_season']}")
        print(f"   📝 Description: {dest['description']}")
        print(f"   🆔 ID: {dest['id']}")

def show_attractions():
    """Display all attractions with full details"""
    print("\n🎯 ATTRACTIONS TABLE - Complete Data:")
    print("=" * 60)
    
    attractions = supabase.table("attractions").select("*").execute()
    
    # Group by destination
    dest_attractions = {}
    for attr in attractions.data:
        dest_id = attr['destination_id']
        if dest_id not in dest_attractions:
            dest_attractions[dest_id] = []
        dest_attractions[dest_id].append(attr)
    
    # Get destination names
    destinations = supabase.table("destinations").select("id, name").execute()
    dest_names = {dest['id']: dest['name'] for dest in destinations.data}
    
    for dest_id, attrs in dest_attractions.items():
        dest_name = dest_names.get(dest_id, f"Unknown (ID: {dest_id})")
        print(f"\n🏙️ {dest_name}:")
        print("-" * 40)
        
        for attr in attrs:
            print(f"   • {attr['name']} ({attr['type']})")
            print(f"     ⭐ Rating: {attr['rating']}")
            print(f"     📝 {attr['description']}")
            print(f"     🆔 ID: {attr['id']}")
            print()

def show_travel_history():
    """Display all travel history records"""
    print("\n📜 TRAVEL HISTORY TABLE - Complete Data:")
    print("=" * 60)
    
    history = supabase.table("travel_history").select("*").execute()
    
    for i, record in enumerate(history.data, 1):
        print(f"\n{i}. Trip to {record['destination']}")
        print(f"   � Travel Dates: {record['travel_dates']}")
        print(f"   ⏱️  Duration: {record['duration_days']} days")
        print(f"   💰 Budget: ${record['budget']}")
        print(f"   🎯 Preferences: {record['preferences']}")
        print(f"   � Plan Summary: {record['plan_summary']}")
        print(f"   � Created: {record['created_at']}")
        print(f"   🆔 ID: {record['id']}")

def show_user_preferences():
    """Display all user preferences"""
    print("\n⚙️ USER PREFERENCES TABLE - Complete Data:")
    print("=" * 60)
    
    preferences = supabase.table("user_preferences").select("*").execute()
    
    for i, pref in enumerate(preferences.data, 1):
        print(f"\n{i}. Preference Setting:")
        print(f"   🏷️  Type: {pref['preference_type']}")
        print(f"   💎 Value: {pref['preference_value']}")
        print(f"   📊 Frequency: {pref['frequency']}")
        print(f"   🕐 Last Used: {pref['last_used']}")
        print(f"   🆔 ID: {pref['id']}")

def show_database_statistics():
    """Show comprehensive database statistics"""
    print("\n📊 DATABASE STATISTICS:")
    print("=" * 40)
    
    # Count records in each table
    dest_count = len(supabase.table("destinations").select("id").execute().data)
    attr_count = len(supabase.table("attractions").select("id").execute().data)
    history_count = len(supabase.table("travel_history").select("id").execute().data)
    pref_count = len(supabase.table("user_preferences").select("id").execute().data)
    
    print(f"📍 Destinations: {dest_count} records")
    print(f"🎯 Attractions: {attr_count} records")
    print(f"📜 Travel History: {history_count} records")
    print(f"⚙️  User Preferences: {pref_count} records")
    print(f"🔢 Total Records: {dest_count + attr_count + history_count + pref_count}")
    
    # Budget analysis
    destinations = supabase.table("destinations").select("average_cost_per_day, continent").execute()
    
    if destinations.data:
        costs = [dest['average_cost_per_day'] for dest in destinations.data]
        min_cost = min(costs)
        max_cost = max(costs)
        avg_cost = sum(costs) / len(costs)
        
        print(f"\n💰 BUDGET ANALYSIS:")
        print(f"   Cheapest destination: ${min_cost}/day")
        print(f"   Most expensive: ${max_cost}/day")
        print(f"   Average cost: ${avg_cost:.0f}/day")
        
        # Continent breakdown
        continent_costs = {}
        for dest in destinations.data:
            cont = dest['continent']
            if cont not in continent_costs:
                continent_costs[cont] = []
            continent_costs[cont].append(dest['average_cost_per_day'])
        
        print(f"\n🌍 BY CONTINENT:")
        for continent, costs in continent_costs.items():
            avg = sum(costs) / len(costs)
            print(f"   {continent}: {len(costs)} destinations, ${avg:.0f}/day avg")

def show_sample_queries():
    """Show sample data queries"""
    print("\n🔍 SAMPLE DATA QUERIES:")
    print("=" * 40)
    
    # Most expensive destinations
    print("\n💎 Most Expensive Destinations:")
    expensive = supabase.table("destinations").select("name, country, average_cost_per_day").order("average_cost_per_day", desc=True).limit(3).execute()
    for dest in expensive.data:
        print(f"   • {dest['name']}, {dest['country']}: ${dest['average_cost_per_day']}/day")
    
    # Budget destinations
    print("\n💚 Budget-Friendly Destinations:")
    budget = supabase.table("destinations").select("name, country, average_cost_per_day").order("average_cost_per_day", asc=True).limit(3).execute()
    for dest in budget.data:
        print(f"   • {dest['name']}, {dest['country']}: ${dest['average_cost_per_day']}/day")
    
    # Top-rated attractions
    print("\n⭐ Highest Rated Attractions:")
    top_attractions = supabase.table("attractions").select("name, type, rating").order("rating", desc=True).limit(5).execute()
    for attr in top_attractions.data:
        print(f"   • {attr['name']} ({attr['type']}): {attr['rating']} stars")
    
    # Museums
    print("\n🏛️ Museums in Database:")
    museums = supabase.table("attractions").select("name").ilike("type", "%museum%").execute()
    for museum in museums.data:
        print(f"   • {museum['name']}")

def export_all_data():
    """Export all data to JSON format"""
    print("\n💾 EXPORTING ALL DATA TO JSON:")
    print("=" * 40)
    
    try:
        # Fetch all data
        destinations = supabase.table("destinations").select("*").execute().data
        attractions = supabase.table("attractions").select("*").execute().data
        travel_history = supabase.table("travel_history").select("*").execute().data
        user_preferences = supabase.table("user_preferences").select("*").execute().data
        
        # Combine into single structure
        all_data = {
            "destinations": destinations,
            "attractions": attractions,
            "travel_history": travel_history,
            "user_preferences": user_preferences,
            "export_info": {
                "total_records": len(destinations) + len(attractions) + len(travel_history) + len(user_preferences),
                "tables": ["destinations", "attractions", "travel_history", "user_preferences"]
            }
        }
        
        # Save to file
        filename = "travel_agent_demo_data.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Data exported to: {filename}")
        print(f"📊 Total records exported: {all_data['export_info']['total_records']}")
        
    except Exception as e:
        print(f"❌ Export failed: {e}")

def main():
    """Main function to display all demo data"""
    
    print("📊" * 20)
    print("🗄️  AI TRAVEL AGENT - COMPLETE DEMO DATA OVERVIEW 🗄️")
    print("📊" * 20)
    
    try:
        show_destinations()
        show_attractions()
        show_travel_history()
        show_user_preferences()
        show_database_statistics()
        show_sample_queries()
        
        print("\n" + "=" * 60)
        print("💾 Would you like to export all data to JSON? (y/n)")
        choice = input("Choice: ").strip().lower()
        
        if choice in ['y', 'yes']:
            export_all_data()
        
        print("\n✅ Demo data overview complete!")
        
    except Exception as e:
        print(f"❌ Error accessing database: {e}")
        print("Please ensure your .env file has correct Supabase credentials.")

if __name__ == "__main__":
    main()
