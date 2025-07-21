"""
🔧 Database Schema Updater
Script to update Supabase database with missing tables and columns for enhanced AI features
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

class DatabaseSchemaUpdater:
    """Updates database schema to support enhanced AI features"""
    
    def __init__(self):
        self.supabase = supabase
    
    def update_destinations_table(self):
        """Add missing columns to destinations table"""
        print("🔧 Updating destinations table...")
        
        sql_commands = [
            """
            ALTER TABLE destinations 
            ADD COLUMN IF NOT EXISTS region VARCHAR,
            ADD COLUMN IF NOT EXISTS languages TEXT[],
            ADD COLUMN IF NOT EXISTS best_months TEXT[],
            ADD COLUMN IF NOT EXISTS peak_season TEXT[],
            ADD COLUMN IF NOT EXISTS budget_range JSONB,
            ADD COLUMN IF NOT EXISTS cultural_highlights TEXT[],
            ADD COLUMN IF NOT EXISTS travel_warnings TEXT[],
            ADD COLUMN IF NOT EXISTS visa_requirements JSONB,
            ADD COLUMN IF NOT EXISTS accessibility_rating INTEGER,
            ADD COLUMN IF NOT EXISTS family_friendly BOOLEAN DEFAULT TRUE,
            ADD COLUMN IF NOT EXISTS solo_travel_safe BOOLEAN DEFAULT TRUE;
            """,
            """
            -- Update coordinates to use JSONB for easier access
            ALTER TABLE destinations 
            ADD COLUMN IF NOT EXISTS coordinates JSONB;
            """
        ]
        
        for sql in sql_commands:
            try:
                result = self.supabase.rpc('exec_sql', {'sql': sql}).execute()
                print("✅ Destinations table updated successfully")
                return True
            except Exception as e:
                print(f"⚠️ Destinations update: {e}")
        return False
    
    def update_attractions_table(self):
        """Add missing columns to attractions table"""
        print("🔧 Updating attractions table...")
        
        sql_commands = [
            """
            ALTER TABLE attractions 
            ADD COLUMN IF NOT EXISTS destination VARCHAR,
            ADD COLUMN IF NOT EXISTS coordinates JSONB,
            ADD COLUMN IF NOT EXISTS price_range VARCHAR,
            ADD COLUMN IF NOT EXISTS duration_hours INTEGER,
            ADD COLUMN IF NOT EXISTS best_time VARCHAR,
            ADD COLUMN IF NOT EXISTS crowd_level VARCHAR,
            ADD COLUMN IF NOT EXISTS tourist_trap_score INTEGER,
            ADD COLUMN IF NOT EXISTS local_authenticity INTEGER,
            ADD COLUMN IF NOT EXISTS cultural_significance INTEGER,
            ADD COLUMN IF NOT EXISTS photo_worthiness INTEGER,
            ADD COLUMN IF NOT EXISTS accessibility_rating INTEGER,
            ADD COLUMN IF NOT EXISTS seasonal_notes JSONB,
            ADD COLUMN IF NOT EXISTS insider_tips TEXT[];
            """
        ]
        
        for sql in sql_commands:
            try:
                result = self.supabase.rpc('exec_sql', {'sql': sql}).execute()
                print("✅ Attractions table updated successfully")
                return True
            except Exception as e:
                print(f"⚠️ Attractions update: {e}")
        return False
    
    def create_missing_tables(self):
        """Create tables that don't exist"""
        print("🏗️ Creating missing tables...")
        
        # Cultural insights table
        cultural_insights_sql = """
        CREATE TABLE IF NOT EXISTS cultural_insights (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            destination VARCHAR NOT NULL,
            cultural_category VARCHAR NOT NULL,
            insight_type VARCHAR NOT NULL,
            content TEXT NOT NULL,
            importance_level INTEGER CHECK (importance_level >= 1 AND importance_level <= 10),
            traveler_type VARCHAR DEFAULT 'all',
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        );
        """
        
        # Seasonal data table
        seasonal_data_sql = """
        CREATE TABLE IF NOT EXISTS seasonal_data (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            destination VARCHAR NOT NULL,
            month VARCHAR NOT NULL,
            temperature_avg INTEGER,
            temperature_range JSONB,
            rainfall_mm INTEGER,
            humidity_percent INTEGER,
            daylight_hours INTEGER,
            crowd_level VARCHAR,
            price_multiplier DECIMAL(3,2),
            seasonal_highlights TEXT[],
            what_to_pack TEXT[],
            local_events TEXT[],
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        );
        """
        
        # Activities table
        activities_sql = """
        CREATE TABLE IF NOT EXISTS activities (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            name VARCHAR NOT NULL,
            destination VARCHAR NOT NULL,
            category VARCHAR NOT NULL,
            description TEXT,
            duration_hours INTEGER,
            price_range VARCHAR,
            difficulty_level VARCHAR,
            group_size JSONB,
            what_included TEXT[],
            booking_required BOOLEAN DEFAULT FALSE,
            advance_booking_days INTEGER,
            personality_match JSONB,
            local_authenticity INTEGER,
            tourist_trap_score INTEGER,
            best_time VARCHAR,
            seasonal_availability VARCHAR,
            anti_tourist_trap BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        );
        """
        
        tables = [
            ("cultural_insights", cultural_insights_sql),
            ("seasonal_data", seasonal_data_sql),
            ("activities", activities_sql)
        ]
        
        success_count = 0
        for table_name, sql in tables:
            try:
                result = self.supabase.rpc('exec_sql', {'sql': sql}).execute()
                print(f"✅ Created {table_name} table")
                success_count += 1
            except Exception as e:
                print(f"⚠️ Creating {table_name}: {e}")
        
        return success_count == len(tables)
    
    def update_hotels_table(self):
        """Add missing columns to hotels table"""
        print("🔧 Updating hotels table...")
        
        sql_commands = [
            """
            ALTER TABLE hotels 
            ADD COLUMN IF NOT EXISTS destination VARCHAR,
            ADD COLUMN IF NOT EXISTS category VARCHAR,
            ADD COLUMN IF NOT EXISTS rating DECIMAL(2,1),
            ADD COLUMN IF NOT EXISTS booking_platforms JSONB,
            ADD COLUMN IF NOT EXISTS customer_reviews JSONB,
            ADD COLUMN IF NOT EXISTS check_in_time VARCHAR,
            ADD COLUMN IF NOT EXISTS check_out_time VARCHAR,
            ADD COLUMN IF NOT EXISTS cancellation_policy VARCHAR;
            """,
            """
            -- Update coordinates to use JSONB
            ALTER TABLE hotels 
            ADD COLUMN IF NOT EXISTS coordinates JSONB;
            """
        ]
        
        for sql in sql_commands:
            try:
                result = self.supabase.rpc('exec_sql', {'sql': sql}).execute()
                print("✅ Hotels table updated successfully")
                return True
            except Exception as e:
                print(f"⚠️ Hotels update: {e}")
        return False
    
    def update_restaurants_table(self):
        """Add missing columns to restaurants table"""
        print("🔧 Updating restaurants table...")
        
        sql_commands = [
            """
            ALTER TABLE restaurants 
            ADD COLUMN IF NOT EXISTS destination VARCHAR,
            ADD COLUMN IF NOT EXISTS location VARCHAR,
            ADD COLUMN IF NOT EXISTS specialties TEXT[],
            ADD COLUMN IF NOT EXISTS dietary_options TEXT[],
            ADD COLUMN IF NOT EXISTS atmosphere VARCHAR,
            ADD COLUMN IF NOT EXISTS customer_reviews JSONB,
            ADD COLUMN IF NOT EXISTS opening_hours JSONB,
            ADD COLUMN IF NOT EXISTS booking_required BOOLEAN DEFAULT FALSE,
            ADD COLUMN IF NOT EXISTS booking_url TEXT,
            ADD COLUMN IF NOT EXISTS local_favorite BOOLEAN DEFAULT FALSE,
            ADD COLUMN IF NOT EXISTS tourist_trap_score INTEGER,
            ADD COLUMN IF NOT EXISTS michelin_stars INTEGER;
            """,
            """
            -- Update coordinates to use JSONB
            ALTER TABLE restaurants 
            ADD COLUMN IF NOT EXISTS coordinates JSONB;
            """
        ]
        
        for sql in sql_commands:
            try:
                result = self.supabase.rpc('exec_sql', {'sql': sql}).execute()
                print("✅ Restaurants table updated successfully")
                return True
            except Exception as e:
                print(f"⚠️ Restaurants update: {e}")
        return False
    
    def update_user_profiles_table(self):
        """Add missing columns to user_profiles table"""
        print("🔧 Updating user_profiles table...")
        
        sql_commands = [
            """
            ALTER TABLE user_profiles 
            ADD COLUMN IF NOT EXISTS user_id VARCHAR,
            ADD COLUMN IF NOT EXISTS name VARCHAR,
            ADD COLUMN IF NOT EXISTS personality_traits JSONB,
            ADD COLUMN IF NOT EXISTS previous_destinations TEXT[],
            ADD COLUMN IF NOT EXISTS travel_frequency VARCHAR;
            """
        ]
        
        for sql in sql_commands:
            try:
                result = self.supabase.rpc('exec_sql', {'sql': sql}).execute()
                print("✅ User profiles table updated successfully")
                return True
            except Exception as e:
                print(f"⚠️ User profiles update: {e}")
        return False
    
    def create_exec_sql_function(self):
        """Create a function to execute SQL if it doesn't exist"""
        print("🔧 Creating SQL execution function...")
        
        function_sql = """
        CREATE OR REPLACE FUNCTION exec_sql(sql text)
        RETURNS text
        LANGUAGE plpgsql
        SECURITY DEFINER
        AS $$
        BEGIN
            EXECUTE sql;
            RETURN 'SQL executed successfully';
        END;
        $$;
        """
        
        try:
            # Try to create the function using raw SQL
            result = self.supabase.rpc('exec_sql', {'sql': function_sql}).execute()
            print("✅ SQL execution function created")
            return True
        except Exception as e:
            print(f"⚠️ Function creation: {e}")
            print("📝 Note: You may need to create this function manually in Supabase")
            return False
    
    def run_schema_update(self):
        """Run complete schema update"""
        print("🔧 Database Schema Update for Enhanced AI Features")
        print("="*70)
        
        # Try to create the exec function first
        self.create_exec_sql_function()
        
        operations = [
            ("Create Missing Tables", self.create_missing_tables),
            ("Update Destinations", self.update_destinations_table),
            ("Update Attractions", self.update_attractions_table),
            ("Update Hotels", self.update_hotels_table),
            ("Update Restaurants", self.update_restaurants_table),
            ("Update User Profiles", self.update_user_profiles_table)
        ]
        
        success_count = 0
        for operation_name, operation_func in operations:
            try:
                if operation_func():
                    success_count += 1
            except Exception as e:
                print(f"❌ Failed {operation_name}: {e}")
        
        print(f"\n🎉 Schema update completed!")
        print(f"✅ Successfully completed {success_count}/{len(operations)} operations")
        
        if success_count < len(operations):
            print("\n⚠️ Some operations failed. You may need to run SQL commands manually in Supabase.")
            print("📝 Alternative: Use the enhanced_database_schema.sql file")

def main():
    """Main execution function"""
    print("🔧 Enhanced AI Travel Platform - Database Schema Update")
    print("="*70)
    
    updater = DatabaseSchemaUpdater()
    updater.run_schema_update()

if __name__ == "__main__":
    main()
