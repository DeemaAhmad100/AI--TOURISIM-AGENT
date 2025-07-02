"""
👥 Travel Planning Crews
All CrewAI crew configurations for different travel planning scenarios
"""

from crewai import Crew
from ..agents.travel_agents import (
    get_all_basic_agents,
    get_all_enhanced_agents,
    create_travel_planner_agent,
    create_local_expert_agent,
    create_budget_optimizer_agent,
    create_activity_recommender_agent,
    create_travel_writer_agent,
    create_enhanced_itinerary_architect,
    create_experience_curator_agent
)
from ..tasks.travel_tasks import (
    create_basic_travel_tasks,
    create_enhanced_travel_tasks,
    create_comprehensive_travel_tasks
)

def create_basic_travel_crew(destination: str, travel_dates: str, duration_days: int, 
                           preferences: dict, budget: str):
    """Create basic travel planning crew"""
    
    # Get agents
    agents = get_all_basic_agents()
    
    # Create tasks
    tasks = create_basic_travel_tasks(
        destination=destination,
        travel_dates=travel_dates,
        duration_days=duration_days,
        preferences=preferences,
        budget=budget
    )
    
    # Create crew
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True,
        memory=True,
        planning=True
    )
    
    return crew

def create_enhanced_travel_crew(destination: str, travel_dates: str, duration_days: int,
                              preferences: dict, budget: str):
    """Create enhanced travel planning crew with AI intelligence"""
    
    # Get enhanced agents
    basic_agents = get_all_basic_agents()
    enhanced_agents = get_all_enhanced_agents()
    
    # Combine agents for comprehensive planning
    all_agents = list(basic_agents.values()) + list(enhanced_agents.values())
    
    # Create enhanced tasks
    tasks = create_enhanced_travel_tasks(
        destination=destination,
        travel_dates=travel_dates,
        duration_days=duration_days,
        preferences=preferences,
        budget=budget
    )
    
    # Create enhanced crew
    crew = Crew(
        agents=all_agents,
        tasks=tasks,
        verbose=True,
        memory=True,
        planning=True,
        max_execution_time=300  # 5 minutes max
    )
    
    return crew

def create_comprehensive_travel_crew(destination: str, travel_dates: str, duration_days: int,
                                   preferences: dict, budget: str):
    """Create comprehensive travel planning crew with full capabilities"""
    
    # Get all agents
    all_agents = get_all_basic_agents()
    all_agents.update(get_all_enhanced_agents())
    
    # Create comprehensive tasks
    tasks = create_comprehensive_travel_tasks(
        destination=destination,
        travel_dates=travel_dates,
        duration_days=duration_days,
        preferences=preferences,
        budget=budget
    )
    
    # Create comprehensive crew
    crew = Crew(
        agents=list(all_agents.values()),
        tasks=tasks,
        verbose=True,
        memory=True,
        planning=True,
        max_execution_time=600,  # 10 minutes max
        max_rpm=10,  # Rate limiting
        embedder={
            "provider": "openai",
            "config": {"model": "text-embedding-3-small"}
        }
    )
    
    return crew

def create_quick_travel_crew(destination: str, preferences: dict, budget: str):
    """Create quick travel planning crew for rapid recommendations"""
    
    # Get essential agents only
    agents = [
        create_travel_planner_agent(),
        create_local_expert_agent(),
        create_activity_recommender_agent()
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
            create_budget_optimizer_agent(),
            create_travel_planner_agent(),
            create_local_expert_agent()
        ]
    elif crew_type == "cultural_immersion":
        agents = [
            create_experience_curator_agent(),
            create_enhanced_itinerary_architect(),
            create_local_expert_agent()
        ]
    elif crew_type == "luxury_travel":
        agents = [
            create_travel_planner_agent(),
            create_activity_recommender_agent(),
            create_travel_writer_agent()
        ]
    else:
        # Default to basic crew
        agents = list(get_all_basic_agents().values())
    
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
