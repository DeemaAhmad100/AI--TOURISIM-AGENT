#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 Test Interactive Setup Script
Demonstrates how to use the interactive setup with automated responses
"""

import subprocess
import sys
from pathlib import Path

def test_interactive_setup():
    """Test the interactive setup with various scenarios"""
    
    print("🧪 Testing AI Travel Platform Interactive Setup")
    print("=" * 60)
    
    # Test scenarios
    test_scenarios = {
        "skip_all": {
            "description": "Skip all optional features",
            "inputs": "3\nn\nn\nn\nn\n"  # Skip email, no to all others, no to dependencies
        },
        "email_only": {
            "description": "Configure email only (Gmail)",
            "inputs": "2\ntest@gmail.com\ntest_password\nn\nn\nn\nn\n"  # Gmail setup, skip others
        },
        "sendgrid_only": {
            "description": "Configure SendGrid only",
            "inputs": "1\nSG.test_key\nnoreply@test.com\nn\nn\nn\nn\n"  # SendGrid setup, skip others
        }
    }
    
    print("Available test scenarios:")
    for key, scenario in test_scenarios.items():
        print(f"  {key}: {scenario['description']}")
    
    print("\n🎯 Running 'skip_all' scenario...")
    
    # Run the skip_all scenario
    try:
        result = subprocess.run(
            [sys.executable, "interactive_setup.py"],
            input=test_scenarios["skip_all"]["inputs"],
            capture_output=True,
            text=True,
            cwd=Path.cwd()
        )
        
        print("✅ Script executed successfully!")
        print("📄 Output:")
        print(result.stdout)
        
        if result.stderr:
            print("⚠️ Warnings/Errors:")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ Error running script: {e}")

def show_manual_usage():
    """Show how to use the interactive setup manually"""
    print("\n📖 Manual Usage Instructions:")
    print("=" * 40)
    print()
    print("1. 🚀 Run the interactive setup:")
    print("   python interactive_setup.py")
    print()
    print("2. 📧 Email Service Options:")
    print("   • Option 1: SendGrid (Production)")
    print("     - Requires: API key + from email")
    print("     - Best for: Live applications")
    print("   • Option 2: Gmail (Development)")
    print("     - Requires: Gmail + app password")
    print("     - Best for: Testing")
    print("   • Option 3: Skip")
    print()
    print("3. 💳 Payment Processing:")
    print("   • Stripe integration")
    print("   • Requires: Publishable key + Secret key")
    print("   • Optional for testing")
    print()
    print("4. 🌐 Google Services:")
    print("   • Maps, Calendar, Places APIs")
    print("   • Requires: Google Maps API key")
    print("   • Enhances location features")
    print()
    print("5. 🛫 Travel APIs:")
    print("   • Amadeus (Flights)")
    print("   • Booking.com (Hotels)")
    print("   • Provides real-time data")
    print()
    print("6. 📦 Dependencies:")
    print("   • Auto-install enhanced packages")
    print("   • Optional but recommended")

def show_current_status():
    """Show current platform status"""
    print("\n📊 Current Platform Status:")
    print("=" * 30)
    
    # Check .env file
    env_file = Path('.env')
    if env_file.exists():
        print("✅ .env file exists")
        
        # Read and check for key variables
        with open(env_file, 'r') as f:
            content = f.read()
            
        essential_keys = ['OPENAI_API_KEY', 'SUPABASE_URL', 'SUPABASE_KEY']
        optional_keys = ['SENDGRID_API_KEY', 'STRIPE_SECRET_KEY', 'GOOGLE_MAPS_API_KEY']
        
        print("\n🔑 Essential APIs:")
        for key in essential_keys:
            if key in content and f"{key}=" in content:
                print(f"   ✅ {key}")
            else:
                print(f"   ❌ {key}")
        
        print("\n🎯 Optional APIs:")
        for key in optional_keys:
            if key in content and f"{key}=" in content:
                print(f"   ✅ {key}")
            else:
                print(f"   ⭕ {key} (not configured)")
    else:
        print("❌ .env file not found")
        print("   Run: python setup_enhanced_features.py first")

def main():
    """Main function"""
    print("🌍 AI Travel Platform - Setup Testing Tool")
    print("=" * 50)
    
    # Show current status
    show_current_status()
    
    # Show manual usage
    show_manual_usage()
    
    # Ask if user wants to run test
    print("\n🧪 Testing Options:")
    print("1. Run automated test (skip all features)")
    print("2. Show me how to run manually")
    print("3. Exit")
    
    try:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            test_interactive_setup()
        elif choice == '2':
            print("\n🚀 To run manually:")
            print("python interactive_setup.py")
            print("\nThen follow the prompts step by step!")
        else:
            print("👋 Goodbye!")
            
    except KeyboardInterrupt:
        print("\n👋 Setup testing cancelled.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
