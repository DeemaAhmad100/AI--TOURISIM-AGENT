"""
📋 Travel Planning Tasks
All CrewAI task definitions for travel planning workflows
"""

from crewai import Task
from ..tools.travel_tools import get_all_tools, get_basic_travel_tools
from typing import Dict, List

def create_basic_travel_tasks(destination: str, travel_dates: str, duration_days: int,
                            preferences: Dict, budget: str) -> List[Task]:
    """Create basic travel planning tasks"""
    
    # Import agents (will be passed when creating crew)
    tools = get_basic_travel_tools()
    
    research_task = Task(
        description=f"""Conduct comprehensive research for a {duration_days}-day trip to {destination}.
        
        Research Requirements:
        - Travel dates: {travel_dates}
        - Budget level: {budget}
        - Preferences: {preferences}
        
        Use available tools to gather information about:
        1. Flight options and transportation
        2. Accommodation recommendations
        3. Local attractions and activities
        4. Cultural information and etiquette
        5. Weather conditions and what to pack
        6. Safety information and travel advisories
        7. Budget considerations and money-saving tips
        
        Provide detailed, practical information that will inform the itinerary creation.""",
        expected_output=f"Comprehensive research report for {destination} trip with practical recommendations",
        tools=tools
    )
    
    itinerary_task = Task(
        description=f"""Create a detailed {duration_days}-day itinerary for {destination} based on the research findings.
        
        Itinerary Requirements:
        - Duration: {duration_days} days
        - Budget: {budget}
        - Preferences: {preferences}
        - Travel dates: {travel_dates}
        
        Create a day-by-day schedule that includes:
        1. Daily themes and objectives
        2. Morning, afternoon, and evening activities
        3. Restaurant recommendations for each meal
        4. Transportation between activities
        5. Estimated costs and time allocations
        6. Alternative options for weather contingencies
        7. Cultural learning opportunities
        8. Rest periods and flexibility for spontaneous exploration
        
        Ensure the itinerary balances must-see attractions with authentic local experiences.""",
        expected_output=f"Detailed {duration_days}-day itinerary for {destination} with daily schedules and alternatives",
        tools=tools,
        context=[research_task]
    )
    
    optimization_task = Task(
        description=f"""Optimize the itinerary for budget efficiency and practical logistics.
        
        Optimization Focus:
        - Budget level: {budget}
        - Preferences: {preferences}
        
        Review and improve:
        1. Cost optimization while maintaining quality
        2. Logistics and transportation efficiency
        3. Time management and realistic scheduling
        4. Balance between activities and rest
        5. Seasonal considerations and timing
        6. Local money-saving opportunities
        7. Package deals and group discounts
        
        Provide final cost estimates and budget breakdown.""",
        expected_output=f"Optimized itinerary with budget breakdown and practical improvements",
        tools=tools,
        context=[research_task, itinerary_task]
    )
    
    documentation_task = Task(
        description=f"""Create a comprehensive travel guide document for the {destination} trip.
        
        Guide Components:
        - Executive summary of the trip
        - Daily detailed itinerary
        - Practical travel information
        - Budget breakdown and cost estimates
        - Cultural tips and etiquette guidelines
        - Emergency contacts and important information
        - Packing list and preparation checklist
        - Alternative options and contingency plans
        
        Format the guide as a professional, easy-to-follow travel document.""",
        expected_output=f"Complete travel guide document for {destination} trip",
        context=[research_task, itinerary_task, optimization_task]
    )
    
    return [research_task, itinerary_task, optimization_task, documentation_task]

def create_enhanced_travel_tasks(destination: str, travel_dates: str, duration_days: int,
                               preferences: Dict, budget: str) -> List[Task]:
    """Create enhanced travel planning tasks with AI intelligence"""
    
    tools = get_all_tools()
    
    enhanced_research_task = Task(
        description=f"""Conduct advanced intelligent research for {destination} using AI-powered analysis.
        
        Enhanced Research Requirements:
        - Destination: {destination}
        - Duration: {duration_days} days
        - Travel dates: {travel_dates}
        - Budget: {budget}
        - Preferences: {preferences}
        
        Advanced Analysis:
        1. Personality-based activity matching
        2. Cultural intelligence assessment
        3. Seasonal optimization opportunities
        4. Local authenticity scoring
        5. Anti-tourist-trap intelligence
        6. Progressive cultural immersion planning
        7. Energy management considerations
        8. Social interaction opportunities
        
        Use intelligent tools to create deep cultural understanding.""",
        expected_output=f"Advanced intelligence report for {destination} with cultural and personality insights",
        tools=tools
    )
    
    intelligent_itinerary_task = Task(
        description=f"""Create revolutionary intelligent itinerary using advanced AI systems.
        
        Intelligence Requirements:
        - Use generate_intelligent_itinerary tool
        - Apply contextual activity selection
        - Implement progressive cultural immersion
        - Design anti-repetition protocols
        - Optimize for authentic local experiences
        
        Daily Intelligence Features:
        1. Cultural progression that builds day by day
        2. Energy pattern optimization
        3. Local rhythm integration
        4. Authentic experience prioritization
        5. Weather and crowd intelligence
        6. Social interaction design
        7. Learning objective progression
        
        Create transformative journey architecture.""",
        expected_output=f"Revolutionary intelligent {duration_days}-day itinerary with dynamic adaptation",
        tools=tools,
        context=[enhanced_research_task]
    )
    
    experience_curation_task = Task(
        description=f"""Curate deeply authentic experiences using cultural intelligence.
        
        Curation Focus:
        - Replace tourist activities with authentic alternatives
        - Design meaningful cultural connections
        - Implement local social integration
        - Create learning progression opportunities
        
        Experience Intelligence:
        1. Authenticity scoring and verification
        2. Cultural significance assessment
        3. Local interaction opportunities
        4. Insider approach guidance
        5. Respectful participation protocols
        6. Photo opportunity intelligence
        7. Cultural learning outcomes
        
        Transform travelers into cultural participants.""",
        expected_output=f"Culturally intelligent experience curation for {destination}",
        tools=tools,
        context=[enhanced_research_task, intelligent_itinerary_task]
    )
    
    return [enhanced_research_task, intelligent_itinerary_task, experience_curation_task]

def create_comprehensive_travel_tasks(destination: str, travel_dates: str, duration_days: int,
                                    preferences: Dict, budget: str) -> List[Task]:
    """Create comprehensive travel planning tasks with full capabilities"""
    
    # Combine basic and enhanced tasks
    basic_tasks = create_basic_travel_tasks(destination, travel_dates, duration_days, preferences, budget)
    enhanced_tasks = create_enhanced_travel_tasks(destination, travel_dates, duration_days, preferences, budget)
    
    # Add additional comprehensive tasks
    tools = get_all_tools()
    
    integration_task = Task(
        description=f"""Integrate all research and planning into final comprehensive travel plan.
        
        Integration Requirements:
        - Combine basic research with AI intelligence
        - Merge practical logistics with cultural experiences
        - Balance budget optimization with authentic experiences
        - Create seamless daily flow with intelligent adaptation
        
        Final Integration:
        1. Unified itinerary with all intelligence features
        2. Complete budget breakdown with optimization
        3. Cultural progression mapped across all days
        4. Contingency plans for all scenarios
        5. Local integration opportunities
        6. Learning outcomes and growth tracking
        
        Deliver world-class travel experience design.""",
        expected_output=f"Comprehensive integrated travel plan for {destination}",
        tools=tools,
        context=basic_tasks + enhanced_tasks
    )
    
    return basic_tasks + enhanced_tasks + [integration_task]

def create_quick_travel_tasks(destination: str, preferences: Dict, budget: str) -> List[Task]:
    """Create quick travel planning tasks for rapid recommendations"""
    
    tools = get_basic_travel_tools()[:5]  # Limited tools for speed
    
    quick_research_task = Task(
        description=f"""Quickly research essential information for {destination}.
        
        Focus on:
        - Must-see attractions
        - Local food recommendations
        - Transportation basics
        - Cultural highlights
        
        Preferences: {preferences}
        Budget: {budget}""",
        expected_output=f"Essential travel information for {destination}",
        tools=tools
    )
    
    quick_recommendations_task = Task(
        description=f"""Create quick travel recommendations for {destination}.
        
        Provide:
        - Top 5 must-do activities
        - Best local restaurants
        - Transportation tips
        - Cultural insights
        
        Keep recommendations practical and actionable.""",
        expected_output=f"Quick travel recommendations for {destination}",
        tools=tools,
        context=[quick_research_task]
    )
    
    return [quick_research_task, quick_recommendations_task]

def create_specialized_tasks(crew_type: str, **kwargs) -> List[Task]:
    """Create specialized tasks based on crew type"""
    
    if crew_type == "budget_focused":
        return create_budget_focused_tasks(**kwargs)
    elif crew_type == "cultural_immersion":
        return create_cultural_immersion_tasks(**kwargs)
    elif crew_type == "luxury_travel":
        return create_luxury_travel_tasks(**kwargs)
    else:
        return create_basic_travel_tasks(**kwargs)

def create_budget_focused_tasks(**kwargs) -> List[Task]:
    """Create budget-focused travel tasks"""
    tools = get_basic_travel_tools()
    
    budget_research_task = Task(
        description=f"""Research budget travel options for {kwargs.get('destination', 'destination')}.
        
        Focus on:
        - Budget accommodations
        - Free and low-cost activities
        - Money-saving transportation
        - Affordable dining options
        - Student/group discounts
        """,
        expected_output="Budget travel research with cost-saving opportunities",
        tools=tools
    )
    
    return [budget_research_task]

def create_cultural_immersion_tasks(**kwargs) -> List[Task]:
    """Create cultural immersion focused tasks"""
    tools = get_all_tools()
    
    cultural_research_task = Task(
        description=f"""Research deep cultural experiences for {kwargs.get('destination', 'destination')}.
        
        Focus on:
        - Local festivals and events
        - Cultural workshops and classes
        - Traditional neighborhoods
        - Authentic local interactions
        - Historical and cultural significance
        """,
        expected_output="Cultural immersion research with authentic experiences",
        tools=tools
    )
    
    return [cultural_research_task]

def create_luxury_travel_tasks(**kwargs) -> List[Task]:
    """Create luxury travel focused tasks"""
    tools = get_basic_travel_tools()
    
    luxury_research_task = Task(
        description=f"""Research luxury travel options for {kwargs.get('destination', 'destination')}.
        
        Focus on:
        - Premium accommodations
        - Exclusive experiences
        - Fine dining establishments
        - Private tours and guides
        - Luxury transportation
        """,
        expected_output="Luxury travel research with premium options",
        tools=tools
    )
    
    return [luxury_research_task]
