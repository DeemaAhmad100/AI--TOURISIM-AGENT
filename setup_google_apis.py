"""
🚀 Quick Setup Script for Google APIs
Automates the initial setup process for the AI Travel Platform
"""

import os
import shutil
import subprocess
import sys

def check_requirements():
    """Check if required packages are installed"""
    print("🔧 Checking requirements...")
    
    try:
        import requests
        print("   ✅ requests library is available")
    except ImportError:
        print("   ❌ requests library not found")
        print("   Installing requests...")
        subprocess.run([sys.executable, "-m", "pip", "install", "requests"])
    
    try:
        import dotenv
        print("   ✅ python-dotenv is available")
    except ImportError:
        print("   ❌ python-dotenv not found")
        print("   Installing python-dotenv...")
        subprocess.run([sys.executable, "-m", "pip", "install", "python-dotenv"])

def setup_env_file():
    """Set up the .env file from template"""
    print("\n📁 Setting up environment file...")
    
    if os.path.exists('.env'):
        print("   ✅ .env file already exists")
        return
    
    if os.path.exists('.env.template'):
        shutil.copy('.env.template', '.env')
        print("   ✅ Created .env file from template")
        print("   💡 Please edit .env file and add your Google API keys")
    else:
        print("   ❌ .env.template not found")
        create_basic_env_file()

def create_basic_env_file():
    """Create a basic .env file"""
    content = """# Google APIs Configuration
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
GOOGLE_PLACES_API_KEY=your_google_places_api_key_here
GOOGLE_CALENDAR_API_KEY=your_google_calendar_api_key_here
GOOGLE_GEOCODING_API_KEY=your_google_geocoding_api_key_here
"""
    
    with open('.env', 'w') as f:
        f.write(content)
    
    print("   ✅ Created basic .env file")
    print("   💡 Please edit .env file and add your Google API keys")

def run_test():
    """Run the Google APIs test"""
    print("\n🧪 Running Google APIs test...")
    
    if os.path.exists('test_google_apis.py'):
        try:
            subprocess.run([sys.executable, 'test_google_apis.py'])
        except Exception as e:
            print(f"   ❌ Error running test: {e}")
    else:
        print("   ❌ test_google_apis.py not found")

def show_next_steps():
    """Show the next steps to the user"""
    print("\n🎯 Next Steps:")
    print("   1. Follow the Google Cloud setup guide: GOOGLE_APIS_SETUP_GUIDE.md")
    print("   2. Get your API keys from: https://console.cloud.google.com/apis/credentials")
    print("   3. Edit the .env file and add your actual API keys")
    print("   4. Run: python test_google_apis.py to verify setup")
    print("   5. Once working, integrate with your travel platform")
    
    print("\n📚 Documentation:")
    print("   - Setup Guide: GOOGLE_APIS_SETUP_GUIDE.md")
    print("   - Test Script: test_google_apis.py")
    print("   - Environment Template: .env.template")
    
    print("\n🆘 Need Help?")
    print("   - Check the troubleshooting section in GOOGLE_APIS_SETUP_GUIDE.md")
    print("   - Run test_google_apis.py for specific error messages")
    print("   - Make sure billing is enabled in Google Cloud Console")

def main():
    """Main setup function"""
    print("🚀 AI Travel Platform - Google APIs Quick Setup")
    print("=" * 60)
    
    # Check and install requirements
    check_requirements()
    
    # Set up environment file
    setup_env_file()
    
    # Run test (will show what needs to be configured)
    run_test()
    
    # Show next steps
    show_next_steps()
    
    print("\n" + "=" * 60)
    print("✨ Setup script completed!")

if __name__ == "__main__":
    main()
