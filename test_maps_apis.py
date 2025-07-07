#!/usr/bin/env python3
"""
🧪 Maps API Test Script
Test different mapping services to see which ones work
"""

import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def test_google_maps():
    """Test Google Maps API"""
    print("🌍 Testing Google Maps API...")
    
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    if not api_key:
        print("❌ Google Maps API key not found")
        return False
    
    try:
        # Test Places API
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json"
        params = {
            'query': 'restaurants in Tokyo',
            'key': api_key
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'OK':
                print("✅ Google Maps API working!")
                print(f"   Found {len(data.get('results', []))} results")
                return True
            else:
                print(f"❌ Google Maps API error: {data.get('status')}")
                return False
        else:
            print(f"❌ Google Maps API request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Google Maps API error: {e}")
        return False

def test_openstreetmap():
    """Test OpenStreetMap/Nominatim API"""
    print("🗺️ Testing OpenStreetMap API...")
    
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            'q': 'restaurants Tokyo',
            'format': 'json',
            'limit': 5
        }
        
        headers = {
            'User-Agent': 'AI Travel Platform Test'
        }
        
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                print("✅ OpenStreetMap API working!")
                print(f"   Found {len(data)} results")
                return True
            else:
                print("❌ OpenStreetMap API returned no results")
                return False
        else:
            print(f"❌ OpenStreetMap API request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ OpenStreetMap API error: {e}")
        return False

def test_mapbox():
    """Test Mapbox API"""
    print("📍 Testing Mapbox API...")
    
    access_token = os.getenv('MAPBOX_ACCESS_TOKEN')
    if not access_token:
        print("❌ Mapbox access token not found")
        return False
    
    try:
        url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/restaurant.json"
        params = {
            'proximity': '139.6917,35.6895',  # Tokyo coordinates
            'access_token': access_token,
            'limit': 5
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('features'):
                print("✅ Mapbox API working!")
                print(f"   Found {len(data.get('features', []))} results")
                return True
            else:
                print("❌ Mapbox API returned no results")
                return False
        else:
            print(f"❌ Mapbox API request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Mapbox API error: {e}")
        return False

def test_here_maps():
    """Test Here Maps API"""
    print("📍 Testing Here Maps API...")
    
    api_key = os.getenv('HERE_MAPS_API_KEY')
    if not api_key:
        print("❌ Here Maps API key not found")
        return False
    
    try:
        url = "https://discover.search.hereapi.com/v1/discover"
        params = {
            'at': '35.6895,139.6917',  # Tokyo coordinates
            'q': 'restaurant',
            'apiKey': api_key,
            'limit': 5
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('items'):
                print("✅ Here Maps API working!")
                print(f"   Found {len(data.get('items', []))} results")
                return True
            else:
                print("❌ Here Maps API returned no results")
                return False
        else:
            print(f"❌ Here Maps API request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Here Maps API error: {e}")
        return False

def show_recommendations():
    """Show recommendations based on test results"""
    print("\n💡 RECOMMENDATIONS:")
    print("=" * 30)
    
    # Check which services are configured
    has_google = bool(os.getenv('GOOGLE_MAPS_API_KEY'))
    has_openstreetmap = os.getenv('USE_OPENSTREETMAP', 'false').lower() == 'true'
    has_mapbox = bool(os.getenv('MAPBOX_ACCESS_TOKEN'))
    has_here = bool(os.getenv('HERE_MAPS_API_KEY'))
    
    if not any([has_google, has_openstreetmap, has_mapbox, has_here]):
        print("🔧 No mapping services configured yet.")
        print("   Run: python alternative_maps_setup.py")
        print("   Recommendation: Start with OpenStreetMap (free)")
        return
    
    working_services = []
    
    if has_google:
        working_services.append("Google Maps")
    if has_openstreetmap:
        working_services.append("OpenStreetMap")
    if has_mapbox:
        working_services.append("Mapbox")
    if has_here:
        working_services.append("Here Maps")
    
    if working_services:
        print(f"✅ Configured services: {', '.join(working_services)}")
        print("\n🎯 For best results:")
        print("• Use Google Maps for comprehensive features (if billing enabled)")
        print("• Use OpenStreetMap for free, reliable mapping")
        print("• Use Mapbox for beautiful, customizable maps")
        print("• Use Here Maps for excellent geocoding")
    else:
        print("⚠️ Services configured but may need setup verification")
        print("   Check your API keys and network connection")

def main():
    """Main test function"""
    print("🧪 MAPS API TEST SUITE")
    print("=" * 50)
    print("Testing configured mapping services...")
    print()
    
    test_functions = [
        ("Google Maps", test_google_maps),
        ("OpenStreetMap", test_openstreetmap),
        ("Mapbox", test_mapbox),
        ("Here Maps", test_here_maps)
    ]
    
    results = {}
    
    for service_name, test_func in test_functions:
        results[service_name] = test_func()
        print()
    
    # Show summary
    print("📊 TEST RESULTS SUMMARY:")
    print("=" * 30)
    
    working_services = []
    for service, working in results.items():
        status = "✅ Working" if working else "❌ Not working"
        print(f"{service}: {status}")
        if working:
            working_services.append(service)
    
    print(f"\n🎯 Total working services: {len(working_services)}")
    
    if working_services:
        print(f"✅ Your platform can use: {', '.join(working_services)}")
    else:
        print("⚠️ No mapping services are currently working")
        print("   This might be due to:")
        print("   • Missing API keys")
        print("   • Network connectivity issues")
        print("   • API quota limits")
        print("   • Need to enable billing (for Google)")
    
    show_recommendations()
    
    print("\n🚀 Next steps:")
    print("• Configure more services: python alternative_maps_setup.py")
    print("• Test your platform: python working_user_demo.py")
    print("• Full setup: python interactive_setup.py")

if __name__ == "__main__":
    main()
