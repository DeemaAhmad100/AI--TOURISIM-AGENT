"""
🛠️ Travel Planning Tools
All CrewAI tools for travel research, booking, and recommendations
"""

from crewai.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv

load_dotenv()

# Initialize search tool
try:
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if tavily_api_key:
        search_tool = TavilySearchResults(api_key=tavily_api_key, max_results=5)
    else:
        search_tool = None
        print("⚠️ Tavily API key not found. Search functionality limited.")
except Exception as e:
    search_tool = None
    print(f"⚠️ Search tool initialization failed: {e}")

@tool
def search_travel_information(query: str) -> str:
    """
    Search for comprehensive travel information including flights, hotels, restaurants, and activities.
    
    Args:
        query (str): Search query for travel information
        
    Returns:
        str: Detailed travel information and recommendations
    """
    if not search_tool:
        return f"Search unavailable. Please manually research: {query}"
    
    try:
        results = search_tool.run(query)
        return f"Travel Information for '{query}':\\n{results}"
    except Exception as e:
        return f"Search error for '{query}': {str(e)}"

@tool
def search_flights(departure: str, destination: str, date: str, budget: str = "moderate") -> str:
    """
    Search for flight options between destinations.
    
    Args:
        departure (str): Departure city/airport
        destination (str): Destination city/airport  
        date (str): Travel date (YYYY-MM-DD format)
        budget (str): Budget level (budget/moderate/luxury)
        
    Returns:
        str: Flight options and recommendations
    """
    query = f"flights from {departure} to {destination} on {date} {budget} budget airline options"
    return search_travel_information(query)

@tool
def search_hotels(destination: str, checkin: str, checkout: str, budget: str = "moderate") -> str:
    """
    Search for hotel accommodations in destination.
    
    Args:
        destination (str): Destination city
        checkin (str): Check-in date (YYYY-MM-DD)
        checkout (str): Check-out date (YYYY-MM-DD)
        budget (str): Budget level (budget/moderate/luxury)
        
    Returns:
        str: Hotel options and recommendations
    """
    query = f"hotels in {destination} {checkin} to {checkout} {budget} budget accommodation"
    return search_travel_information(query)

@tool
def search_restaurants(destination: str, cuisine_type: str = "local", budget: str = "moderate") -> str:
    """
    Search for restaurant recommendations in destination.
    
    Args:
        destination (str): Destination city
        cuisine_type (str): Type of cuisine (local/international/specific cuisine)
        budget (str): Budget level (budget/moderate/luxury)
        
    Returns:
        str: Restaurant recommendations
    """
    query = f"best {cuisine_type} restaurants in {destination} {budget} budget dining recommendations"
    return search_travel_information(query)

@tool
def search_activities(destination: str, interests: List[str], duration: str = "half-day") -> str:
    """
    Search for activities and attractions based on interests.
    
    Args:
        destination (str): Destination city
        interests (List[str]): List of interests (culture, adventure, food, etc.)
        duration (str): Activity duration preference
        
    Returns:
        str: Activity recommendations
    """
    interests_str = ", ".join(interests) if isinstance(interests, list) else str(interests)
    query = f"best {interests_str} activities and attractions in {destination} {duration} experiences"
    return search_travel_information(query)

@tool
def search_local_culture(destination: str, aspect: str = "general") -> str:
    """
    Search for local culture, customs, and etiquette information.
    
    Args:
        destination (str): Destination city/country
        aspect (str): Specific cultural aspect (customs/etiquette/traditions/general)
        
    Returns:
        str: Cultural information and guidelines
    """
    query = f"{destination} local culture {aspect} customs etiquette travel tips"
    return search_travel_information(query)

@tool
def search_weather_info(destination: str, travel_date: str) -> str:
    """
    Search for weather information and seasonal considerations.
    
    Args:
        destination (str): Destination city
        travel_date (str): Travel date (YYYY-MM-DD)
        
    Returns:
        str: Weather forecast and seasonal travel advice
    """
    query = f"weather forecast {destination} {travel_date} seasonal travel advice what to pack"
    return search_travel_information(query)

@tool
def search_budget_tips(destination: str, duration_days: int, budget_level: str) -> str:
    """
    Search for budget-specific travel tips and money-saving advice.
    
    Args:
        destination (str): Destination city
        duration_days (int): Length of stay
        budget_level (str): Budget level (budget/moderate/luxury)
        
    Returns:
        str: Budget tips and cost-saving recommendations
    """
    query = f"{destination} {duration_days} days {budget_level} budget travel tips money saving advice costs"
    return search_travel_information(query)

@tool
def search_transportation(destination: str, transport_type: str = "public") -> str:
    """
    Search for transportation options in destination.
    
    Args:
        destination (str): Destination city
        transport_type (str): Type of transport (public/taxi/rental/all)
        
    Returns:
        str: Transportation options and recommendations
    """
    query = f"{destination} {transport_type} transportation options getting around travel tips"
    return search_travel_information(query)

@tool
def search_safety_info(destination: str) -> str:
    """
    Search for safety information and travel advisories.
    
    Args:
        destination (str): Destination city/country
        
    Returns:
        str: Safety information and travel advisories
    """
    query = f"{destination} travel safety information advisories security tips safe areas"
    return search_travel_information(query)

@tool
def generate_intelligent_itinerary(destination: str, duration: int, preferences: dict, budget: str) -> dict:
    """
    Generate intelligent itinerary using advanced AI systems.
    
    Args:
        destination (str): Travel destination
        duration (int): Trip duration in days
        preferences (dict): Traveler preferences and interests
        budget (str): Budget level
        
    Returns:
        dict: Intelligent itinerary structure
    """
    try:
        # This would integrate with the intelligent itinerary engine
        base_structure = {
            "destination": destination,
            "duration_days": duration,
            "budget_level": budget,
            "traveler_profile": preferences,
            "daily_plans": [],
            "contingency_plans": [],
            "cultural_progression": {
                "day_1": "Cultural foundation and orientation",
                "progression": "Daily deepening of cultural understanding",
                "outcome": "Transformation from tourist to cultural participant"
            }
        }
        
        # Generate daily structure
        for day in range(1, duration + 1):
            daily_plan = {
                "day": day,
                "theme": f"Day {day} Cultural Focus",
                "morning": {"time": "07:00-12:00", "activities": []},
                "afternoon": {"time": "12:00-17:00", "activities": []},
                "evening": {"time": "17:00-21:00", "activities": []},
                "alternatives": [],
                "learning_objectives": [],
                "cultural_progression": ""
            }
            base_structure["daily_plans"].append(daily_plan)
        
        return base_structure
        
    except Exception as e:
        return {"error": f"Failed to generate intelligent itinerary: {str(e)}"}

@tool
def get_contextual_activities(destination: str, criteria: dict) -> list:
    """
    Get contextually relevant activities based on intelligent criteria.
    
    Args:
        destination (str): Travel destination
        criteria (dict): Activity selection criteria
        
    Returns:
        list: Contextually relevant activities
    """
    try:
        # This would integrate with the dynamic activity database
        sample_activities = [
            {
                "name": f"Authentic {destination} Cultural Experience",
                "category": "cultural",
                "duration": "2-3 hours",
                "cost_range": criteria.get("budget", "moderate"),
                "authenticity": "high",
                "cultural_significance": "significant",
                "insider_tips": ["Best time is early morning", "Bring small gifts", "Learn basic greetings"],
                "best_time": "09:00-11:00",
                "weather_notes": "Indoor activity with outdoor components"
            }
        ]
        
        return sample_activities[:5]  # Return top 5
        
    except Exception as e:
        return [{"error": f"Failed to get activities: {str(e)}"}]

# Tool Collections
def get_basic_travel_tools():
    """Get basic travel planning tools"""
    return [
        search_travel_information,
        search_flights,
        search_hotels,
        search_restaurants,
        search_activities,
        search_local_culture,
        search_weather_info,
        search_budget_tips,
        search_transportation,
        search_safety_info
    ]

def get_enhanced_ai_tools():
    """Get enhanced AI-powered tools"""
    return [
        generate_intelligent_itinerary,
        get_contextual_activities
    ]

def get_all_tools():
    """Get all available tools"""
    return get_basic_travel_tools() + get_enhanced_ai_tools()
