"""
🛠️ CrewAI Tools Collection
All travel planning tools organized and ready to use
"""

from .travel_tools import (
    search_travel_information,
    search_flights,
    search_hotels,
    search_restaurants,
    search_activities,
    search_local_culture,
    search_weather_info,
    search_budget_tips,
    search_transportation,
    search_safety_info,
    get_basic_travel_tools,
    get_enhanced_ai_tools,
    get_all_tools
)

from .booking_tools import (
    create_booking_tool,
    payment_processing_tool,
    booking_confirmation_tool,
    cancellation_tool,
    get_booking_status_tool,
    modify_booking_tool,
    get_booking_tools,
    check_booking_tools_availability
)

from .search_tools import (
    tavily_search_tool,
    google_search_tool,
    local_search_tool,
    review_search_tool,
    real_time_search_tool,
    price_search_tool,
    get_search_tools
)

# Enhanced tools are now handled directly in travel_tools.py

# Tool categories for easy access
TRAVEL_TOOLS = [
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

OOKING_TOOLS = [
    create_booking_tool,
    payment_processing_tool,
    booking_confirmation_tool,
    cancellation_tool,
    get_booking_status_tool,
    modify_booking_tool
]

SEARCH_TOOLS = [
    tavily_search_tool,
    google_search_tool,
    local_search_tool,
    review_search_tool,
    real_time_search_tool,
    price_search_tool
]

def get_all_available_tools():
    """Get all available tools categorized"""
    return {
        "travel_tools": TRAVEL_TOOLS,
        "booking_tools": BOOKING_TOOLS,
        "search_tools": SEARCH_TOOLS,
        "enhanced_tools": get_enhanced_ai_tools()
    }

def get_tools_by_category(category: str):
    """Get tools by specific category"""
    categories = {
        "travel": TRAVEL_TOOLS,
        "booking": BOOKING_TOOLS,
        "search": SEARCH_TOOLS,
        "enhanced": get_enhanced_ai_tools()
    }
    return categories.get(category, [])

__all__ = [
    # Travel tools
    "search_travel_information",
    "search_flights",
    "search_hotels", 
    "search_restaurants",
    "search_activities",
    "search_local_culture",
    "search_weather_info",
    "search_budget_tips",
    "search_transportation",
    "search_safety_info",
    "get_basic_travel_tools",
    "get_enhanced_ai_tools",
    "get_all_tools",
    
    # Booking tools
    "create_booking_tool",
    "payment_processing_tool",
    "booking_confirmation_tool", 
    "cancellation_tool",
    "get_booking_status_tool",
    "modify_booking_tool",
    "get_booking_tools",
    "check_booking_tools_availability",
    
    # Search tools
    "tavily_search_tool",
    "google_search_tool",
    "local_search_tool",
    "review_search_tool",
    "real_time_search_tool",
    "price_search_tool",
    "get_search_tools",
    
    # Enhanced tools
    "get_enhanced_tools",
    "ENHANCED_TOOLS_AVAILABLE",
    
    # Tool categories
    "TRAVEL_TOOLS",
    "BOOKING_TOOLS", 
    "SEARCH_TOOLS",
    "get_all_available_tools",
    "get_tools_by_category"
]
