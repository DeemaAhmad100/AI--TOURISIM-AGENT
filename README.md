# 🌍 AI Travel Platform - Intelligent Travel Planning System

<div align="center">

![AI Travel Platform](https://img.shields.io/badge/AI%20Travel%20Platform-2.0-blue?style=for-the-badge&logo=airplane&logoColor=white)

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.130.0-red.svg?style=for-the-badge)](https://crewai.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--Turbo-green.svg?style=for-the-badge)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**🚀 Transform travel planning with AI-powered intelligence, automated booking, and personalized recommendations**

[🎮 Try Demo](#-quick-start) | [📖 Documentation](#-features) | [🔧 Setup](#-installation) | [🤝 Contributing](#-contributing)

</div>

---

## 🎯 **What is AI Travel Platform?**

An advanced AI-powered travel planning system that revolutionizes how people plan, book, and experience travel. Using cutting-edge artificial intelligence, our platform provides personalized itineraries, real-time booking, price optimization, and cultural intelligence for authentic travel experiences.

### **🧠 Core Problem We Solve:**
- **Complex Travel Planning**: Eliminates hours of research and planning
- **Price Optimization**: Finds best deals across multiple services  
- **Cultural Barriers**: Provides local insights and authentic experiences
- **Group Coordination**: Streamlines group travel management
- **Booking Fragmentation**: One platform for flights, hotels, restaurants, activities

---

## 🚀 **Quick Start**

### **🎮 Try the Interactive Demo (No Setup Required)**
```bash
git clone https://github.com/DeemaAhmad100/AI--TOURISIM-AGENT.git
cd "AI TRAVEL AGENT (TOURISIM)"
pip install -r requirements.txt
python apps/experience_demo.py
```
*Perfect for first-time users - experience AI travel planning instantly!*

### **🖥️ Run the Full Platform (CLI Interface)**
```bash
python apps/main.py
```
*Complete travel booking system with 10+ professional features*

### **🌐 Web Interface (Streamlit)**
```bash
streamlit run src/ui/streamlit_main.py
```
*Modern web interface with full platform features*
```bash
streamlit run src/ui/streamlit_ui.py
```
*Modern web dashboard - currently in development*

---

## ✨ **Key Features**

<details>
<summary>🧠 <strong>AI Travel Intelligence</strong></summary>

- **5 Specialized AI Agents**: Itinerary Architect, Experience Curator, Cultural Specialist, and more
- **GPT-3.5 Integration**: Advanced natural language processing for personalized planning
- **Real-time Research**: Live data integration with Tavily search API
- **Cultural Intelligence**: Local insights, customs, and authentic experiences
- **Smart Recommendations**: Personality-based activity matching and preferences

</details>

<details>
<summary>💳 <strong>Complete Booking System</strong></summary>

- **One-Click Booking**: Flights + Hotels + Restaurants + Activities in one package
- **Payment Processing**: Secure integration ready for multiple payment providers
- **Group Bookings**: Automated group coordination with smart discount calculation
- **Price Tracking**: Real-time price monitoring with alert notifications
- **PDF Itineraries**: Automated travel guide generation with maps and details

</details>

<details>
<summary>📱 <strong>Advanced Features</strong></summary>

- **Calendar Integration**: Google Calendar sync for trip management
- **Budget Optimization**: Dynamic pricing algorithms for maximum value
- **Accessibility Support**: Wheelchair accessibility and special needs accommodation
- **Multi-language**: International travel support with language preferences
- **Offline Access**: PDF guides work without internet connection

</details>

<details>
<summary>🔍 <strong>Smart Discovery</strong></summary>

- **Hidden Gems**: Local experiences beyond tourist attractions
- **Seasonal Intelligence**: Best times to visit with weather considerations
- **Anti-Tourist-Trap**: Authentic local recommendations over commercial options
- **Activity Matching**: Personality-based activity recommendations
- **Local Insider Tips**: Cultural etiquette and local customs guidance

</details>

---

## 🛠️ **Technology Stack**

### **🤖 AI & Intelligence**
- **CrewAI**: Multi-agent AI system for specialized travel planning
- **OpenAI GPT-3.5**: Natural language processing and intelligent responses
- **LangChain**: AI agent orchestration and tool integration
- **Tavily API**: Real-time travel research and data aggregation

### **💾 Database & Backend**
- **Supabase**: PostgreSQL database with real-time capabilities
- **Python 3.11+**: Modern Python with async capabilities
- **Dataclasses**: Type-safe data structures for travel components

### **📊 Integrations**
- **Google APIs**: Calendar integration and location services
- **Payment Ready**: Stripe integration framework for secure payments
- **PDF Generation**: ReportLab for automated travel guide creation
- **Email/SMS**: Notification system for booking confirmations

### **🎨 User Interfaces**
- **CLI Interface**: Full-featured command-line application (working)
- **Streamlit Web UI**: Modern web interface (in development)
- **Interactive Demo**: User-friendly experience demonstration

---

## 🔧 **Installation**

### **Prerequisites**
- Python 3.11 or higher
- Git

### **1. Clone Repository**
```bash
git clone https://github.com/DeemaAhmad100/AI--TOURISIM-AGENT.git
cd "AI TRAVEL AGENT (TOURISIM)"
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Environment Setup**
```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API keys
```

### **4. API Keys Configuration** 📋

> **� Complete Guide**: See [API_KEYS_GUIDE.md](API_KEYS_GUIDE.md) for detailed setup instructions

#### **🚨 ESSENTIAL (Required for AI Features):**
```env
OPENAI_API_KEY=your_openai_api_key_here
```
**Impact**: Powers AI travel agents and intelligent recommendations
**Cost**: ~$5-10/month for moderate usage
**Without it**: Platform runs in demo mode with mock data only

#### **🎯 RECOMMENDED (Enhanced Features):**
```env
TAVILY_API_KEY=your_tavily_api_key_here
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```
**Impact**: Real-time search + data persistence
**Cost**: Free tiers available (Tavily: 1,000 searches/month, Supabase: 50MB)
**Without it**: No live search or data persistence

#### **� OPTIONAL (Additional Features):**
```env
EMAIL_PASSWORD=your_email_password
GOOGLE_MAPS_API_KEY=your_google_maps_key
STRIPE_SECRET_KEY=your_stripe_key
```
**Impact**: Email notifications, maps, real payment processing
**Without it**: Features are disabled but core functionality remains

### **5. Usage Scenarios**

| Scenario | Keys Required | What Works | Best For |
|----------|---------------|------------|----------|
| **Demo Mode** | None | Basic UI, mock data | Testing & evaluation |
| **AI Mode** | OpenAI only | AI features, mock data | Development |
| **Enhanced Mode** | OpenAI + Tavily | AI + real-time search | Production testing |
| **Full Production** | OpenAI + Tavily + Supabase | All features | Live deployment |

### **6. Get Your API Keys**
- **OpenAI**: [Get API Key](https://platform.openai.com/api-keys) - Essential for AI
- **Tavily**: [Get API Key](https://app.tavily.com/) - Recommended for live data
- **Supabase**: [Create Project](https://supabase.com/) - Recommended for data persistence

---

## 📖 **Usage Examples**

### **🎯 Creating a Travel Package**
```bash
python src/core/platform_core.py
# Select option 1: Create Complete Travel Package
# Follow interactive prompts for destination, dates, preferences
```

### **🤖 Interactive Demo Experience**
```bash
python demos/experience_demo.py
# Experience AI travel planning with simulated responses
# Perfect for testing without API keys
```

### **🧪 Testing the System**
```bash
python tests/validate_tool_optimization.py
# Run comprehensive system validation
```

---

## 🏗️ **Project Structure**

```
AI TRAVEL AGENT (TOURISIM)/
├── 📁 src/                           # Main application source
│   ├── 📁 core/                      # Core application logic
│   │   ├── platform_core.py          # 🎯 MAIN APPLICATION
│   │   ├── main_app.py               # Organized architecture demo
│   │   └── config.py                 # Configuration management
│   ├── 📁 agents/                    # AI agents system
│   │   └── local_crewai/             # Custom travel AI agents
│   ├── 📁 database/                  # Database tools
│   ├── 📁 ui/                        # User interface components
│   └── 📁 utils/                     # Utility functions
├── 📁 demos/                         # Demo applications
│   └── experience_demo.py            # 🎮 INTERACTIVE DEMO
├── 📁 tests/                         # Testing framework
├── 📁 database/                      # Database schemas & scripts
├── 📁 docs/                          # Documentation
├── 📄 requirements.txt               # Python dependencies
└── 📄 README.md                      # This file
```

### **🎯 Main Entry Points:**
- **Full Platform**: `python src/core/platform_core.py`
- **Interactive Demo**: `python demos/experience_demo.py`
- **Database Setup**: `python database/setup_database.py`
- **Database Check**: `python database/check_database.py`

---

## 🏗️ **Expert Project Structure**

```
🏗️ AI-TRAVEL-PLATFORM (EXPERT STRUCTURE)/
├── 📁 src/                          # Source Code
│   ├── 📁 api_integration/          # API Integration Layer
│   │   ├── 📁 openai/              # OpenAI API services
│   │   ├── 📁 supabase/            # Supabase database services
│   │   ├── 📁 stripe/              # Stripe payment services
│   │   ├── 📁 google_apis/         # Google APIs integration
│   │   └── 📁 tavily/              # Tavily search services
│   ├── 📁 ai_agents/               # AI Agents & Workflows
│   ├── 📁 booking_system/          # Booking & Payment System
│   ├── 📁 core/                    # Core Business Logic
│   ├── 📁 database/                # Database Layer
│   ├── 📁 services/                # Business Services
│   └── 📁 ui/                      # User Interface
├── 📁 apps/                        # Application Entry Points
├── 📁 config/                      # Configuration
├── 📁 scripts/                     # Utility Scripts
├── 📁 tests/                       # Test Suite
├── 📁 docs/                        # Documentation
└── 📁 deployment/                  # Deployment Files
```

📋 **[View Complete Structure Guide](EXPERT_RESTRUCTURING_COMPLETE.md)**
🧭 **[Navigation Guide](NAVIGATION_GUIDE.md)**

---

## 🔍 **AI Agent Architecture**

### **Custom CrewAI Integration**
Our platform uses a hybrid approach combining the CrewAI framework with custom travel-specific agents:

- **CrewAI Package**: Core AI agent framework (external dependency)
- **Local CrewAI**: Custom travel agent implementations in `src/agents/local_crewai/`
- **5 Streamlined Agents**: Consolidated from 15+ basic agents for optimal performance

### **Intelligent Agents:**
1. **🏗️ Itinerary Architect**: Master trip planner with cultural intelligence
2. **🎨 Experience Curator**: Activity and restaurant specialist
3. **🌍 Cultural Specialist**: Local customs and authentic experiences
4. **💰 Budget Optimizer**: Price tracking and deal optimization
5. **🔍 Research Specialist**: Real-time data aggregation and analysis

---

## 🗄️ **Database Setup**

### **🎯 Quick Setup (Recommended)**
```bash
# 1. Create Supabase project at https://supabase.com
# 2. Add credentials to .env file
# 3. Run automated setup
python database/setup_database.py

# 4. Verify setup
python database/check_database.py
```

### **📊 Database Status**
- ✅ **Schema**: Complete 20+ table schema with relationships
- ✅ **Integration**: Fully coded in platform core
- ✅ **Security**: Row Level Security (RLS) policies
- ✅ **Performance**: Optimized indexes and views
- ✅ **Fallback**: Works without database for demos

### **🔧 Manual Setup Option**
1. **Create Supabase Project**: [supabase.com](https://supabase.com)
2. **Execute Schema**: Copy `database/schemas/enhanced_database_schema.sql` to Supabase SQL Editor
3. **Configure Environment**: Add `SUPABASE_URL` and `SUPABASE_KEY` to `.env`
4. **Test Connection**: Run `python database/check_database.py`

### **🎮 Demo Mode (No Database Required)**
The platform works with simulated data when database isn't configured - perfect for testing!

### **📋 Database Features**
- **User Management**: Profiles, preferences, travel history
- **Booking System**: Complete transaction tracking and management
- **Travel Services**: Hotels, flights, restaurants, activities
- **Intelligence**: Cultural insights, seasonal data, price tracking
- **Analytics**: Search behavior, user statistics, performance metrics

**📖 Detailed Setup Guide**: [database/DATABASE_SETUP_GUIDE.md](database/DATABASE_SETUP_GUIDE.md)

---

## 🎮 **Demo Capabilities**

The platform includes comprehensive demo functionality:

- **🎯 Intelligent Fallbacks**: Works without API keys using simulated responses
- **🌍 Global Coverage**: Demo data for destinations worldwide
- **💡 Feature Showcase**: Demonstrates all major platform capabilities
- **📊 Realistic Data**: Believable hotel, flight, and restaurant recommendations
- **🎨 Interactive Experience**: Guided tour through AI travel planning

---

## 🤝 **Contributing**

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### **Development Setup**
```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/AI--TOURISIM-AGENT.git

# Install development dependencies
pip install -r requirements.txt

# Run tests
python tests/validate_tool_optimization.py
```

### **Areas for Contribution**
- 🌐 Streamlit web interface development
- 🗄️ Database schema completion
- 🔌 Additional API integrations
- 🌍 Multi-language support
- 📱 Mobile application development
- 🧪 Test coverage expansion

---

## 📊 **Project Status**

- ✅ **Core AI System**: Fully functional with 5 specialized agents
- ✅ **CLI Interface**: Complete with 10+ features
- ✅ **Booking System**: End-to-end booking workflow
- ✅ **Demo System**: Comprehensive demonstration capabilities
- 🚧 **Web Interface**: Streamlit UI in development
- 🚧 **Database Schema**: Schema definition in progress
- 📋 **Mobile App**: Planned for future development

---

## 📞 **Support & Contact**

- **🐛 Issues**: [GitHub Issues](https://github.com/DeemaAhmad100/AI--TOURISIM-AGENT/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/DeemaAhmad100/AI--TOURISIM-AGENT/discussions)
- **📖 Documentation**: Available in `docs/` folder
- **✉️ Email**: For business inquiries and partnerships

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **CrewAI Team**: For the exceptional AI agent framework
- **OpenAI**: For GPT-3.5 capabilities enabling intelligent travel planning
- **Supabase**: For the robust database platform
- **Travel Community**: For feedback and feature suggestions

---

<div align="center">

**⭐ Star this repo if you find it valuable! ⭐**

*Transform your travel planning experience with AI-powered intelligence*

**Made with ❤️ for travelers around the world 🌍**

</div>
