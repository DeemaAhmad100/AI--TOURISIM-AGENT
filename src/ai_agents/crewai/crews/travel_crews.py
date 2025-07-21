"""
👥 Travel Planning Crews
Streamlined CrewAI crew configurations using enhanced agents only
"""

from crewai import Crew
from ..agents.travel_agents import (
    get_all_agents,
    create_itinerary_architect,
    create_experience_curator, 
    create_cultural_specialist,
    create_psychology_analyst,
    create_seasonal_specialist
)
from ..tasks.travel_tasks import (
    create_enhanced_travel_tasks,
    create_comprehensive_travel_tasks
)

def create_streamlined_travel_crew(destination: str, travel_dates: str, duration_days: int, 
                                 preferences: dict, budget: str):
    """Create streamlined travel planning crew with enhanced agents only"""
    
    # Get streamlined agents
    agents = get_all_agents()
    
    # Create enhanced tasks
    tasks = create_enhanced_travel_tasks(
        destination=destination,
        travel_dates=travel_dates,
        duration_days=duration_days,
        preferences=preferences,
        budget=budget
    )
    
    # Create streamlined crew
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True,
        memory=True,
        planning=True
    )
    
    return crew

# DEPRECATED: Use create_streamlined_travel_crew instead
def create_basic_travel_crew(destination: str, travel_dates: str, duration_days: int, 
                           preferences: dict, budget: str):
    """DEPRECATED: Use create_streamlined_travel_crew instead"""
    return create_streamlined_travel_crew(destination, travel_dates, duration_days, preferences, budget)

# DEPRECATED: Use create_streamlined_travel_crew instead  
def create_enhanced_travel_crew(destination: str, travel_dates: str, duration_days: int,
                              preferences: dict, budget: str):
    """DEPRECATED: Use create_streamlined_travel_crew instead"""
    return create_streamlined_travel_crew(destination, travel_dates, duration_days, preferences, budget)

# DEPRECATED: Use create_streamlined_travel_crew instead
def create_comprehensive_travel_crew(destination: str, travel_dates: str, duration_days: int,
                                   preferences: dict, budget: str):
    """DEPRECATED: Use create_streamlined_travel_crew instead"""
    return create_streamlined_travel_crew(destination, travel_dates, duration_days, preferences, budget)

def create_quick_travel_crew(destination: str, preferences: dict, budget: str):
    """Create quick travel planning crew for rapid recommendations"""
    
    # Get essential agents only - using current active agents
    agents = [
        create_itinerary_architect(),
        create_cultural_specialist(),
        create_experience_curator()
    ]
    
    # Create quick tasks (simplified)
    from ..tasks.travel_tasks import create_quick_travel_tasks
    tasks = create_quick_travel_tasks(
        destination=destination,
        preferences=preferences,
        budget=budget
    )
    
    # Create quick crew
    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=False,
        memory=False,
        planning=False,
        max_execution_time=120  # 2 minutes max
    )
    
    return crew

def create_specialized_crew(crew_type: str, **kwargs):
    """Create specialized crews for specific use cases"""
    
    if crew_type == "budget_focused":
        agents = [
            create_itinerary_architect(),  # Includes budget optimization
            create_cultural_specialist(),
            create_experience_curator()
        ]
    elif crew_type == "cultural_immersion":
        agents = [
            create_experience_curator(),
            create_itinerary_architect(),
            create_cultural_specialist()
        ]
    elif crew_type == "luxury_travel":
        agents = [
            create_itinerary_architect(),
            create_experience_curator(),  # Includes writing capabilities
            create_cultural_specialist()
        ]
    else:
        # Default to enhanced crew with all active agents
        agents = list(get_all_agents().values())
    
    # Create appropriate tasks based on crew type
    from ..tasks.travel_tasks import create_specialized_tasks
    tasks = create_specialized_tasks(crew_type=crew_type, **kwargs)
    
    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True,
        memory=True,
        planning=True
    )
    
    return crew

# Crew Factory Functions
def get_crew_by_complexity(complexity: str, **kwargs):
    """Get crew based on complexity level"""
    
    complexity_map = {
        "basic": create_basic_travel_crew,
        "enhanced": create_enhanced_travel_crew,
        "comprehensive": create_comprehensive_travel_crew,
        "quick": create_quick_travel_crew
    }
    
    crew_function = complexity_map.get(complexity, create_basic_travel_crew)
    return crew_function(**kwargs)

def get_crew_by_purpose(purpose: str, **kwargs):
    """Get crew based on specific purpose"""
    
    purpose_map = {
        "budget": lambda **kw: create_specialized_crew("budget_focused", **kw),
        "cultural": lambda **kw: create_specialized_crew("cultural_immersion", **kw),
        "luxury": lambda **kw: create_specialized_crew("luxury_travel", **kw),
        "adventure": lambda **kw: create_specialized_crew("adventure_travel", **kw)
    }
    
    crew_function = purpose_map.get(purpose, create_basic_travel_crew)
    return crew_function(**kwargs)
