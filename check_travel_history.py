import os
from supabase import create_client, Client

# Set credentials directly
supabase_url = "https://crpopiicbwzxemaxlgnh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNycG9waWljYnd6eGVtYXhsZ25oIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA5NTYwMTMsImV4cCI6MjA2NjUzMjAxM30.EX0QIPn46KrnMLLvt-5hA7le_A_sUhMoVZjjCjMP6eY"

# Initialize Supabase client
supabase: Client = create_client(supabase_url, supabase_key)

def check_travel_history_structure():
    """Insert a test record to see the travel_history table structure."""
    print("🔍 CHECKING TRAVEL_HISTORY TABLE STRUCTURE")
    print("=" * 50)
    
    try:
        # Try to insert a minimal test record to see what columns are required
        test_data = {
            "destination": "Test City",
            "travel_dates": "2025-07-01",
            "duration_days": 3,
            "preferences": "Cultural",
            "budget": "moderate"
        }
        
        # Try the insert
        result = supabase.table("travel_history").insert(test_data).execute()
        
        if result.data:
            print("✅ Test insert successful!")
            print("📋 TRAVEL_HISTORY TABLE COLUMNS:")
            columns = list(result.data[0].keys())
            for i, col in enumerate(columns, 1):
                print(f"  {i}. {col}")
            
            # Delete the test record
            record_id = result.data[0]['id']
            supabase.table("travel_history").delete().eq("id", record_id).execute()
            print("\n✅ Test record cleaned up")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Let me try a different approach...")
        
        # Try to get table info another way
        try:
            # Try inserting with different field combinations
            minimal_data = {
                "destination": "Test",
                "duration_days": 1
            }
            result2 = supabase.table("travel_history").insert(minimal_data).execute()
            print("Alternative insert worked:", result2.data)
        except Exception as e2:
            print(f"Alternative error: {e2}")

if __name__ == "__main__":
    check_travel_history_structure()
