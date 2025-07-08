"""
🔑 API Key Restrictions Tester
Tests if your Google API key restrictions are working correctly
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_api_restrictions():
    """Test API key restrictions"""
    print("🔑 Testing API Key Restrictions...")
    print("=" * 50)
    
    api_key = os.getenv('GOOGLE_MAPS_API_KEY') or os.getenv('GOOGLE_PLACES_API_KEY')
    
    if not api_key:
        print("❌ No API key found in environment variables")
        print("💡 Add your API key to .env file first")
        return
    
    print(f"🔍 Testing with key: {api_key[:8]}...{api_key[-4:]}")
    print()
    
    # Test Places API
    test_places_with_restrictions(api_key)
    
    # Test Geocoding API  
    test_geocoding_with_restrictions(api_key)
    
    # Test with invalid referrer (simulation)
    test_invalid_referrer_simulation(api_key)

def test_places_with_restrictions(api_key):
    """Test Places API with current restrictions"""
    print("🔍 Testing Places API...")
    
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': 'restaurants in Paris',
        'key': api_key
    }
    
    # Set a referrer header to simulate web request
    headers = {
        'Referer': 'http://localhost:3000/',
        'User-Agent': 'AI Travel Platform Test'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            status = data.get('status')
            
            if status == 'OK':
                print("✅ Places API: Restrictions allow access")
                print(f"   Found {len(data.get('results', []))} results")
            elif status == 'REQUEST_DENIED':
                error_msg = data.get('error_message', 'Unknown error')
                print("🚫 Places API: Request denied by restrictions")
                print(f"   Error: {error_msg}")
                
                if 'referrer' in error_msg.lower():
                    print("💡 Fix: Add your domain to HTTP referrers")
                elif 'api key' in error_msg.lower():
                    print("💡 Fix: Check API key and ensure Places API is enabled")
            else:
                print(f"⚠️ Places API: Unexpected status - {status}")
                print(f"   Message: {data.get('error_message', 'No details')}")
        else:
            print(f"❌ Places API: HTTP Error {response.status_code}")
            
    except requests.exceptions.Timeout:
        print("❌ Places API: Request timeout")
    except Exception as e:
        print(f"❌ Places API: Exception - {str(e)}")
    
    print()

def test_geocoding_with_restrictions(api_key):
    """Test Geocoding API with current restrictions"""
    print("🌍 Testing Geocoding API...")
    
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': 'Eiffel Tower, Paris, France',
        'key': api_key
    }
    
    headers = {
        'Referer': 'http://localhost:3000/',
        'User-Agent': 'AI Travel Platform Test'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            status = data.get('status')
            
            if status == 'OK':
                print("✅ Geocoding API: Restrictions allow access")
                results = data.get('results', [])
                if results:
                    location = results[0].get('geometry', {}).get('location', {})
                    print(f"   Location: {location.get('lat')}, {location.get('lng')}")
            elif status == 'REQUEST_DENIED':
                error_msg = data.get('error_message', 'Unknown error')
                print("🚫 Geocoding API: Request denied by restrictions")
                print(f"   Error: {error_msg}")
            else:
                print(f"⚠️ Geocoding API: Unexpected status - {status}")
        else:
            print(f"❌ Geocoding API: HTTP Error {response.status_code}")
            
    except requests.exceptions.Timeout:
        print("❌ Geocoding API: Request timeout")
    except Exception as e:
        print(f"❌ Geocoding API: Exception - {str(e)}")
    
    print()

def test_invalid_referrer_simulation(api_key):
    """Simulate request from invalid referrer"""
    print("🚫 Testing with invalid referrer (should be blocked)...")
    
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': 'test',
        'key': api_key
    }
    
    # Use an unauthorized referrer
    headers = {
        'Referer': 'https://malicious-site.com/',
        'User-Agent': 'Unauthorized Access Attempt'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            status = data.get('status')
            
            if status == 'REQUEST_DENIED':
                print("✅ Security: Invalid referrer properly blocked")
                print(f"   Message: {data.get('error_message', 'Access denied')}")
            elif status == 'OK':
                print("⚠️ Security Warning: Invalid referrer was NOT blocked")
                print("💡 Check your HTTP referrer restrictions")
            else:
                print(f"🔍 Security: Unexpected response - {status}")
        else:
            print(f"❌ Security Test: HTTP Error {response.status_code}")
            
    except Exception as e:
        print(f"❌ Security Test: Exception - {str(e)}")

def show_restriction_recommendations():
    """Show recommendations for API key restrictions"""
    print("\n" + "=" * 50)
    print("🛡️ API Key Restriction Recommendations")
    print("=" * 50)
    
    print("\n🌐 For Web Applications:")
    print("   Application restrictions: HTTP referrers")
    print("   Add these referrers:")
    print("   - localhost:*")
    print("   - 127.0.0.1:*")
    print("   - https://yourdomain.com/*")
    print("   - https://*.yourdomain.com/*")
    
    print("\n📱 For Mobile Apps:")
    print("   Application restrictions: Android/iOS apps")
    print("   Add your app's package name/bundle ID")
    
    print("\n🖥️ For Server Applications:")
    print("   Application restrictions: IP addresses")
    print("   Add your server's IP address")
    
    print("\n🔧 API Restrictions (enable only what you need):")
    print("   ✅ Maps JavaScript API")
    print("   ✅ Places API")
    print("   ✅ Calendar API")
    print("   ✅ Geocoding API")
    print("   ❌ All other APIs")

def main():
    """Main test function"""
    print("🔑 Google API Key Restrictions Tester")
    print("=" * 50)
    
    # Test current restrictions
    test_api_restrictions()
    
    # Show recommendations
    show_restriction_recommendations()
    
    print("\n💡 Next Steps:")
    print("1. Go to Google Cloud Console → APIs & Services → Credentials")
    print("2. Click on your API key to edit restrictions")
    print("3. Set appropriate application and API restrictions")
    print("4. Save changes and wait 2-5 minutes")
    print("5. Run this test again to verify")

if __name__ == "__main__":
    main()
