"""
Test Configuration Setup
اختبار إعدادات التكوين
"""
import sys
import os

# Add project path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_config_import():
    """Test configuration import"""
    print("🧪 Testing config.py import...")
    try:
        from config import Config, validate_config, print_config_summary
        print("✅ Config imported successfully!")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_environment_variables():
    """Test environment variables loading"""
    print("\n🔍 Testing environment variables...")
    try:
        from config import Config
        
        # Test critical variables
        critical_vars = [
            ("SUPABASE_URL", Config.SUPABASE_URL),
            ("SUPABASE_KEY", Config.SUPABASE_KEY),
            ("OPENAI_API_KEY", Config.OPENAI_API_KEY)
        ]
        
        for var_name, var_value in critical_vars:
            if var_value:
                print(f"  ✅ {var_name}: Loaded")
            else:
                print(f"  ❌ {var_name}: Missing")
        
        return True
    except Exception as e:
        print(f"❌ Error testing environment variables: {e}")
        return False

def test_config_validation():
    """Test configuration validation"""
    print("\n🔐 Testing configuration validation...")
    try:
        from config import validate_config
        validate_config()
        return True
    except Exception as e:
        print(f"❌ Validation error: {e}")
        print("💡 This is expected if you haven't filled in all API keys yet")
        return False

def test_config_summary():
    """Test configuration summary"""
    print("\n📋 Testing configuration summary...")
    try:
        from config import print_config_summary
        print_config_summary()
        return True
    except Exception as e:
        print(f"❌ Summary error: {e}")
        return False

def main():
    """Run all configuration tests"""
    print("🔧 AI Travel Agent - Configuration Test")
    print("=" * 50)
    
    tests = [
        test_config_import,
        test_environment_variables,
        test_config_summary,
        test_config_validation
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test failed: {e}")
            results.append(False)
    
    # Summary
    passed = sum(results)
    total = len(results)
    
    print(f"\n📊 TEST RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All configuration tests passed!")
        print("✅ Your configuration is ready!")
    else:
        print("⚠️  Some tests failed, but this might be expected")
        print("💡 Missing API keys will disable certain features")
        print("🔧 You can add API keys later as needed")
    
    return passed == total

if __name__ == "__main__":
    main()
