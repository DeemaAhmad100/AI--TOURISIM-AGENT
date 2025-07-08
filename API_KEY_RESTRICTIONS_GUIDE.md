# 🔑 API Key Restriction Visual Guide

## 📋 **Step-by-Step Screenshots Guide**

### **Step 1: Navigate to Credentials**
1. Go to Google Cloud Console: https://console.cloud.google.com/
2. Select your project: "AI Travel Platform"
3. Go to "APIs & Services" → "Credentials"

### **Step 2: Edit Your API Key**
1. Find your API key in the credentials list
2. Click on the API key name (not the key itself)
3. You'll see the "Edit API Key" page

### **Step 3: Set Application Restrictions**

#### **For Web Application (Recommended for Travel Platform):**
```
✅ HTTP referrers (web sites)

Website restrictions:
- localhost:*                    (for local testing)
- 127.0.0.1:*                  (for local testing)
- https://yourdomain.com/*       (your production domain)
- https://*.yourdomain.com/*     (subdomains)
```

#### **For Mobile App:**
```
✅ Android apps
- Add your Android package name
- Add SHA-1 certificate fingerprint

✅ iOS apps  
- Add your iOS bundle identifier
```

#### **For Server/Backend:**
```
✅ IP addresses (web servers, cron jobs, etc.)
- Your server's IP address
- For testing: 0.0.0.0/0 (REMOVE in production!)
```

### **Step 4: Set API Restrictions**

**Select ONLY the APIs you need:**

```
✅ Maps JavaScript API
✅ Places API
✅ Calendar API
✅ Geocoding API

❌ All other APIs (uncheck them)
```

### **Step 5: Save and Test**

1. Click "Save" at the bottom
2. Wait 2-5 minutes for changes to propagate
3. Test with your application or test script

## 🚨 **Security Best Practices**

### **✅ DO:**
- Always restrict your API keys
- Use different keys for development/production
- Regularly rotate your API keys
- Monitor usage in Google Cloud Console
- Set up billing alerts

### **❌ DON'T:**
- Use unrestricted API keys
- Commit API keys to source control
- Use the same key for all environments
- Share API keys publicly
- Ignore usage monitoring

## 🧪 **Testing Your Restrictions**

### **Test 1: Valid Request**
If your restrictions are correct, this should work:
```bash
curl "https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants+in+Paris&key=YOUR_API_KEY"
```

### **Test 2: Invalid Referrer**
If you try from an unauthorized domain, you should get:
```json
{
  "error_message": "This API key is not valid for the provided referrer",
  "status": "REQUEST_DENIED"
}
```

## 🛠️ **Common Issues and Solutions**

### **Issue: "API key not valid for the provided referrer"**
**Solution:** Add your domain to HTTP referrers list

### **Issue: "This API project is not authorized"**
**Solution:** Check that the API is enabled and billing is active

### **Issue: "API key not found"**
**Solution:** Verify the API key is copied correctly

### **Issue: "Quota exceeded"**
**Solution:** Check your usage limits and billing account

## 📊 **Production Deployment Checklist**

- [ ] ✅ API key created and restricted
- [ ] ✅ Production domain added to restrictions
- [ ] ✅ Only required APIs enabled
- [ ] ✅ Billing account active
- [ ] ✅ Usage monitoring set up
- [ ] ✅ Backup API keys prepared
- [ ] ✅ Key rotation schedule planned

## 🎯 **Next Steps**

1. **Apply the restrictions** in Google Cloud Console
2. **Test your setup** with the test script
3. **Deploy to production** with proper domain restrictions
4. **Monitor usage** and set up alerts

Your API key restrictions are now properly configured for security! 🔒
