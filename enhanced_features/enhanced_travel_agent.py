#!/usr/bin/env python3
"""
🚀 Enhanced Travel Agent with Intelligent Itinerary System
Upgraded agent that generates dynamic, personalized, and truly intelligent itineraries
"""

import os
import sys
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from pathlib import Path

# Add the current directory to the Python path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew
from crewai.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

# Import our intelligent systems
try:
    from enhanced_features.intelligent_itinerary_engine import IntelligentItineraryEngine
    from enhanced_features.dynamic_activity_database import DynamicActivityDatabase
    ENHANCED_INTELLIGENCE_AVAILABLE = True
except ImportError:
    print("⚠️ Enhanced intelligence modules not found. Using fallback...")
    ENHANCED_INTELLIGENCE_AVAILABLE = False

# Load environment variables
load_dotenv()

# Initialize LLM
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key is missing. Please check your .env file.")

llm = ChatOpenAI(model="gpt-4", api_key=openai_api_key)

# Initialize intelligent systems
if ENHANCED_INTELLIGENCE_AVAILABLE:
    itinerary_engine = IntelligentItineraryEngine()
    activity_database = DynamicActivityDatabase()

@tool
def generate_intelligent_itinerary_tool(destination: str, duration: int, preferences: dict, budget: str) -> dict:
    """
    Generate truly intelligent, dynamic itinerary using advanced AI systems
    """
    if not ENHANCED_INTELLIGENCE_AVAILABLE:
        return {"error": "Enhanced intelligence system not available"}
    
    try:
        # Create traveler profile from preferences
        traveler_profile = {
            "travel_style": preferences.get("travel_style", "cultural"),
            "group_size": preferences.get("group_size", 1),
            "interests": preferences.get("interests", []),
            "pace": preferences.get("pace", "moderate"),
            "budget_priority": budget
        }
        
        # Generate intelligent itinerary
        intelligent_itinerary = itinerary_engine.generate_intelligent_itinerary(
            destination=destination,
            duration_days=duration,
            preferences=preferences,
            budget=budget,
            travel_dates=datetime.now().strftime("%Y-%m-%d"),
            traveler_profile=traveler_profile
        )
        
        return intelligent_itinerary
        
    except Exception as e:
        return {"error": f"Failed to generate intelligent itinerary: {str(e)}"}

@tool
def get_contextual_activities_tool(destination: str, criteria: dict) -> list:
    """
    Get contextually relevant activities based on intelligent criteria
    """
    if not ENHANCED_INTELLIGENCE_AVAILABLE:
        return []
    
    try:
        activities = activity_database.get_activities_by_criteria(destination, criteria)
        return [
            {
                "name": activity.name,
                "category": activity.category,
                "duration": f"{activity.duration_min}-{activity.duration_max} minutes",
                "cost_range": activity.cost_range,
                "authenticity": activity.authenticity_level,
                "cultural_significance": activity.cultural_significance,
                "insider_tips": activity.insider_tips[:3],  # Top 3 tips
                "best_time": activity.crowd_patterns.get("low", "flexible"),
                "weather_notes": "Indoor" if not activity.weather_dependent else "Weather dependent"
            }
            for activity in activities[:5]  # Top 5 activities
        ]
    except Exception as e:
        return [{"error": f"Failed to get activities: {str(e)}"}]

@tool
def get_weather_alternatives_tool(destination: str, original_activities: list, weather: str) -> list:
    """
    Get weather-appropriate alternative activities
    """
    if not ENHANCED_INTELLIGENCE_AVAILABLE:
        return []
    
    try:
        # This would integrate with the dynamic database
        alternatives = activity_database.get_weather_alternatives(
            original_activities=[], 
            destination=destination, 
            weather_condition=weather
        )
        
        return [
            {
                "name": alt.name,
                "why_better": f"Perfect for {weather} weather",
                "category": alt.category,
                "insider_tip": alt.insider_tips[0] if alt.insider_tips else "No special tips"
            }
            for alt in alternatives[:3]
        ]
    except Exception as e:
        return [{"error": f"Failed to get alternatives: {str(e)}"}]

# Enhanced Agents with Intelligence Integration
enhanced_itinerary_architect = Agent(
    role="Enhanced Strategic Itinerary Architect & Intelligence Coordinator",
    goal="Create revolutionary intelligent itineraries that adapt dynamically to traveler preferences, local conditions, and real-time intelligence.",
    backstory="""You are an advanced AI travel architect with access to cutting-edge intelligence systems. Your expertise includes:
    
    🧠 ADVANCED INTELLIGENCE CAPABILITIES:
    - Real-time integration with intelligent activity databases
    - Dynamic adaptation based on traveler behavioral analysis
    - Contextual awareness of local conditions, weather, and crowds
    - Progressive experience design that builds cultural understanding
    - Energy management and sustainable travel pacing
    
    🎯 INTELLIGENT DESIGN PRINCIPLES:
    - No two days should feel repetitive or generic
    - Each activity should build upon previous experiences
    - Timing optimized for crowds, weather, and local rhythms
    - Budget allocation intelligent across experiences
    - Authentic progression from tourist to cultural participant
    
    🔄 ADAPTIVE INTELLIGENCE:
    - Real-time alternatives for weather or preference changes
    - Smart contingency planning for every scenario
    - Cultural immersion that deepens day by day
    - Energy pattern optimization for sustainable enjoyment
    
    You don't just create schedules - you architect transformative journeys that feel effortlessly intelligent.""",
    verbose=True,
    llm=llm,
    tools=[generate_intelligent_itinerary_tool, get_contextual_activities_tool, get_weather_alternatives_tool]
)

enhanced_experience_curator = Agent(
    role="Enhanced Experience Curator & Cultural Intelligence Specialist",
    goal="Curate deeply intelligent, contextually aware experiences that create meaningful cultural connections and avoid tourist-trap repetition.",
    backstory="""You are an enhanced experience curator with access to advanced cultural intelligence systems. Your capabilities include:
    
    🎨 INTELLIGENT CURATION:
    - Access to dynamic databases of authentic local experiences
    - Real-time analysis of cultural significance and authenticity levels
    - Smart categorization by energy, cost, time, and cultural value
    - Contextual pairing of complementary experiences
    
    🌍 CULTURAL INTELLIGENCE:
    - Deep understanding of local rhythms and social patterns
    - Insider knowledge of timing, etiquette, and cultural nuances
    - Anti-tourist-trap intelligence with authentic alternative detection
    - Progressive cultural immersion design
    
    🔄 ADAPTIVE PERSONALIZATION:
    - Dynamic adjustment based on traveler energy and interests
    - Smart progression from comfort zone to authentic exploration
    - Context-aware recommendations that build upon daily discoveries
    
    You create experiences that locals would appreciate and that transform travelers into temporary cultural participants.""",
    verbose=True,
    llm=llm,
    tools=[get_contextual_activities_tool, get_weather_alternatives_tool]
)

def create_enhanced_travel_tasks(destination: str, 
                               travel_dates: str, 
                               duration_days: int, 
                               preferences: Dict, 
                               budget: str) -> List[Task]:
    """Create enhanced tasks with intelligent systems integration"""
    
    enhanced_itinerary_task = Task(
        description=f"""Create a revolutionary intelligent itinerary for {duration_days} days in {destination} using advanced AI systems.
        
        🧠 INTELLIGENT ITINERARY REQUIREMENTS:
        
        **Traveler Profile Analysis:**
        - Preferences: {preferences}
        - Budget: {budget}
        - Duration: {duration_days} days
        - Travel Dates: {travel_dates}
        
        **Advanced Intelligence Integration:**
        1. Use generate_intelligent_itinerary_tool to create the base intelligent structure
        2. Use get_contextual_activities_tool to enhance with real activity intelligence
        3. Use get_weather_alternatives_tool to add adaptive weather planning
        
        **Dynamic Intelligence Features Required:**
        
        📅 **Daily Progression Intelligence:**
        - Day 1: Cultural foundation with gentle immersion
        - Day 2+: Progressive deepening based on Day 1 discoveries
        - Each day builds cultural understanding from previous days
        - NO REPETITIVE ACTIVITIES - each experience must be unique
        
        ⏰ **Temporal Intelligence:**
        - Morning activities optimized for energy and crowds
        - Afternoon experiences building on morning discoveries
        - Evening activities synthesizing the day's cultural learning
        - Smart timing avoiding tourist crowds and embracing local rhythms
        
        🌟 **Experience Differentiation:**
        - Zero generic "visit monument, take photo, leave" activities
        - Every activity includes cultural context and learning outcomes
        - Authentic local interactions woven throughout
        - Progressive skill building (language, cultural understanding, local navigation)
        
        🎯 **Intelligent Adaptation Features:**
        - Weather contingencies for every outdoor activity
        - Energy management with rest and stimulation balance
        - Budget optimization with free and paid experience mixing
        - Flexibility zones for spontaneous discovery
        
        **Output Format - Revolutionary Intelligent Itinerary:**
        For each day provide:
        
        📋 **Day X Theme & Intelligence:**
        - **Cultural Focus:** Specific cultural aspect being explored
        - **Learning Progression:** How this builds on previous days
        - **Energy Pattern:** Designed energy flow for sustainable enjoyment
        
        ⏰ **Intelligent Time Blocks:**
        
        **Morning Intelligence (07:00-12:00):**
        - **Primary Activity:** [Unique, specific experience]
        - **Cultural Context:** Why this matters and what you'll learn
        - **Timing Rationale:** Why this time is optimal
        - **Local Intelligence:** Insider tips for authentic experience
        - **Photo Opportunities:** Beyond typical tourist shots
        - **Progression Logic:** How this builds toward afternoon
        
        **Afternoon Intelligence (12:00-17:00):**
        - **Primary Activity:** [Building on morning's cultural foundation]
        - **Connection Logic:** How this relates to morning experience
        - **Cultural Deepening:** Advancing understanding from morning
        - **Local Interaction Opportunities:** Authentic engagement points
        - **Alternative Plans:** Weather/energy adaptations
        
        **Evening Intelligence (17:00-21:00):**
        - **Synthesis Activity:** [Integrating day's cultural discoveries]
        - **Reflection Opportunity:** Processing and deepening understanding
        - **Local Social Integration:** Authentic evening cultural participation
        - **Day's Culmination:** How evening completes the day's story
        
        🔄 **Adaptive Intelligence Per Day:**
        - **If Ahead of Schedule:** Spontaneous deepening opportunities
        - **If Behind Schedule:** Essential experience preservation
        - **Weather Alternatives:** Complete indoor/outdoor alternatives
        - **Energy Adjustments:** High/low energy modifications
        
        💡 **Daily Intelligence Summary:**
        - **Cultural Skills Gained:** Specific learning outcomes
        - **Local Connections Made:** Social interaction opportunities
        - **Authentic Moments:** Non-tourist experiences achieved
        - **Tomorrow's Foundation:** How today prepares for tomorrow
        
        **CRITICAL SUCCESS CRITERIA:**
        ✅ No two activities should feel similar or repetitive
        ✅ Each day must have clear cultural progression and learning
        ✅ Every timing decision must have intelligent rationale
        ✅ Local rhythm integration is mandatory, not optional
        ✅ Authentic experiences must outnumber tourist activities 2:1
        ✅ Every activity includes specific cultural context and learning
        ✅ Weather and energy adaptations must be comprehensive
        ✅ Budget distribution must be intelligent across experience types""",
        
        agent=enhanced_itinerary_architect,
        expected_output=f"Revolutionary intelligent {duration_days}-day itinerary for {destination} with dynamic adaptation, cultural progression, and zero repetition"
    )
    
    enhanced_experience_task = Task(
        description=f"""Enhance the itinerary with deeply intelligent, culturally authentic experiences that avoid all tourist-trap repetition.
        
        🎯 ENHANCED EXPERIENCE CURATION:
        
        **Cultural Intelligence Integration:**
        - Use get_contextual_activities_tool with criteria:
          - authenticity_min: 2 (mixed to local experiences preferred)
          - categories: based on traveler preferences {preferences}
          - budget_max: appropriate for {budget} budget
        
        **Experience Intelligence Requirements:**
        
        🌟 **Authenticity Over Tourism:**
        - Replace any generic tourist activities with authentic alternatives
        - Prioritize experiences locals would actually enjoy
        - Include cultural learning opportunities in every activity
        - Avoid anything that feels like a "tourist assembly line"
        
        🧠 **Intelligence-Enhanced Experiences:**
        For each activity, provide:
        
        **Cultural Intelligence:**
        - **Why Locals Love This:** Authentic cultural significance
        - **Insider Approach:** How to experience this like a local
        - **Cultural Etiquette:** Respectful participation guidelines
        - **Learning Opportunity:** Specific cultural knowledge gained
        
        **Practical Intelligence:**
        - **Optimal Timing:** Crowd avoidance and best experience windows
        - **Cost Intelligence:** Value assessment and money-saving tips
        - **Energy Management:** How this fits into daily energy flow
        - **Preparation Needed:** What to know, bring, or learn beforehand
        
        **Contextual Intelligence:**
        - **Before This Activity:** How to prepare mentally and practically
        - **During This Activity:** How to maximize cultural engagement
        - **After This Activity:** How to process and build upon the experience
        - **Connection Points:** How this relates to other day's activities
        
        🔄 **Adaptive Experience Design:**
        - Multiple authentic alternatives for different weather conditions
        - Scalable experiences (can be extended or shortened)
        - Social interaction opportunities embedded naturally
        - Photo opportunities that tell cultural stories, not just tourist selfies
        
        **Experience Categories - Intelligence Requirements:**
        
        🍽️ **Culinary Intelligence:**
        - Local food experiences with cultural context
        - Cooking classes or market tours with learning outcomes
        - Restaurant recommendations with cultural significance
        - Street food experiences with safety and etiquette guidance
        
        🏛️ **Cultural Intelligence:**
        - Museums/sites with specific learning objectives
        - Cultural performances with background context
        - Religious/spiritual sites with respectful participation guidance
        - Neighborhood explorations with social interaction opportunities
        
        🎨 **Creative Intelligence:**
        - Art experiences with local artist interactions
        - Craft workshops with cultural significance
        - Performance attendance with cultural context
        - Creative expression opportunities that connect with local culture
        
        🌿 **Nature Intelligence:**
        - Natural experiences unique to the destination
        - Outdoor activities with cultural or historical context
        - Seasonal opportunities specific to travel dates
        - Sustainable tourism practices embedded
        
        **ANTI-REPETITION PROTOCOL:**
        ❌ **Forbidden Repetitions:**
        - Multiple "visit and photo" museum experiences
        - Repetitive shopping mall or tourist shopping experiences
        - Similar restaurant types without cultural variety
        - Multiple observation decks or similar viewpoints
        - Generic walking tours without specific cultural focus
        
        ✅ **Variety Requirements:**
        - Each day must have different primary activity types
        - Cultural learning must vary in style and subject matter
        - Social interaction opportunities must be diverse
        - Budget allocation must vary between free, moderate, and premium experiences
        
        **CULTURAL PROGRESSION REQUIREMENTS:**
        - Day 1: Gentle cultural introduction with support systems
        - Day 2+: Progressive independence and deeper cultural engagement
        - Each day's experiences must build cultural confidence for next day
        - Learning from previous days must inform subsequent experiences""",
        
        agent=enhanced_experience_curator,
        expected_output=f"Culturally intelligent experience enhancements for {destination} itinerary with authentic local connections and zero tourist-trap repetition"
    )
    
    return [enhanced_itinerary_task, enhanced_experience_task]

def run_enhanced_travel_planning(destination: str, 
                               travel_dates: str, 
                               duration_days: int, 
                               preferences: Dict, 
                               budget: str) -> str:
    """Run enhanced travel planning with intelligent systems"""
    
    print(f"🧠 Starting Enhanced Intelligent Travel Planning for {destination}")
    print(f"🔄 Integrating advanced AI systems...")
    
    # Create enhanced tasks
    tasks = create_enhanced_travel_tasks(
        destination=destination,
        travel_dates=travel_dates,
        duration_days=duration_days,
        preferences=preferences,
        budget=budget
    )
    
    # Create enhanced crew
    enhanced_crew = Crew(
        agents=[enhanced_itinerary_architect, enhanced_experience_curator],
        tasks=tasks,
        verbose=True
    )
    
    # Execute enhanced planning
    try:
        print("🚀 Executing Enhanced AI Travel Planning...")
        result = enhanced_crew.kickoff()
        
        print("✅ Enhanced Intelligent Itinerary Generated!")
        return str(result)
        
    except Exception as e:
        print(f"❌ Enhanced planning error: {e}")
        return f"Error in enhanced planning: {str(e)}"

if __name__ == "__main__":
    # Test the enhanced system
    test_preferences = {
        "travel_style": "cultural",
        "interests": ["food", "history", "local_culture"],
        "pace": "relaxed",
        "group_size": 2
    }
    
    result = run_enhanced_travel_planning(
        destination="Tokyo",
        travel_dates="2024-03-15",
        duration_days=4,
        preferences=test_preferences,
        budget="moderate"
    )
    
    print("\n" + "="*80)
    print("🌟 ENHANCED INTELLIGENT ITINERARY RESULT")
    print("="*80)
    print(result)
