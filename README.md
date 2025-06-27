# 🌍 AI Travel Agent - Intelligent Travel Planning System

An advanced AI-powered travel planning application that combines CrewAI agents with intelligent intent detection to provide comprehensive, context-aware travel recommendations for any destination worldwide.

## ✨ Features

### 🧠 Intelligent AI Agents
- **Destination Researcher & Cultural Analyst**: Provides comprehensive destination intelligence with cultural insights
- **Experience Curator & Activity Specialist**: Curates personalized attractions based on preferences and budget
- **Strategic Itinerary Architect**: Creates optimized day-by-day travel itineraries
- **Cultural Intelligence Expert & Insider Guide**: Offers deep cultural knowledge and practical travel advice

### 🎯 Core Capabilities
- **Smart Travel Planning**: CrewAI-powered multi-agent system for comprehensive travel plans
- **Intelligent Chat**: Natural language queries about any country with intent detection
- **Database Integration**: Supabase backend for storing destinations, attractions, and travel history
- **Global Coverage**: Expert knowledge for destinations worldwide
- **Cultural Sensitivity**: Respectful travel practices and authentic experiences
- **Budget Optimization**: Tailored recommendations for any budget level

### 🚀 Advanced Features
- Real-time web search integration via Tavily
- Context-aware recommendations based on traveler preferences
- Embedding-based intent detection system
- Adaptive itinerary planning with weather and crowd considerations
- Cultural intelligence and insider knowledge
- Multi-format output (console, file export)

## 🛠️ Technology Stack

- **AI Framework**: CrewAI for multi-agent orchestration
- **Language Model**: OpenAI GPT-3.5-turbo
- **Web Search**: Tavily Search API
- **Database**: Supabase (PostgreSQL)
- **Intent Detection**: Sentence Transformers, scikit-learn
- **Backend**: Python 3.8+
- **Environment**: dotenv for configuration

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Git (for cloning)
- OpenAI API key
- Tavily API key
- Supabase account and project

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-travel-agent.git
   cd ai-travel-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   SUPABASE_URL=your_supabase_project_url
   SUPABASE_KEY=your_supabase_anon_key
   ```

4. **Database Setup**
   - Create a Supabase project at [supabase.com](https://supabase.com)
   - Run the SQL scripts in `/database` folder to create tables
   - Update your `.env` file with Supabase credentials

5. **Run the application**
   ```bash
   python travel_agent.py
   ```

## 🎮 Usage

### Main Menu Options
1. **🗺️ Plan a New Trip**: Full AI-powered travel planning with 4 specialized agents
2. **📍 Browse Destinations**: View destinations stored in database
3. **🎯 View Attractions**: Explore attractions for specific destinations
4. **📚 Travel History**: View your previous travel plans
5. **🧠 Intelligent Chat**: Ask about any country with natural language
6. **🔧 Test Connection**: Verify database connectivity

### Example Queries
- "What are the best activities in Malaysia?"
- "Plan a 7-day cultural trip to Japan with moderate budget"
- "Tell me about food experiences in Thailand"
- "Best time to visit France for wine tourism"

## 🏗️ Project Structure

```
ai-travel-agent/
├── travel_agent.py              # Main application with menu system
├── enhanced_travel_agent.py     # Smart travel agent with embeddings
├── world_travel_expert.py       # Global travel expertise system
├── intent_detection.py          # Intent detection and classification
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── README.md                    # Project documentation
├── database/                    # Database setup scripts
│   ├── schema.sql              # Supabase table definitions
│   └── sample_data.sql         # Sample destinations and attractions
├── docs/                       # Additional documentation
│   ├── API_SETUP.md           # API keys setup guide
│   └── DATABASE_SETUP.md      # Database configuration guide
└── tests/                      # Test files and demos
    ├── test_enhanced_agents.py # Integration tests
    └── enhanced_system_demo.py # System demonstration
```

## 🔧 Configuration

### Required API Keys

1. **OpenAI API Key**
   - Sign up at [platform.openai.com](https://platform.openai.com)
   - Create an API key
   - Add to `.env` file

2. **Tavily API Key**
   - Register at [tavily.com](https://tavily.com)
   - Get your API key
   - Add to `.env` file

3. **Supabase Setup**
   - Create project at [supabase.com](https://supabase.com)
   - Copy project URL and anon key
   - Run database schema setup

### Database Schema
The application uses these main tables:
- `destinations`: Travel destinations with descriptions
- `attractions`: Tourist attractions linked to destinations  
- `travel_history`: User's travel plans and preferences
- `user_preferences`: Personalization data

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CrewAI** for the multi-agent framework
- **OpenAI** for the language model capabilities
- **Supabase** for the backend database solution
- **Tavily** for real-time web search functionality
- **Sentence Transformers** for embedding-based intent detection

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/YOUR_USERNAME/ai-travel-agent/issues) page
2. Create a new issue with detailed description
3. Join our [Discussions](https://github.com/YOUR_USERNAME/ai-travel-agent/discussions) for community support

## 🗺️ Roadmap

- [ ] Mobile app version
- [ ] Advanced visualization features
- [ ] Multi-language support
- [ ] Offline mode capabilities
- [ ] Social travel planning features
- [ ] Integration with booking platforms

---

**Made with ❤️ for travelers worldwide** 🌍✈️
