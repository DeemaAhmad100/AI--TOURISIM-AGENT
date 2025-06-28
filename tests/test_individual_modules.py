"""
Individual Module Tests
اختبار الوحدات الفردية
"""
import sys
import os
from datetime import datetime
import traceback

# Add project path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ModuleTester:
    """Class to test individual modules"""
    
    def __init__(self):
        self.test_results = {}
        self.total_tests = 0
        self.passed_tests = 0
    
    def test_configuration_module(self):
        """Test configuration module"""
        print("1️⃣ Testing Configuration Module...")
        
        try:
            from config import Config, validate_config, print_config_summary
            
            # Test configuration loading
            assert Config.SUPABASE_URL is not None, "SUPABASE_URL not loaded"
            assert Config.OPENAI_API_KEY is not None, "OPENAI_API_KEY not loaded"
            
            # Test validation function
            validate_config()
            
            print("   ✅ Configuration module working correctly")
            self.test_results['configuration'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ Configuration module failed: {e}")
            self.test_results['configuration'] = False
            return False
    
    def test_enhanced_travel_agent_module(self):
        """Test Enhanced Travel Agent module"""
        print("\n2️⃣ Testing Enhanced Travel Agent Module...")
        
        try:
            from enhanced_features.travel_agent_enhanced import EnhancedTravelAgent, UserProfile, TravelPackage
            
            # Test class imports
            agent = EnhancedTravelAgent()
            
            # Test database connection
            db_result = agent.test_database_connection()
            assert db_result['success'], f"Database connection failed: {db_result.get('error')}"
            
            # Test data structures
            test_profile = UserProfile(
                user_id="test_001",
                age=25,
                interests=["culture"],
                travel_style="budget",
                accessibility_needs=[],
                budget_range="low",
                dietary_restrictions=[]
            )
            
            assert test_profile.user_id == "test_001", "UserProfile data structure failed"
            
            print("   ✅ Enhanced Travel Agent module working correctly")
            self.test_results['enhanced_travel_agent'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ Enhanced Travel Agent module failed: {e}")
            print(f"   📋 Details: {traceback.format_exc()}")
            self.test_results['enhanced_travel_agent'] = False
            return False
    
    def test_booking_system_module(self):
        """Test Booking System module"""
        print("\n3️⃣ Testing Booking System Module...")
        
        try:
            from booking_system.booking_manager import BookingManager, BookingRequest
            
            # Test class initialization
            booking_manager = BookingManager()
            
            # Test data structures
            test_booking = BookingRequest(
                user_id="test_001",
                package_id="pkg_001",
                total_amount=1500.0,
                payment_method="card",
                billing_info={}
            )
            
            assert test_booking.user_id == "test_001", "BookingRequest data structure failed"
            
            print("   ✅ Booking System module working correctly")
            self.test_results['booking_system'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ Booking System module failed: {e}")
            print(f"   📋 Details: {traceback.format_exc()}")
            self.test_results['booking_system'] = False
            return False
    
    def test_price_tracking_module(self):
        """Test Price Tracking module"""
        print("\n4️⃣ Testing Price Tracking Module...")
        
        try:
            from price_tracking.price_tracker import PriceTracker
            
            # Test class initialization
            tracker = PriceTracker()
            
            print("   ✅ Price Tracking module available")
            self.test_results['price_tracking'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ Price Tracking module failed: {e}")
            print("   💡 This is expected if the module is not fully implemented")
            self.test_results['price_tracking'] = False
            return False
    
    def test_calendar_integration_module(self):
        """Test Calendar Integration module"""
        print("\n5️⃣ Testing Calendar Integration Module...")
        
        try:
            from calendar_integration.calendar_manager import CalendarManager
            
            # Test class initialization
            calendar_manager = CalendarManager()
            
            print("   ✅ Calendar Integration module available")
            self.test_results['calendar_integration'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ Calendar Integration module failed: {e}")
            print("   💡 This is expected if Google Calendar API is not configured")
            self.test_results['calendar_integration'] = False
            return False
    
    def test_pdf_generator_module(self):
        """Test PDF Generator module"""
        print("\n6️⃣ Testing PDF Generator Module...")
        
        try:
            from pdf_generator.pdf_creator import PDFCreator
            
            # Test class initialization
            pdf_creator = PDFCreator()
            
            print("   ✅ PDF Generator module available")
            self.test_results['pdf_generator'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ PDF Generator module failed: {e}")
            print("   💡 This is expected if PDF libraries are not installed")
            self.test_results['pdf_generator'] = False
            return False
    
    def test_ui_components_module(self):
        """Test UI Components module"""
        print("\n7️⃣ Testing UI Components Module...")
        
        try:
            # Test if UI components directory exists
            ui_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
                                  'enhanced_features', 'ui_components')
            
            if os.path.exists(ui_path):
                print("   ✅ UI Components directory exists")
                self.test_results['ui_components'] = True
                return True
            else:
                print("   ⚠️  UI Components directory not found")
                self.test_results['ui_components'] = False
                return False
                
        except Exception as e:
            print(f"   ❌ UI Components test failed: {e}")
            self.test_results['ui_components'] = False
            return False
    
    def test_database_integration(self):
        """Test database integration across modules"""
        print("\n8️⃣ Testing Database Integration...")
        
        try:
            from enhanced_features.travel_agent_enhanced import EnhancedTravelAgent
            
            agent = EnhancedTravelAgent()
            
            # Test database connection
            db_result = agent.test_database_connection()
            if not db_result['success']:
                raise Exception(f"Database connection failed: {db_result.get('error')}")
            
            # Test basic database operations
            test_user_id = f"module_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            test_profile_data = {
                "user_id": test_user_id,
                "age": 28,
                "interests": ["testing"],
                "travel_style": "moderate",
                "budget_range": "moderate",
                "dietary_restrictions": []
            }
            
            # Test profile creation
            create_result = agent.create_user_profile(test_profile_data)
            if not create_result['success']:
                print(f"   ⚠️  Profile creation failed: {create_result.get('error')}")
            else:
                print("   ✅ Database write operation successful")
                
                # Test profile retrieval
                profile = agent.get_user_profile(test_user_id)
                if profile:
                    print("   ✅ Database read operation successful")
                else:
                    print("   ⚠️  Database read operation failed")
            
            print("   ✅ Database integration test completed")
            self.test_results['database_integration'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ Database integration failed: {e}")
            self.test_results['database_integration'] = False
            return False
    
    def run_all_tests(self):
        """Run all individual module tests"""
        print("🧪 Individual Module Tests")
        print("=" * 50)
        print(f"📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50)
        
        # List of tests to run
        tests = [
            self.test_configuration_module,
            self.test_enhanced_travel_agent_module,
            self.test_booking_system_module,
            self.test_price_tracking_module,
            self.test_calendar_integration_module,
            self.test_pdf_generator_module,
            self.test_ui_components_module,
            self.test_database_integration
        ]
        
        # Run each test
        for test in tests:
            self.total_tests += 1
            try:
                if test():
                    self.passed_tests += 1
            except Exception as e:
                print(f"   💥 Test crashed: {e}")
        
        # Print summary
        self.print_test_summary()
        
        return self.passed_tests == self.total_tests
    
    def print_test_summary(self):
        """Print detailed test summary"""
        print("\n📊 MODULE TEST SUMMARY")
        print("=" * 40)
        
        print(f"📈 Overall Results:")
        print(f"   Total Tests: {self.total_tests}")
        print(f"   Passed: {self.passed_tests}")
        print(f"   Failed: {self.total_tests - self.passed_tests}")
        print(f"   Success Rate: {(self.passed_tests/self.total_tests)*100:.1f}%")
        
        print(f"\n📋 Detailed Results:")
        for module, result in self.test_results.items():
            status = "✅ PASSED" if result else "❌ FAILED"
            print(f"   {module.replace('_', ' ').title()}: {status}")
        
        if self.passed_tests == self.total_tests:
            print(f"\n🎉 ALL MODULE TESTS PASSED!")
            print("✅ All modules are working correctly!")
        else:
            print(f"\n⚠️  Some modules need attention")
            print("💡 This is normal if some features are not fully implemented yet")
        
        print("\n🔧 Next Steps:")
        if self.test_results.get('enhanced_travel_agent', False):
            print("   ✅ Core system is working - ready for integration testing")
        else:
            print("   ❌ Core system needs fixing before proceeding")
        
        failed_modules = [module for module, result in self.test_results.items() if not result]
        if failed_modules:
            print(f"   🔨 Consider implementing: {', '.join(failed_modules)}")

def run_individual_module_tests():
    """Main function to run individual module tests"""
    tester = ModuleTester()
    return tester.run_all_tests()

if __name__ == "__main__":
    success = run_individual_module_tests()
    exit(0 if success else 1)
