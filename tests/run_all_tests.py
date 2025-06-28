"""
Test Suite Runner
مشغل مجموعة الاختبارات الشامل
"""
import sys
import os
import subprocess
from datetime import datetime

# Add project path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestSuiteRunner:
    """Main test suite runner for AI Travel Agent"""
    
    def __init__(self):
        self.test_results = {}
        self.start_time = datetime.now()
    
    def run_health_check(self):
        """Run quick health check"""
        print("🏥 Running Health Check...")
        try:
            from tests.quick_health_check import quick_health_check
            result = quick_health_check()
            self.test_results['health_check'] = result
            return result
        except Exception as e:
            print(f"❌ Health check failed: {e}")
            self.test_results['health_check'] = False
            return False
    
    def run_individual_module_tests(self):
        """Run individual module tests"""
        print("\n🧪 Running Individual Module Tests...")
        try:
            from tests.test_individual_modules import run_individual_module_tests
            result = run_individual_module_tests()
            self.test_results['individual_modules'] = result
            return result
        except Exception as e:
            print(f"❌ Individual module tests failed: {e}")
            self.test_results['individual_modules'] = False
            return False
    
    def run_complete_system_test(self):
        """Run complete system integration test"""
        print("\n🔧 Running Complete System Test...")
        try:
            from tests.test_complete_system import run_complete_system_test
            result = run_complete_system_test()
            self.test_results['complete_system'] = result
            return result
        except Exception as e:
            print(f"❌ Complete system test failed: {e}")
            self.test_results['complete_system'] = False
            return False
    
    def run_performance_check(self):
        """Run basic performance check"""
        print("\n⚡ Running Performance Check...")
        try:
            start_time = datetime.now()
            
            # Test configuration loading speed
            from config import Config
            config_time = (datetime.now() - start_time).total_seconds()
            
            # Test travel agent initialization speed
            init_start = datetime.now()
            from enhanced_features.travel_agent_enhanced import EnhancedTravelAgent
            agent = EnhancedTravelAgent()
            init_time = (datetime.now() - init_start).total_seconds()
            
            print(f"   📊 Configuration Load Time: {config_time:.2f}s")
            print(f"   📊 Agent Initialization Time: {init_time:.2f}s")
            
            # Performance thresholds
            if config_time < 1.0 and init_time < 5.0:
                print("   ✅ Performance within acceptable limits")
                self.test_results['performance'] = True
                return True
            else:
                print("   ⚠️  Performance slower than expected")
                self.test_results['performance'] = False
                return False
                
        except Exception as e:
            print(f"   ❌ Performance check failed: {e}")
            self.test_results['performance'] = False
            return False
    
    def run_security_check(self):
        """Run basic security check"""
        print("\n🔒 Running Security Check...")
        try:
            from config import Config
            
            security_issues = []
            
            # Check if critical keys are set
            if not Config.SECRET_KEY or Config.SECRET_KEY == "your-secret-key-change-this":
                security_issues.append("Weak or default SECRET_KEY")
            
            # Check if debug mode is appropriate
            if Config.DEBUG and os.getenv('FLASK_ENV') == 'production':
                security_issues.append("Debug mode enabled in production")
            
            # Check if API keys are properly configured
            if Config.OPENAI_API_KEY and len(Config.OPENAI_API_KEY) < 20:
                security_issues.append("OpenAI API key seems invalid")
            
            if security_issues:
                print(f"   ⚠️  Security Issues Found:")
                for issue in security_issues:
                    print(f"      - {issue}")
                self.test_results['security'] = False
                return False
            else:
                print("   ✅ No critical security issues found")
                self.test_results['security'] = True
                return True
                
        except Exception as e:
            print(f"   ❌ Security check failed: {e}")
            self.test_results['security'] = False
            return False
    
    def generate_test_report(self):
        """Generate comprehensive test report"""
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()
        
        print("\n📋 COMPREHENSIVE TEST REPORT")
        print("=" * 60)
        print(f"📅 Test Date: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏱️  Duration: {duration:.1f} seconds")
        print("=" * 60)
        
        # Test Results Summary
        print("\n📊 TEST RESULTS SUMMARY:")
        total_tests = len(self.test_results)
        passed_tests = sum(self.test_results.values())
        
        for test_name, result in self.test_results.items():
            status = "✅ PASSED" if result else "❌ FAILED"
            print(f"   {test_name.replace('_', ' ').title()}: {status}")
        
        print(f"\n   Overall: {passed_tests}/{total_tests} tests passed")
        success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        print(f"   Success Rate: {success_rate:.1f}%")
        
        # System Status
        print(f"\n🎯 SYSTEM STATUS:")
        if success_rate >= 90:
            print("   🟢 EXCELLENT - System fully operational")
            status = "excellent"
        elif success_rate >= 75:
            print("   🟡 GOOD - System operational with minor issues")
            status = "good"
        elif success_rate >= 50:
            print("   🟠 FAIR - System partially operational")
            status = "fair"
        else:
            print("   🔴 POOR - System needs major fixes")
            status = "poor"
        
        # Recommendations
        print(f"\n💡 RECOMMENDATIONS:")
        if status == "excellent":
            print("   • System ready for production use")
            print("   • Consider adding optional features")
            print("   • Set up monitoring and logging")
        elif status == "good":
            print("   • Address minor issues for optimal performance")
            print("   • System ready for testing and development")
        elif status == "fair":
            print("   • Fix failing tests before proceeding")
            print("   • Check configuration and dependencies")
        else:
            print("   • Major fixes required")
            print("   • Review setup guide and documentation")
        
        # Next Steps
        print(f"\n🚀 NEXT STEPS:")
        if self.test_results.get('health_check', False):
            print("   ✅ Health check passed - core system working")
        else:
            print("   ❌ Fix health check issues first")
        
        if self.test_results.get('complete_system', False):
            print("   ✅ System integration working - ready for use")
            print("   📋 Try: python enhanced_features/travel_agent_enhanced.py")
            print("   🌐 Try: streamlit run streamlit_ui.py")
        else:
            print("   ⚠️  System integration needs work")
        
        return success_rate >= 75
    
    def run_full_test_suite(self):
        """Run complete test suite"""
        print("🧪 AI Travel Agent - Complete Test Suite")
        print("=" * 60)
        print(f"📅 Started: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        # Run all tests in order
        test_sequence = [
            ("Health Check", self.run_health_check),
            ("Individual Modules", self.run_individual_module_tests),
            ("Complete System", self.run_complete_system_test),
            ("Performance", self.run_performance_check),
            ("Security", self.run_security_check)
        ]
        
        for test_name, test_function in test_sequence:
            print(f"\n🔄 Starting {test_name}...")
            try:
                test_function()
            except Exception as e:
                print(f"💥 {test_name} crashed: {e}")
                self.test_results[test_name.lower().replace(' ', '_')] = False
        
        # Generate final report
        success = self.generate_test_report()
        return success

def main():
    """Main function to run the complete test suite"""
    runner = TestSuiteRunner()
    success = runner.run_full_test_suite()
    
    print(f"\n{'='*60}")
    if success:
        print("🎉 TEST SUITE COMPLETED SUCCESSFULLY!")
        print("✅ Your AI Travel Agent system is ready!")
    else:
        print("⚠️  TEST SUITE COMPLETED WITH ISSUES")
        print("🔧 Please address the issues above before proceeding")
    print(f"{'='*60}")
    
    return success

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
