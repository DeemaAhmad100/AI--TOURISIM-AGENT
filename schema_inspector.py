"""
🔍 Database Schema Inspector
Comprehensive tool to inspect the actual database schema in Supabase
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment
load_dotenv()

# Initialize Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    print("❌ Error: SUPABASE_URL and SUPABASE_KEY must be set in .env file")
    exit(1)

supabase: Client = create_client(supabase_url, supabase_key)

class DatabaseSchemaInspector:
    """Inspect actual database schema"""
    
    def __init__(self):
        self.supabase = supabase
    
    def get_table_structure(self, table_name):
        """Get the actual structure of a table"""
        try:
            # Get a sample record to see the structure
            result = self.supabase.table(table_name).select("*").limit(1).execute()
            
            if result.data and len(result.data) > 0:
                sample_record = result.data[0]
                return list(sample_record.keys())
            else:
                print(f"   ℹ️ {table_name} table exists but has no data to inspect structure")
                return []
                
        except Exception as e:
            print(f"   ❌ Error inspecting {table_name}: {e}")
            return None
    
    def inspect_all_tables(self):
        """Inspect all tables in the database"""
        print("🗃️ DATABASE SCHEMA INSPECTION")
        print("="*80)
        
        # Known tables to check
        tables_to_check = [
            "destinations", "attractions", "hotels", "restaurants", 
            "user_profiles", "users", "airlines", "flights", 
            "car_rentals", "car_rental_companies", "activities",
            "cultural_insights", "seasonal_data", "travel_bookings",
            "price_tracking"
        ]
        
        existing_tables = {}
        
        for table_name in tables_to_check:
            print(f"\n📋 TABLE: {table_name}")
            print("-" * 40)
            
            try:
                # Check if table exists by trying to count records
                result = self.supabase.table(table_name).select("*", count="exact").execute()
                count = result.count if hasattr(result, 'count') else len(result.data)
                
                print(f"✅ Exists | Records: {count}")
                
                # Get structure
                columns = self.get_table_structure(table_name)
                if columns:
                    print(f"📝 Columns ({len(columns)}):")
                    for i, column in enumerate(columns, 1):
                        print(f"   {i:2d}. {column}")
                    existing_tables[table_name] = {
                        "exists": True,
                        "record_count": count,
                        "columns": columns
                    }
                else:
                    existing_tables[table_name] = {
                        "exists": True,
                        "record_count": count,
                        "columns": []
                    }
                
                # Show sample data if exists
                if count > 0 and count < 100:  # Only for small tables
                    sample_result = self.supabase.table(table_name).select("*").limit(2).execute()
                    if sample_result.data:
                        print(f"📊 Sample Data:")
                        for i, record in enumerate(sample_result.data, 1):
                            print(f"   Record {i}:")
                            for key, value in record.items():
                                value_str = str(value)[:50] + "..." if len(str(value)) > 50 else str(value)
                                print(f"     {key}: {value_str}")
                
            except Exception as e:
                error_msg = str(e)
                if "does not exist" in error_msg:
                    print("❌ Does not exist")
                    existing_tables[table_name] = {"exists": False, "error": error_msg}
                else:
                    print(f"⚠️ Error: {error_msg}")
                    existing_tables[table_name] = {"exists": "unknown", "error": error_msg}
        
        return existing_tables
    
    def show_schema_summary(self, tables_info):
        """Show a summary of the database schema"""
        print("\n" + "="*80)
        print("📊 DATABASE SCHEMA SUMMARY")
        print("="*80)
        
        existing_tables = [name for name, info in tables_info.items() if info.get("exists") == True]
        missing_tables = [name for name, info in tables_info.items() if info.get("exists") == False]
        error_tables = [name for name, info in tables_info.items() if info.get("exists") == "unknown"]
        
        print(f"✅ Existing Tables ({len(existing_tables)}):")
        for table in existing_tables:
            count = tables_info[table].get("record_count", 0)
            columns_count = len(tables_info[table].get("columns", []))
            print(f"   • {table}: {count} records, {columns_count} columns")
        
        if missing_tables:
            print(f"\n❌ Missing Tables ({len(missing_tables)}):")
            for table in missing_tables:
                print(f"   • {table}")
        
        if error_tables:
            print(f"\n⚠️ Tables with Errors ({len(error_tables)}):")
            for table in error_tables:
                print(f"   • {table}")
        
        print(f"\n📈 Total Database Records: {sum(info.get('record_count', 0) for info in tables_info.values() if info.get('exists') == True)}")
    
    def show_detailed_schema(self, tables_info):
        """Show detailed schema information"""
        print("\n" + "="*80)
        print("📋 DETAILED SCHEMA BREAKDOWN")
        print("="*80)
        
        for table_name, info in tables_info.items():
            if info.get("exists") == True and info.get("columns"):
                print(f"\n🗂️ {table_name.upper()}")
                print(f"   Records: {info.get('record_count', 0)}")
                print(f"   Columns: {', '.join(info['columns'])}")
    
    def run_complete_inspection(self):
        """Run complete database schema inspection"""
        print("🔍 Starting comprehensive database schema inspection...")
        print()
        
        # Inspect all tables
        tables_info = self.inspect_all_tables()
        
        # Show summaries
        self.show_schema_summary(tables_info)
        self.show_detailed_schema(tables_info)
        
        print("\n" + "="*80)
        print("🎯 SCHEMA INSPECTION COMPLETE")
        print("="*80)
        print("📝 Use this information to understand your current database structure")
        print("🔧 Use database_schema_updater.py to add missing tables/columns")

def main():
    """Main execution function"""
    inspector = DatabaseSchemaInspector()
    inspector.run_complete_inspection()

if __name__ == "__main__":
    main()
