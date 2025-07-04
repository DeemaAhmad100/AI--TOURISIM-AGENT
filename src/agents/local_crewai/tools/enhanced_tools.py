"""
🛠️ Enhanced Travel Tools
Export enhanced tools for use throughout the platform
"""

# Export enhanced tools with clean names
try:
    from enhanced_features.enhanced_travel_agent import (
        generate_itinerary,
        search_activities,
        get_weather_alternatives
    )
    
    ENHANCED_TOOLS_AVAILABLE = True
    
    def get_enhanced_tools():
        """Get all enhanced travel tools"""
        return [
            generate_itinerary,
            search_activities,
            get_weather_alternatives
        ]
        
except ImportError as e:
    print(f"⚠️ Enhanced tools not available: {e}")
    ENHANCED_TOOLS_AVAILABLE = False
    
    def get_enhanced_tools():
        """Fallback when enhanced tools not available"""
        return []

__all__ = [
    "generate_itinerary",
    "search_activities", 
    "get_weather_alternatives",
    "get_enhanced_tools",
    "ENHANCED_TOOLS_AVAILABLE"
]
