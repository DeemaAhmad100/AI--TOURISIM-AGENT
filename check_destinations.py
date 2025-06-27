import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def check_destinations():
    """Check all destinations currently in the database."""
    try:
        print("🔍 Checking current destinations in database...")
        response = supabase.table("destinations").select("*").order("id").execute()
        destinations = response.data
        
        if destinations:
            print(f"\n📍 Found {len(destinations)} destinations:")
            print("-" * 60)
            for dest in destinations:
                print(f"ID: {dest['id']} | Name: {dest['name']}")
                print(f"   Description: {dest['description']}")
                if dest.get('best_season'):
                    print(f"   Best Season: {dest['best_season']}")
                print()
        else:
            print("❌ No destinations found in database!")
            
        return destinations
    except Exception as e:
        print(f"❌ Error checking destinations: {str(e)}")
        return []

def check_attractions():
    """Check all attractions currently in the database."""
    try:
        print("\n🎯 Checking current attractions in database...")
        response = supabase.table("attractions").select("*").order("destination_id", "id").execute()
        attractions = response.data
        
        if attractions:
            print(f"\n🎯 Found {len(attractions)} attractions:")
            print("-" * 60)
            for attr in attractions:
                print(f"ID: {attr['id']} | Destination ID: {attr['destination_id']} | Name: {attr['name']}")
                print(f"   Type: {attr['type']} | Rating: {attr.get('rating', 'N/A')}")
                print()
        else:
            print("❌ No attractions found in database!")
            
        return attractions
    except Exception as e:
        print(f"❌ Error checking attractions: {str(e)}")
        return []

if __name__ == "__main__":
    print("🔍 CHECKING DATABASE CONTENTS")
    print("=" * 50)
    
    destinations = check_destinations()
    attractions = check_attractions()
    
    # Provide guidance
    print("\n💡 GUIDANCE:")
    print("-" * 30)
    if destinations:
        print("✅ You have destinations in your database.")
        print("📋 When adding attractions, use one of these destination IDs:")
        for dest in destinations:
            print(f"   • ID {dest['id']}: {dest['name']}")
    else:
        print("❌ No destinations found! You need to add destinations first.")
    
    print("\n🔗 Remember: attraction.destination_id must match an existing destination.id")
