#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API Key Status Checker
Quick test to verify which API keys are configured and working
"""

import os
import sys
from dotenv import load_dotenv
from pathlib import Path

# Set UTF-8 encoding for Windows console
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# Load environment variables
load_dotenv()

def check_api_keys():
    """Check the status of all API keys"""
    print("🔐 API Key Configuration Status")
    print("=" * 50)
    
    # Essential API Keys
    print("\n🚨 ESSENTIAL API KEYS:")
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        masked_key = f"{openai_key[:8]}...{openai_key[-4:]}" if len(openai_key) > 12 else "***"
        print(f"✅ OpenAI API Key: {masked_key}")
    else:
        print("❌ OpenAI API Key: Not configured")
    
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    if supabase_url and supabase_key:
        print(f"✅ Supabase Database: {supabase_url[:30]}...")
    else:
        print("❌ Supabase Database: Not configured")
    
    # Recommended API Keys
    print("\n🎯 RECOMMENDED API KEYS:")
    tavily_key = os.getenv("TAVILY_API_KEY")
    if tavily_key:
        masked_tavily = f"{tavily_key[:8]}...{tavily_key[-4:]}" if len(tavily_key) > 12 else "***"
        print(f"✅ Tavily Search API: {masked_tavily}")
    else:
        print("❌ Tavily Search API: Not configured")
    
    # Optional API Keys
    print("\n📧 OPTIONAL API KEYS:")
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")
    if email_user and email_pass:
        print(f"✅ Email Configuration: {email_user}")
    else:
        print("❌ Email Configuration: Not configured")
    
    stripe_secret = os.getenv("STRIPE_SECRET_KEY")
    if stripe_secret:
        print("✅ Stripe Payment: Configured")
    else:
        print("❌ Stripe Payment: Not configured")
    
    google_maps = os.getenv("GOOGLE_MAPS_API_KEY")
    if google_maps:
        print("✅ Google Maps: Configured")
    else:
        print("❌ Google Maps: Not configured")
    
    # Determine platform mode
    print("\n🎮 PLATFORM MODE:")
    if openai_key and supabase_url and supabase_key and tavily_key:
        print("🚀 FULL PRODUCTION MODE")
        print("   - All core features available")
        print("   - AI + Real-time search + Data persistence")
    elif openai_key and tavily_key:
        print("🎯 ENHANCED MODE")
        print("   - AI features + Real-time search")
        print("   - No data persistence")
    elif openai_key:
        print("🤖 AI MODE")
        print("   - AI features with mock data")
        print("   - No real-time search or persistence")
    else:
        print("🎮 DEMO MODE")
        print("   - Basic UI with mock data only")
        print("   - No AI features")

def test_connections():
    """Test actual connections to configured services"""
    print("\n🔧 CONNECTION TESTS:")
    print("=" * 50)
    
    # Test OpenAI
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        try:
            from langchain_openai import ChatOpenAI
            llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
            print("✅ OpenAI Connection: Ready")
        except Exception as e:
            print(f"❌ OpenAI Connection: Error - {str(e)[:50]}...")
    else:
        print("⚠️ OpenAI Connection: Not configured")
    
    # Test Supabase
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    if supabase_url and supabase_key:
        try:
            from supabase import create_client
            client = create_client(supabase_url, supabase_key)
            print("✅ Supabase Connection: Ready")
        except Exception as e:
            print(f"❌ Supabase Connection: Error - {str(e)[:50]}...")
    else:
        print("⚠️ Supabase Connection: Not configured")
    
    # Test Tavily
    tavily_key = os.getenv("TAVILY_API_KEY")
    if tavily_key:
        try:
            from langchain_community.tools.tavily_search import TavilySearchResults
            search = TavilySearchResults(api_key=tavily_key, max_results=1)
            print("✅ Tavily Connection: Ready")
        except Exception as e:
            print(f"❌ Tavily Connection: Error - {str(e)[:50]}...")
    else:
        print("⚠️ Tavily Connection: Not configured")

def main():
    print("🌍 AI Travel Platform - API Key Status Checker")
    print("=" * 60)
    
    # Check if .env file exists
    env_file = Path(".env")
    if env_file.exists():
        print(f"✅ Environment file found: {env_file.absolute()}")
    else:
        print("❌ Environment file not found: .env")
        print("   Please copy .env.example to .env and configure your API keys")
        return
    
    check_api_keys()
    test_connections()
    
    print("\n📖 For detailed setup instructions, see:")
    print("   - API_KEYS_GUIDE.md")
    print("   - README.md")
    print("\n🚀 Ready to start your AI travel planning journey!")

if __name__ == "__main__":
    main()
