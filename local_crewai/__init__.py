"""
🤖 CrewAI System - Organized AI Agent Framework
Complete CrewAI implementation with agents, tools, crews, and workflows
"""

# Import specific components to avoid circular imports
from .agents.travel_agents import (
    get_all_basic_agents,
    get_all_enhanced_agents,
    get_all_agents
)

from .tools.travel_tools import (
    get_basic_travel_tools,
    get_enhanced_ai_tools,
    get_all_tools
)

from .workflows.travel_workflows import (
    WorkflowFactory,
    run_basic_workflow,
    run_enhanced_workflow
)

__version__ = "1.0.0"
