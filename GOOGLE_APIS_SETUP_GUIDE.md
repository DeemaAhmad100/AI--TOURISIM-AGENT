# 🌍 Google APIs Setup Guide for AI Travel Platform

## 📋 **Required Google APIs**
- Google Maps JavaScript API
- Google Places API 
- Google Calendar API
- Google Geocoding API (optional but recommended)

## 🚀 **Step-by-Step Setup Process**

### **1. Create Google Cloud Project**

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/
   - Sign in with your Google account

2. **Create New Project**
   - Click "Select a project" dropdown
   - Click "New Project"
   - Project name: "AI Travel Platform"
   - Click "Create"

3. **Wait for project creation** (takes 30-60 seconds)

### **2. Enable Required APIs**

1. **Go to APIs & Services**
   - In left menu: "APIs & Services" → "Library"

2. **Enable Google Maps JavaScript API**
   - Search: "Maps JavaScript API"
   - Click on it → Click "Enable"
   - Wait for activation

3. **Enable Google Places API**
   - Search: "Places API"
   - Click on it → Click "Enable"
   - Wait for activation

4. **Enable Google Calendar API**
   - Search: "Calendar API"
   - Click on it → Click "Enable"
   - Wait for activation

5. **Enable Geocoding API (Optional)**
   - Search: "Geocoding API"
   - Click on it → Click "Enable"

### **3. Create API Credentials**

1. **Go to Credentials**
   - "APIs & Services" → "Credentials"

2. **Create API Key**
   - Click "Create Credentials" → "API Key"
   - Copy the generated API key
   - Click "Restrict Key" (recommended)

3. **Restrict the API Key**
   - Application restrictions: 
     - For web: "HTTP referrers"
     - For mobile: "Android/iOS apps"
     - For server: "IP addresses"
   - API restrictions: Select the APIs you enabled
   - Click "Save"

#### **🎯 Specific Restriction Examples**

**For Development/Testing:**
```
Application restrictions: HTTP referrers (web sites)
- localhost:*
- 127.0.0.1:*
- http://localhost:*
- https://localhost:*
- file://*
```

**For Production Website:**
```
Application restrictions: HTTP referrers (web sites)
- yourdomain.com/*
- *.yourdomain.com/*
- https://yourdomain.com/*
```

**For Server/Backend Use:**
```
Application restrictions: IP addresses (web servers, cron jobs, etc.)
- Your server IP address
- 0.0.0.0/0 (for testing only - remove in production)
```

**API Restrictions (Select only what you need):**
- ✅ Maps JavaScript API
- ✅ Places API
- ✅ Calendar API  
- ✅ Geocoding API
- ❌ Uncheck all others

### **4. Billing Setup (Required)**

⚠️ **Important: Google requires billing to be enabled**

1. **Enable Billing**
   - Go to "Billing" in left menu
   - Click "Link a billing account"
   - Add payment method (credit card)
   - You get $300 free credits for new accounts

2. **Set Budget Alerts**
   - Go to "Billing" → "Budgets & alerts"
   - Create budget alert for $50/month
   - Set up email notifications

### **5. Test Your Setup**

Use this test URL (replace YOUR_API_KEY):
```
https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places
```

## 🔧 **Common Issues & Solutions**

### **Issue 1: "This API project is not authorized"**
- Solution: Make sure billing is enabled
- Solution: Check API restrictions match your domain

### **Issue 2: "API key not valid"**
- Solution: Wait 5-10 minutes after creating key
- Solution: Check if API is enabled in your project

### **Issue 3: "Quota exceeded"**
- Solution: Check billing account is active
- Solution: Review usage limits in console

### **Issue 4: "Referer not allowed"**
- Solution: Add your domain to HTTP referrers
- Solution: For testing, use "*" (remove in production)

## 🔑 **Environment Variables Setup**

### **Create .env file**
Create a `.env` file in your project root:

```env
# Google API Configuration
GOOGLE_MAPS_API_KEY=your_api_key_here
GOOGLE_PLACES_API_KEY=your_api_key_here
GOOGLE_CALENDAR_API_KEY=your_api_key_here
GOOGLE_GEOCODING_API_KEY=your_api_key_here

# Optional: Different keys for different environments
GOOGLE_MAPS_API_KEY_PROD=your_production_key_here
GOOGLE_MAPS_API_KEY_DEV=your_development_key_here
```

### **Windows PowerShell Setup**
For Windows development, set environment variables:

```powershell
# Temporary (current session only)
$env:GOOGLE_MAPS_API_KEY="your_api_key_here"

# Permanent (for your user)
[Environment]::SetEnvironmentVariable("GOOGLE_MAPS_API_KEY", "your_api_key_here", "User")
```

### **Python Integration**
```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Use in your code
google_maps_key = os.getenv('GOOGLE_MAPS_API_KEY')
google_places_key = os.getenv('GOOGLE_PLACES_API_KEY')
```

## 🧪 **Testing Your Integration**

### **Simple Test Script**
Create `test_google_apis.py`:

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_places_api():
    """Test Google Places API"""
    api_key = os.getenv('GOOGLE_PLACES_API_KEY')
    if not api_key:
        print("❌ GOOGLE_PLACES_API_KEY not found in environment")
        return False
    
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': 'restaurants in Paris',
        'key': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'OK':
                print("✅ Google Places API working!")
                print(f"Found {len(data.get('results', []))} results")
                return True
            else:
                print(f"❌ API Error: {data.get('status')} - {data.get('error_message', 'Unknown error')}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        return False

def test_geocoding_api():
    """Test Google Geocoding API"""
    api_key = os.getenv('GOOGLE_GEOCODING_API_KEY')
    if not api_key:
        print("❌ GOOGLE_GEOCODING_API_KEY not found in environment")
        return False
    
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': 'Paris, France',
        'key': api_key
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'OK':
                print("✅ Google Geocoding API working!")
                return True
            else:
                print(f"❌ API Error: {data.get('status')} - {data.get('error_message', 'Unknown error')}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Google APIs Integration...\n")
    
    # Test APIs
    places_ok = test_places_api()
    geocoding_ok = test_geocoding_api()
    
    print(f"\n📊 Test Results:")
    print(f"Places API: {'✅ Working' if places_ok else '❌ Failed'}")
    print(f"Geocoding API: {'✅ Working' if geocoding_ok else '❌ Failed'}")
    
    if places_ok and geocoding_ok:
        print("\n🎉 All APIs working correctly!")
    else:
        print("\n⚠️  Some APIs need attention. Check your keys and billing.")
```

## 🪟 **Windows-Specific Troubleshooting**

### **PowerShell Execution Policy**
If you get execution policy errors:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **Path Issues**
Make sure your project path doesn't contain spaces or special characters:
```powershell
# Good
C:\Projects\ai-travel-platform

# Avoid
C:\Users\Your Name\AI TRAVEL AGENT (TOURISIM)
```

### **Certificate Issues**
If you get SSL certificate errors:
```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

## 💡 **Free Usage Limits**

- **Maps JavaScript API**: 28,000 loads/month free
- **Places API**: $0.032 per request after free tier
- **Calendar API**: 1,000,000 requests/day free
- **Geocoding API**: 40,000 requests/month free

## 🛡️ **Security Best Practices**

1. **Restrict API Keys**: Always set application and API restrictions
2. **Use Environment Variables**: Never commit API keys to code
3. **Monitor Usage**: Set up billing alerts
4. **Rotate Keys**: Change API keys periodically

## 🆘 **Alternative Solutions**

If you continue having issues with Google APIs, we can use:

### **Alternative 1: OpenStreetMap (Free)**
- Maps: Leaflet.js with OpenStreetMap
- Places: Nominatim API (free)
- No billing required

### **Alternative 2: Mapbox (Free Tier)**
- Maps: Mapbox GL JS
- Places: Mapbox Search API
- 50,000 free requests/month

### **Alternative 3: Here Maps (Free Tier)**
- Maps: Here Maps API
- Places: Here Places API
- 250,000 free requests/month

## 🎯 **Next Steps**

1. Follow the setup process above
2. Add your API key to the platform
3. Test the integration
4. If issues persist, let me know and we'll use alternatives

## 📞 **Need Help?**

If you encounter specific errors, please share:
- The exact error message
- Which step you're stuck on
- Screenshots of the Google Cloud Console

I'll help you resolve it immediately!

## ⚡ **Quick Start Commands**

Once you have your API keys, run these commands:

```powershell
# 1. Run the setup script
python setup_google_apis.py

# 2. Edit your .env file with real API keys
notepad .env

# 3. Test your setup
python test_google_apis.py

# 4. Run the travel platform
python complete_booking_demo.py
```

## 📋 **Checklist**

- [ ] ✅ Created Google Cloud Project
- [ ] ✅ Enabled required APIs (Maps, Places, Calendar, Geocoding)
- [ ] ✅ Created API key with proper restrictions
- [ ] ✅ Set up billing (required for API usage)
- [ ] ✅ Added API keys to .env file
- [ ] ✅ Tested APIs with test_google_apis.py
- [ ] ✅ Integrated with travel platform

## 🔄 **Maintenance**

### **Monthly Tasks**
- Review API usage in Google Cloud Console
- Check billing alerts
- Rotate API keys if needed

### **Monitoring**
- Set up usage alerts at 80% of quota
- Monitor for unusual usage patterns
- Keep backup API keys for production

## 📈 **Scaling for Production**

### **API Key Management**
- Use separate keys for development/staging/production
- Implement key rotation strategy
- Store keys in secure key management system

### **Usage Optimization**
- Implement caching for geocoding results
- Use batch requests when possible
- Implement rate limiting in your application

### **Cost Management**
- Set strict quotas per API
- Implement usage analytics
- Consider alternative providers for high-volume use cases

---

**🎉 Congratulations!** Your Google APIs setup is now complete and production-ready!
