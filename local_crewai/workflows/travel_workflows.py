"""
🔄 Travel Planning Workflows
Complete workflow orchestration for different travel planning scenarios
"""

from ..crews.travel_crews import (
    create_basic_travel_crew,
    create_enhanced_travel_crew,
    create_comprehensive_travel_crew,
    get_crew_by_complexity,
    get_crew_by_purpose
)
from typing import Dict, Any
import asyncio
from datetime import datetime

class TravelPlanningWorkflow:
    """Main workflow orchestrator for travel planning"""
    
    def __init__(self, workflow_type: str = "basic"):
        self.workflow_type = workflow_type
        self.results = {}
        
    def execute_workflow(self, **kwargs) -> Dict[str, Any]:
        """Execute the complete travel planning workflow"""
        
        print(f"🚀 Starting {self.workflow_type} travel planning workflow...")
        
        try:
            # Get appropriate crew based on workflow type
            crew = get_crew_by_complexity(self.workflow_type, **kwargs)
            
            # Execute the workflow
            result = crew.kickoff()
            
            # Store results
            self.results = {
                "workflow_type": self.workflow_type,
                "execution_time": datetime.now().isoformat(),
                "parameters": kwargs,
                "result": str(result),
                "status": "completed"
            }
            
            print(f"✅ {self.workflow_type.title()} workflow completed successfully!")
            return self.results
            
        except Exception as e:
            error_result = {
                "workflow_type": self.workflow_type,
                "execution_time": datetime.now().isoformat(),
                "parameters": kwargs,
                "error": str(e),
                "status": "failed"
            }
            print(f"❌ Workflow failed: {e}")
            return error_result

def run_basic_workflow(destination: str, travel_dates: str, duration_days: int,
                      preferences: Dict, budget: str) -> Dict[str, Any]:
    """Run basic travel planning workflow"""
    
    workflow = TravelPlanningWorkflow("basic")
    return workflow.execute_workflow(
        destination=destination,
        travel_dates=travel_dates,
        duration_days=duration_days,
        preferences=preferences,
        budget=budget
    )

def run_enhanced_workflow(destination: str, travel_dates: str, duration_days: int,
                         preferences: Dict, budget: str) -> Dict[str, Any]:
    """Run enhanced travel planning workflow with AI intelligence"""
    
    workflow = TravelPlanningWorkflow("enhanced")
    return workflow.execute_workflow(
        destination=destination,
        travel_dates=travel_dates,
        duration_days=duration_days,
        preferences=preferences,
        budget=budget
    )

def run_comprehensive_workflow(destination: str, travel_dates: str, duration_days: int,
                             preferences: Dict, budget: str) -> Dict[str, Any]:
    """Run comprehensive travel planning workflow with full capabilities"""
    
    workflow = TravelPlanningWorkflow("comprehensive")
    return workflow.execute_workflow(
        destination=destination,
        travel_dates=travel_dates,
        duration_days=duration_days,
        preferences=preferences,
        budget=budget
    )

def run_quick_workflow(destination: str, preferences: Dict, budget: str) -> Dict[str, Any]:
    """Run quick travel planning workflow for rapid recommendations"""
    
    workflow = TravelPlanningWorkflow("quick")
    return workflow.execute_workflow(
        destination=destination,
        preferences=preferences,
        budget=budget
    )

def run_specialized_workflow(purpose: str, **kwargs) -> Dict[str, Any]:
    """Run specialized workflow based on purpose"""
    
    print(f"🎯 Starting {purpose} specialized workflow...")
    
    try:
        crew = get_crew_by_purpose(purpose, **kwargs)
        result = crew.kickoff()
        
        return {
            "workflow_type": f"specialized_{purpose}",
            "execution_time": datetime.now().isoformat(),
            "parameters": kwargs,
            "result": str(result),
            "status": "completed"
        }
        
    except Exception as e:
        return {
            "workflow_type": f"specialized_{purpose}",
            "execution_time": datetime.now().isoformat(),
            "parameters": kwargs,
            "error": str(e),
            "status": "failed"
        }

# Workflow Factory
class WorkflowFactory:
    """Factory for creating and managing workflows"""
    
    @staticmethod
    def create_workflow(workflow_type: str, **kwargs) -> Dict[str, Any]:
        """Create and execute workflow based on type"""
        
        workflow_map = {
            "basic": run_basic_workflow,
            "enhanced": run_enhanced_workflow,
            "comprehensive": run_comprehensive_workflow,
            "quick": run_quick_workflow
        }
        
        if workflow_type.startswith("specialized_"):
            purpose = workflow_type.replace("specialized_", "")
            return run_specialized_workflow(purpose, **kwargs)
        
        workflow_function = workflow_map.get(workflow_type)
        if not workflow_function:
            raise ValueError(f"Unknown workflow type: {workflow_type}")
        
        return workflow_function(**kwargs)
    
    @staticmethod
    def get_workflow_info() -> Dict[str, str]:
        """Get information about available workflows"""
        
        return {
            "basic": "Standard travel planning with core features",
            "enhanced": "AI-powered planning with intelligent features",
            "comprehensive": "Full-featured planning with all capabilities",
            "quick": "Rapid recommendations for immediate needs",
            "specialized_budget": "Budget-focused travel planning",
            "specialized_cultural": "Cultural immersion focused planning",
            "specialized_luxury": "Luxury travel planning",
            "specialized_adventure": "Adventure travel planning"
        }
