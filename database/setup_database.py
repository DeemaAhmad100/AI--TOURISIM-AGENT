#!/usr/bin/env python3
"""
🗄️ AI Travel Platform - Database Setup Script
Automated database setup and initialization for production deployment

This script handles:
- Database schema creation
- Data population
- Configuration verification
- Health checks
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

class DatabaseSetup:
    """Complete database setup and initialization"""
    
    def __init__(self):
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_KEY")
        self.project_root = Path(__file__).parent.parent
        self.schema_file = self.project_root / "database" / "schemas" / "enhanced_database_schema.sql"
        self.supabase: Optional[Client] = None
        
        # Setup logging
        self.setup_log = []
        
    def log(self, message: str, level: str = "INFO"):
        """Log setup messages"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}"
        self.setup_log.append(log_entry)
        print(log_entry)
    
    def check_prerequisites(self) -> bool:
        """Check if all prerequisites are met"""
        self.log("🔍 Checking prerequisites...")
        
        # Check environment variables
        if not self.supabase_url:
            self.log("❌ SUPABASE_URL not found in environment", "ERROR")
            return False
        
        if not self.supabase_key:
            self.log("❌ SUPABASE_KEY not found in environment", "ERROR")
            return False
        
        # Check schema file exists
        if not self.schema_file.exists():
            self.log(f"❌ Schema file not found: {self.schema_file}", "ERROR")
            return False
        
        # Check Supabase connection
        try:
            self.supabase = create_client(self.supabase_url, self.supabase_key)
            # Test connection with a simple query
            result = self.supabase.table("destinations").select("count", count="exact").execute()
            self.log("✅ Supabase connection successful")
            return True
        except Exception as e:
            self.log(f"❌ Supabase connection failed: {e}", "ERROR")
            return False
    
    def backup_existing_data(self) -> bool:
        """Backup existing data before schema changes"""
        self.log("💾 Backing up existing data...")
        
        try:
            backup_dir = self.project_root / "database" / "backups"
            backup_dir.mkdir(exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = backup_dir / f"backup_{timestamp}.json"
            
            # Get existing tables
            existing_tables = [
                "destinations", "attractions", "hotels", "restaurants", 
                "user_profiles", "flights", "price_tracking", "travel_bookings"
            ]
            
            backup_data = {}
            for table in existing_tables:
                try:
                    result = self.supabase.table(table).select("*").execute()
                    backup_data[table] = result.data
                    self.log(f"✅ Backed up {len(result.data)} records from {table}")
                except Exception as e:
                    self.log(f"⚠️ Could not backup {table}: {e}", "WARNING")
            
            # Save backup
            import json
            with open(backup_file, 'w') as f:
                json.dump(backup_data, f, indent=2, default=str)
            
            self.log(f"✅ Backup saved to: {backup_file}")
            return True
            
        except Exception as e:
            self.log(f"❌ Backup failed: {e}", "ERROR")
            return False
    
    def execute_schema(self) -> bool:
        """Execute the database schema"""
        self.log("🏗️ Executing database schema...")
        
        try:
            # Read schema file
            with open(self.schema_file, 'r', encoding='utf-8') as f:
                schema_sql = f.read()
            
            # Split into individual statements
            statements = [stmt.strip() for stmt in schema_sql.split(';') if stmt.strip()]
            
            successful_statements = 0
            failed_statements = 0
            
            for i, statement in enumerate(statements):
                try:
                    # Skip comments and empty statements
                    if statement.startswith('--') or statement.startswith('/*') or not statement:
                        continue
                    
                    # Execute statement
                    self.supabase.postgrest.rpc("exec_sql", {"query": statement}).execute()
                    successful_statements += 1
                    
                    # Log progress every 10 statements
                    if (i + 1) % 10 == 0:
                        self.log(f"📊 Progress: {i + 1}/{len(statements)} statements executed")
                
                except Exception as e:
                    failed_statements += 1
                    self.log(f"⚠️ Statement {i+1} failed: {str(e)[:100]}...", "WARNING")
                    continue
            
            self.log(f"✅ Schema execution completed: {successful_statements} successful, {failed_statements} failed")
            return successful_statements > 0
            
        except Exception as e:
            self.log(f"❌ Schema execution failed: {e}", "ERROR")
            return False
    
    def create_schema_alternative(self) -> bool:
        """Alternative schema creation using individual table creation"""
        self.log("🔄 Using alternative schema creation method...")
        
        try:
            # Create tables individually
            tables_created = 0
            
            # Core tables with their SQL
            core_tables = {
                "users": """
                CREATE TABLE IF NOT EXISTS users (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    user_id VARCHAR(255) UNIQUE NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    name VARCHAR(255) NOT NULL,
                    phone VARCHAR(50),
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
                )
                """,
                "user_profiles": """
                CREATE TABLE IF NOT EXISTS user_profiles (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    user_id VARCHAR(255) UNIQUE NOT NULL,
                    name VARCHAR(255) NOT NULL,
                    age INTEGER NOT NULL,
                    interests TEXT[] DEFAULT '{}',
                    travel_style VARCHAR(100) DEFAULT 'cultural',
                    budget_range VARCHAR(50) DEFAULT 'moderate',
                    accessibility_needs TEXT[] DEFAULT '{}',
                    dietary_restrictions TEXT[] DEFAULT '{}',
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
                )
                """,
                "bookings": """
                CREATE TABLE IF NOT EXISTS bookings (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    booking_type VARCHAR(50) NOT NULL,
                    user_id VARCHAR(255) NOT NULL,
                    item_id UUID NOT NULL,
                    details JSONB NOT NULL,
                    total_amount DECIMAL(10,2) NOT NULL,
                    currency VARCHAR(10) DEFAULT 'USD',
                    status VARCHAR(20) DEFAULT 'pending',
                    confirmation_number VARCHAR(100) UNIQUE NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
                )
                """,
                "travel_bookings": """
                CREATE TABLE IF NOT EXISTS travel_bookings (
                    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    destination VARCHAR(255) NOT NULL,
                    duration INTEGER NOT NULL,
                    total_price DECIMAL(10,2) NOT NULL,
                    savings DECIMAL(10,2) DEFAULT 0,
                    flight_details JSONB,
                    hotel_details JSONB,
                    booking_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
                    status VARCHAR(20) DEFAULT 'confirmed',
                    user_id VARCHAR(255)
                )
                """
            }
            
            # Create each table
            for table_name, sql in core_tables.items():
                try:
                    # Use raw SQL execution
                    result = self.supabase.postgrest.rpc("exec_sql", {"query": sql}).execute()
                    tables_created += 1
                    self.log(f"✅ Created table: {table_name}")
                except Exception as e:
                    self.log(f"⚠️ Could not create {table_name}: {e}", "WARNING")
            
            self.log(f"✅ Created {tables_created} core tables")
            return tables_created > 0
            
        except Exception as e:
            self.log(f"❌ Alternative schema creation failed: {e}", "ERROR")
            return False
    
    def verify_schema(self) -> bool:
        """Verify that the schema was created correctly"""
        self.log("🔍 Verifying schema...")
        
        try:
            # Check if key tables exist
            essential_tables = ["users", "user_profiles", "bookings", "travel_bookings"]
            
            for table in essential_tables:
                try:
                    result = self.supabase.table(table).select("count", count="exact").execute()
                    count = result.count if hasattr(result, 'count') else 0
                    self.log(f"✅ Table '{table}' exists with {count} records")
                except Exception as e:
                    self.log(f"❌ Table '{table}' verification failed: {e}", "ERROR")
                    return False
            
            self.log("✅ Schema verification completed successfully")
            return True
            
        except Exception as e:
            self.log(f"❌ Schema verification failed: {e}", "ERROR")
            return False
    
    def populate_sample_data(self) -> bool:
        """Populate database with sample data"""
        self.log("📊 Populating sample data...")
        
        try:
            # Insert sample admin user
            try:
                admin_user = {
                    "user_id": "admin",
                    "email": "admin@aitravelplatform.com",
                    "name": "AI Travel Platform Admin",
                    "phone": "+1-555-0100"
                }
                
                result = self.supabase.table("users").upsert(admin_user).execute()
                self.log("✅ Created admin user")
            except Exception as e:
                self.log(f"⚠️ Could not create admin user: {e}", "WARNING")
            
            # Insert sample destinations if destinations table exists
            try:
                sample_destinations = [
                    {
                        "name": "Paris, France",
                        "country": "France",
                        "city": "Paris",
                        "description": "The City of Light",
                        "safety_rating": 8,
                        "cost_level": "expensive"
                    },
                    {
                        "name": "Tokyo, Japan", 
                        "country": "Japan",
                        "city": "Tokyo",
                        "description": "Modern metropolis",
                        "safety_rating": 9,
                        "cost_level": "expensive"
                    }
                ]
                
                for dest in sample_destinations:
                    try:
                        result = self.supabase.table("destinations").upsert(dest).execute()
                        self.log(f"✅ Added destination: {dest['name']}")
                    except Exception as e:
                        self.log(f"⚠️ Could not add destination {dest['name']}: {e}", "WARNING")
                        
            except Exception as e:
                self.log(f"⚠️ Could not populate destinations: {e}", "WARNING")
            
            return True
            
        except Exception as e:
            self.log(f"❌ Sample data population failed: {e}", "ERROR")
            return False
    
    def run_setup(self) -> bool:
        """Run the complete database setup"""
        self.log("🚀 Starting AI Travel Platform Database Setup")
        self.log("=" * 50)
        
        # Step 1: Check prerequisites
        if not self.check_prerequisites():
            self.log("❌ Prerequisites check failed", "ERROR")
            return False
        
        # Step 2: Backup existing data
        if not self.backup_existing_data():
            self.log("⚠️ Backup failed, continuing anyway...", "WARNING")
        
        # Step 3: Execute schema
        schema_success = self.execute_schema()
        if not schema_success:
            self.log("⚠️ Primary schema execution failed, trying alternative method...")
            schema_success = self.create_schema_alternative()
        
        if not schema_success:
            self.log("❌ Schema creation failed", "ERROR")
            return False
        
        # Step 4: Verify schema
        if not self.verify_schema():
            self.log("❌ Schema verification failed", "ERROR")
            return False
        
        # Step 5: Populate sample data
        if not self.populate_sample_data():
            self.log("⚠️ Sample data population failed, but continuing...", "WARNING")
        
        # Success!
        self.log("=" * 50)
        self.log("🎉 Database setup completed successfully!")
        self.log("✅ Your AI Travel Platform is ready for production!")
        self.log("📊 Check your Supabase dashboard for the created tables")
        self.log("🚀 You can now run: python src/core/platform_core.py")
        
        return True
    
    def save_setup_log(self):
        """Save setup log to file"""
        log_dir = self.project_root / "database" / "logs"
        log_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"setup_log_{timestamp}.txt"
        
        with open(log_file, 'w') as f:
            f.write("AI Travel Platform Database Setup Log\n")
            f.write("=" * 50 + "\n\n")
            for entry in self.setup_log:
                f.write(entry + "\n")
        
        print(f"📝 Setup log saved to: {log_file}")

def main():
    """Main function"""
    print("🌍 AI Travel Platform Database Setup")
    print("=" * 40)
    
    setup = DatabaseSetup()
    
    try:
        success = setup.run_setup()
        setup.save_setup_log()
        
        if success:
            print("\n🎉 Setup completed successfully!")
            print("💡 Next steps:")
            print("   1. Check your Supabase dashboard")
            print("   2. Run: python src/core/platform_core.py")
            print("   3. Or try: python demos/experience_demo.py")
            sys.exit(0)
        else:
            print("\n❌ Setup failed. Check the log for details.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n⚠️ Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
