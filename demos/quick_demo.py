#!/usr/bin/env python3
"""
🌍 AI Travel Platform - Quick Demo
Simple demo script to showcase the travel platform functionality
"""

import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the current directory to the Python path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

def main():
    """Main demo function"""
    print("🌍 AI Travel Platform - Quick Demo")
    print("=" * 50)
    
    # Check environment setup
    print("\n📋 Environment Check:")
    print("-" * 20)
    
    required_vars = [
        "OPENAI_API_KEY",
        "SUPABASE_URL", 
        "SUPABASE_KEY",
        "TAVILY_API_KEY"
    ]
    
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if value:
            print(f"✅ {var}: {'*' * 8}...")
        else:
            print(f"❌ {var}: Not set")
            missing_vars.append(var)
    
    if missing_vars:
        print(f"\n⚠️  Missing environment variables: {', '.join(missing_vars)}")
        print("Please check your .env file and ensure all required keys are set.")
        return
    
    print("\n🎯 Features Available:")
    print("-" * 20)
    features = [
        "✈️  AI Travel Planning",
        "🏨 Hotel Recommendations", 
        "🍽️  Restaurant Suggestions",
        "🚗 Car Rental Options",
        "💰 Price Tracking",
        "📅 Calendar Integration",
        "👥 Group Booking Management",
        "📄 PDF Itinerary Generation",
        "💳 Booking Management",
        "🔔 Notifications",
        "👤 User Profiles",
        "🌐 Multi-language Support"
    ]
    
    for feature in features:
        print(feature)
    
    print("\n🚀 Quick Usage Examples:")
    print("-" * 25)
    
    examples = [
        "Plan a 7-day trip to Paris for 2 people",
        "Find family-friendly hotels in Tokyo under $200/night", 
        "Recommend authentic restaurants in Rome",
        "Track flight prices from NYC to London",
        "Generate a detailed PDF itinerary",
        "Set up price alerts for vacation packages"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example}")
    
    print("\n🌐 Access Methods:")
    print("-" * 18)
    print("1. 🖥️  Web Interface: Run 'streamlit run main_app.py'")
    print("2. 📱 API Endpoints: Use the enhanced_travel_platform module")
    print("3. 🔧 Direct Integration: Import and use SmartTravelAssistant class")
    
    print("\n📂 Project Structure:")
    print("-" * 18)
    structure = [
        "main_app.py - Main Streamlit web interface",
        "enhanced_travel_platform.py - Core travel platform logic",
        "booking_system/ - Booking and payment management",
        "enhanced_features/ - Advanced AI travel features", 
        "tests/ - Comprehensive testing suite",
        "config.py - Configuration management",
        ".env - Environment variables"
    ]
    
    for item in structure:
        print(f"📁 {item}")
    
    print("\n🔧 Next Steps:")
    print("-" * 13)
    steps = [
        "1. Ensure all environment variables are properly set",
        "2. Run 'streamlit run main_app.py' to start the web interface",
        "3. Access the application at http://localhost:8501", 
        "4. Create a user profile and start planning your trip!",
        "5. Explore advanced features like price tracking and group bookings"
    ]
    
    for step in steps:
        print(step)
    
    print("\n" + "=" * 50)
    print("🎉 AI Travel Platform is ready to use!")
    print("Happy travels! ✈️🌍")

if __name__ == "__main__":
    main()
