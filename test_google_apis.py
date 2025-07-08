"""
🧪 Google APIs Integration Test Script
Tests the Google APIs setup for the AI Travel Platform
"""

import os
import requests
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

def test_places_api():
    """Test Google Places API"""
    print("🔍 Testing Google Places API...")
    api_key = os.getenv('GOOGLE_PLACES_API_KEY') or os.getenv('GOOGLE_MAPS_API_KEY')
    
    if not api_key:
        print("❌ GOOGLE_PLACES_API_KEY not found in environment")
        print("💡 Add your API key to .env file or set environment variable")
        return False
    
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': 'restaurants in Paris',
        'key': api_key
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'OK':
                results = data.get('results', [])
                print(f"✅ Google Places API working!")
                print(f"   Found {len(results)} restaurants in Paris")
                if results:
                    print(f"   Sample: {results[0].get('name', 'Unknown')}")
                return True
            else:
                error_msg = data.get('error_message', 'Unknown error')
                print(f"❌ API Error: {data.get('status')} - {error_msg}")
                
                # Provide specific help based on error
                if data.get('status') == 'REQUEST_DENIED':
                    print("💡 This usually means:")
                    print("   - API key is invalid")
                    print("   - Places API is not enabled")
                    print("   - Billing is not set up")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print("❌ Request timeout - check your internet connection")
        return False
    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        return False

def test_geocoding_api():
    """Test Google Geocoding API"""
    print("\n🌍 Testing Google Geocoding API...")
    api_key = os.getenv('GOOGLE_GEOCODING_API_KEY') or os.getenv('GOOGLE_MAPS_API_KEY')
    
    if not api_key:
        print("❌ GOOGLE_GEOCODING_API_KEY not found in environment")
        print("💡 Add your API key to .env file or set environment variable")
        return False
    
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': 'Eiffel Tower, Paris, France',
        'key': api_key
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'OK':
                results = data.get('results', [])
                print(f"✅ Google Geocoding API working!")
                if results:
                    location = results[0].get('geometry', {}).get('location', {})
                    print(f"   Eiffel Tower coordinates: {location.get('lat')}, {location.get('lng')}")
                return True
            else:
                error_msg = data.get('error_message', 'Unknown error')
                print(f"❌ API Error: {data.get('status')} - {error_msg}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print("❌ Request timeout - check your internet connection")
        return False
    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        return False

def test_maps_static_api():
    """Test Google Static Maps API"""
    print("\n🗺️ Testing Google Static Maps API...")
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    
    if not api_key:
        print("❌ GOOGLE_MAPS_API_KEY not found in environment")
        return False
    
    url = "https://maps.googleapis.com/maps/api/staticmap"
    params = {
        'center': 'Paris, France',
        'zoom': '12',
        'size': '400x400',
        'key': api_key
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            if response.headers.get('content-type', '').startswith('image/'):
                print(f"✅ Google Static Maps API working!")
                print(f"   Generated map image ({len(response.content)} bytes)")
                return True
            else:
                # Try to parse as JSON error
                try:
                    error_data = response.json()
                    error_msg = error_data.get('error_message', 'Unknown error')
                    print(f"❌ API Error: {error_data.get('status')} - {error_msg}")
                except:
                    print(f"❌ Unexpected response format")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print("❌ Request timeout - check your internet connection")
        return False
    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        return False

def check_environment_setup():
    """Check if environment is properly set up"""
    print("🔧 Checking environment setup...")
    
    # Check for .env file
    env_file_exists = os.path.exists('.env')
    print(f"   .env file: {'✅ Found' if env_file_exists else '❌ Not found'}")
    
    # Check for API keys
    maps_key = os.getenv('GOOGLE_MAPS_API_KEY')
    places_key = os.getenv('GOOGLE_PLACES_API_KEY')
    geocoding_key = os.getenv('GOOGLE_GEOCODING_API_KEY')
    
    print(f"   GOOGLE_MAPS_API_KEY: {'✅ Set' if maps_key else '❌ Not set'}")
    print(f"   GOOGLE_PLACES_API_KEY: {'✅ Set' if places_key else '❌ Not set'}")
    print(f"   GOOGLE_GEOCODING_API_KEY: {'✅ Set' if geocoding_key else '❌ Not set'}")
    
    # Check if requests library is available
    try:
        import requests
        print(f"   requests library: ✅ Available")
    except ImportError:
        print(f"   requests library: ❌ Not installed")
        print("   Run: pip install requests")
    
    # Check if python-dotenv is available
    try:
        from dotenv import load_dotenv
        print(f"   python-dotenv: ✅ Available")
    except ImportError:
        print(f"   python-dotenv: ❌ Not installed")
        print("   Run: pip install python-dotenv")

def main():
    """Main test function"""
    print("🧪 Google APIs Integration Test")
    print("=" * 50)
    
    # Check environment setup
    check_environment_setup()
    print()
    
    # Test APIs
    places_ok = test_places_api()
    geocoding_ok = test_geocoding_api()
    maps_ok = test_maps_static_api()
    
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    print(f"   Places API: {'✅ Working' if places_ok else '❌ Failed'}")
    print(f"   Geocoding API: {'✅ Working' if geocoding_ok else '❌ Failed'}")
    print(f"   Static Maps API: {'✅ Working' if maps_ok else '❌ Failed'}")
    
    working_count = sum([places_ok, geocoding_ok, maps_ok])
    total_count = 3
    
    if working_count == total_count:
        print(f"\n🎉 All {total_count} APIs working correctly!")
        print("   Your Google APIs setup is ready for production!")
    elif working_count > 0:
        print(f"\n⚠️  {working_count}/{total_count} APIs working. Some need attention.")
        print("   Check your API keys and billing setup.")
    else:
        print(f"\n❌ No APIs working. Check the setup guide:")
        print("   See GOOGLE_APIS_SETUP_GUIDE.md for detailed instructions")
    
    print("\n💡 Next steps:")
    if not places_ok or not geocoding_ok:
        print("   1. Verify API keys are correct")
        print("   2. Ensure billing is enabled in Google Cloud")
        print("   3. Check that APIs are enabled in your project")
    else:
        print("   1. Integrate APIs into your travel platform")
        print("   2. Set up monitoring and usage alerts")
        print("   3. Configure production environment")

if __name__ == "__main__":
    main()
