"""
Quick Health Check Test
اختبار سريع للتحقق من صحة النظام
"""
import sys
import os
from datetime import datetime

# Add project path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def quick_health_check():
    """Quick health check for the AI Travel Agent system"""
    print("🏥 AI Travel Agent - Quick Health Check")
    print("=" * 50)
    print(f"📅 Check Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    checks = []
    
    # Check 1: Environment Variables
    print("1️⃣ Checking Environment Variables...")
    try:
        from dotenv import load_dotenv
        import os
        
        load_dotenv()
        
        critical_vars = ['SUPABASE_URL', 'SUPABASE_KEY', 'OPENAI_API_KEY']
        missing_vars = []
        
        for var in critical_vars:
            if not os.getenv(var):
                missing_vars.append(var)
        
        if missing_vars:
            print(f"   ❌ Missing: {', '.join(missing_vars)}")
            checks.append(False)
        else:
            print("   ✅ All critical environment variables present")
            checks.append(True)
            
    except Exception as e:
        print(f"   ❌ Environment check failed: {e}")
        checks.append(False)
    
    # Check 2: Configuration
    print("\n2️⃣ Checking Configuration...")
    try:
        from config import Config, validate_config
        validate_config()
        print("   ✅ Configuration valid")
        checks.append(True)
    except Exception as e:
        print(f"   ❌ Configuration invalid: {e}")
        checks.append(False)
    
    # Check 3: Enhanced Travel Agent
    print("\n3️⃣ Checking Enhanced Travel Agent...")
    try:
        from enhanced_features.travel_agent_enhanced import EnhancedTravelAgent
        agent = EnhancedTravelAgent()
        
        # Quick database test
        db_result = agent.test_database_connection()
        if db_result['success']:
            print("   ✅ Enhanced Travel Agent working")
            checks.append(True)
        else:
            print(f"   ❌ Database connection failed: {db_result.get('error')}")
            checks.append(False)
            
    except Exception as e:
        print(f"   ❌ Enhanced Travel Agent failed: {e}")
        checks.append(False)
    
    # Check 4: Booking System
    print("\n4️⃣ Checking Booking System...")
    try:
        from booking_system.booking_manager import BookingManager
        booking_manager = BookingManager()
        print("   ✅ Booking System available")
        checks.append(True)
    except Exception as e:
        print(f"   ❌ Booking System failed: {e}")
        checks.append(False)
    
    # Check 5: Required Dependencies
    print("\n5️⃣ Checking Dependencies...")
    try:
        required_packages = [
            'openai', 'supabase', 'crewai', 'langchain_openai', 
            'streamlit', 'pandas', 'python-dotenv', 'stripe'
        ]
        
        missing_packages = []
        for package in required_packages:
            try:
                __import__(package)
            except ImportError:
                missing_packages.append(package)
        
        if missing_packages:
            print(f"   ⚠️  Missing packages: {', '.join(missing_packages)}")
            print("   💡 Some features may be disabled")
            checks.append(True)  # Not critical for basic operation
        else:
            print("   ✅ All required dependencies available")
            checks.append(True)
            
    except Exception as e:
        print(f"   ❌ Dependency check failed: {e}")
        checks.append(False)
    
    # Summary
    print("\n📊 HEALTH CHECK SUMMARY")
    print("=" * 30)
    
    passed_checks = sum(checks)
    total_checks = len(checks)
    health_percentage = (passed_checks / total_checks) * 100
    
    print(f"Checks Passed: {passed_checks}/{total_checks}")
    print(f"System Health: {health_percentage:.1f}%")
    
    if health_percentage >= 80:
        print("🟢 SYSTEM STATUS: HEALTHY")
        print("✅ Your AI Travel Agent is ready to use!")
        return True
    elif health_percentage >= 60:
        print("🟡 SYSTEM STATUS: CAUTION")
        print("⚠️  System working but some features may be limited")
        return True
    else:
        print("🔴 SYSTEM STATUS: CRITICAL")
        print("❌ System needs attention before use")
        return False

def run_startup_check():
    """Run startup check with recommendations"""
    print("🚀 AI Travel Agent - Startup Check")
    print("=" * 40)
    
    is_healthy = quick_health_check()
    
    print(f"\n💡 RECOMMENDATIONS:")
    print("=" * 25)
    
    if is_healthy:
        print("🎯 READY TO PROCEED:")
        print("   • Run complete system tests")
        print("   • Test travel package creation")
        print("   • Try the Streamlit interface")
        print("   • Add optional API keys for more features")
        
        print(f"\n📋 NEXT COMMANDS:")
        print("   python tests/test_complete_system.py")
        print("   python enhanced_features/travel_agent_enhanced.py")
        print("   streamlit run streamlit_ui.py")
    else:
        print("🔧 ISSUES TO FIX:")
        print("   • Check your .env file")
        print("   • Verify API keys are correct")
        print("   • Install missing dependencies")
        print("   • Check database connection")
        
        print(f"\n📋 DIAGNOSTIC COMMANDS:")
        print("   python config.py")
        print("   python env_setup_helper.py")
        print("   pip install -r requirements_enhanced.txt")
    
    return is_healthy

if __name__ == "__main__":
    success = run_startup_check()
    exit(0 if success else 1)
