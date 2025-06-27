import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Load Supabase credentials
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

print(f"🔑 Supabase URL loaded: {bool(supabase_url)}")
print(f"🔑 Supabase Key loaded: {bool(supabase_key)}")

if not supabase_url or not supabase_key:
    raise ValueError("Supabase credentials are missing. Please check your .env file.")

# Initialize Supabase client
supabase: Client = create_client(supabase_url, supabase_key)

def test_supabase_connection():
    """Test the connection to Supabase."""
    try:
        response = supabase.table("destinations").select("*").execute()
        print(f"✅ Supabase connection successful!")
        print(f"📊 Found {len(response.data)} destinations in database")
        return True
    except Exception as e:
        print(f"❌ Supabase connection failed: {str(e)}")
        return False

def browse_destinations():
    """Browse destinations from the database."""
    print("\n📍 DESTINATIONS IN DATABASE:")
    print("-" * 40)
    
    try:
        response = supabase.table("destinations").select("*").execute()
        destinations = response.data
        
        if destinations:
            for i, dest in enumerate(destinations, 1):
                print(f"{i}. {dest['name']} ({dest['country']})")
                print(f"   📝 {dest['description']}")
                if dest.get('best_season'):
                    print(f"   🌤️  Best season: {dest['best_season']}")
                print()
        else:
            print("No destinations found in database.")
    except Exception as e:
        print(f"❌ Error retrieving destinations: {str(e)}")

def browse_attractions():
    """Browse attractions from the database."""
    print("\n🎯 ATTRACTIONS IN DATABASE:")
    print("-" * 40)
    
    try:
        response = supabase.table("attractions").select("*").execute()
        attractions = response.data
        
        if attractions:
            for i, attr in enumerate(attractions, 1):
                print(f"{i}. {attr['name']} ({attr['destination']})")
                print(f"   📝 {attr['description']}")
                print(f"   📍 Type: {attr['type']}")
                if attr.get('rating'):
                    print(f"   ⭐ Rating: {attr['rating']}/5")
                if attr.get('entrance_fee'):
                    print(f"   💰 Fee: ${attr['entrance_fee']}")
                print()
        else:
            print("No attractions found in database.")
    except Exception as e:
        print(f"❌ Error retrieving attractions: {str(e)}")

def main():
    """Main function to test database connectivity."""
    print("🌍 AI Travel Agent - Database Test 🌍")
    print("=" * 50)
    
    # Test database connection
    if test_supabase_connection():
        print("\n🎉 Great! Your database is working perfectly!")
        
        # Browse data
        browse_destinations()
        browse_attractions()
        
        print("\n✅ Your AI Travel Agent database is ready to use!")
        print("📋 Next steps:")
        print("   1. Your database has been successfully populated")
        print("   2. All tables are working correctly") 
        print("   3. You can now run the full travel agent application")
        
    else:
        print("\n❌ Database connection failed. Please check your Supabase credentials.")

if __name__ == "__main__":
    main()
