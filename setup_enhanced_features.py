#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
from pathlib import Path

def setup_enhanced_features():
    """
    Enhanced Features Setup Script
    This script sets up all the enhanced features for the AI Travel Platform
    """
    
    print("🚀 Setting up Enhanced Features for AI Travel Platform")
    print("=" * 60)
    
    # Create directory structure
    directories = [
        "src/utils",
        "src/integrations", 
        "src/ui",
        "tests",
        "config"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")
    
    # Create enhanced configuration file
    config = {
        "enhanced_features": {
            "email_service": {
                "enabled": True,
                "providers": ["sendgrid", "smtp"],
                "fallback_enabled": True
            },
            "payment_processing": {
                "enabled": True,
                "providers": ["stripe"],
                "currencies": ["USD", "EUR", "GBP"]
            },
            "google_services": {
                "calendar": True,
                "maps": True,
                "places": True
            },
            "travel_apis": {
                "flights": ["amadeus"],
                "hotels": ["booking"],
                "real_time_data": True
            }
        },
        "security": {
            "rate_limiting": True,
            "api_key_rotation": True,
            "webhook_verification": True
        },
        "monitoring": {
            "error_tracking": True,
            "performance_monitoring": True,
            "uptime_monitoring": True
        }
    }
    
    with open("config/enhanced_features.json", "w", encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    
    print("✓ Created enhanced features configuration")
    
    # Create environment template
    env_template = """# AI Travel Platform - Enhanced Features Environment Variables

# === CORE CONFIGURATION ===
OPENAI_API_KEY=your_openai_api_key_here
SUPABASE_URL=your_supabase_url_here
SUPABASE_KEY=your_supabase_key_here

# === EMAIL SERVICES ===
# Option 1: SendGrid (Recommended for Production)
SENDGRID_API_KEY=your_sendgrid_api_key_here
SENDGRID_FROM_EMAIL=noreply@yourdomain.com

# Option 2: Gmail SMTP (Development)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_specific_password_here
EMAIL_USE_TLS=True

# === PAYMENT PROCESSING ===
STRIPE_PUBLISHABLE_KEY=pk_test_your_publishable_key_here
STRIPE_SECRET_KEY=sk_test_your_secret_key_here
STRIPE_WEBHOOK_SECRET=whsec_your_webhook_secret_here

# === GOOGLE SERVICES ===
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
GOOGLE_CALENDAR_API_KEY=your_google_calendar_api_key_here
GOOGLE_PLACES_API_KEY=your_google_places_api_key_here

# === TRAVEL APIS ===
AMADEUS_CLIENT_ID=your_amadeus_client_id_here
AMADEUS_CLIENT_SECRET=your_amadeus_client_secret_here
BOOKING_API_KEY=your_booking_api_key_here
BOOKING_SECRET=your_booking_secret_here

# === SECURITY & MONITORING ===
SENTRY_DSN=your_sentry_dsn_here
WEBHOOK_SECRET=your_webhook_secret_here
RATE_LIMIT_PER_MINUTE=100
"""
    
    with open(".env.enhanced", "w", encoding='utf-8') as f:
        f.write(env_template)
    
    print("✓ Created .env.enhanced template")
    
    # Create setup verification script
    verification_script = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Enhanced Features Verification Script
Run this script to verify all enhanced features are properly configured
'''

import os
import sys
from pathlib import Path

def verify_setup():
    print("Verifying Enhanced Features Setup...")
    
    # Check environment variables
    required_vars = [
        'OPENAI_API_KEY',
        'SUPABASE_URL', 
        'SUPABASE_KEY'
    ]
    
    optional_vars = [
        'SENDGRID_API_KEY',
        'STRIPE_SECRET_KEY',
        'GOOGLE_MAPS_API_KEY',
        'AMADEUS_CLIENT_ID'
    ]
    
    print("\\nRequired Environment Variables:")
    for var in required_vars:
        if os.getenv(var):
            print(f"✓ {var}")
        else:
            print(f"✗ {var} - MISSING")
    
    print("\\nOptional Environment Variables:")
    for var in optional_vars:
        if os.getenv(var):
            print(f"✓ {var}")
        else:
            print(f"○ {var} - Not configured")
    
    # Check directory structure
    print("\\nDirectory Structure:")
    directories = [
        "src/utils",
        "src/integrations",
        "src/ui", 
        "tests",
        "config"
    ]
    
    for directory in directories:
        if Path(directory).exists():
            print(f"✓ {directory}")
        else:
            print(f"✗ {directory} - Missing")
    
    print("\\nSetup verification complete!")

if __name__ == "__main__":
    verify_setup()
"""
    
    with open("verify_setup.py", "w", encoding='utf-8') as f:
        f.write(verification_script)
    
    os.chmod("verify_setup.py", 0o755)
    print("✓ Created setup verification script")
    
    # Create requirements for enhanced features
    enhanced_requirements = """# Enhanced Features Dependencies

# Email Services
sendgrid==6.10.0

# Payment Processing
stripe==5.5.0

# Google Services
google-api-python-client==2.95.0
google-auth-httplib2==0.1.0
google-auth-oauthlib==1.0.0
googlemaps==4.10.0

# Travel APIs
amadeus==8.0.0
requests==2.31.0

# Security & Monitoring
sentry-sdk==1.32.0
python-dotenv==1.0.0

# Additional utilities
Pillow==10.0.0
python-dateutil==2.8.2
"""
    
    with open("requirements.enhanced.txt", "w", encoding='utf-8') as f:
        f.write(enhanced_requirements)
    
    print("✓ Created enhanced requirements file")
    
    print("\n" + "=" * 60)
    print("🎉 Enhanced Features Setup Complete!")
    print("=" * 60)
    print("\nNext Steps:")
    print("1. Copy .env.enhanced to .env and fill in your API keys")
    print("2. Install enhanced dependencies: pip install -r requirements.enhanced.txt")
    print("3. Run verification script: python verify_setup.py")
    print("4. Follow the API_KEYS_GUIDE.md for detailed setup instructions")
    print("\nFor support, refer to the comprehensive API_KEYS_GUIDE.md")

if __name__ == "__main__":
    setup_enhanced_features()