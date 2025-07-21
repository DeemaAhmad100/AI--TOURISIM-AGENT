"""
👥 CrewAI Crews Collection
All travel planning crew configurations organized and ready to use
"""

from .travel_crews import (
    create_basic_travel_crew,
    create_enhanced_travel_crew,
    create_comprehensive_travel_crew,
    create_quick_travel_crew,
    create_specialized_crew,
    get_crew_by_complexity,
    get_crew_by_purpose
)

__all__ = [
    "create_basic_travel_crew",
    "create_enhanced_travel_crew",
    "create_comprehensive_travel_crew",
    "create_quick_travel_crew",
    "create_specialized_crew",
    "get_crew_by_complexity",
    "get_crew_by_purpose"
]
