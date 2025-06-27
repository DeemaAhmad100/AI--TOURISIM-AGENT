import os
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

# Define the intelligent, context-aware agents
destination_researcher = Agent(
    role="Intelligent Destination Researcher & Cultural Analyst",
    goal="Provide comprehensive, context-aware destination intelligence that combines real-time research with deep cultural insights and traveler-specific recommendations.",
    backstory="""You are an elite travel intelligence analyst with extensive global experience. You specialize in:
    - Synthesizing information from multiple authoritative sources
    - Analyzing cultural patterns and local customs with nuance
    - Providing context-aware recommendations based on traveler profiles
    - Identifying current trends, seasonal factors, and real-time conditions
    - Cross-referencing database knowledge with fresh research for complete accuracy
    
    Your approach is methodical yet insightful, always considering the human element of travel and what makes each destination unique for different types of travelers.""",
    verbose=True,
    llm=llm,
    tools=[search_internet]
)

attractions_specialist = Agent(
    role="Intelligent Experience Curator & Activity Specialist",
    goal="Curate personalized attraction recommendations using intelligent analysis of traveler preferences, budget constraints, and authentic local experiences.",
    backstory="""You are a master experience curator who understands that great travel is about meaningful connections, not just checking boxes. Your expertise includes:
    - Analyzing traveler psychology to match experiences with deep interests
    - Identifying hidden gems and authentic local experiences beyond tourist traps
    - Understanding the economics of travel to optimize value for any budget
    - Recognizing seasonal opportunities and time-sensitive experiences
    - Balancing must-see landmarks with unique, personal discoveries
    
    You think like both a local insider and a seasoned traveler, always asking: 'What will make this trip truly memorable and authentic?'""",
    verbose=True,
    llm=llm,
    tools=[search_internet]
)

itinerary_planner = Agent(
    role="Strategic Itinerary Architect & Logistics Optimizer",
    goal="Design intelligently optimized travel itineraries that maximize experience quality while minimizing stress and inefficiency.",
    backstory="""You are a strategic travel architect who understands that perfect itineraries are both art and science. Your expertise encompasses:
    - Advanced logistics optimization to maximize time and minimize travel stress
    - Understanding energy flows and experience pacing for sustainable travel
    - Integrating local rhythms and cultural timing into daily schedules
    - Building adaptive flexibility into structured plans
    - Balancing efficiency with spontaneity and authentic discovery
    - Considering weather patterns, crowd dynamics, and seasonal factors
    
    You create itineraries that feel effortless to follow while delivering extraordinary experiences at every turn.""",
    verbose=True,
    llm=llm
)

local_guide = Agent(
    role="Cultural Intelligence Expert & Insider Guide",
    goal="Provide deep cultural intelligence and insider knowledge that transforms tourists into informed, respectful, and connected travelers.",
    backstory="""You are a cultural intelligence expert and master insider guide with deep connections to local communities worldwide. Your knowledge includes:
    - Profound understanding of cultural nuances, etiquette, and social dynamics
    - Insider access to authentic experiences and local secrets
    - Expertise in cross-cultural communication and respectful travel practices
    - Advanced knowledge of local economics, safety, and practical considerations
    - Understanding of how to help travelers connect meaningfully with local culture
    - Ability to bridge cultural gaps and prevent common misunderstandings
    
    You don't just share information – you provide the cultural keys that unlock authentic, respectful, and transformative travel experiences.""",
    verbose=True,
    llm=llm,
    tools=[search_internet]
)

def create_destination_tasks(destination, travel_dates, duration_days, preferences, budget):
    """Create tasks customized for a specific travel destination with intelligent, comprehensive responses."""
    
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
    
    destination_research_task = Task(
        description=f"""As an expert destination researcher, provide comprehensive, intelligent analysis of {destination} as a travel destination.
        
        INTELLIGENCE FRAMEWORK:
        - Analyze current trends, seasonal patterns, and real-time conditions
        - Cross-reference multiple reliable sources for accuracy
        - Provide context-aware recommendations based on traveler preferences: {preferences}
        - Consider budget implications for {budget} travelers
        
        {destination_context}
        
        COMPREHENSIVE RESEARCH AREAS:
        1. CLIMATE & TIMING: Detailed weather patterns, best seasons, what to expect during {travel_dates}
        2. CULTURAL INTELLIGENCE: Local customs, etiquette, cultural nuances, dos and don'ts
        3. SAFETY & SECURITY: Current safety situation, travel advisories, health considerations
        4. TRANSPORTATION HUB: Getting there, local transport options, costs for {budget} budget
        5. LANGUAGE & COMMUNICATION: Language basics, useful phrases, communication tips
        6. FINANCIAL PLANNING: Currency, payment methods, tipping culture, cost expectations
        7. REAL-TIME INSIGHTS: Current events, festivals, seasonal highlights during {travel_dates}
        8. TRAVELER-SPECIFIC ADVICE: Tailored recommendations for someone interested in {preferences}
        
        INTELLIGENT OUTPUT REQUIREMENTS:
        - Synthesize information from multiple sources
        - Provide actionable, specific advice
        - Include insider tips and lesser-known insights
        - Address potential challenges and solutions
        - Format with clear headings and bullet points for easy reading
        
        Be thorough, intelligent, and provide value beyond basic tourist information.""",
        agent=destination_researcher,
        expected_output=f"An intelligent, comprehensive destination analysis for {destination} with expert insights and actionable advice organized in clear sections"
    )

    attractions_task = Task(
        description=f"""Using intelligent analysis and comprehensive research, curate the best attractions and activities in {destination} perfectly matched to these preferences: {preferences}.
        
        🧠 INTELLIGENT CURATION FRAMEWORK:
        - Analyze traveler preferences to understand motivation and interests
        - Cross-reference database knowledge with current information
        - Consider {budget} budget constraints and {duration_days}-day timeframe
        - Identify must-see vs. optional experiences based on traveler profile
        
        {attractions_context}
        
        📍 COMPREHENSIVE ATTRACTION ANALYSIS:
        For each recommended attraction, provide:
        1. NAME & SMART DESCRIPTION: What makes it special and why it fits {preferences}
        2. INTELLIGENT REASONING: Why this specific traveler should prioritize this experience
        3. TIME OPTIMIZATION: Recommended duration and best visiting strategy
        4. BUDGET BREAKDOWN: Costs, value assessment for {budget} travelers
        5. TIMING INTELLIGENCE: Optimal times to visit (seasons, days, hours)
        6. INSIDER INTELLIGENCE: Local secrets, hidden features, pro tips
        7. EXPERIENCE ENHANCEMENT: How to maximize enjoyment and avoid pitfalls
        
        🎯 SMART CATEGORIZATION:
        - Priority Level: Must-see vs. Nice-to-have based on preferences
        - Experience Type: Cultural, adventure, culinary, relaxation, etc.
        - Budget Impact: Free, low-cost, moderate, premium experiences
        - Time Investment: Quick stops, half-day, full-day experiences
        
        🔍 BEYOND THE OBVIOUS:
        - Include authentic local experiences not in typical guidebooks
        - Suggest seasonal or time-sensitive opportunities during {travel_dates}
        - Recommend connected experiences that create meaningful journeys
        
        Format with intelligent prioritization and clear categorization.""",
        agent=attractions_specialist,
        expected_output=f"An intelligently curated list of attractions and activities in {destination} with smart prioritization and detailed analysis"
    )

    itinerary_task = Task(
        description=f"""Create an intelligently optimized, context-aware day-by-day itinerary for a {duration_days}-day trip to {destination} starting on {travel_dates}.
        
        🧠 INTELLIGENT ITINERARY DESIGN:
        - Analyze traveler profile: {preferences} interests with {budget} budget
        - Optimize for efficiency, experience quality, and personal satisfaction
        - Consider real-time factors: weather, crowds, seasonal events, local patterns
        - Balance structured activities with spontaneous discovery opportunities
        
        📅 SMART DAILY STRUCTURE:
        For each day, provide intelligent scheduling:
        
        1. ⏰ TIMING INTELLIGENCE:
           - Morning (with specific times): Optimal activities for fresh energy
           - Afternoon (with transitions): Peak experience times and crowd management
           - Evening (with wind-down): Perfect sunset/dinner/cultural experiences
        
        2. 🍽️ CULINARY INTEGRATION:
           - Breakfast suggestions aligned with day's activities
           - Lunch spots strategically located near attractions
           - Dinner experiences that enhance cultural immersion
           - Include cuisine types, ambiance, and {budget}-appropriate pricing
        
        3. 🚌 INTELLIGENT LOGISTICS:
           - Optimized routing to minimize travel time and maximize experience
           - Transportation methods with time estimates and costs
           - Contingency options for weather or unexpected closures
        
        4. 🎯 EXPERIENCE OPTIMIZATION:
           - Group complementary attractions and experiences
           - Account for realistic timing and energy levels
           - Include buffer time for authentic interactions
           - Balance must-see items with personal discovery time
        
        📊 SMART ITINERARY FEATURES:
        - Energy Management: Alternate high-intensity and relaxation periods
        - Weather Contingencies: Indoor/outdoor alternatives for each day
        - Budget Monitoring: Daily spending estimates with cost-saving opportunities
        - Flexibility Zones: Built-in time for spontaneous exploration
        - Local Intelligence: Incorporate local rhythms and cultural timing
        
        🔄 ADAPTIVE DESIGN:
        - Day-by-day progression that builds cultural understanding
        - Opportunities to dive deeper into discovered interests
        - Easy modifications for energy levels or weather changes
        
        Format as a detailed daily schedule with smart alternatives and practical guidance.""",
        agent=itinerary_planner,
        expected_output=f"An intelligently optimized day-by-day itinerary for {duration_days} days in {destination} with smart logistics and adaptive features"
    )

    guide_task = Task(
        description=f"""Create an intelligent, comprehensive travel guide for {destination} that serves as the ultimate insider companion.
        
        🧠 INTELLIGENT GUIDE FRAMEWORK:
        - Synthesize local knowledge with traveler-specific needs
        - Provide context-aware advice for {preferences} enthusiasts
        - Optimize recommendations for {budget} budget travelers
        - Include cultural intelligence that enhances authentic experiences
        
        📚 COMPREHENSIVE GUIDE SECTIONS:
        
        1. 💡 CULTURAL INTELLIGENCE BRIEFING:
           - Essential etiquette that locals appreciate
           - Cultural nuances that enhance interactions
           - Dress codes and behavioral expectations
           - Sacred/sensitive areas and respectful approaches
        
        2. 🛡️ SMART SAFETY & HEALTH GUIDE:
           - Destination-specific safety protocols
           - Health considerations and local medical resources
           - Emergency contacts and procedures
           - Scam awareness and prevention strategies
        
        3. 💰 INTELLIGENT BUDGET OPTIMIZATION:
           - Money-saving strategies specific to {destination}
           - Local pricing knowledge and negotiation tips
           - Free and low-cost authentic experiences
           - Budget allocation recommendations for {budget} travelers
        
        4. 📱 DIGITAL TRAVEL TOOLKIT:
           - Essential apps for navigation, translation, payments
           - Offline resources and backup strategies
           - Local WiFi and connectivity solutions
           - Digital etiquette and local tech customs
        
        5. 🗣️ COMMUNICATION MASTERY:
           - Essential phrases with pronunciation guides
           - Non-verbal communication insights
           - Situations where English works vs. local language needed
           - Cultural conversation topics and taboos
        
        6. 🍜 CULINARY ADVENTURE GUIDE:
           - Must-try local specialties aligned with {preferences}
           - Food safety and dietary accommodation strategies
           - Local dining customs and tipping culture
           - Market visits and cooking experience opportunities
        
        7. 🛍️ AUTHENTIC SHOPPING INTELLIGENCE:
           - Genuine local products vs. tourist traps
           - Best markets and shopping areas for authentic items
           - Quality indicators and fair pricing knowledge
           - Shipping and customs considerations for purchases
        
        8. 🎭 CULTURAL IMMERSION ACCELERATOR:
           - Local festivals, events, and seasonal celebrations
           - Community experiences and volunteer opportunities
           - Authentic cultural exchanges and learning experiences
           - Respectful photography and interaction guidelines
        
        9. ⚡ PRO TRAVEL HACKS:
           - Local transportation secrets and shortcuts
           - Timing strategies to avoid crowds and maximize experiences
           - Weather adaptation strategies
           - Equipment and packing recommendations specific to {destination}
        
        Format with clear sections, practical checklists, and actionable insider tips.""",
        agent=local_guide,
        expected_output=f"An intelligent, comprehensive insider's travel guide for {destination} with cultural intelligence and practical optimization strategies"
    )

    return [destination_research_task, attractions_task, itinerary_task, guide_task]



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
    print("1. 🗺️  Plan a New Trip")
    print("2. 📍 Browse Destinations in Database")
    print("3. 🎯 View Attractions for a Destination")
    print("4. 📚 View Your Travel History")
    print("5. 🧠 Ask About Any Country (Intelligent Chat)")
    print("6. 🔧 Test Database Connection")
    print("7. 🚪 Exit")
    print("="*60)

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
        print(f"❌ Error retrieving destinations: {str(e)}")

def view_attractions_menu():
    """View attractions for a specific destination."""
    destination = input("\n🎯 Enter destination name to view attractions: ")
    attractions = get_attractions_from_supabase(destination)
    
    if attractions:
        print(f"\n🎯 ATTRACTIONS IN {destination.upper()}:")
        print("-" * 50)
        for i, attr in enumerate(attractions, 1):
            print(f"{i}. {attr['name']}")
            print(f"   📝 {attr['description']}")
            print(f"   📍 Type: {attr['type']}")
            if attr.get('rating'):
                print(f"   ⭐ Rating: {attr['rating']}/5")
            print()
    else:
        print(f"No attractions found for {destination}")

def view_travel_history_menu():
    """View travel history from the database."""
    history = get_travel_history_from_supabase()
    
    if history:
        print("\n📚 YOUR TRAVEL HISTORY:")
        print("-" * 50)
        for i, trip in enumerate(history, 1):
            print(f"{i}. {trip['destination']} - {trip['travel_dates']}")
            print(f"   ⏰ Duration: {trip['duration_days']} days")
            print(f"   💰 Budget: {trip['budget']}")
            print(f"   🎨 Preferences: {trip['preferences']}")
            created_at = trip['created_at'][:10] if trip.get('created_at') else 'Unknown'
            print(f"   📅 Planned on: {created_at}")
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

def plan_new_trip():
    """Plan a new trip with enhanced features."""
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
    print("\n⏳ Our AI agents are working on your personalized travel plan...")
    
    # Create tasks
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

    print("\n" + "="*80)
    print("🎉 YOUR PERSONALIZED TRAVEL PLAN IS READY! 🎉")
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
        choice = input("\n🎯 Please select an option (1-6): ").strip()
        
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
            print("\n👋 Thank you for using AI Travel Agent! Safe travels! 🌍✈️")
            break
        else:
            print("\n❌ Invalid option. Please select 1-7.")
        
        input("\n🔄 Press Enter to continue...")

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

# Execute the main application
if __name__ == "__main__":
    main()
