"""
🤖 CrewAI Agents Collection
Streamlined travel planning agents - Enhanced and optimized
"""

from .travel_agents import (
    create_itinerary_architect,
    create_experience_curator,
    create_cultural_specialist,
    create_psychology_analyst,
    create_seasonal_specialist,
    get_all_agents,
    # Deprecated functions kept for backwards compatibility
    get_all_basic_agents,
    get_all_enhanced_agents
)

__all__ = [
    "create_itinerary_architect",
    "create_experience_curator", 
    "create_cultural_specialist",
    "create_psychology_analyst",
    "create_seasonal_specialist",
    "get_all_agents",
    # Deprecated - for backwards compatibility only
    "get_all_basic_agents",
    "get_all_enhanced_agents"
]
