import os
from supabase import create_client, Client

# Set credentials directly
supabase_url = "https://crpopiicbwzxemaxlgnh.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNycG9waWljYnd6eGVtYXhsZ25oIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA5NTYwMTMsImV4cCI6MjA2NjUzMjAxM30.EX0QIPn46KrnMLLvt-5hA7le_A_sUhMoVZjjCjMP6eY"

# Initialize Supabase client
supabase: Client = create_client(supabase_url, supabase_key)

def check_table_structure():
    """Check the exact column structure of all tables."""
    print("🔍 CHECKING YOUR TABLE STRUCTURES")
    print("=" * 50)
    
    tables = ["destinations", "attractions", "travel_history", "user_preferences"]
    
    for table_name in tables:
        try:
            # Get one record to see the structure
            response = supabase.table(table_name).select("*").limit(1).execute()
            
            print(f"\n📋 {table_name.upper()} TABLE COLUMNS:")
            if response.data:
                columns = list(response.data[0].keys())
                for i, col in enumerate(columns, 1):
                    print(f"  {i}. {col}")
            else:
                print("  (No data to show columns)")
                
            # Count records
            count_response = supabase.table(table_name).select("*").execute()
            print(f"  📊 Records: {len(count_response.data)}")
            
        except Exception as e:
            print(f"  ❌ Error checking {table_name}: {e}")
    
    print("\n" + "=" * 50)
    print("Now I'll generate the correct SQL based on your actual table structure!")

if __name__ == "__main__":
    check_table_structure()
