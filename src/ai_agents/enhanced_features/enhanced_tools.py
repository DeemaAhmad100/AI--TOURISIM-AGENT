#!/usr/bin/env python3
"""
🔧 Enhanced Tools Factory
Creates enhanced travel tools for the AI travel platform
"""

import os
import sys
from pathlib import Path
from typing import List

# Add the current directory to the Python path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

from crewai.tools import tool

@tool
def generate_itinerary(destination: str, duration: int, preferences: dict, budget: str) -> dict:
    """
    Generate truly intelligent, dynamic itinerary using advanced AI systems
    """
    # Import the actual function from enhanced_travel_agent
    try:
        from .enhanced_travel_agent import generate_itinerary as _generate_itinerary
        return _generate_itinerary(destination, duration, preferences, budget)
    except ImportError:
        return {
            "destination": destination,
            "duration": duration,
            "message": "Enhanced itinerary generation (fallback mode)",
            "status": "generated"
        }

@tool
def search_activities(destination: str, criteria: dict) -> list:
    """
    Get contextually relevant activities based on intelligent criteria
    """
    try:
        from .enhanced_travel_agent import search_activities as _search_activities
        return _search_activities(destination, criteria)
    except ImportError:
        return [f"Activity search for {destination} (fallback mode)"]

@tool
def get_weather_alternatives(destination: str, original_activities: list, weather: str) -> list:
    """
    Get weather-appropriate alternative activities
    """
    try:
        from .enhanced_travel_agent import get_weather_alternatives as _get_weather_alternatives
        return _get_weather_alternatives(destination, original_activities, weather)
    except ImportError:
        return [f"Weather alternatives for {destination} in {weather} weather (fallback mode)"]

def create_enhanced_tools() -> List:
    """
    Create and return all enhanced travel tools
    """
    return [
        generate_itinerary,
        search_activities,
        get_weather_alternatives
    ]

def get_enhanced_tools():
    """
    Alias for create_enhanced_tools for compatibility
    """
    return create_enhanced_tools()

if __name__ == "__main__":
    tools = create_enhanced_tools()
    print(f"✅ Created {len(tools)} enhanced tools")
    for tool in tools:
        print(f"   - {tool.name}")
