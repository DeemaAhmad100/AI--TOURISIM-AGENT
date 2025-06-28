"""
Configuration settings for Enhanced AI Travel Agent
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class for all API keys and settings"""
    
    # ==================== DATABASE ====================
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    
    # ==================== AI & LANGUAGE MODELS ====================
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
    
    # ==================== PAYMENT PROCESSING ====================
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
    STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")
    STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
    
    # ==================== EMAIL CONFIGURATION ====================
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
    SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    EMAIL_FROM = os.getenv("EMAIL_FROM", EMAIL_USER)
    
    # ==================== GOOGLE CALENDAR ====================
    GOOGLE_CALENDAR_CLIENT_ID = os.getenv("GOOGLE_CALENDAR_CLIENT_ID")
    GOOGLE_CALENDAR_CLIENT_SECRET = os.getenv("GOOGLE_CALENDAR_CLIENT_SECRET")
    GOOGLE_CALENDAR_REDIRECT_URI = os.getenv("GOOGLE_CALENDAR_REDIRECT_URI", "http://localhost:8080/callback")
    
    # ==================== PRICE TRACKING APIs ====================
    AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
    AMADEUS_API_SECRET = os.getenv("AMADEUS_API_SECRET")
    SKYSCANNER_API_KEY = os.getenv("SKYSCANNER_API_KEY")
    BOOKING_API_KEY = os.getenv("BOOKING_API_KEY")
    
    # ==================== SMS & NOTIFICATIONS ====================
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
    
    # ==================== MAPS & LOCATION ====================
    MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY")
    GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
    
    # ==================== FILE STORAGE ====================
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "travel-agent-files")
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    
    # ==================== APPLICATION SETTINGS ====================
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-this")
    
    # ==================== RATE LIMITING ====================
    API_RATE_LIMIT = int(os.getenv("API_RATE_LIMIT", "100"))  # requests per minute
    PRICE_CHECK_INTERVAL = int(os.getenv("PRICE_CHECK_INTERVAL", "3600"))  # seconds
    
    # ==================== PDF GENERATION ====================
    PDF_TEMPLATE_PATH = os.getenv("PDF_TEMPLATE_PATH", "templates/pdf_templates/")
    PDF_OUTPUT_PATH = os.getenv("PDF_OUTPUT_PATH", "generated_pdfs/")
    PDF_FONT_PATH = os.getenv("PDF_FONT_PATH", "fonts/")
    
    # ==================== CACHE SETTINGS ====================
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    CACHE_TTL = int(os.getenv("CACHE_TTL", "3600"))  # seconds
    
    # ==================== CURRENCY & LOCALIZATION ====================
    DEFAULT_CURRENCY = os.getenv("DEFAULT_CURRENCY", "USD")
    SUPPORTED_CURRENCIES = ["USD", "EUR", "GBP", "CAD", "AUD", "JPY"]
    DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")
    SUPPORTED_LANGUAGES = ["en", "ar", "es", "fr", "de"]

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    LOG_LEVEL = "DEBUG"

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    LOG_LEVEL = "WARNING"

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    LOG_LEVEL = "DEBUG"
    # Use test database
    SUPABASE_URL = os.getenv("TEST_SUPABASE_URL", Config.SUPABASE_URL)
    SUPABASE_KEY = os.getenv("TEST_SUPABASE_KEY", Config.SUPABASE_KEY)

# Configuration mapping
config_map = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

def get_config(environment=None):
    """Get configuration based on environment"""
    if environment is None:
        environment = os.getenv('FLASK_ENV', 'development')
    
    return config_map.get(environment, DevelopmentConfig)

def validate_config():
    """Validate required configuration variables"""
    print("🔍 Validating configuration...")
    
    # Critical variables that must be present
    required_vars = [
        ("SUPABASE_URL", Config.SUPABASE_URL),
        ("SUPABASE_KEY", Config.SUPABASE_KEY),
        ("OPENAI_API_KEY", Config.OPENAI_API_KEY)
    ]
    
    # Important but optional variables
    optional_vars = [
        ("STRIPE_SECRET_KEY", Config.STRIPE_SECRET_KEY, "Payment processing"),
        ("EMAIL_USER", Config.EMAIL_USER, "Email notifications"),
        ("GOOGLE_CALENDAR_CLIENT_ID", Config.GOOGLE_CALENDAR_CLIENT_ID, "Calendar integration"),
        ("AMADEUS_API_KEY", Config.AMADEUS_API_KEY, "Flight price tracking"),
        ("TWILIO_ACCOUNT_SID", Config.TWILIO_ACCOUNT_SID, "SMS notifications"),
        ("MAPBOX_API_KEY", Config.MAPBOX_API_KEY, "Maps in PDF guides")
    ]
    
    missing_required = []
    missing_optional = []
    
    # Check required variables
    for var_name, var_value in required_vars:
        if not var_value:
            missing_required.append(var_name)
        else:
            print(f"  ✅ {var_name}: Configured")
    
    # Check optional variables
    for var_name, var_value, feature in optional_vars:
        if not var_value:
            missing_optional.append((var_name, feature))
        else:
            print(f"  ✅ {var_name}: Configured")
    
    # Report results
    if missing_required:
        print(f"\n❌ Missing REQUIRED environment variables:")
        for var in missing_required:
            print(f"  - {var}")
        raise ValueError(f"Missing required environment variables: {', '.join(missing_required)}")
    
    if missing_optional:
        print(f"\n⚠️  Missing OPTIONAL environment variables:")
        for var, feature in missing_optional:
            print(f"  - {var} (needed for: {feature})")
        print("\n💡 These features will be disabled but the system will still work.")
    
    print(f"\n✅ Configuration validation completed!")
    return True

def print_config_summary():
    """Print a summary of current configuration"""
    print("\n📋 CONFIGURATION SUMMARY")
    print("=" * 50)
    
    print(f"🔧 Environment: {os.getenv('FLASK_ENV', 'development')}")
    print(f"🐛 Debug Mode: {Config.DEBUG}")
    print(f"📊 Log Level: {Config.LOG_LEVEL}")
    print(f"💰 Default Currency: {Config.DEFAULT_CURRENCY}")
    print(f"🌐 Default Language: {Config.DEFAULT_LANGUAGE}")
    
    print(f"\n🔌 INTEGRATIONS STATUS:")
    integrations = [
        ("Database (Supabase)", bool(Config.SUPABASE_URL and Config.SUPABASE_KEY)),
        ("AI (OpenAI)", bool(Config.OPENAI_API_KEY)),
        ("Payments (Stripe)", bool(Config.STRIPE_SECRET_KEY)),
        ("Email", bool(Config.EMAIL_USER and Config.EMAIL_PASS)),
        ("Calendar (Google)", bool(Config.GOOGLE_CALENDAR_CLIENT_ID)),
        ("Price Tracking (Amadeus)", bool(Config.AMADEUS_API_KEY)),
        ("SMS (Twilio)", bool(Config.TWILIO_ACCOUNT_SID)),
        ("Maps (Mapbox)", bool(Config.MAPBOX_API_KEY))
    ]
    
    for integration, status in integrations:
        status_icon = "✅" if status else "❌"
        print(f"  {status_icon} {integration}")
    
    print("=" * 50)

def create_sample_env_file():
    """Create a sample .env file with all required variables"""
    sample_content = """# ==================== CORE SETTINGS ====================
# Supabase Database
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key

# OpenAI for AI features
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_TEMPERATURE=0.7

# ==================== PAYMENT PROCESSING ====================
# Stripe for payments
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret

# ==================== EMAIL & NOTIFICATIONS ====================
# Email configuration (Gmail example)
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_specific_password
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587

# SMS notifications (Twilio)
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number

# ==================== GOOGLE SERVICES ====================
# Google Calendar Integration
GOOGLE_CALENDAR_CLIENT_ID=your_google_client_id
GOOGLE_CALENDAR_CLIENT_SECRET=your_google_client_secret

# Google Maps for location services
GOOGLE_MAPS_API_KEY=your_google_maps_api_key

# ==================== TRAVEL APIs ====================
# Amadeus for flight data
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_API_SECRET=your_amadeus_api_secret

# Skyscanner for price comparison
SKYSCANNER_API_KEY=your_skyscanner_api_key

# Booking.com for hotels
BOOKING_API_KEY=your_booking_api_key

# ==================== MAPS & VISUALIZATION ====================
# Mapbox for PDF maps
MAPBOX_API_KEY=your_mapbox_api_key

# ==================== OPTIONAL SETTINGS ====================
# Application settings
DEBUG=True
LOG_LEVEL=INFO
SECRET_KEY=your-secret-key-change-this-in-production

# AWS for file storage (optional)
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_BUCKET_NAME=travel-agent-files
AWS_REGION=us-east-1

# Cache settings
REDIS_URL=redis://localhost:6379
CACHE_TTL=3600

# Localization
DEFAULT_CURRENCY=USD
DEFAULT_LANGUAGE=en

# Rate limiting
API_RATE_LIMIT=100
PRICE_CHECK_INTERVAL=3600
"""
    
    try:
        with open('.env.example', 'w', encoding='utf-8') as f:
            f.write(sample_content)
        print("✅ Created .env.example file with all configuration options")
        print("💡 Copy this to .env and fill in your actual API keys")
    except Exception as e:
        print(f"❌ Error creating .env.example: {e}")

# Test function
def test_config():
    """Test configuration loading"""
    print("🧪 Testing configuration...")
    
    try:
        validate_config()
        print_config_summary()
        print("✅ Configuration test passed!")
        return True
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

if __name__ == "__main__":
    print("🔧 AI Travel Agent Configuration")
    print("=" * 40)
    
    # Test configuration
    test_config()
    
    # Create sample env file
    print("\n📝 Creating sample environment file...")
    create_sample_env_file()
