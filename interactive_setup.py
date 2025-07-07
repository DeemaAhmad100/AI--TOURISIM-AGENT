#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 Enhanced Features Interactive Setup Script
Helps users configure optional features step by step
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Set UTF-8 encoding for Windows console
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

load_dotenv()

class EnhancedFeaturesSetup:
    def __init__(self):
        self.env_file = Path('.env')
        self.features_status = {}
    
    def check_current_status(self):
        """Check which features are already configured"""
        print("Checking current configuration...")
        
        # Email
        if os.getenv('SENDGRID_API_KEY') or os.getenv('EMAIL_HOST_USER'):
            self.features_status['email'] = '✅ Configured'
        else:
            self.features_status['email'] = '❌ Not configured'
        
        # Payment
        if os.getenv('STRIPE_SECRET_KEY'):
            self.features_status['payment'] = '✅ Configured'
        else:
            self.features_status['payment'] = '❌ Not configured'
        
        # Google Services
        if os.getenv('GOOGLE_MAPS_API_KEY'):
            self.features_status['google'] = '✅ Configured'
        else:
            self.features_status['google'] = '❌ Not configured'
        
        # Travel APIs
        if os.getenv('AMADEUS_CLIENT_ID') or os.getenv('BOOKING_API_KEY'):
            self.features_status['travel_apis'] = '✅ Configured'
        else:
            self.features_status['travel_apis'] = '❌ Not configured'
        
        # Display status
        print("\nCurrent Features Status:")
        print(f"Email Services: {self.features_status['email']}")
        print(f"Payment Processing: {self.features_status['payment']}")
        print(f"Google Services: {self.features_status['google']}")
        print(f"Travel APIs: {self.features_status['travel_apis']}")
    
    def setup_email_service(self):
        """Setup email service configuration"""
        print("\nEmail Service Setup")
        print("Choose your email service:")
        print("1. SendGrid (Recommended for production)")
        print("2. Gmail (Good for development)")
        print("3. Skip email setup")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            self._setup_sendgrid()
        elif choice == '2':
            self._setup_gmail()
        else:
            print("Skipping email setup...")
    
    def _setup_sendgrid(self):
        """Setup SendGrid configuration"""
        print("\nSendGrid Setup:")
        print("1. Sign up at https://sendgrid.com/")
        print("2. Verify your sender identity")
        print("3. Create API key with Mail Send permissions")
        
        api_key = input("Enter your SendGrid API key: ").strip()
        from_email = input("Enter your from email (e.g., noreply@yourdomain.com): ").strip()
        
        if api_key and from_email:
            self._add_env_var('SENDGRID_API_KEY', api_key)
            self._add_env_var('SENDGRID_FROM_EMAIL', from_email)
            print("✅ SendGrid configured successfully!")
        else:
            print("❌ Invalid input. Skipping SendGrid setup.")
    
    def _setup_gmail(self):
        """Setup Gmail configuration"""
        print("\nGmail Setup:")
        print("1. Enable 2-Factor Authentication on your Google account")
        print("2. Go to Google Account Settings → Security → App passwords")
        print("3. Generate app password for 'Mail'")
        
        email = input("Enter your Gmail address: ").strip()
        app_password = input("Enter your app password: ").strip()
        
        if email and app_password:
            self._add_env_var('EMAIL_HOST', 'smtp.gmail.com')
            self._add_env_var('EMAIL_PORT', '587')
            self._add_env_var('EMAIL_HOST_USER', email)
            self._add_env_var('EMAIL_HOST_PASSWORD', app_password)
            self._add_env_var('EMAIL_USE_TLS', 'True')
            print("✅ Gmail configured successfully!")
        else:
            print("❌ Invalid input. Skipping Gmail setup.")
    
    def setup_payment_service(self):
        """Setup payment processing"""
        print("\nPayment Processing Setup")
        print("Setting up Stripe integration...")
        print("1. Sign up at https://stripe.com/")
        print("2. Complete business verification")
        print("3. Get API keys from Dashboard → Developers → API keys")
        
        setup = input("Do you want to setup Stripe now? (y/n): ").strip().lower()
        
        if setup == 'y':
            publishable_key = input("Enter your Stripe Publishable Key (pk_test_...): ").strip()
            secret_key = input("Enter your Stripe Secret Key (sk_test_...): ").strip()
            
            if publishable_key and secret_key:
                self._add_env_var('STRIPE_PUBLISHABLE_KEY', publishable_key)
                self._add_env_var('STRIPE_SECRET_KEY', secret_key)
                print("✅ Stripe configured successfully!")
            else:
                print("❌ Invalid input. Skipping Stripe setup.")
        else:
            print("Skipping payment setup...")
    
    def setup_google_services(self):
        """Setup Google services"""
        print("\nGoogle Services Setup")
        print("Setting up Google Maps and Calendar integration...")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create project and enable APIs:")
        print("   - Google Maps API")
        print("   - Google Calendar API")
        print("   - Google Places API")
        
        setup = input("Do you want to setup Google services now? (y/n): ").strip().lower()
        
        if setup == 'y':
            maps_key = input("Enter your Google Maps API Key: ").strip()
            
            if maps_key:
                self._add_env_var('GOOGLE_MAPS_API_KEY', maps_key)
                self._add_env_var('GOOGLE_CALENDAR_API_KEY', maps_key)  # Same key usually works
                self._add_env_var('GOOGLE_PLACES_API_KEY', maps_key)
                print("✅ Google services configured successfully!")
                print("ℹ️  For Calendar integration, you'll need to set up OAuth2 credentials")
            else:
                print("❌ Invalid input. Skipping Google services setup.")
        else:
            print("Skipping Google services setup...")
    
    def setup_travel_apis(self):
        """Setup travel APIs"""
        print("\nTravel APIs Setup")
        print("Setting up real-time flight and hotel data...")
        print("Available APIs:")
        print("1. Amadeus (Flight data)")
        print("2. Booking.com (Hotel data)")
        print("3. Skip travel APIs")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            self._setup_amadeus()
        elif choice == '2':
            self._setup_booking_api()
        else:
            print("Skipping travel APIs setup...")
    
    def _setup_amadeus(self):
        """Setup Amadeus API"""
        print("\nAmadeus Setup:")
        print("1. Sign up at https://developers.amadeus.com/")
        print("2. Create application and get credentials")
        
        client_id = input("Enter your Amadeus Client ID: ").strip()
        client_secret = input("Enter your Amadeus Client Secret: ").strip()
        
        if client_id and client_secret:
            self._add_env_var('AMADEUS_CLIENT_ID', client_id)
            self._add_env_var('AMADEUS_CLIENT_SECRET', client_secret)
            print("✅ Amadeus configured successfully!")
        else:
            print("❌ Invalid input. Skipping Amadeus setup.")
    
    def _setup_booking_api(self):
        """Setup Booking.com API"""
        print("\nBooking.com Setup:")
        print("1. Contact Booking.com for API access")
        print("2. Get API key and secret")
        
        api_key = input("Enter your Booking.com API Key: ").strip()
        
        if api_key:
            self._add_env_var('BOOKING_API_KEY', api_key)
            print("✅ Booking.com configured successfully!")
        else:
            print("❌ Invalid input. Skipping Booking.com setup.")
    
    def _add_env_var(self, key: str, value: str):
        """Add environment variable to .env file"""
        if not self.env_file.exists():
            self.env_file.touch()
        
        # Read existing content
        with open(self.env_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Check if key already exists
        key_exists = False
        for i, line in enumerate(lines):
            if line.startswith(f'{key}='):
                lines[i] = f'{key}={value}\n'
                key_exists = True
                break
        
        # Add new key if it doesn't exist
        if not key_exists:
            lines.append(f'{key}={value}\n')
        
        # Write back to file
        with open(self.env_file, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    
    def install_dependencies(self):
        """Install required dependencies"""
        print("\nInstalling Enhanced Dependencies...")
        
        enhanced_packages = [
            'sendgrid==6.10.0',
            'stripe==5.5.0',
            'google-api-python-client==2.95.0',
            'google-auth-httplib2==0.1.0',
            'google-auth-oauthlib==1.0.0',
            'googlemaps==4.10.0',
            'amadeus==8.0.0'
        ]
        
        import subprocess
        
        for package in enhanced_packages:
            try:
                subprocess.run([sys.executable, '-m', 'pip', 'install', package], 
                             check=True, capture_output=True)
                print(f"✅ Installed {package}")
            except subprocess.CalledProcessError:
                print(f"❌ Failed to install {package}")
    
    def run_setup(self):
        """Run the complete setup process"""
        print("AI Travel Platform - Enhanced Features Setup")
        print("=" * 50)
        
        self.check_current_status()
        
        print("\nLet's configure your enhanced features:")
        
        try:
            # Setup each feature
            self.setup_email_service()
            self.setup_payment_service()
            self.setup_google_services()
            self.setup_travel_apis()
            
            # Install dependencies
            install_deps = input("\nInstall required dependencies? (y/n): ").strip().lower()
            if install_deps == 'y':
                self.install_dependencies()
            
            print("\nSetup Complete!")
            print("Check the API_KEYS_GUIDE.md file for detailed configuration instructions.")
            print("Test your setup by running: python demos/experience_demo.py")
            
        except EOFError:
            print("\n\nSetup interrupted. Configuration has been saved.")
            print("You can run this script again to continue setup.")
        except KeyboardInterrupt:
            print("\n\nSetup cancelled by user.")
            print("Configuration has been saved up to this point.")

def main():
    setup = EnhancedFeaturesSetup()
    setup.run_setup()

if __name__ == "__main__":
    main()
