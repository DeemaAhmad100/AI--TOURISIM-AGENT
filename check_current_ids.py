import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def check_current_destination_ids():
    """Check what destination IDs are currently in the database."""
    try:
        print("🔍 Checking current destination IDs...")
        response = supabase.table("destinations").select("id, name").order("id").execute()
        
        if response.data:
            print("\n📍 Current destinations and their IDs:")
            print("-" * 50)
            for dest in response.data:
                print(f"ID: {dest['id']} | Name: {dest['name']}")
        else:
            print("❌ No destinations found in database!")
            
        return response.data
    except Exception as e:
        print(f"❌ Error checking destinations: {str(e)}")
        return []

def check_current_attraction_ids():
    """Check what attractions are currently in the database."""
    try:
        print("\n🎯 Checking current attractions...")
        response = supabase.table("attractions").select("id, name, destination_id").order("destination_id").execute()
        
        if response.data:
            print("\n🎯 Current attractions and their destination IDs:")
            print("-" * 60)
            for attr in response.data:
                print(f"Attraction ID: {attr['id']} | Name: {attr['name']} | Dest ID: {attr['destination_id']}")
        else:
            print("❌ No attractions found in database!")
            
        return response.data
    except Exception as e:
        print(f"❌ Error checking attractions: {str(e)}")
        return []

def suggest_correct_inserts():
    """Suggest correct insert statements based on existing destination IDs."""
    destinations = check_current_destination_ids()
    
    if not destinations:
        print("\n❌ No destinations found. You need to insert destinations first!")
        return
    
    print("\n💡 Here are some example INSERT statements using correct destination IDs:")
    print("-" * 70)
    
    # Find Paris, Tokyo, New York IDs from existing destinations
    paris_id = None
    tokyo_id = None
    nyc_id = None
    
    for dest in destinations:
        if "paris" in dest['name'].lower():
            paris_id = dest['id']
        elif "tokyo" in dest['name'].lower():
            tokyo_id = dest['id']
        elif "new york" in dest['name'].lower():
            nyc_id = dest['id']
    
    # Provide example inserts based on what exists
    if paris_id:
        print(f"""
-- For Paris (ID: {paris_id}):
INSERT INTO attractions (name, description, type, rating, destination_id) VALUES
('Eiffel Tower', 'Iconic iron tower and symbol of Paris', 'landmark', 4.8, {paris_id}),
('Louvre Museum', 'World-famous art museum', 'museum', 4.7, {paris_id});
""")
    
    if tokyo_id:
        print(f"""
-- For Tokyo (ID: {tokyo_id}):
INSERT INTO attractions (name, description, type, rating, destination_id) VALUES
('Tokyo Tower', 'Communications tower and landmark', 'landmark', 4.5, {tokyo_id}),
('Senso-ji Temple', 'Ancient Buddhist temple', 'temple', 4.6, {tokyo_id});
""")
    
    if nyc_id:
        print(f"""
-- For New York (ID: {nyc_id}):
INSERT INTO attractions (name, description, type, rating, destination_id) VALUES
('Statue of Liberty', 'Symbol of freedom and democracy', 'landmark', 4.7, {nyc_id}),
('Central Park', 'Large public park in Manhattan', 'park', 4.6, {nyc_id});
""")

if __name__ == "__main__":
    print("🔍 CHECKING CURRENT DATABASE IDS")
    print("=" * 50)
    
    destinations = check_current_destination_ids()
    attractions = check_current_attraction_ids()
    
    suggest_correct_inserts()
    
    print("\n✅ Check complete!")
    print("\n💡 TIP: Always use the destination IDs shown above when inserting new attractions!")
