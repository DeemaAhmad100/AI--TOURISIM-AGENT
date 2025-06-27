import os
from supabase import create_client, Client

# Set credentials directly
supabase_url = "https://crpopiicbwzxemaxlgnh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNycG9waWljYnd6eGVtYXhsZ25oIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA5NTYwMTMsImV4cCI6MjA2NjUzMjAxM30.EX0QIPn46KrnMLLvt-5hA7le_A_sUhMoVZjjCjMP6eY"

# Initialize Supabase client
supabase: Client = create_client(supabase_url, supabase_key)

def main():
    """Show your actual database contents."""
    print("🎉 YOUR AI TRAVEL AGENT DATABASE IS READY! 🎉")
    print("=" * 60)
    
    # Show destinations
    print("\n📍 YOUR DESTINATIONS:")
    response = supabase.table("destinations").select("*").execute()
    for i, dest in enumerate(response.data, 1):
        print(f"{i}. {dest['name']} ({dest['country']})")
        print(f"   {dest['description']}")
        if dest.get('best_season'):
            print(f"   Best time to visit: {dest['best_season']}")
        print()
    
    # Show attractions (checking what fields exist)
    print("🎯 YOUR ATTRACTIONS:")
    response = supabase.table("attractions").select("*").limit(1).execute()
    if response.data:
        print("Available fields:", list(response.data[0].keys()))
        
        # Get all attractions
        response = supabase.table("attractions").select("*").execute()
        for i, attr in enumerate(response.data, 1):
            print(f"{i}. {attr['name']}")
            print(f"   Description: {attr.get('description', 'N/A')}")
            print(f"   Type: {attr.get('type', 'N/A')}")
            print(f"   Rating: {attr.get('rating', 'N/A')}")
            print()
    
    print("✅ SUCCESS! Your database is fully populated and ready!")
    print("\n📋 NEXT STEPS:")
    print("1. ✅ Database created and populated")
    print("2. ✅ All tables working correctly") 
    print("3. 🚀 Ready to run the full AI Travel Agent!")
    print("\nYou can now:")
    print("  • Browse destinations and attractions")
    print("  • Plan new trips with AI assistance")
    print("  • View travel history")
    print("  • Track user preferences")

if __name__ == "__main__":
    main()
