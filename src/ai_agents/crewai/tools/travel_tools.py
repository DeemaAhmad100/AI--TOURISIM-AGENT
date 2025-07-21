"""
🛠️ Travel Planning Tools
All CrewAI tools for travel research, booking, and recommendations
"""

import sys
import os
from pathlib import Path

# Add the project root to path but avoid the local crewai folder
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

# Now import from the actual CrewAI package
try:
    from crewai import tool
except ImportError:
    # Fallback: create a simple decorator if CrewAI is not available
    def tool(name=None, description=None):
        def decorator(func):
            func._tool_name = name or func.__name__
            func._tool_description = description or func.__doc__
            return func
        return decorator

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

# REMOVED REDUNDANT BASIC TOOLS:
# - generate_intelligent_itinerary (replaced by enhanced version)
# - get_contextual_activities (replaced by enhanced version)
# These tools have been replaced by their enhanced counterparts with superior AI capabilities

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
    # Import enhanced tools from enhanced_features
    try:
        from ...enhanced_features.enhanced_travel_agent import (
            generate_itinerary, 
            search_activities as enhanced_search_activities, 
            get_weather_alternatives
        )
        return [
            generate_itinerary,
            enhanced_search_activities,
            get_weather_alternatives
        ]
    except ImportError:
        print("⚠️ Enhanced AI tools not available")
        return []

def get_all_tools():
    """Get all available tools"""
    return get_basic_travel_tools() + get_enhanced_ai_tools()
