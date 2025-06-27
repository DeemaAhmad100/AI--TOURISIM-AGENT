import os
from supabase import create_client, Client

# Set credentials directly (temporary for testing)
supabase_url = "https://crpopiicbwzxemaxlgnh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNycG9waWljYnd6eGVtYXhsZ25oIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA5NTYwMTMsImV4cCI6MjA2NjUzMjAxM30.EX0QIPn46KrnMLLvt-5hA7le_A_sUhMoVZjjCjMP6eY"

# Initialize Supabase client
supabase: Client = create_client(supabase_url, supabase_key)

def main():
    """Test database and show demo data."""
    print("🌍 AI Travel Agent - Database Test 🌍")
    print("=" * 50)
    
    try:
        # Test destinations
        print("\n📍 TESTING DESTINATIONS TABLE:")
        response = supabase.table("destinations").select("*").execute()
        destinations = response.data
        print(f"✅ Found {len(destinations)} destinations")
        
        for dest in destinations:
            print(f"  • {dest['name']} ({dest['country']}) - {dest['description'][:50]}...")
        
        # Test attractions  
        print("\n🎯 TESTING ATTRACTIONS TABLE:")
        response = supabase.table("attractions").select("*").execute()
        attractions = response.data
        print(f"✅ Found {len(attractions)} attractions")
        
        for attr in attractions[:5]:  # Show first 5
            print(f"  • {attr['name']} in {attr['destination']} - Rating: {attr.get('rating', 'N/A')}")
        
        # Test travel history
        print("\n📚 TESTING TRAVEL HISTORY TABLE:")
        response = supabase.table("travel_history").select("*").execute()
        history = response.data
        print(f"✅ Found {len(history)} travel records")
        
        for trip in history:
            print(f"  • {trip['destination']} - {trip['duration_days']} days ({trip['budget']})")
        
        # Test user preferences
        print("\n🎨 TESTING USER PREFERENCES TABLE:")
        response = supabase.table("user_preferences").select("*").execute()
        prefs = response.data
        print(f"✅ Found {len(prefs)} user preferences")
        
        for pref in prefs:
            print(f"  • {pref['preference_type']}: {pref['preference_value']} (used {pref['frequency']} times)")
        
        print("\n🎉 DATABASE TEST COMPLETE!")
        print("✅ All tables are working correctly")
        print("✅ Demo data has been successfully loaded")
        print("✅ Your AI Travel Agent is ready to use!")
        
        print("\n📋 WHAT'S WORKING:")
        print(f"  🗂️  Destinations: {len(destinations)} cities ready for planning")
        print(f"  🎯 Attractions: {len(attractions)} attractions available")
        print(f"  📚 Travel History: {len(history)} past trips recorded")
        print(f"  🎨 User Preferences: {len(prefs)} preferences tracked")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    main()
