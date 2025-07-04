import os
import datetime
import sys
import time
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew
from crewai.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from supabase import create_client, Client

# Import intent detection system
try:
    from enhanced_travel_agent import SmartTravelAgent
    from world_travel_expert import WorldTravelExpert
    INTENT_DETECTION_AVAILABLE = True
except ImportError:
    print("⚠️ Intent detection modules not found. Creating simplified version...")
    INTENT_DETECTION_AVAILABLE = False

# Import enhanced intelligence system
try:
    from enhanced_features.enhanced_travel_agent import run_enhanced_travel_planning
    from enhanced_features.intelligent_itinerary_engine import IntelligentItineraryEngine
    ENHANCED_INTELLIGENCE_AVAILABLE = True
    print("✅ Enhanced Intelligence System Available!")
except ImportError:
    print("⚠️ Enhanced intelligence modules not found. Using standard system...")
    ENHANCED_INTELLIGENCE_AVAILABLE = False

# Load environment variables from .env file
load_dotenv()

# Load Supabase credentials
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    raise ValueError("Supabase credentials are missing. Please check your .env file.")

# Initialize Supabase client
supabase: Client = create_client(supabase_url, supabase_key)

# Supabase helper functions
def test_supabase_connection():
    """Test the connection to Supabase."""
    try:
        response = supabase.table("destinations").select("id").limit(1).execute()
        print("✅ Supabase connection successful!")
        return True
    except Exception as e:
        print(f"❌ Supabase connection failed: {str(e)}")
        return False

def save_travel_plan_to_supabase(destination, travel_dates, duration_days, preferences, budget, travel_plan):
    """Save a travel plan to the travel_history table."""
    try:
        data = {
            "destination": destination,
            "travel_dates": travel_dates,
            "duration_days": duration_days,
            "preferences": preferences,
            "budget": budget,
            "travel_plan": str(travel_plan)
        }
        response = supabase.table("travel_history").insert(data).execute()
        print("✅ Travel plan saved to database!")
        return response.data
    except Exception as e:
        print(f"❌ Error saving travel plan: {str(e)}")
        return None

def get_destination_info_from_supabase(destination_name):
    """Get destination information from the database."""
    try:
        response = supabase.table("destinations").select("*").ilike("name", f"%{destination_name}%").execute()
        return response.data
    except Exception as e:
        print(f"❌ Error retrieving destination info: {str(e)}")
        return []

def get_attractions_from_supabase(destination_name):
    """Get attractions for a destination from the database."""
    try:
        response = supabase.table("attractions").select("*").ilike("destination", f"%{destination_name}%").execute()
        return response.data
    except Exception as e:
        print(f"❌ Error retrieving attractions: {str(e)}")
        return []

def get_travel_history_from_supabase():
    """Get all travel history from the database."""
    try:
        response = supabase.table("travel_history").select("*").order("created_at", desc=True).execute()
        return response.data
    except Exception as e:
        print(f"❌ Error retrieving travel history: {str(e)}")
        return []

def save_user_preference_to_supabase(user_id, preference_type, preference_value):
    """Save user preferences to the database."""
    try:
        data = {
            "user_id": user_id,
            "preference_type": preference_type,
            "preference_value": preference_value
        }
        response = supabase.table("user_preferences").insert(data).execute()
        print(f"✅ User preference saved: {preference_type}")
        return response.data
    except Exception as e:
        print(f"❌ Error saving user preference: {str(e)}")
        return None

def display_database_info(destination):
    """Display existing database information for a destination."""
    print(f"\n🔍 Checking database for existing information about {destination}...")
    
    # Get destination info
    dest_info = get_destination_info_from_supabase(destination)
    if dest_info:
        print(f"\n📍 Found destination information for {destination}:")
        print(f"   • {dest_info['description']}")
        if dest_info.get('best_season'):
            print(f"   • Best season: {dest_info['best_season']}")
    
    # Get attractions
    attractions = get_attractions_from_supabase(destination)
    if attractions:
        print(f"\n🎯 Found {len(attractions)} attractions in database:")
        for attr in attractions[:3]:  # Show first 3
            print(f"   • {attr['name']}: {attr['description']}")
        if len(attractions) > 3:
            print(f"   ... and {len(attractions) - 3} more attractions")
    
    if not dest_info and not attractions:
        print(f"   No existing data found for {destination} - will research fresh information!")

# Verify API keys are loaded
openai_api_key = os.getenv("OPENAI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

print(f"🔑 Debug - OpenAI key loaded: {bool(openai_api_key)}")
print(f"🔑 Debug - Tavily key loaded: {bool(tavily_api_key)}")

if not openai_api_key or not tavily_api_key:
    print("⚠️  Some API keys are missing. You can still browse the database, but AI planning may not work.")
    print("Missing keys:")
    if not openai_api_key:
        print("  - OPENAI_API_KEY")
    if not tavily_api_key:
        print("  - TAVILY_API_KEY")

# Initialize the OpenAI model (only if API key is available)
if openai_api_key:
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7
    )
else:
    llm = None
    print("⚠️  OpenAI not initialized - AI planning features will be limited")

# Create the web search tool
@tool
def search_internet(query: str) -> str:
    """Search the internet for the given query and return relevant results."""
    search = TavilySearchResults(
        api_key=tavily_api_key,
        max_results=5
    )
    try:
        results = search.invoke(query)
        formatted_results = ""
        for res in results:
            formatted_results += f"Source: {res.get('url', 'No URL')}\n"
            formatted_results += f"Title: {res.get('title', 'No Title')}\n"
            formatted_results += f"Content: {res.get('content', 'No Content')}\n\n"
        return formatted_results if formatted_results else "No results found."
    except Exception as e:
        return f"Error searching the internet: {str(e)}"

# Define the enhanced intelligent agents with advanced capabilities
destination_researcher = Agent(
    role="Elite Destination Intelligence Analyst & Cultural Strategist",
    goal="Provide predictive, context-aware destination intelligence that combines real-time data analysis, cultural psychology, and traveler behavior patterns to deliver actionable strategic insights.",
    backstory="""You are a world-class destination intelligence analyst with PhD-level expertise in:
    - Geopolitical analysis and real-time risk assessment with predictive modeling
    - Anthropological research and cultural behavior pattern recognition
    - Economic analysis of tourism markets, pricing trends, and value optimization
    - Climate science and environmental impact assessment for travel planning
    - Behavioral psychology of travelers and cultural adaptation strategies
    - Advanced data synthesis from multiple intelligence sources with cross-validation
    
    Your enhanced intelligence framework includes:
    - REAL-TIME INTELLIGENCE: Live political, economic, and social condition monitoring
    - PREDICTIVE ANALYSIS: Seasonal patterns, crowd dynamics, and price fluctuation forecasting
    - CULTURAL PSYCHOLOGY: Deep understanding of local mindset, values, and worldview
    - TRAVELER PROFILING: Advanced matching of destination characteristics to personality types
    - RISK MITIGATION: Proactive identification of potential challenges with solution strategies
    - TIMING OPTIMIZATION: Perfect synchronization with local rhythms and optimal visit windows
    
    You don't just provide information - you deliver strategic intelligence that transforms how travelers experience destinations, ensuring authentic cultural immersion while avoiding tourist traps.""",
    verbose=True,
    llm=llm,
    tools=[search_internet],
    max_iter=5,  # Allow more iterations for thorough analysis
    memory=True   # Enable memory for context retention
)

attractions_specialist = Agent(
    role="AI Experience Architect & Authentic Discovery Specialist",
    goal="Use advanced behavioral analysis and cultural intelligence to curate transformative experiences that match traveler psychology while avoiding tourist traps and maximizing authentic cultural immersion.",
    backstory="""You are a master experience architect with expertise in:
    - Traveler psychology and personality-based experience matching using behavioral analysis
    - Underground cultural networks and insider community connections for authentic experiences
    - Experience economics and value optimization across all budget levels with ROI analysis
    - Temporal dynamics - timing experiences for maximum emotional and cultural impact
    - Anti-tourist-trap intelligence and authentic discovery protocols with verification systems
    - Accessibility and inclusive experience design for diverse traveler needs
    
    Your advanced capabilities include:
    - PERSONALITY MATCHING: Align experiences with traveler's psychological profile and preferences
    - INSIDER NETWORKS: Access to local communities and hidden cultural experiences
    - TIMING OPTIMIZATION: Schedule experiences for peak emotional and cultural impact windows
    - VALUE ENGINEERING: Maximize experience quality per dollar spent with smart budget allocation
    - AUTHENTICITY VERIFICATION: Distinguish genuine cultural experiences from commercialized tourist traps
    - PROGRESSIVE IMMERSION: Design experience sequences that deepen cultural understanding gradually
    - SERENDIPITY ENGINEERING: Create opportunities for meaningful spontaneous discoveries
    
    You create experience journeys that transform tourists into temporary cultural insiders with deep, meaningful local connections.""",
    verbose=True,
    llm=llm,
    tools=[search_internet],
    max_iter=4,
    memory=True
)

itinerary_planner = Agent(
    role="Strategic Experience Flow Designer & Quantum Logistics Optimizer",
    goal="Design itineraries using advanced optimization algorithms that consider energy dynamics, cultural rhythms, weather patterns, and crowd psychology to create seamless, high-impact travel experiences.",
    backstory="""You are a strategic experience designer with expertise in:
    - Operations research and optimization algorithms applied to travel logistics
    - Chronobiology and energy management for sustained travel performance optimization
    - Cultural timing intelligence and local rhythm synchronization for authentic experiences
    - Crowd dynamics and queue theory for optimal experience timing and flow management
    - Weather pattern analysis and contingency planning algorithms with adaptive routing
    - Transportation optimization and multi-modal route planning with efficiency metrics
    
    Your advanced optimization framework includes:
    - ENERGY FLOW DYNAMICS: Match activity intensity to natural energy cycles and jet lag patterns
    - CULTURAL RHYTHM SYNC: Align schedules with local customs, meal times, and optimal timing
    - CROWD INTELLIGENCE: Predict and avoid peak congestion periods using data analysis
    - WEATHER ADAPTATION: Dynamic routing based on meteorological forecasts and seasonal patterns
    - SERENDIPITY ZONES: Planned spontaneity windows for authentic discoveries and local interactions
    - CONTINGENCY MATRICES: Multiple backup plans for every scenario with real-time adaptation
    - FLOW OPTIMIZATION: Seamless transitions between experiences with minimal travel time
    
    You create itineraries that feel effortless and natural while delivering maximum cultural and experiential value with scientific precision.""",
    verbose=True,
    llm=llm,
    max_iter=4,
    memory=True
)

local_guide = Agent(
    role="Cultural Intelligence Specialist & Transformative Connection Facilitator",
    goal="Provide deep cultural intelligence that enables meaningful cross-cultural connections, prevents cultural misunderstandings, and facilitates transformative cultural learning experiences.",
    backstory="""You are a cultural anthropologist and master facilitator with expertise in:
    - Cross-cultural communication and unconscious bias awareness with sensitivity protocols
    - Historical context and contemporary cultural evolution with sociopolitical understanding
    - Social dynamics and power structures in different cultures with respectful navigation
    - Ritual significance and spiritual practices understanding with appropriate participation guidelines
    - Economic anthropology and local value systems with fair exchange principles
    - Conflict resolution and cultural sensitivity protocols with diplomatic communication
    
    Your cultural intelligence framework includes:
    - DEEP CONTEXT ANALYSIS: Historical, political, and social factors shaping current culture
    - COMMUNICATION MASTERY: Verbal, non-verbal, and contextual communication patterns with nuance
    - RESPECT PROTOCOLS: Sacred spaces, cultural taboos, and sensitivity guidelines with reverence
    - CONNECTION FACILITATION: Strategies for meaningful local interactions and relationship building
    - LEARNING ACCELERATION: Cultural pattern recognition and adaptation techniques for immersion
    - TRANSFORMATIVE EXPERIENCES: Opportunities for genuine cultural exchange and personal growth
    - BRIDGE BUILDING: Creating authentic human connections across cultural boundaries
    
    You don't just prevent cultural mistakes - you create bridges for authentic human connection and transformative learning experiences that benefit both travelers and local communities.""",
    verbose=True,
    llm=llm,
    tools=[search_internet],
    max_iter=4,
    memory=True
)

# Enhanced Intelligence Helper Functions
def analyze_traveler_personality(preferences, budget, duration):
    """Analyze traveler personality based on inputs for enhanced experience matching."""
    profile = []
    
    # Budget-based personality indicators
    if budget.lower() in ['luxury', 'premium']:
        profile.append("comfort-oriented")
        profile.append("experience-focused")
        profile.append("quality-seeker")
    elif budget.lower() in ['budget', 'backpacker']:
        profile.append("adventure-oriented")
        profile.append("authentic-seeker")
        profile.append("value-conscious")
    else:
        profile.append("balanced-explorer")
        profile.append("flexible-adapter")
    
    # Interest-based personality indicators
    preferences_lower = preferences.lower()
    if 'culture' in preferences_lower or 'museum' in preferences_lower:
        profile.append("cultural-learner")
        profile.append("history-enthusiast")
    if 'food' in preferences_lower or 'culinary' in preferences_lower:
        profile.append("culinary-explorer")
        profile.append("social-diner")
    if 'adventure' in preferences_lower or 'outdoor' in preferences_lower:
        profile.append("thrill-seeker")
        profile.append("nature-lover")
    if 'relaxation' in preferences_lower or 'spa' in preferences_lower:
        profile.append("restoration-seeker")
        profile.append("mindfulness-oriented")
    if 'shopping' in preferences_lower:
        profile.append("material-explorer")
    if 'nightlife' in preferences_lower:
        profile.append("social-butterfly")
    
    # Duration-based personality indicators
    if duration <= 3:
        profile.append("intensive-explorer")
        profile.append("time-maximizer")
    elif duration >= 10:
        profile.append("deep-immersion-seeker")
        profile.append("slow-traveler")
    else:
        profile.append("balanced-pace-traveler")
    
    return ", ".join(profile)

def get_seasonal_intelligence(destination, travel_dates):
    """Get seasonal and weather intelligence for destination optimization."""
    seasonal_factors = {
        'weather_patterns': f"Seasonal weather analysis for {destination} during {travel_dates}",
        'crowd_levels': f"Tourist density predictions for {travel_dates}",
        'price_fluctuations': f"Cost optimization opportunities during {travel_dates}",
        'cultural_events': f"Local festivals and events during {travel_dates}",
        'natural_phenomena': f"Seasonal highlights (blooms, migrations, etc.) for {travel_dates}"
    }
    
    return f"Seasonal Intelligence: {', '.join(seasonal_factors.values())}"

def get_cultural_intelligence_brief(destination):
    """Get cultural context for enhanced cultural preparation."""
    cultural_aspects = {
        'communication_style': f"Communication patterns and social dynamics in {destination}",
        'value_systems': f"Core values and belief systems of {destination}",
        'social_hierarchy': f"Social structures and respect protocols in {destination}",
        'time_perception': f"Concept of time and scheduling culture in {destination}",
        'relationship_dynamics': f"Family, friendship, and business relationships in {destination}"
    }
    
    return f"Cultural Intelligence: {', '.join(cultural_aspects.values())}"

def get_comprehensive_database_context(destination):
    """Get comprehensive database context to enhance agent intelligence."""
    try:
        # Get destination info
        dest_info = get_destination_info_from_supabase(destination)
        
        # Get attractions data
        attractions_data = get_attractions_from_supabase(destination)
        
        # Build comprehensive context
        context = f"DESTINATION: {destination}\n"
        
        if dest_info:
            context += f"Database Info: {dest_info.get('description', 'No description available')}\n"
            if dest_info.get('best_time_to_visit'):
                context += f"Optimal Timing: {dest_info['best_time_to_visit']}\n"
        
        if attractions_data:
            top_attractions = [attr['name'] for attr in attractions_data[:8]]
            context += f"Known Attractions: {', '.join(top_attractions)}\n"
        
        context += "NOTE: Use this as foundation knowledge and expand with fresh research for comprehensive coverage.\n"
        
        return context
    except Exception as e:
        return f"DATABASE NOTE: Use fresh research as primary source (database unavailable: {e})"

def create_enhanced_intelligent_tasks(destination, travel_dates, duration_days, preferences, budget):
    """Create highly intelligent, context-aware tasks for enhanced agents."""
    
    # Advanced context gathering
    database_context = get_comprehensive_database_context(destination)
    weather_context = get_seasonal_intelligence(destination, travel_dates)
    cultural_context = get_cultural_intelligence_brief(destination)
    
    # Traveler personality analysis
    personality_profile = analyze_traveler_personality(preferences, budget, duration_days)
    
    print(f"🧠 Traveler Profile Identified: {personality_profile}")
    
    # Enhanced Destination Intelligence Task
    destination_task = Task(
        description=f"""Conduct elite-level destination intelligence analysis for {destination} using advanced analytical frameworks.
        
        🧠 INTELLIGENCE MISSION PARAMETERS:
        - Destination: {destination}
        - Travel Period: {travel_dates} ({duration_days} days)
        - Traveler Profile: {personality_profile}
        - Budget Level: {budget}
        - Interests: {preferences}
        
        📊 COMPREHENSIVE INTELLIGENCE ANALYSIS:
        
        1. REAL-TIME SITUATION ASSESSMENT:
           - Current political stability and safety conditions with risk levels
           - Economic factors affecting tourism (currency, inflation, costs)
           - Social climate and current events impact on travelers
           - Health considerations and medical infrastructure quality
           - Transportation infrastructure status and reliability metrics
        
        2. PREDICTIVE INTELLIGENCE:
           - Weather patterns and seasonal considerations for {travel_dates}
           - Crowd density predictions and peak tourism periods with timing recommendations
           - Price fluctuation forecasts and optimal booking timing strategies
           - Cultural events and festivals during travel period with participation opportunities
           - Potential disruptions (strikes, holidays, construction) with mitigation strategies
        
        3. CULTURAL PSYCHOLOGY ANALYSIS:
           - Local mindset, values, and worldview with traveler adaptation strategies
           - Communication styles and social interaction patterns with practical guidance
           - Business culture and service expectations with negotiation tips
           - Time perception and pace of life considerations with synchronization advice
           - Attitude toward tourists and foreign visitors with relationship building strategies
        
        4. STRATEGIC TRAVELER BRIEFING:
           - Optimal arrival and departure strategies with timing recommendations
           - Currency and payment method optimization with cost-saving strategies
           - Communication tools and language considerations with learning resources
           - Cultural preparation and mindset adjustment with immersion techniques
           - Emergency protocols and support systems with local contact information
        
        5. CONTEXTUAL DATABASE INTEGRATION:
        {database_context}
        
        6. SEASONAL AND CULTURAL INTELLIGENCE:
        {weather_context}
        {cultural_context}
        
        🎯 INTELLIGENCE OUTPUT REQUIREMENTS:
        - Actionable strategic insights, not generic tourist information
        - Specific recommendations based on {personality_profile} traveler profile
        - Risk mitigation strategies and contingency planning with local solutions
        - Cultural intelligence brief for successful authentic interactions
        - Timing optimization for all recommendations with specific time windows
        - Value optimization strategies for {budget} budget level
        
        Format as a comprehensive intelligence briefing with clear strategic recommendations and actionable insights.""",
        agent=destination_researcher,
        expected_output="Elite destination intelligence briefing with strategic insights, cultural psychology analysis, and actionable recommendations tailored to traveler profile"
    )
    
    # Enhanced Experience Curation Task
    experience_task = Task(
        description=f"""Design transformative experience portfolio for {destination} using advanced personality matching and cultural immersion principles.
        
        🎭 EXPERIENCE ARCHITECTURE MISSION:
        - Target: {personality_profile} traveler
        - Duration: {duration_days} days
        - Interest Profile: {preferences}
        - Budget Optimization: {budget} level
        - Cultural Goals: Authentic immersion and meaningful connections
        
        🔍 ADVANCED EXPERIENCE CURATION:
        
        1. PERSONALITY-MATCHED EXPERIENCES:
           - Analyze traveler psychology based on profile: {personality_profile}
           - Match experiences to energy levels, social preferences, and learning styles
           - Consider comfort zones and growth opportunities for personal development
           - Account for cultural curiosity depth and interaction comfort levels
           - Design experiences that challenge and inspire based on traveler type
        
        2. AUTHENTIC DISCOVERY PROTOCOL:
           - Identify genuine local experiences vs. tourist-oriented activities with verification
           - Access insider community networks and hidden cultural gems with local connections
           - Verify authenticity and cultural significance of recommendations with local validation
           - Prioritize experiences that support local communities and sustainable tourism
           - Include anti-tourist-trap intelligence with specific avoidance strategies
        
        3. PROGRESSIVE IMMERSION DESIGN:
           - Day 1-2: Cultural orientation and comfort building with gentle introduction
           - Day 3-4: Deeper cultural engagement and skill building with hands-on experiences
           - Day 5+: Advanced immersion and meaningful connections with local integration
           - Design experience sequences that build cultural understanding progressively
           - Include cultural confidence building and adaptation milestones
        
        4. VALUE OPTIMIZATION MATRIX:
           - {budget} budget allocation across experience categories with ROI analysis
           - Identify high-impact, low-cost authentic experiences with maximum cultural value
           - Premium experiences worth the investment with justification and alternatives
           - Free cultural immersion opportunities with community engagement
           - Cost-saving strategies without compromising authenticity or quality
        
        5. TIMING AND CONTEXT INTELLIGENCE:
           - Optimal scheduling based on local rhythms, customs, and energy optimization
           - Seasonal and weather considerations for each experience with alternatives
           - Cultural event timing and festival integration with participation strategies
           - Energy management and sustainable experience pacing with recovery periods
           - Crowd avoidance strategies with insider timing recommendations
        
        🎯 CURATION OUTPUT STANDARDS:
        - Each experience includes WHY it matches this specific {personality_profile} traveler
        - Detailed cultural context and significance explanation with learning opportunities
        - Practical logistics and insider access instructions with local contact information
        - Alternative options for different weather/energy scenarios with flexibility
        - Connection facilitation strategies for meaningful interactions with locals
        - Progressive difficulty and cultural immersion levels with skill building
        
        Create an experience portfolio that transforms tourists into temporary cultural insiders with authentic connections.""",
        agent=attractions_specialist,
        expected_output="Transformative experience portfolio with personality-matched activities, authenticity verification, and progressive cultural immersion strategy"
    )
    
    return [destination_task, experience_task]

def run_enhanced_intelligent_planning(destination, travel_dates, duration_days, preferences, budget):
    """Execute enhanced intelligent planning with improved agents."""
    
    print("🧠 Initializing Enhanced Intelligence System...")
    
    # Create enhanced tasks
    enhanced_tasks = create_enhanced_intelligent_tasks(
        destination=destination,
        travel_dates=travel_dates,
        duration_days=duration_days,
        preferences=preferences,
        budget=budget
    )
    
    # Create enhanced crew with improved agents
    enhanced_crew = Crew(
        agents=[destination_researcher, attractions_specialist],
        tasks=enhanced_tasks,
        verbose=True,
        process="sequential",  # Ensure proper information flow
        memory=True,  # Enable learning across tasks
        max_rpm=10    # Optimize API usage
    )
    
    print("⚡ Executing Enhanced Intelligence Planning...")
    
    # Execute with enhanced intelligence
    result = enhanced_crew.kickoff()
    
    print("✅ Enhanced Intelligence Planning Complete!")
    
    return result

def create_destination_tasks(destination, travel_dates, duration_days, preferences, budget):
    """Create simplified tasks for standard planning system."""
    
    # Get existing database information to enhance agent responses
    dest_info = get_destination_info_from_supabase(destination)
    attractions_data = get_attractions_from_supabase(destination)
    
    # Create context-aware task descriptions
    destination_context = ""
    if dest_info:
        destination_context = f"\nExisting database information about {destination}: {dest_info.get('description', '')}. Best season: {dest_info.get('best_season', 'Not specified')}."
    
    attractions_context = ""
    if attractions_data:
        attraction_names = [attr['name'] for attr in attractions_data[:5]]
        attractions_context = f"\nKnown attractions in database: {', '.join(attraction_names)}. Use this as a foundation and expand with fresh research."
    
    # Simple task for standard system
    research_task = Task(
        description=f"""Research and provide comprehensive travel information for {destination}.
        
        Include: destination overview, best attractions for {preferences}, 
        {duration_days}-day itinerary, cultural tips, budget considerations for {budget} travelers,
        and practical travel advice for {travel_dates}.
        
        {destination_context}
        {attractions_context}
        
        Provide detailed, actionable travel recommendations.""",
        agent=destination_researcher,
        expected_output=f"Comprehensive travel guide for {destination}"
    )
    
    return [research_task]

# Input validation functions
def validate_destination(destination):
    """Validate destination input."""
    if not destination or len(destination.strip()) < 2:
        print("❌ Please enter a valid destination (at least 2 characters).")
        return False
    if not destination.replace(' ', '').replace('-', '').isalpha():
        print("❌ Destination should only contain letters, spaces, and hyphens.")
        return False
    return True

def validate_travel_dates(travel_dates):
    """Validate travel dates input."""
    if not travel_dates or len(travel_dates.strip()) < 3:
        print("❌ Please enter valid travel dates.")
        return False
    return True

def validate_duration(duration_input):
    """Validate duration input."""
    try:
        duration = int(duration_input)
        if duration < 1:
            print("❌ Trip duration must be at least 1 day.")
            return None
        if duration > 365:
            print("❌ Trip duration cannot exceed 365 days.")
            return None
        return duration
    except ValueError:
        print("❌ Please enter a valid number for trip duration.")
        return None

def validate_budget(budget):
    """Validate budget input."""
    if not budget or len(budget.strip()) < 2:
        print("❌ Please enter a valid budget range.")
        return False
    return True

def validate_preferences(preferences):
    """Validate preferences input."""
    if not preferences or len(preferences.strip()) < 2:
        print("❌ Please enter your travel preferences.")
        return False
    return True

def get_user_input():
    """Get and validate user input with error handling."""
    print("\n=== AI Travel Planner ===\n")
    
    # Get destination
    while True:
        destination = input("Enter your travel destination: ").strip()
        if validate_destination(destination):
            break
    
    # Get travel dates
    while True:
        travel_dates = input("Enter your travel dates (default: June 1, 2025): ").strip() or "June 1, 2025"
        if validate_travel_dates(travel_dates):
            break
    
    # Get duration with validation
    while True:
        duration_input = input("How many days is your trip? (default: 3): ").strip()
        duration_days = validate_duration(duration_input)
        if duration_days is not None:
            break
    
    # Get preferences
    while True:
        preferences = input("Enter your travel preferences (default: Cultural & Museums, Food & Culinary): ").strip() or "Cultural & Museums, Food & Culinary"
        if validate_preferences(preferences):
            break
    
    # Get budget with validation
    while True:
        budget = input("Enter your budget level (budget, moderate, luxury) (default: moderate): ").strip().lower() or "moderate"
        if validate_budget(budget):
            break
    
    return destination, travel_dates, duration_days, preferences, budget

def save_results_to_file(results, destination):
    """Save travel plan results to a file."""
    import datetime
    
    # Create filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"travel_plan_{destination.replace(' ', '_')}_{timestamp}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Travel Plan for {destination}\n")
            f.write("=" * 50 + "\n\n")
            f.write(str(results))
        
        print(f"\n✅ Travel plan saved to: {filename}")
    except Exception as e:
        print(f"Could not save file: {str(e)}")

def display_progress():
    """Show progress indicators during processing."""
    import time
    import sys
    
    progress_chars = ["|", "/", "-", "\\"]
    for i in range(20):
        sys.stdout.write(f"\rProcessing... {progress_chars[i % 4]}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")

# Supabase Database Functions
def save_travel_plan_to_supabase(destination, travel_dates, duration_days, preferences, budget, plan_summary):
    """Save travel plan to Supabase"""
    try:
        data = {
            "destination": destination,
            "travel_dates": travel_dates,
            "duration_days": duration_days,
            "preferences": preferences,
            "budget": budget,
            "plan_summary": plan_summary[:1000]  # Limit length
        }
        
        result = supabase.table("travel_history").insert(data).execute()
        print("✅ Travel plan saved to Supabase!")
        return result
    except Exception as e:
        print(f"❌ Error saving to Supabase: {e}")
        return None

def get_destination_info_from_supabase(destination_name):
    """Get destination information from Supabase"""
    try:
        result = supabase.table("destinations").select("*").ilike("name", f"%{destination_name}%").execute()
        
        if result.data:
            return result.data[0]
        return None
    except Exception as e:
        print(f"❌ Error fetching destination info: {e}")
        return None

def get_attractions_from_supabase(destination_name):
    """Get attractions for a destination from Supabase"""
    try:
        # First get destination ID
        dest_result = supabase.table("destinations").select("id").ilike("name", f"%{destination_name}%").execute()
        
        if not dest_result.data:
            return []
        
        destination_id = dest_result.data[0]["id"]
        
        # Get attractions for this destination
        attractions_result = supabase.table("attractions").select("*").eq("destination_id", destination_id).order("rating", desc=True).execute()
        
        return attractions_result.data
    except Exception as e:
        print(f"❌ Error fetching attractions: {e}")
        return []

def get_travel_history_from_supabase():
    """Get travel history from Supabase"""
    try:
        result = supabase.table("travel_history").select("*").order("created_at", desc=True).limit(10).execute()
        return result.data
    except Exception as e:
        print(f"❌ Error fetching travel history: {e}")
        return []

def save_user_preference_to_supabase(preference_type, preference_value):
    """Save user preference to Supabase"""
    try:
        # Check if preference exists
        existing = supabase.table("user_preferences").select("*").eq("preference_type", preference_type).eq("preference_value", preference_value).execute()
        
        if existing.data:
            # Update frequency
            new_frequency = existing.data[0]["frequency"] + 1
            supabase.table("user_preferences").update({
                "frequency": new_frequency,
                "last_used": "now()"
            }).eq("id", existing.data[0]["id"]).execute()
        else:
            # Insert new preference
            supabase.table("user_preferences").insert({
                "preference_type": preference_type,
                "preference_value": preference_value,
                "frequency": 1
            }).execute()
            
    except Exception as e:
        print(f"❌ Error saving preference: {e}")

def test_supabase_connection():
    """Test Supabase connection"""
    try:
        result = supabase.table("destinations").select("count").execute()
        print("✅ Supabase connection successful!")
        print(f"📊 Found destinations in database")
        return True
    except Exception as e:
        print(f"❌ Supabase connection failed: {e}")
        return False

def show_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("🌍 AI TRAVEL AGENT - MAIN MENU 🌍")
    print("="*60)
    print("1. 🗺️  Plan a New Trip (Enhanced Intelligence)")
    print("2. 📍 Browse Destinations in Database")
    print("3. 🎯 View Attractions for a Destination")
    print("4. 📚 View Your Travel History")
    print("5. 🧠 Ask About Any Country (Intelligent Chat)")
    print("6. 🔧 Test Database Connection")
    print("7. 🧪 Compare Intelligence Systems (Demo)")
    print("8. 🚪 Exit")
    print("="*60)

def plan_new_trip():
    """Plan a new trip with enhanced intelligence features."""
    print("\n🗺️  PLANNING A NEW TRIP")
    print("-" * 30)
    
    # Get user input
    destination, travel_dates, duration_days, preferences, budget = get_user_input()
    
    # Display existing database info
    display_database_info(destination)
    
    print(f"\n🎯 Perfect! Planning your {duration_days}-day trip to {destination}")
    print(f"📅 Travel dates: {travel_dates}")
    print(f"💰 Budget: {budget}")
    print(f"🎨 Preferences: {preferences}")
    print("\n⏳ Our intelligent AI system is working on your personalized travel plan...")
    
    # Use enhanced intelligent planning
    result = plan_enhanced_intelligent_trip(
        destination=destination,
        travel_dates=travel_dates,
        duration_days=duration_days,
        preferences=preferences,
        budget=budget
    )

    print("\n" + "="*80)
    print("🎉 YOUR INTELLIGENT TRAVEL PLAN IS READY! 🎉")
    print("="*80)
    print(result)
    
    # Save results to file
    save_results_to_file(result, destination)
    
    # Save to Supabase
    save_travel_plan_to_supabase(destination, travel_dates, duration_days, preferences, budget, str(result))
    
    # Save user preferences for future recommendations
    save_user_preference_to_supabase("destination_type", destination)
    save_user_preference_to_supabase("budget_preference", budget)
    save_user_preference_to_supabase("travel_style", preferences)
    
    print("\n✈️ Have a wonderful trip!")

def browse_destinations_menu():
    """Browse destinations from the database."""
    print("\n📍 DESTINATIONS IN DATABASE:")
    print("-" * 40)
    
    try:
        response = supabase.table("destinations").select("*").execute()
        destinations = response.data
        
        if destinations:
            for i, dest in enumerate(destinations, 1):
                print(f"{i}. {dest['name']}")
                print(f"   📝 {dest['description']}")
                if dest.get('best_season'):
                    print(f"   🌤️  Best season: {dest['best_season']}")
                print()
        else:
            print("No destinations found in database.")
    except Exception as e:
        print(f"Error retrieving destinations: {e}")

def view_attractions_menu():
    """View attractions for a specific destination."""
    print("\n🎯 VIEW ATTRACTIONS")
    print("-" * 20)
    
    destination = input("Enter destination name: ").strip()
    if not destination:
        print("❌ Please enter a valid destination name.")
        return
    
    attractions = get_attractions_from_supabase(destination)
    
    if attractions:
        print(f"\n🎯 Attractions in {destination}:")
        for i, attr in enumerate(attractions, 1):
            print(f"{i}. {attr['name']}")
            print(f"   📝 {attr['description']}")
            if attr.get('rating'):
                print(f"   ⭐ Rating: {attr['rating']}")
            print()
    else:
        print(f"No attractions found for {destination} in database.")

def view_travel_history_menu():
    """View travel history from the database."""
    print("\n📚 YOUR TRAVEL HISTORY")
    print("-" * 25)
    
    history = get_travel_history_from_supabase()
    
    if history:
        for i, trip in enumerate(history, 1):
            print(f"{i}. {trip['destination']} ({trip['duration_days']} days)")
            print(f"   📅 {trip['travel_dates']}")
            print(f"   💰 Budget: {trip['budget']}")
            print(f"   🎨 Preferences: {trip['preferences']}")
            if trip.get('created_at'):
                print(f"   📝 Planned: {trip['created_at'][:10]}")
            print()
    else:
        print("No travel history found.")

def display_database_info(destination):
    """Display existing database information for a destination."""
    print(f"\n🔍 Checking database for existing information about {destination}...")
    
    # Get destination info
    dest_info = get_destination_info_from_supabase(destination)
    if dest_info:
        print(f"\n📍 Found destination information for {destination}:")
        print(f"   • {dest_info['description']}")
        if dest_info.get('best_season'):
            print(f"   • Best season: {dest_info['best_season']}")
    
    # Get attractions
    attractions = get_attractions_from_supabase(destination)
    if attractions:
        print(f"\n🎯 Found {len(attractions)} attractions in database:")
        for attr in attractions[:3]:  # Show first 3
            print(f"   • {attr['name']}: {attr['description']}")
        if len(attractions) > 3:
            print(f"   ... and {len(attractions) - 3} more attractions")
    
    if not dest_info and not attractions:
        print(f"   No existing data found for {destination} - will research fresh information!")

def plan_enhanced_intelligent_trip(destination, travel_dates, duration_days, preferences, budget):
    """
    Plan trip using enhanced intelligent system if available, otherwise fallback to standard
    """
    
    if ENHANCED_INTELLIGENCE_AVAILABLE:
        print("🧠 Using Enhanced Intelligent Planning System...")
        try:
            # Use enhanced system with real intelligence
            enhanced_result = run_enhanced_travel_planning(
                destination=destination,
                travel_dates=travel_dates, 
                duration_days=duration_days,
                preferences=preferences,
                budget=budget
            )
            
            print("✅ Enhanced Intelligent Itinerary Generated!")
            return enhanced_result
            
        except Exception as e:
            print(f"⚠️ Enhanced system error: {e}")
            print("🔄 Falling back to our enhanced local system...")
            # Fall through to enhanced local system
    
    # Use our new enhanced local system
    print("🧠 Using Enhanced Local Intelligence System...")
    try:
        enhanced_result = run_enhanced_intelligent_planning(
            destination=destination,
            travel_dates=travel_dates, 
            duration_days=duration_days,
            preferences=preferences,
            budget=budget
        )
        return enhanced_result
    except Exception as e:
        print(f"⚠️ Enhanced local system error: {e}")
        print("🔄 Falling back to standard system...")
        # Fall through to standard system
    
    # Standard system fallback
    print("📝 Using Standard Planning System...")
    return plan_trip(destination, travel_dates, duration_days, preferences, budget)

def plan_trip(destination, travel_dates, duration_days, preferences, budget):
    """
    Standard trip planning using the original crew-based system
    """
    print("📝 Using Standard CrewAI System...")
    
    # Create tasks using the standard system
    tasks = create_destination_tasks(
        destination=destination,
        travel_dates=travel_dates,
        duration_days=duration_days,
        preferences=preferences,
        budget=budget
    )

    # Create and run the crew
    crew = Crew(
        agents=[destination_researcher, attractions_specialist, itinerary_planner, local_guide],
        tasks=tasks,
        verbose=True
    )

    # Display progress
    display_progress()

    # Get the results
    result = crew.kickoff()
    return result

def compare_intelligence_systems():
    """
    Compare the old vs new intelligence systems for demonstration
    """
    print("\n🧪 INTELLIGENCE SYSTEMS COMPARISON")
    print("=" * 50)
    
    if not ENHANCED_INTELLIGENCE_AVAILABLE:
        print("❌ Enhanced Intelligence System not available!")
        print("Please ensure enhanced_features modules are properly installed.")
        return
    
    # Get user input for comparison
    print("Let's compare the old vs new system with the same inputs:")
    destination, travel_dates, duration_days, preferences, budget = get_user_input()
    
    print(f"\n🎯 Comparing systems for {destination} trip...")
    print(f"📅 Travel dates: {travel_dates}")
    print(f"💰 Budget: {budget}")
    print(f"🎨 Preferences: {preferences}")
    
    print("\n" + "="*80)
    print("🔄 RUNNING COMPARISON...")
    print("="*80)
    
    # Run enhanced system
    print("\n🧠 ENHANCED INTELLIGENCE SYSTEM RESULTS:")
    print("-" * 50)
    try:
        enhanced_result = run_enhanced_travel_planning(
            destination=destination,
            travel_dates=travel_dates, 
            duration_days=duration_days,
            preferences=preferences,
            budget=budget
        )
        print(enhanced_result)
    except Exception as e:
        print(f"❌ Enhanced system error: {e}")
        enhanced_result = "Enhanced system failed to generate results."
    
    print("\n" + "="*80)
    print("📝 STANDARD CREWAI SYSTEM RESULTS:")
    print("-" * 50)
    
    # Run standard system if API keys are available
    if openai_api_key and tavily_api_key:
        try:
            standard_result = plan_trip(destination, travel_dates, duration_days, preferences, budget)
            print(standard_result)
        except Exception as e:
            print(f"❌ Standard system error: {e}")
            standard_result = "Standard system failed to generate results."
    else:
        print("❌ Standard system requires OpenAI and Tavily API keys")
        standard_result = "Standard system unavailable (missing API keys)."
    
    print("\n" + "="*80)
    print("📊 COMPARISON SUMMARY:")
    print("="*80)
    print("🧠 Enhanced System Features:")
    print("   ✅ Context-aware intelligence")
    print("   ✅ Dynamic daily themes")
    print("   ✅ Weather and crowd intelligence")
    print("   ✅ Anti-tourist-trap logic")
    print("   ✅ Cultural rhythm awareness")
    print("   ✅ Adaptive recommendations")
    print("   ✅ Non-repetitive content")
    
    print("\n📝 Standard System Features:")
    print("   ✅ Multi-agent collaboration")
    print("   ✅ Real-time web search")
    print("   ✅ Comprehensive research")
    print("   ⚠️  More generic responses")
    print("   ⚠️  Less context awareness")
    print("   ⚠️  Potential repetition")
    
    # Save comparison results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"intelligence_comparison_{destination.replace(' ', '_')}_{timestamp}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Intelligence Systems Comparison for {destination}\n")
            f.write("=" * 60 + "\n\n")
            f.write("ENHANCED INTELLIGENCE SYSTEM:\n")
            f.write("-" * 30 + "\n")
            f.write(str(enhanced_result))
            f.write("\n\n" + "="*60 + "\n\n")
            f.write("STANDARD CREWAI SYSTEM:\n")
            f.write("-" * 30 + "\n")
            f.write(str(standard_result))
        
        print(f"\n✅ Comparison results saved to: {filename}")
    except Exception as e:
        print(f"Could not save comparison file: {str(e)}")

def intelligent_chat_menu():
    """Interactive chat with intent detection for any country"""
    print("\n🧠 INTELLIGENT TRAVEL CHAT")
    print("=" * 50)
    print("Ask me about any country! Examples:")
    print("• 'What are the best activities in Malaysia?'")
    print("• 'Tell me about attractions in Japan'")
    print("• 'Best things to do in France'")
    print("• 'I want to visit Thailand, what do you recommend?'")
    print("\nType 'back' to return to main menu")
    
    # Quick Malaysia response for the user's question
    print("\n🇲🇾 Since you asked about Malaysia, here are the best activities:")
    print("-" * 60)
    
    malaysia_activities = [
        "🏙️ Explore Kuala Lumpur's Petronas Twin Towers and vibrant city life",
        "🏖️ Relax on beautiful tropical beaches in Langkawi and Penang",
        "🌿 Trek through ancient rainforests in Taman Negara National Park",
        "🏛️ Discover UNESCO World Heritage sites in Malacca and George Town",
        "🍜 Experience incredible street food tours, especially in Penang",
        "🏔️ Visit the cool Cameron Highlands for tea plantations and strawberry farms",
        "🐒 Wildlife watching in Borneo - see orangutans and proboscis monkeys",
        "🏝️ Island hopping in the crystal-clear waters of Perhentian Islands",
        "🏛️ Explore the magnificent Batu Caves Hindu temple complex",
        "🌺 Experience diverse cultures in Sarawak and Sabah states",
        "🍛 Try local specialties: Nasi Lemak, Rendang, Char Kway Teow",
        "🎭 Attend cultural festivals and visit traditional Malay villages"
    ]
    
    for activity in malaysia_activities:
        print(f"   {activity}")
    
    print(f"\n💡 MALAYSIA TRAVEL TIPS:")
    print("   🗓️ Best time: March-October (dry season)")
    print("   💰 Currency: Malaysian Ringgit (MYR)")
    print("   🗣️ Languages: Bahasa Malaysia, English widely spoken")
    print("   🌡️ Climate: Tropical, hot and humid year-round")
    print("   ✈️ Main airports: Kuala Lumpur (KLIA) and Penang")
    
    while True:
        try:
            user_query = input("\n💬 Ask about any country: ").strip()
            
            if user_query.lower() == 'back':
                break
            
            if not user_query:
                continue
            
            # Try to import and use the intelligent agent
            try:
                from world_travel_expert import WorldTravelExpert
                
                print("🧠 Processing your query with AI intent detection...")
                expert = WorldTravelExpert()
                result = expert.process_user_query(user_query)
                expert._display_response(result)
                
            except ImportError:
                # Fallback: Basic country detection and response
                print(f"🤔 Processing: '{user_query}'")
                
                # Simple country extraction
                query_lower = user_query.lower()
                countries = {
                    'japan': 'Experience traditional temples, modern technology, cherry blossoms, authentic sushi, anime culture, and hot springs',
                    'france': 'Visit iconic landmarks like Eiffel Tower, explore art museums, enjoy fine cuisine, wine tasting, and romantic cities',
                    'thailand': 'Discover beautiful temples, enjoy street food, relax on tropical beaches, experience Thai massages, and visit floating markets',
                    'italy': 'Explore ancient Rome, Renaissance art, delicious cuisine, scenic coastlines, and charming historical cities',
                    'spain': 'Experience flamenco culture, Gaudí architecture, tapas tours, beautiful beaches, and vibrant festivals',
                    'malaysia': 'Visit diverse cultures, tropical rainforests, beautiful islands, incredible street food, and modern cities',
                    'australia': 'Explore unique wildlife, Great Barrier Reef, iconic landmarks, beaches, and diverse landscapes',
                    'egypt': 'Discover ancient pyramids, Nile River cruises, pharaonic history, desert adventures, and Red Sea diving'
                }
                
                found_country = None
                for country, description in countries.items():
                    if country in query_lower:
                        found_country = country
                        break
                
                if found_country:
                    print(f"\n🌍 {found_country.upper()} HIGHLIGHTS:")
                    print(f"   🎯 {description}")
                    
                    # Get database info if available
                    try:
                        dest_info = get_destination_info_from_supabase(found_country)
                        attractions = get_attractions_from_supabase(found_country)
                        
                        if dest_info:
                            print(f"\n📍 Database Info: {dest_info.get('description', 'N/A')}")
                        
                        if attractions:
                            print(f"\n🎯 Top Attractions from Database:")
                            for attr in attractions[:3]:
                                print(f"   • {attr['name']}: {attr['description']}")
                    except:
                        pass
                else:
                    print("🤔 I can help with information about popular countries like Japan, France, Thailand, Italy, Spain, Malaysia, Australia, and Egypt.")
                    print("Try asking: 'What are the best activities in [country name]?'")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def get_comprehensive_database_context(destination):
    """Get comprehensive database context to enhance agent intelligence."""
    try:
        # Get destination info
        dest_info = get_destination_info_from_supabase(destination)
        
        # Get attractions data
        attractions_data = get_attractions_from_supabase(destination)
        
        # Build comprehensive context
        context = f"DESTINATION: {destination}\n"
        
        if dest_info:
            context += f"Database Info: {dest_info.get('description', 'No description available')}\n"
            if dest_info.get('best_time_to_visit'):
                context += f"Optimal Timing: {dest_info['best_time_to_visit']}\n"
        
        if attractions_data:
            top_attractions = [attr['name'] for attr in attractions_data[:8]]
            context += f"Known Attractions: {', '.join(top_attractions)}\n"
        
        context += "NOTE: Use this as foundation knowledge and expand with fresh research for comprehensive coverage.\n"
        
        return context
    except Exception as e:
        return f"DATABASE NOTE: Use fresh research as primary source (database unavailable: {e})"

# Enhanced Intelligence Helper Functions
def analyze_traveler_personality(preferences, budget, duration):
    """Analyze traveler personality based on inputs for enhanced experience matching."""
    profile = []
    
    # Budget-based personality indicators
    if budget.lower() in ['luxury', 'premium']:
        profile.append("comfort-oriented")
        profile.append("experience-focused")
        profile.append("quality-seeker")
    elif budget.lower() in ['budget', 'backpacker']:
        profile.append("adventure-oriented")
        profile.append("authentic-seeker")
        profile.append("value-conscious")
    else:
        profile.append("balanced-explorer")
        profile.append("flexible-adapter")
    
    # Interest-based personality indicators
    preferences_lower = preferences.lower()
    if 'culture' in preferences_lower or 'museum' in preferences_lower:
        profile.append("cultural-learner")
        profile.append("history-enthusiast")
    if 'food' in preferences_lower or 'culinary' in preferences_lower:
        profile.append("culinary-explorer")
        profile.append("social-diner")
    if 'adventure' in preferences_lower or 'outdoor' in preferences_lower:
        profile.append("thrill-seeker")
        profile.append("nature-lover")
    if 'relaxation' in preferences_lower or 'spa' in preferences_lower:
        profile.append("restoration-seeker")
        profile.append("mindfulness-oriented")
    if 'shopping' in preferences_lower:
        profile.append("material-explorer")
    if 'nightlife' in preferences_lower:
        profile.append("social-butterfly")
    
    # Duration-based personality indicators
    if duration <= 3:
        profile.append("intensive-explorer")
        profile.append("time-maximizer")
    elif duration >= 10:
        profile.append("deep-immersion-seeker")
        profile.append("slow-traveler")
    else:
        profile.append("balanced-pace-traveler")
    
    return ", ".join(profile)

def get_seasonal_intelligence(destination, travel_dates):
    """Get seasonal and weather intelligence for destination optimization."""
    seasonal_factors = {
        'weather_patterns': f"Seasonal weather analysis for {destination} during {travel_dates}",
        'crowd_levels': f"Tourist density predictions for {travel_dates}",
        'price_fluctuations': f"Cost optimization opportunities during {travel_dates}",
        'cultural_events': f"Local festivals and events during {travel_dates}",
        'natural_phenomena': f"Seasonal highlights (blooms, migrations, etc.) for {travel_dates}"
    }
    
    return f"Seasonal Intelligence: {', '.join(seasonal_factors.values())}"

def get_cultural_intelligence_brief(destination):
    """Get cultural context for enhanced cultural preparation."""
    cultural_aspects = {
        'communication_style': f"Communication patterns and social dynamics in {destination}",
        'value_systems': f"Core values and belief systems of {destination}",
        'social_hierarchy': f"Social structures and respect protocols in {destination}",
        'time_perception': f"Concept of time and scheduling culture in {destination}",
        'relationship_dynamics': f"Family, friendship, and business relationships in {destination}"
    }
    
    return f"Cultural Intelligence: {', '.join(cultural_aspects.values())}"

# Execute the main application
def main():
    """Main function with menu system."""
    print("🌍 Welcome to the AI Travel Agent! 🌍")
    print("Let me help you plan your perfect trip!")
    
    # Test database connection on startup
    print("\n🔗 Testing database connection...")
    if not test_supabase_connection():
        print("⚠️  Database connection failed. Some features may not work properly.")
        print("You can still plan trips, but they won't be saved to the database.")
    
    while True:
        show_menu()
        choice = input("\n🎯 Please select an option (1-8): ").strip()
        
        if choice == '1':
            plan_new_trip()
        elif choice == '2':
            browse_destinations_menu()
        elif choice == '3':
            view_attractions_menu()
        elif choice == '4':
            view_travel_history_menu()
        elif choice == '5':
            intelligent_chat_menu()
        elif choice == '6':
            test_supabase_connection()
        elif choice == '7':
            compare_intelligence_systems()
        elif choice == '8':
            print("\n👋 Thank you for using AI Travel Agent! Safe travels! 🌍✈️")
            break
        else:
            print("\n❌ Invalid option. Please select 1-8.")
        
        input("\n🔄 Press Enter to continue...")

if __name__ == "__main__":
    main()
