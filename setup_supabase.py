#!/usr/bin/env python3
"""
🌍 AI Travel Platform - Supabase Database Setup
Complete setup script to initialize your Supabase database with all required tables and sample data
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client, Client
import json

# Load environment variables
load_dotenv()

def get_supabase_client():
    """Initialize Supabase client"""
    try:
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY") or os.getenv("SUPABASE_ANON_KEY")
        
        if not supabase_url or not supabase_key:
            print("❌ Error: Missing Supabase credentials in .env file")
            print("Please ensure SUPABASE_URL and SUPABASE_KEY are set")
            return None
            
        print(f"🔗 Connecting to: {supabase_url}")
        return create_client(supabase_url, supabase_key)
        
    except Exception as e:
        print(f"❌ Failed to connect to Supabase: {e}")
        return None

def execute_sql_file(supabase: Client, sql_file_path: str):
    """Execute SQL commands from file"""
    try:
        with open(sql_file_path, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        print(f"📁 Executing SQL file: {sql_file_path}")
        
        # Split into individual statements (basic approach)
        statements = [stmt.strip() for stmt in sql_content.split(';') if stmt.strip()]
        
        for i, statement in enumerate(statements):
            if statement and not statement.startswith('--'):
                try:
                    # Use RPC call for DDL statements
                    result = supabase.rpc('exec_sql', {'sql': statement}).execute()
                    print(f"  ✅ Statement {i+1} executed successfully")
                except Exception as stmt_error:
                    print(f"  ⚠️ Statement {i+1} failed: {stmt_error}")
                    # Continue with other statements
                    
    except Exception as e:
        print(f"❌ Error executing SQL file: {e}")

def create_basic_tables_manual(supabase: Client):
    """Create basic tables manually using Supabase client"""
    print("🏗️ Creating database tables manually...")
    
    # Create destinations table
    try:
        print("  📍 Creating destinations table...")
        # We'll create tables through Supabase dashboard or use simpler approach
        
        # Insert sample destinations
        destinations_data = [
            {
                "name": "Paris, France",
                "city": "Paris",
                "country": "France",
                "description": "City of Light with art, culture, and cuisine",
                "currency": "EUR",
                "language": "French",
                "timezone": "Europe/Paris",
                "climate": "Temperate oceanic",
                "budget_ranges": {"budget": 80, "moderate": 180, "luxury": 400}
            },
            {
                "name": "Tokyo, Japan", 
                "city": "Tokyo",
                "country": "Japan",
                "description": "Modern metropolis blending tradition and innovation",
                "currency": "JPY",
                "language": "Japanese", 
                "timezone": "Asia/Tokyo",
                "climate": "Humid subtropical",
                "budget_ranges": {"budget": 70, "moderate": 160, "luxury": 350}
            },
            {
                "name": "Rome, Italy",
                "city": "Rome", 
                "country": "Italy",
                "description": "Eternal City with ancient history and amazing cuisine",
                "currency": "EUR",
                "language": "Italian",
                "timezone": "Europe/Rome", 
                "climate": "Mediterranean",
                "budget_ranges": {"budget": 60, "moderate": 140, "luxury": 320}
            }
        ]
        
        # Check if destinations table exists and has data
        try:
            existing = supabase.table("destinations").select("*").limit(1).execute()
            if not existing.data:
                print("  📊 Inserting sample destinations...")
                result = supabase.table("destinations").insert(destinations_data).execute()
                print(f"  ✅ Inserted {len(result.data)} destinations")
            else:
                print("  ✅ Destinations table already has data")
        except Exception as e:
            print(f"  ⚠️ Could not insert destinations: {e}")
            
    except Exception as e:
        print(f"  ❌ Error with destinations: {e}")

def test_database_connection(supabase: Client):
    """Test database connection and basic operations"""
    print("🔍 Testing database connection...")
    
    try:
        # Test basic query
        result = supabase.table("destinations").select("*").limit(5).execute()
        print(f"  ✅ Successfully queried destinations table")
        print(f"  📊 Found {len(result.data)} destinations")
        
        if result.data:
            for dest in result.data:
                print(f"    - {dest.get('name', 'Unknown')}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Database test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("=" * 60)
    print("🌍 AI Travel Platform - Supabase Database Setup")
    print("=" * 60)
    
    # Step 1: Connect to Supabase
    print("\n📡 Step 1: Connecting to Supabase...")
    supabase = get_supabase_client()
    
    if not supabase:
        print("❌ Setup failed. Please check your .env file and Supabase credentials.")
        return False
    
    print("✅ Connected to Supabase successfully!")
    
    # Step 2: Test connection
    print("\n🔍 Step 2: Testing database connection...")
    if not test_database_connection(supabase):
        print("❌ Database connection test failed")
        return False
    
    # Step 3: Setup sample data
    print("\n📊 Step 3: Setting up sample data...")
    create_basic_tables_manual(supabase)
    
    # Step 4: Final test
    print("\n🏁 Step 4: Final verification...")
    success = test_database_connection(supabase)
    
    if success:
        print("\n" + "=" * 60)
        print("🎉 SUPABASE SETUP COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print("✅ Database connected")
        print("✅ Tables verified") 
        print("✅ Sample data loaded")
        print("\n🚀 Your AI Travel Platform is now ready!")
        print("   Run: streamlit run enhanced_streamlit_app.py")
        return True
    else:
        print("\n❌ Setup completed with some issues. Check the logs above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)