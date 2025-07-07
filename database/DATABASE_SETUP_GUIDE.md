# 🗄️ Database Setup Guide - AI Travel Platform

## 📋 **Quick Setup Overview**

**Current Status:**
- ✅ **Database Integration**: Fully coded in platform
- ✅ **Schema Definition**: Complete SQL schema created
- ✅ **Automated Setup**: Python script ready
- ✅ **Fallback Mode**: Works without database for demos

---

## 🚀 **Option 1: Automated Setup (Recommended)**

### **Prerequisites:**
- Python 3.11+ installed
- Supabase account created
- Environment variables configured

### **Steps:**

1. **Create Supabase Project:**
   ```bash
   # Go to https://supabase.com
   # Create new project
   # Note your project URL and anon key
   ```

2. **Configure Environment:**
   ```bash
   # Edit .env file
   SUPABASE_URL=your_project_url_here
   SUPABASE_KEY=your_anon_key_here
   ```

3. **Run Automated Setup:**
   ```bash
   python database/setup_database.py
   ```

4. **Verify Setup:**
   ```bash
   # Check Supabase dashboard
   # Tables should be created automatically
   # Sample data should be populated
   ```

---

## 🔧 **Option 2: Manual Setup**

### **Steps:**

1. **Open Supabase SQL Editor:**
   - Go to your Supabase dashboard
   - Navigate to "SQL Editor"
   - Click "New query"

2. **Execute Schema:**
   ```sql
   -- Copy and paste the entire contents of:
   -- database/schemas/enhanced_database_schema.sql
   -- Run the query
   ```

3. **Verify Tables:**
   - Check "Table Editor" in Supabase dashboard
   - Should see 20+ tables created
   - Essential tables: users, user_profiles, bookings, travel_bookings

4. **Test Connection:**
   ```bash
   python src/core/platform_core.py
   ```

---

## 📊 **Database Schema Overview**

### **Core Tables (20 tables):**

#### **User Management:**
- `users` - User authentication and basic info
- `user_profiles` - Travel preferences and history
- `user_travel_history` - Past trips and reviews

#### **Travel Services:**
- `destinations` - Available destinations
- `hotels` - Hotel listings and details
- `flights` - Flight options and schedules
- `restaurants` - Restaurant recommendations
- `attractions` - Tourist attractions
- `activities` - Bookable activities
- `car_rentals` - Car rental options

#### **Booking System:**
- `bookings` - Main booking records
- `travel_bookings` - Complete travel packages
- `travel_packages` - Predefined travel packages
- `price_tracking` - Price monitoring and alerts

#### **Intelligence:**
- `cultural_insights` - Cultural tips and etiquette
- `seasonal_data` - Weather and seasonal information
- `search_analytics` - User search behavior

---

## 🎯 **Database Features**

### **✅ Production Ready:**
- **Row Level Security (RLS)** - User data protection
- **Indexes** - Optimized query performance
- **Triggers** - Automatic timestamp updates
- **Referential Integrity** - Proper foreign key relationships

### **✅ Scalable Design:**
- **UUID Primary Keys** - Globally unique identifiers
- **JSONB Fields** - Flexible data storage
- **Audit Trails** - Created/updated timestamps
- **Backup Support** - Data export capabilities

### **✅ User Experience:**
- **Fallback Mode** - Works without database
- **Demo Data** - Sample data for testing
- **Error Handling** - Graceful failure recovery
- **Performance Views** - Optimized data retrieval

---

## 🔍 **Verification Steps**

### **Check Database Setup:**
```bash
# Run this to verify everything works
python database/check_database.py
```

### **Test Platform:**
```bash
# Full platform test
python src/core/platform_core.py

# Demo mode test
python demos/experience_demo.py
```

### **Verify Tables in Supabase:**
1. Go to your Supabase dashboard
2. Check "Table Editor"
3. Should see tables: users, user_profiles, bookings, destinations, hotels, etc.

---

## 🛠️ **Troubleshooting**

### **Common Issues:**

#### **Connection Failed:**
```bash
# Check environment variables
cat .env

# Test connection
python -c "from supabase import create_client; print('Connection OK')"
```

#### **Tables Not Created:**
```bash
# Check Supabase logs
# Navigate to "Logs" in dashboard
# Look for SQL execution errors
```

#### **Permission Errors:**
```bash
# Check your Supabase project settings
# Ensure anon key has proper permissions
# Check RLS policies
```

### **Reset Database:**
```bash
# If you need to start over
# Go to Supabase dashboard → Settings → General → Reset Database
# Then run setup again
```

---

## 🎉 **Success Indicators**

### **✅ Database Setup Complete When:**
- [ ] 20+ tables created in Supabase
- [ ] Sample data populated
- [ ] `python src/core/platform_core.py` runs without errors
- [ ] User profiles can be created
- [ ] Bookings can be saved
- [ ] No connection errors in logs

### **✅ Platform Ready When:**
- [ ] All API keys configured
- [ ] Database connected successfully
- [ ] Demo runs without errors
- [ ] Travel packages can be created
- [ ] PDF generation works
- [ ] All features functional

---

## 💡 **Next Steps After Setup**

1. **Test the Platform:**
   ```bash
   python src/core/platform_core.py
   ```

2. **Try Interactive Demo:**
   ```bash
   python demos/experience_demo.py
   ```

3. **Explore Features:**
   - Create travel packages
   - Book flights and hotels
   - Generate PDF itineraries
   - Test group bookings

4. **Production Deployment:**
   - Set up domain and SSL
   - Configure production API keys
   - Set up monitoring and backups
   - Deploy web interface

---

## 📞 **Support**

### **If You Need Help:**
- **Check Logs:** `database/logs/setup_log_[timestamp].txt`
- **Supabase Docs:** https://supabase.com/docs
- **Platform Issues:** Check GitHub issues
- **Database Questions:** Review schema file comments

### **Common Commands:**
```bash
# Check setup status
python database/setup_database.py

# Test database connection
python -c "from src.core.platform_core import supabase; print('Connected!' if supabase else 'Not connected')"

# Run platform
python src/core/platform_core.py

# Run demo
python demos/experience_demo.py
```

---

## 🎯 **Summary**

**The AI Travel Platform database setup provides:**
- ✅ Complete schema with 20+ tables
- ✅ Automated setup script
- ✅ Manual setup option
- ✅ Production-ready features
- ✅ Fallback mode for demos
- ✅ Comprehensive documentation

**Choose your setup method and get started! 🚀**
