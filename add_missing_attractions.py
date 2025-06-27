import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def add_missing_attractions():
    """Add attractions for destinations that don't have many."""
    
    # New attractions for destinations that need more
    new_attractions = [
        # New York (ID: 7) - needs attractions
        {
            'name': 'Statue of Liberty',
            'description': 'Symbol of freedom and democracy',
            'type': 'landmark',
            'rating': 4.7,
            'destination_id': 7
        },
        {
            'name': 'Central Park',
            'description': 'Large public park in Manhattan',
            'type': 'park',
            'rating': 4.6,
            'destination_id': 7
        },
        {
            'name': 'Times Square',
            'description': 'Bright commercial intersection and entertainment center',
            'type': 'landmark',
            'rating': 4.3,
            'destination_id': 7
        },
        
        # London (ID: 8) - needs attractions
        {
            'name': 'Big Ben',
            'description': 'Iconic clock tower and symbol of London',
            'type': 'landmark',
            'rating': 4.6,
            'destination_id': 8
        },
        {
            'name': 'Tower of London',
            'description': 'Historic castle and former royal palace',
            'type': 'castle',
            'rating': 4.5,
            'destination_id': 8
        },
        {
            'name': 'British Museum',
            'description': 'World-renowned museum of human history',
            'type': 'museum',
            'rating': 4.7,
            'destination_id': 8
        },
        
        # Sydney (ID: 9) - needs attractions
        {
            'name': 'Sydney Opera House',
            'description': 'Multi-venue performing arts center',
            'type': 'landmark',
            'rating': 4.8,
            'destination_id': 9
        },
        {
            'name': 'Sydney Harbour Bridge',
            'description': 'Steel through arch bridge',
            'type': 'landmark',
            'rating': 4.7,
            'destination_id': 9
        },
        {
            'name': 'Bondi Beach',
            'description': 'Famous beach and surfing spot',
            'type': 'beach',
            'rating': 4.4,
            'destination_id': 9
        },
        
        # Cairo (ID: 10) - needs attractions
        {
            'name': 'Pyramids of Giza',
            'description': 'Ancient pyramid complex and Wonder of the World',
            'type': 'landmark',
            'rating': 4.9,
            'destination_id': 10
        },
        {
            'name': 'Egyptian Museum',
            'description': 'Museum of ancient Egyptian antiquities',
            'type': 'museum',
            'rating': 4.5,
            'destination_id': 10
        },
        {
            'name': 'Khan el-Khalili',
            'description': 'Historic bazaar and marketplace',
            'type': 'market',
            'rating': 4.3,
            'destination_id': 10
        },
        
        # Bangkok (ID: 11) - needs attractions
        {
            'name': 'Grand Palace',
            'description': 'Complex of buildings at the heart of Bangkok',
            'type': 'palace',
            'rating': 4.6,
            'destination_id': 11
        },
        {
            'name': 'Wat Pho Temple',
            'description': 'Buddhist temple with giant reclining Buddha',
            'type': 'temple',
            'rating': 4.7,
            'destination_id': 11
        },
        {
            'name': 'Chatuchak Market',
            'description': 'One of the world\'s largest weekend markets',
            'type': 'market',
            'rating': 4.4,
            'destination_id': 11
        }
    ]
    
    try:
        print("🎯 Adding new attractions to destinations...")
        
        for attraction in new_attractions:
            # Check if attraction already exists
            existing = supabase.table("attractions").select("id").eq("name", attraction['name']).execute()
            
            if not existing.data:
                result = supabase.table("attractions").insert(attraction).execute()
                print(f"✅ Added: {attraction['name']} to destination ID {attraction['destination_id']}")
            else:
                print(f"⚠️  Skipped: {attraction['name']} (already exists)")
                
        print("\n🎉 Finished adding attractions!")
        
    except Exception as e:
        print(f"❌ Error adding attractions: {str(e)}")

def show_final_summary():
    """Show final summary of all destinations and their attractions."""
    try:
        print("\n📊 FINAL SUMMARY - All Destinations & Attractions")
        print("=" * 60)
        
        # Get all destinations
        destinations = supabase.table("destinations").select("*").order("id").execute()
        
        for dest in destinations.data:
            print(f"\n🌍 {dest['name']} (ID: {dest['id']})")
            print(f"   📝 {dest['description']}")
            
            # Get attractions for this destination
            attractions = supabase.table("attractions").select("*").eq("destination_id", dest['id']).execute()
            
            if attractions.data:
                print(f"   🎯 Attractions ({len(attractions.data)}):")
                for attr in attractions.data:
                    print(f"      • {attr['name']} ({attr['type']}) - ⭐ {attr['rating']}")
            else:
                print("   ❌ No attractions found")
                
    except Exception as e:
        print(f"❌ Error generating summary: {str(e)}")

if __name__ == "__main__":
    print("🚀 ADDING MISSING ATTRACTIONS")
    print("=" * 40)
    
    add_missing_attractions()
    show_final_summary()
    
    print("\n✅ Database is now fully populated with demo data!")
    print("💡 You can now test your travel agent with rich destination and attraction data!")
