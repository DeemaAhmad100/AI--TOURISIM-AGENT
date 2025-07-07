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
