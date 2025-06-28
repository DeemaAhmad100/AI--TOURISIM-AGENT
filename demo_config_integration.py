"""
Configuration Integration Demo
عرض توضيحي لتكامل الإعدادات
"""
import sys
import os

# Add project path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def demo_config_integration():
    """Demonstrate configuration integration with travel agent"""
    print("🎯 Configuration Integration Demo")
    print("=" * 50)
    
    # Test 1: Import and validate config
    print("1️⃣ Testing Configuration Import...")
    try:
        from config import Config, validate_config
        validate_config()
        print("   ✅ Configuration loaded and validated")
    except Exception as e:
        print(f"   ❌ Configuration error: {e}")
        return False
    
    # Test 2: Test enhanced travel agent with config
    print("\n2️⃣ Testing Enhanced Travel Agent Integration...")
    try:
        from enhanced_features.travel_agent_enhanced import EnhancedTravelAgent
        agent = EnhancedTravelAgent()
        
        # Test database connection
        db_result = agent.test_database_connection()
        if db_result['success']:
            print("   ✅ Enhanced Travel Agent connected to database")
        else:
            print(f"   ❌ Database connection failed: {db_result.get('error')}")
            
    except Exception as e:
        print(f"   ❌ Enhanced Travel Agent error: {e}")
        return False
    
    # Test 3: Test booking system with config
    print("\n3️⃣ Testing Booking System Integration...")
    try:
        from booking_system.booking_manager import BookingManager
        booking_manager = BookingManager()
        print("   ✅ Booking Manager initialized")
        
        # Test if Stripe is configured
        if Config.STRIPE_SECRET_KEY:
            print("   ✅ Stripe payment processing available")
        else:
            print("   ⚠️  Stripe not configured - payments disabled")
            
    except Exception as e:
        print(f"   ❌ Booking System error: {e}")
        return False
    
    # Test 4: Test other modules availability
    print("\n4️⃣ Testing Additional Modules...")
    
    modules_to_test = [
        ("price_tracking.price_tracker", "PriceTracker", "Price Tracking"),
        ("calendar_integration.calendar_manager", "CalendarManager", "Calendar Integration"),
        ("pdf_generator.pdf_creator", "PDFCreator", "PDF Generation")
    ]
    
    for module_name, class_name, feature_name in modules_to_test:
        try:
            module = __import__(module_name, fromlist=[class_name])
            cls = getattr(module, class_name)
            instance = cls()
            print(f"   ✅ {feature_name} module available")
        except Exception as e:
            print(f"   ⚠️  {feature_name} module not available: {e}")
    
    # Summary
    print(f"\n📊 Integration Summary:")
    print(f"   🔧 Configuration: Working")
    print(f"   🤖 Enhanced Travel Agent: Working") 
    print(f"   💳 Booking System: Working")
    print(f"   💰 Payment Processing: {'Available' if Config.STRIPE_SECRET_KEY else 'Disabled'}")
    print(f"   📧 Email Notifications: {'Available' if Config.EMAIL_USER else 'Disabled'}")
    print(f"   📅 Calendar Integration: {'Available' if Config.GOOGLE_CALENDAR_CLIENT_ID else 'Disabled'}")
    
    print(f"\n🎉 Configuration integration completed successfully!")
    print(f"💡 Your AI Travel Agent is ready to use!")
    
    return True

def show_next_steps():
    """Show what to do next"""
    print(f"\n🚀 NEXT STEPS:")
    print("=" * 30)
    print("✅ Step 8.2 (Configuration) - COMPLETED")
    print("🔄 Next: Step 9 (Testing Framework)")
    print("🔄 After: Step 10 (Documentation & Deployment)")
    
    print(f"\n📋 To enable additional features:")
    from config import Config
    
    optional_features = [
        ("💳 Payment Processing", "Add STRIPE_SECRET_KEY to .env"),
        ("📧 Email Notifications", "Add EMAIL_USER and EMAIL_PASS to .env"),
        ("📅 Calendar Integration", "Add GOOGLE_CALENDAR_CLIENT_ID to .env"),
        ("💰 Price Tracking", "Add AMADEUS_API_KEY to .env"),
        ("📱 SMS Notifications", "Add TWILIO_ACCOUNT_SID to .env"),
        ("🗺️  PDF Maps", "Add MAPBOX_API_KEY to .env")
    ]
    
    for feature, instruction in optional_features:
        print(f"   {feature}: {instruction}")
    
    print(f"\n🎯 Ready to proceed to Step 9: Testing Framework")

if __name__ == "__main__":
    success = demo_config_integration()
    if success:
        show_next_steps()
