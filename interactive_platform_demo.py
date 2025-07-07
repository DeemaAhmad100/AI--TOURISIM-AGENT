#!/usr/bin/env python3
"""
🌍 AI Travel Platform - Interactive Demo
Run this to see how the platform works and interact with users
"""

import os
import sys
import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment
load_dotenv()

def main_menu():
    """Display main menu and handle user interaction"""
    while True:
        print("\n" + "="*60)
        print("🌍 AI TRAVEL PLATFORM - INTERACTIVE DEMO")
        print("="*60)
        print("Choose how you want to experience the platform:")
        print()
        print("1. 🚀 Quick Demo (See all features in action)")
        print("2. 🎯 Interactive Setup (Configure your platform)")
        print("3. 🎪 Live User Interaction (Try the travel agent)")
        print("4. 📊 Platform Status (Check current setup)")
        print("5. 🧪 Run Tests (Verify everything works)")
        print("6. 📚 View Documentation")
        print("7. 🔧 Advanced Features Demo")
        print("8. 🚪 Exit")
        print()
        
        choice = input("🎮 Select option (1-8): ").strip()
        
        if choice == '1':
            run_quick_demo()
        elif choice == '2':
            run_interactive_setup()
        elif choice == '3':
            run_live_interaction()
        elif choice == '4':
            check_platform_status()
        elif choice == '5':
            run_tests()
        elif choice == '6':
            view_documentation()
        elif choice == '7':
            run_advanced_demo()
        elif choice == '8':
            print("👋 Thanks for trying the AI Travel Platform!")
            break
        else:
            print("❌ Invalid choice. Please select 1-8.")

def run_quick_demo():
    """Run a quick demonstration of all features"""
    print("\n🚀 QUICK DEMO - AI Travel Platform in Action")
    print("="*50)
    
    try:
        # Try to run the enhanced demo
        print("🔄 Running enhanced platform demo...")
        os.system("python final_enhanced_demo.py")
    except Exception as e:
        print(f"❌ Enhanced demo failed: {e}")
        try:
            # Fallback to basic demo
            print("🔄 Running basic demo...")
            os.system("python experience_demo.py")
        except Exception as e2:
            print(f"❌ Basic demo failed: {e2}")
            print("💡 Let's create a simple demo instead:")
            simple_demo()

def simple_demo():
    """Simple demonstration when other demos fail"""
    print("\n🎯 SIMPLE TRAVEL PLATFORM DEMO")
    print("="*40)
    
    # Simulate user interaction
    print("👤 User: I want to plan a trip to Paris")
    print("🤖 AI Agent: Great! Let me help you plan an amazing Paris trip...")
    print("   🔍 Searching for Paris attractions...")
    print("   🏨 Finding best hotels...")
    print("   🍽️ Discovering top restaurants...")
    print("   ✈️ Checking flight options...")
    print("   📋 Creating personalized itinerary...")
    
    print("\n📝 Generated Itinerary:")
    print("   Day 1: Eiffel Tower, Seine River Cruise")
    print("   Day 2: Louvre Museum, Champs-Élysées")
    print("   Day 3: Montmartre, Sacré-Cœur")
    print("   🏨 Recommended Hotel: Le Meurice")
    print("   🍽️ Must-try Restaurant: Le Comptoir du Relais")
    
    print("\n💰 Estimated Budget: $1,200 per person")
    print("✅ Demo completed! This shows how the AI agent works.")

def run_interactive_setup():
    """Run the interactive setup"""
    print("\n🎯 INTERACTIVE SETUP")
    print("="*30)
    
    print("This will help you configure your AI Travel Platform.")
    print("You can choose which features to enable.")
    
    try:
        os.system("python interactive_setup.py")
    except Exception as e:
        print(f"❌ Interactive setup failed: {e}")
        print("💡 You can manually configure by editing the .env file")

def run_live_interaction():
    """Run live user interaction demo"""
    print("\n🎪 LIVE USER INTERACTION")
    print("="*35)
    
    print("Let's interact with the AI Travel Agent!")
    print("Type your travel requests and see how the AI responds.")
    print("(Type 'quit' to return to main menu)")
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
        
        if not user_input:
            continue
        
        # Simulate AI response
        print("🤖 AI Agent: ", end="")
        
        if "paris" in user_input.lower():
            print("Paris is an amazing destination! I can help you plan a perfect trip.")
            print("         Would you like me to suggest attractions, hotels, or restaurants?")
        elif "budget" in user_input.lower():
            print("I'll help you find the best value for your budget.")
            print("         What's your approximate budget range?")
        elif "hotel" in user_input.lower():
            print("I'll find the perfect accommodation for you.")
            print("         Do you prefer luxury, boutique, or budget-friendly hotels?")
        elif "flight" in user_input.lower():
            print("Let me search for the best flight options.")
            print("         What are your departure and arrival cities?")
        else:
            print("I understand you want to plan a trip. Let me help you!")
            print("         Could you tell me more about your destination preferences?")

def check_platform_status():
    """Check current platform status"""
    print("\n📊 PLATFORM STATUS CHECK")
    print("="*35)
    
    try:
        print("🔄 Running platform verification...")
        os.system("python verify_setup.py")
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        manual_status_check()

def manual_status_check():
    """Manual status check when automated fails"""
    print("\n🔍 MANUAL STATUS CHECK")
    print("="*25)
    
    # Check key files
    files_to_check = [
        ".env",
        "requirements.txt",
        "src/core/platform_core.py",
        "interactive_setup.py"
    ]
    
    for file in files_to_check:
        if os.path.exists(file):
            print(f"✅ {file} - Found")
        else:
            print(f"❌ {file} - Missing")
    
    # Check environment variables
    print("\n📋 Environment Variables:")
    env_vars = ["OPENAI_API_KEY", "SUPABASE_URL", "SUPABASE_KEY"]
    
    for var in env_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ {var} - Configured")
        else:
            print(f"❌ {var} - Not set")

def run_tests():
    """Run platform tests"""
    print("\n🧪 RUNNING PLATFORM TESTS")
    print("="*35)
    
    tests_to_run = [
        ("Basic Test", "python simple_test.py"),
        ("Enhanced Test", "python enhanced_system_demo.py"),
        ("Database Test", "python test_database.py"),
        ("Interactive Test", "python test_interactive_setup.py")
    ]
    
    for test_name, command in tests_to_run:
        print(f"\n🔄 Running {test_name}...")
        try:
            os.system(command)
            print(f"✅ {test_name} completed")
        except Exception as e:
            print(f"❌ {test_name} failed: {e}")

def view_documentation():
    """Display documentation"""
    print("\n📚 DOCUMENTATION VIEWER")
    print("="*30)
    
    docs = [
        ("README.md", "📖 Main project documentation"),
        ("API_KEYS_GUIDE.md", "🔑 API keys setup guide"),
        ("ENHANCED_FEATURES_GUIDE.md", "🌟 Enhanced features guide"),
        ("PROJECT_STRUCTURE.md", "🏗️ Project structure overview"),
        ("SETUP_TESTING_SUMMARY.md", "🧪 Setup testing summary")
    ]
    
    print("Available documentation:")
    for i, (file, desc) in enumerate(docs, 1):
        print(f"{i}. {desc}")
    
    choice = input("\nSelect document to view (1-5) or 'back': ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(docs):
        file_to_view = docs[int(choice) - 1][0]
        if os.path.exists(file_to_view):
            print(f"\n📄 {file_to_view}:")
            print("="*40)
            with open(file_to_view, 'r', encoding='utf-8') as f:
                content = f.read()
                # Show first 50 lines
                lines = content.split('\n')[:50]
                print('\n'.join(lines))
                if len(content.split('\n')) > 50:
                    print("\n... (truncated)")
        else:
            print(f"❌ {file_to_view} not found")

def run_advanced_demo():
    """Run advanced features demonstration"""
    print("\n🔧 ADVANCED FEATURES DEMO")
    print("="*35)
    
    print("Available advanced demos:")
    print("1. 🤖 Enhanced Intelligence Demo")
    print("2. 🌟 World Travel Expert Demo")
    print("3. 🎯 Malaysia Specific Demo")
    print("4. 🔄 Intent Detection Demo")
    print("5. 🏗️ Organized Architecture Demo")
    
    choice = input("\nSelect demo (1-5): ").strip()
    
    demo_files = {
        '1': 'enhanced_intelligence_demo.py',
        '2': 'world_travel_expert.py',
        '3': 'malaysia_demo.py',
        '4': 'intent_detection.py',
        '5': 'main_app_organized.py'
    }
    
    if choice in demo_files:
        demo_file = demo_files[choice]
        if os.path.exists(demo_file):
            print(f"🔄 Running {demo_file}...")
            os.system(f"python {demo_file}")
        else:
            print(f"❌ {demo_file} not found")
    else:
        print("❌ Invalid choice")

def show_welcome_info():
    """Show welcome information"""
    print("🌟 WELCOME TO AI TRAVEL PLATFORM")
    print("="*45)
    print("This is an intelligent travel planning system that uses AI")
    print("to create personalized travel experiences.")
    print()
    print("Features:")
    print("• 🤖 AI-powered travel recommendations")
    print("• 🏨 Hotel and restaurant suggestions")
    print("• ✈️ Flight search and booking")
    print("• 📋 Custom itinerary generation")
    print("• 💰 Budget optimization")
    print("• 🌍 Global destination database")
    print()
    print("Let's explore what this platform can do!")

if __name__ == "__main__":
    # Change to project directory
    os.chdir(r"c:\Users\AYMAN\AI TRAVEL AGENT (TOURISIM)")
    
    # Show welcome information
    show_welcome_info()
    
    # Start main menu
    main_menu()
