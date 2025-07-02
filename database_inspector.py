"""
🔍 Database Schema Inspector
Script to check the actual structure of existing Supabase tables
"""

import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Initialize Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    print("❌ Error: SUPABASE_URL and SUPABASE_KEY must be set in .env file")
    exit(1)

supabase: Client = create_client(supabase_url, supabase_key)

def inspect_table_structure():
    """Inspect the structure of existing tables"""
    print("🔍 Database Schema Inspector")
    print("="*50)
    
    tables_to_inspect = ["destinations", "attractions", "hotels", "restaurants", "user_profiles"]
    
    for table_name in tables_to_inspect:
        print(f"\n📋 Table: {table_name}")
        print("-" * 30)
        
        try:
            # Get a sample record to see the structure
            result = self.supabase.table(table_name).select("*").limit(1).execute()
            
            if result.data and len(result.data) > 0:
                sample_record = result.data[0]
                print("📝 Existing columns:")
                for column, value in sample_record.items():
                    value_type = type(value).__name__
                    value_preview = str(value)[:50] + "..." if len(str(value)) > 50 else str(value)
                    print(f"   • {column}: {value_type} = {value_preview}")
            else:
                print("   ℹ️ Table exists but has no data")
                
        except Exception as e:
            print(f"   ❌ Error inspecting {table_name}: {e}")

def check_destinations_sample():
    """Check what's in destinations table"""
    print("\n🌍 Sample Destinations Data:")
    print("-" * 40)
    
    try:
        result = supabase.table("destinations").select("*").limit(3).execute()
        
        if result.data:
            for i, dest in enumerate(result.data, 1):
                print(f"\n{i}. {dest.get('name', 'Unknown')}")
                for key, value in dest.items():
                    if key != 'name':
                        print(f"   {key}: {value}")
        else:
            print("   No destinations found")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")

def check_attractions_sample():
    """Check what's in attractions table"""
    print("\n🏛️ Sample Attractions Data:")
    print("-" * 40)
    
    try:
        result = supabase.table("attractions").select("*").limit(3).execute()
        
        if result.data:
            for i, attraction in enumerate(result.data, 1):
                print(f"\n{i}. {attraction.get('name', 'Unknown')}")
                for key, value in attraction.items():
                    if key != 'name':
                        print(f"   {key}: {value}")
        else:
            print("   No attractions found")
            
    except Exception as e:
        print(f"   ❌ Error: {e}")

def main():
    """Main execution"""
    inspect_table_structure()
    check_destinations_sample()
    check_attractions_sample()

if __name__ == "__main__":
    main()
