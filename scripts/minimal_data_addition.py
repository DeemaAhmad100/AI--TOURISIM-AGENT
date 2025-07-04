"""
🗃️ Minimal Data Addition
Add hotels and restaurants with minimal required fields only
"""

import os
import datetime
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment
load_dotenv()

# Initialize Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(supabase_url, supabase_key)

def inspect_table_columns(table_name):
    """Check what columns exist in a table by examining a sample record"""
    print(f"\n🔍 Inspecting {table_name} table structure...")
    
    try:
        # Try to get one record to see the structure
        result = supabase.table(table_name).select("*").limit(1).execute()
        
        if result.data and len(result.data) > 0:
            sample_record = result.data[0]
            print(f"📝 Available columns in {table_name}:")
            for column in sample_record.keys():
                print(f"   • {column}")
            return list(sample_record.keys())
        else:
            print(f"   ℹ️ {table_name} table exists but has no data")
            # If no data, try inserting a test record to see what's required
            test_record = {"name": "test"}
            try:
                result = supabase.table(table_name).insert(test_record).execute()
                # If successful, delete it
                if result.data:
                    supabase.table(table_name).delete().eq("name", "test").execute()
                return ["name"]  # Basic assumption
            except Exception as e:
                print(f"   ❌ Could not determine structure: {e}")
                return []
            
    except Exception as e:
        print(f"   ❌ Error inspecting {table_name}: {e}")
        return []

def add_minimal_hotels():
    """Add hotels with only the required fields"""
    print("\n🏨 Adding minimal hotels...")
    
    # Get available columns
    columns = inspect_table_columns("hotels")
    
    if not columns:
        print("❌ Could not determine hotel table structure")
        return False
    
    # Create minimal hotel records with only safe fields
    minimal_hotels = [
        {
            "name": "Four Seasons Hotel Beirut",
            "description": "Luxury hotel in the heart of Beirut",
            "created_at": datetime.datetime.now().isoformat()
        },
        {
            "name": "Kyoto Traditional Ryokan",
            "description": "Authentic Japanese ryokan experience",
            "created_at": datetime.datetime.now().isoformat()
        },
        {
            "name": "Burj Al Arab Dubai",
            "description": "Iconic sail-shaped luxury hotel",
            "created_at": datetime.datetime.now().isoformat()
        }
    ]
    
    # Filter to only include fields that exist
    safe_hotels = []
    for hotel in minimal_hotels:
        safe_hotel = {}
        for key, value in hotel.items():
            if key in columns or key in ['name', 'description']:  # Always try name and description
                safe_hotel[key] = value
        safe_hotels.append(safe_hotel)
    
    try:
        result = supabase.table("hotels").upsert(safe_hotels).execute()
        print(f"✅ Successfully added {len(safe_hotels)} hotels")
        return True
    except Exception as e:
        print(f"❌ Error adding hotels: {e}")
        
        # Try with just name
        basic_hotels = [{"name": hotel["name"]} for hotel in minimal_hotels]
        try:
            result = supabase.table("hotels").upsert(basic_hotels).execute()
            print(f"✅ Successfully added {len(basic_hotels)} hotels (name only)")
            return True
        except Exception as e2:
            print(f"❌ Even basic hotel insertion failed: {e2}")
            return False

def add_minimal_restaurants():
    """Add restaurants with only the required fields"""
    print("\n🍽️ Adding minimal restaurants...")
    
    # Get available columns
    columns = inspect_table_columns("restaurants")
    
    if not columns:
        print("❌ Could not determine restaurant table structure")
        return False
    
    # Create minimal restaurant records
    minimal_restaurants = [
        {
            "name": "Tawlet Beirut",
            "cuisine_type": "Lebanese Traditional",
            "description": "Authentic Lebanese home cooking",
            "created_at": datetime.datetime.now().isoformat()
        },
        {
            "name": "Kikunoi Kyoto",
            "cuisine_type": "Kaiseki Traditional",
            "description": "3-Michelin-star kaiseki restaurant",
            "created_at": datetime.datetime.now().isoformat()
        },
        {
            "name": "Nobu Dubai",
            "cuisine_type": "Japanese Fusion",
            "description": "World-renowned Japanese-Peruvian fusion",
            "created_at": datetime.datetime.now().isoformat()
        }
    ]
    
    # Filter to only include fields that exist
    safe_restaurants = []
    for restaurant in minimal_restaurants:
        safe_restaurant = {}
        for key, value in restaurant.items():
            if key in columns or key in ['name', 'cuisine_type', 'description']:
                safe_restaurant[key] = value
        safe_restaurants.append(safe_restaurant)
    
    try:
        result = supabase.table("restaurants").upsert(safe_restaurants).execute()
        print(f"✅ Successfully added {len(safe_restaurants)} restaurants")
        return True
    except Exception as e:
        print(f"❌ Error adding restaurants: {e}")
        
        # Try with just name and cuisine_type
        basic_restaurants = [
            {"name": restaurant["name"], "cuisine_type": restaurant["cuisine_type"]} 
            for restaurant in minimal_restaurants
        ]
        try:
            result = supabase.table("restaurants").upsert(basic_restaurants).execute()
            print(f"✅ Successfully added {len(basic_restaurants)} restaurants (basic)")
            return True
        except Exception as e2:
            print(f"❌ Even basic restaurant insertion failed: {e2}")
            return False

def main():
    """Main execution"""
    print("🗃️ Minimal Database Population")
    print("="*50)
    
    # Check current status
    try:
        result = supabase.table("hotels").select("*", count="exact").execute()
        hotels_count = result.count if hasattr(result, 'count') else len(result.data)
        print(f"📊 Current hotels: {hotels_count}")
    except Exception as e:
        print(f"❌ Hotels check: {e}")
    
    try:
        result = supabase.table("restaurants").select("*", count="exact").execute()
        restaurants_count = result.count if hasattr(result, 'count') else len(result.data)
        print(f"📊 Current restaurants: {restaurants_count}")
    except Exception as e:
        print(f"❌ Restaurants check: {e}")
    
    # Run minimal additions
    success_count = 0
    
    if add_minimal_hotels():
        success_count += 1
    
    if add_minimal_restaurants():
        success_count += 1
    
    print(f"\n🎉 Minimal population completed!")
    print(f"✅ Successfully completed {success_count}/2 operations")

if __name__ == "__main__":
    main()
