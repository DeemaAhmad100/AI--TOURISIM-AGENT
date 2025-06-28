"""
Environment Variables Management Helper
مساعد إدارة المتغيرات البيئية
"""
import os
from typing import Dict, List, Tuple

class EnvManager:
    """Helper class to manage environment variables"""
    
    @staticmethod
    def check_required_vars() -> Tuple[List[str], List[str]]:
        """Check which required variables are missing"""
        
        # Critical variables (النظام لن يعمل بدونها)
        critical_vars = [
            "SUPABASE_URL",
            "SUPABASE_KEY", 
            "OPENAI_API_KEY"
        ]
        
        # Optional variables (النظام سيعمل لكن بعض الميزات ستكون معطلة)
        optional_vars = [
            "STRIPE_SECRET_KEY",
            "EMAIL_USER",
            "EMAIL_PASS",
            "GOOGLE_CALENDAR_CLIENT_ID",
            "AMADEUS_API_KEY",
            "TWILIO_ACCOUNT_SID",
            "MAPBOX_API_KEY"
        ]
        
        missing_critical = []
        missing_optional = []
        
        for var in critical_vars:
            if not os.getenv(var):
                missing_critical.append(var)
        
        for var in optional_vars:
            if not os.getenv(var):
                missing_optional.append(var)
        
        return missing_critical, missing_optional
    
    @staticmethod
    def get_api_key_instructions() -> Dict[str, str]:
        """Get instructions for obtaining API keys"""
        
        return {
            "SUPABASE_URL": "Visit https://app.supabase.com → Your Project → Settings → API",
            "SUPABASE_KEY": "Visit https://app.supabase.com → Your Project → Settings → API",
            "OPENAI_API_KEY": "Visit https://platform.openai.com/api-keys",
            "STRIPE_SECRET_KEY": "Visit https://dashboard.stripe.com/apikeys",
            "EMAIL_USER": "Your Gmail address (enable 2FA and create app password)",
            "EMAIL_PASS": "Gmail app-specific password (not your regular password)",
            "GOOGLE_CALENDAR_CLIENT_ID": "Visit https://console.cloud.google.com → APIs & Services → Credentials",
            "AMADEUS_API_KEY": "Visit https://developers.amadeus.com",
            "TWILIO_ACCOUNT_SID": "Visit https://console.twilio.com",
            "MAPBOX_API_KEY": "Visit https://account.mapbox.com/access-tokens/"
        }
    
    @staticmethod
    def print_setup_guide():
        """Print setup guide for missing variables"""
        missing_critical, missing_optional = EnvManager.check_required_vars()
        instructions = EnvManager.get_api_key_instructions()
        
        print("🔧 AI Travel Agent - Setup Guide")
        print("=" * 50)
        
        if missing_critical:
            print("❌ CRITICAL: Missing required variables:")
            print("   (النظام لن يعمل بدون هذه المفاتيح)")
            for var in missing_critical:
                print(f"\n📍 {var}:")
                print(f"   Instructions: {instructions.get(var, 'Check documentation')}")
            
            print(f"\n💡 Add these to your .env file like this:")
            for var in missing_critical:
                print(f"{var}=your_actual_key_here")
        
        if missing_optional:
            print(f"\n⚠️  OPTIONAL: Missing optional variables:")
            print("   (بعض الميزات ستكون معطلة)")
            for var in missing_optional:
                print(f"\n📍 {var}:")
                print(f"   Instructions: {instructions.get(var, 'Check documentation')}")
                print(f"   Feature impact: {EnvManager.get_feature_impact(var)}")
        
        if not missing_critical and not missing_optional:
            print("🎉 All variables are configured!")
        
        print("\n" + "=" * 50)
    
    @staticmethod
    def get_feature_impact(var_name: str) -> str:
        """Get description of what feature will be affected"""
        
        impact_map = {
            "STRIPE_SECRET_KEY": "Payment processing disabled",
            "EMAIL_USER": "Email notifications disabled", 
            "EMAIL_PASS": "Email notifications disabled",
            "GOOGLE_CALENDAR_CLIENT_ID": "Calendar integration disabled",
            "AMADEUS_API_KEY": "Flight price tracking disabled",
            "TWILIO_ACCOUNT_SID": "SMS notifications disabled",
            "MAPBOX_API_KEY": "Maps in PDF guides disabled"
        }
        
        return impact_map.get(var_name, "Some features may be limited")
    
    @staticmethod
    def create_env_template():
        """Create .env template with placeholders"""
        
        template_content = """# ==================== CRITICAL VARIABLES ====================
# These are required for the system to work (مطلوبة لعمل النظام)

# Supabase Database
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key

# OpenAI for AI features
OPENAI_API_KEY=sk-your-openai-key

# ==================== OPTIONAL VARIABLES ====================
# These enable additional features (تفعل ميزات إضافية)

# Payment Processing (معالجة المدفوعات)
STRIPE_SECRET_KEY=sk_test_your_stripe_key
STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_key

# Email Notifications (إشعارات البريد الإلكتروني)
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_specific_password

# Google Calendar Integration (تكامل تقويم جوجل)
GOOGLE_CALENDAR_CLIENT_ID=your_google_client_id
GOOGLE_CALENDAR_CLIENT_SECRET=your_google_client_secret

# Price Tracking APIs (متابعة الأسعار)
AMADEUS_API_KEY=your_amadeus_key
SKYSCANNER_API_KEY=your_skyscanner_key

# SMS Notifications (إشعارات الرسائل النصية)
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token

# Maps for PDF Guides (الخرائط في دلائل السفر)
MAPBOX_API_KEY=your_mapbox_key

# ==================== APPLICATION SETTINGS ====================
DEBUG=True
LOG_LEVEL=INFO
DEFAULT_CURRENCY=USD
DEFAULT_LANGUAGE=en
"""
        
        try:
            with open('.env.template', 'w', encoding='utf-8') as f:
                f.write(template_content)
            print("✅ Created .env.template file")
            print("💡 Copy this to .env and fill in your API keys")
        except Exception as e:
            print(f"❌ Error creating template: {e}")

def main():
    """Main function to run environment setup"""
    print("🔧 Environment Variables Setup Helper")
    print("=" * 50)
    
    # Check current status
    EnvManager.print_setup_guide()
    
    # Create template if needed
    if not os.path.exists('.env'):
        print("\n📝 No .env file found. Creating template...")
        EnvManager.create_env_template()
        print("💡 Please copy .env.template to .env and fill in your keys")
    
    print(f"\n✅ Setup guide completed!")

if __name__ == "__main__":
    main()
