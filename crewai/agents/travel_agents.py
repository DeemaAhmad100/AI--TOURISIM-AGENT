"""
🌍 Travel Planning Agents
Complete CrewAI agent collection for AI Travel Platform
"""

from crewai import Agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
)

# BASIC AGENTS REMOVED - REPLACED BY ENHANCED VERSIONS
# The following basic agents have been consolidated into enhanced agents:
# - create_travel_planner_agent() → create_itinerary_architect() 
# - create_local_expert_agent() → create_cultural_specialist()
# - create_budget_optimizer_agent() → integrated into itinerary_architect
# - create_activity_recommender_agent() → create_experience_curator()
# - create_travel_writer_agent() → integrated into experience_curator

def create_itinerary_architect():
    """Create strategic itinerary architect with AI intelligence and budget optimization"""
    return Agent(
        role="Strategic Itinerary Architect & Intelligence Coordinator",
        goal="Create revolutionary intelligent itineraries that adapt dynamically to traveler preferences with integrated budget optimization",
        backstory="""You are an advanced AI travel architect with access to cutting-edge 
        intelligence systems and integrated budget optimization. You create transformative 
        journeys that feel effortlessly intelligent, with dynamic adaptation, cultural 
        progression, budget optimization, and zero repetition.""",
        verbose=True,
        llm=llm,
        allow_delegation=True
    )

def create_experience_curator():
    """Create enhanced experience curator with documentation capabilities"""
    return Agent(
        role="Experience Curator & Cultural Intelligence Specialist",
        goal="Curate deeply intelligent, contextually aware experiences with integrated travel documentation",
        backstory="""You are an enhanced experience curator with access to advanced 
        cultural intelligence systems and documentation capabilities. You create experiences 
        that locals would appreciate and transform travelers into temporary cultural 
        participants, while generating beautiful travel guides.""",
        verbose=True,
        llm=llm,
        allow_delegation=False
    )

def create_cultural_specialist():
    """Create cultural intelligence specialist"""
    return Agent(
        role="Cultural Intelligence & Etiquette Specialist",
        goal="Provide deep cultural insights and ensure respectful, authentic travel experiences",
        backstory="""You are a cultural anthropologist and international etiquette expert 
        with deep knowledge of customs, traditions, and social norms worldwide. You help 
        travelers engage respectfully and authentically with local cultures while building 
        meaningful connections.""",
        verbose=True,
        llm=llm,
        allow_delegation=False
    )

def create_psychology_analyst():
    """Create traveler personality analysis specialist"""
    return Agent(
        role="Traveler Psychology Analyst",
        goal="Analyze traveler preferences and personality to create highly personalized experiences",
        backstory="""You are a behavioral psychologist specializing in travel preferences 
        and personality analysis. You excel at understanding what makes each traveler unique 
        and translating that into perfectly matched travel experiences.""",
        verbose=True,
        llm=llm,
        allow_delegation=False
    )

def create_seasonal_specialist():
    """Create seasonal intelligence specialist"""
    return Agent(
        role="Seasonal Intelligence Specialist",
        goal="Provide seasonal insights, weather considerations, and time-specific recommendations",
        backstory="""You are a meteorology expert and seasonal travel specialist who 
        understands how seasons, weather, and timing affect travel experiences. You excel 
        at optimizing travel timing and providing weather-appropriate alternatives.""",
        verbose=True,
        llm=llm,
        allow_delegation=False
    )

# Agent Factory Functions
def get_all_basic_agents():
    """DEPRECATED: All basic agents have been replaced by enhanced versions
    This function is kept for backwards compatibility and returns empty dict"""
    return {}

def get_all_agents():
    """Get all streamlined, enhanced agents"""
    return {
        "itinerary_architect": create_itinerary_architect(),
        "experience_curator": create_experience_curator(),
        "cultural_specialist": create_cultural_specialist(),
        "psychology_analyst": create_psychology_analyst(),
        "seasonal_specialist": create_seasonal_specialist()
    }

# DEPRECATED: Use get_all_agents() instead
def get_all_enhanced_agents():
    """DEPRECATED: Use get_all_agents() instead. All agents are now enhanced."""
    return get_all_agents()
