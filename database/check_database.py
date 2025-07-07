#!/usr/bin/env python3
"""
🔍 Database Connection Checker - AI Travel Platform
Quick script to verify database setup and connection status
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Load environment
load_dotenv()

def check_database_status():
    """Check complete database status"""
    print("🔍 AI Travel Platform - Database Status Check")
    print("=" * 50)
    
    # Check environment variables
    print("\n📋 Environment Configuration:")
    
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    
    print(f"   SUPABASE_URL: {'✅ Set' if supabase_url else '❌ Missing'}")
    print(f"   SUPABASE_KEY: {'✅ Set' if supabase_key else '❌ Missing'}")
    print(f"   OPENAI_API_KEY: {'✅ Set' if openai_key else '❌ Missing'}")
    
    # Check Supabase connection
    print("\n🔌 Database Connection:")
    
    if not supabase_url or not supabase_key:
        print("   ❌ Supabase credentials missing")
        print("   💡 Add SUPABASE_URL and SUPABASE_KEY to .env file")
        return False
    
    try:
        from supabase import create_client
        supabase = create_client(supabase_url, supabase_key)
        
        # Test connection
        result = supabase.table("destinations").select("count", count="exact").execute()
        print("   ✅ Supabase connection successful")
        
        # Check tables
        print("\n🗄️ Database Tables:")
        
        essential_tables = [
            "users", "user_profiles", "destinations", "hotels", 
            "restaurants", "bookings", "travel_bookings"
        ]
        
        table_status = {}
        for table in essential_tables:
            try:
                result = supabase.table(table).select("count", count="exact").execute()
                count = result.count if hasattr(result, 'count') else 0
                table_status[table] = count
                print(f"   ✅ {table}: {count} records")
            except Exception as e:
                table_status[table] = "ERROR"
                print(f"   ❌ {table}: {str(e)[:50]}...")
        
        # Check platform integration
        print("\n🚀 Platform Integration:")
        
        try:
            from src.core.platform_core import supabase as platform_supabase
            if platform_supabase:
                print("   ✅ Platform database connection active")
            else:
                print("   ⚠️ Platform database connection inactive")
        except Exception as e:
            print(f"   ❌ Platform integration error: {e}")
        
        # Summary
        print("\n📊 Summary:")
        working_tables = len([t for t in table_status.values() if t != "ERROR"])
        total_tables = len(essential_tables)
        
        print(f"   📋 Tables: {working_tables}/{total_tables} working")
        print(f"   🔗 Connection: {'✅ Active' if working_tables > 0 else '❌ Failed'}")
        
        if working_tables == total_tables:
            print("   🎉 Database setup is complete and working!")
            return True
        elif working_tables > 0:
            print("   ⚠️ Database partially working - some tables missing")
            return False
        else:
            print("   ❌ Database setup incomplete")
            return False
            
    except Exception as e:
        print(f"   ❌ Connection failed: {e}")
        return False

def check_platform_status():
    """Check if platform can run"""
    print("\n🌍 Platform Status:")
    
    try:
        # Check if platform core can be imported
        from src.core.platform_core import TravelPlatformUI
        print("   ✅ Platform core imports successfully")
        
        # Check if demo can run
        from demos.experience_demo import main as demo_main
        print("   ✅ Demo system available")
        
        # Check API keys
        openai_key = os.getenv("OPENAI_API_KEY")
        if openai_key:
            print("   ✅ OpenAI API key configured")
        else:
            print("   ⚠️ OpenAI API key missing (demo mode available)")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Platform check failed: {e}")
        return False

def provide_recommendations():
    """Provide setup recommendations"""
    print("\n💡 Recommendations:")
    
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")
    
    if not supabase_url or not supabase_key:
        print("   📋 Database Setup:")
        print("      1. Create Supabase project: https://supabase.com")
        print("      2. Add credentials to .env file")
        print("      3. Run: python database/setup_database.py")
    
    if not openai_key:
        print("   🤖 AI Features:")
        print("      1. Get OpenAI API key: https://platform.openai.com")
        print("      2. Add OPENAI_API_KEY to .env file")
    
    print("   🚀 Quick Start:")
    print("      • Demo mode: python demos/experience_demo.py")
    print("      • Full platform: python src/core/platform_core.py")
    print("      • Database setup: python database/setup_database.py")

def main():
    """Main function"""
    try:
        db_status = check_database_status()
        platform_status = check_platform_status()
        provide_recommendations()
        
        print("\n" + "=" * 50)
        
        if db_status and platform_status:
            print("🎉 Status: READY FOR PRODUCTION")
            print("✅ All systems operational")
            print("🚀 Run: python src/core/platform_core.py")
        elif platform_status:
            print("⚠️ Status: DEMO MODE READY")
            print("🎮 Database not configured, but demos work")
            print("🚀 Run: python demos/experience_demo.py")
        else:
            print("❌ Status: SETUP REQUIRED")
            print("🔧 Complete setup steps above")
            print("📖 See: database/DATABASE_SETUP_GUIDE.md")
        
        return db_status and platform_status
        
    except Exception as e:
        print(f"❌ Check failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
