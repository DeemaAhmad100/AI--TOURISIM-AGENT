"""
🤖 CrewAI Agents Collection
All travel planning and AI agents organized and ready to use
"""

from .travel_agents import (
    create_travel_planner_agent,
    create_local_expert_agent,
    create_budget_optimizer_agent,
    create_activity_recommender_agent,
    create_travel_writer_agent,
    create_enhanced_itinerary_architect,
    create_experience_curator_agent,
    create_personality_analysis_agent,
    create_cultural_intelligence_agent,
    create_seasonal_expert_agent,
    get_all_basic_agents,
    get_all_enhanced_agents,
    get_all_agents
)

__all__ = [
    "create_travel_planner_agent",
    "create_local_expert_agent", 
    "create_budget_optimizer_agent",
    "create_activity_recommender_agent",
    "create_travel_writer_agent",
    "create_enhanced_itinerary_architect",
    "create_experience_curator_agent",
    "create_personality_analysis_agent",
    "create_cultural_intelligence_agent",
    "create_seasonal_expert_agent",
    "get_all_basic_agents",
    "get_all_enhanced_agents",
    "get_all_agents"
]
