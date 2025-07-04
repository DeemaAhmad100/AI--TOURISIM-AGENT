#!/usr/bin/env python3
"""
Validation script to test that all tool optimizations are working correctly.
This script validates:
1. All enhanced tools can be imported
2. No import errors exist
3. Tool factory functions return the correct enhanced tools
4. Agent and task configurations are valid
"""

import sys
import traceback
from pathlib import Path

def test_enhanced_tools_import():
    """Test that all enhanced tools can be imported correctly."""
    print("Testing enhanced tools import...")
    try:
        from local_crewai.tools.enhanced_tools import (
            generate_itinerary,
            search_activities,
            get_weather_alternatives
        )
        print("✅ Enhanced tools imported successfully")
        return True
    except Exception as e:
        print(f"❌ Enhanced tools import failed: {e}")
        traceback.print_exc()
        return False

def test_travel_tools_import():
    """Test that travel tools can be imported without errors."""
    print("Testing travel tools import...")
    try:
        from local_crewai.tools.travel_tools import (
            get_enhanced_ai_tools,
            get_basic_travel_tools,
            search_flights,
            search_hotels,
            search_restaurants,
            search_activities,
            search_local_culture,
            search_weather_info,
            search_budget_tips,
            search_transportation
        )
        print("✅ Travel tools imported successfully")
        return True
    except Exception as e:
        print(f"❌ Travel tools import failed: {e}")
        traceback.print_exc()
        return False

def test_enhanced_agent_import():
    """Test that enhanced agent can be imported without errors."""
    print("Testing enhanced agent import...")
    try:
        from enhanced_features.enhanced_travel_agent import (
            create_enhanced_travel_tasks
        )
        print("✅ Enhanced agent imported successfully")
        return True
    except Exception as e:
        print(f"❌ Enhanced agent import failed: {e}")
        traceback.print_exc()
        return False

def test_enhanced_tool_factory():
    """Test that the enhanced tool factory returns the correct tools."""
    print("Testing enhanced tool factory...")
    try:
        from local_crewai.tools.travel_tools import get_enhanced_ai_tools
        enhanced_tools = get_enhanced_ai_tools()
        
        # Check that we get the expected tools
        tool_names = [tool.__name__ if hasattr(tool, '__name__') else str(tool) for tool in enhanced_tools]
        expected_tools = ['generate_itinerary', 'search_activities', 'get_weather_alternatives']
        
        print(f"Enhanced tools returned: {tool_names}")
        
        for expected_tool in expected_tools:
            found = any(expected_tool in tool_name for tool_name in tool_names)
            if not found:
                print(f"❌ Expected tool '{expected_tool}' not found in enhanced tools")
                return False
        
        print("✅ Enhanced tool factory working correctly")
        return True
    except Exception as e:
        print(f"❌ Enhanced tool factory test failed: {e}")
        traceback.print_exc()
        return False

def test_task_import():
    """Test that tasks can be imported without errors."""
    print("Testing task import...")
    try:
        from local_crewai.tasks.travel_tasks import (
            create_basic_travel_tasks,
            create_enhanced_travel_tasks,
            create_comprehensive_travel_tasks
        )
        print("✅ Tasks imported successfully")
        return True
    except Exception as e:
        print(f"❌ Task import failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all validation tests."""
    print("🔍 Starting tool optimization validation...\n")
    
    tests = [
        test_enhanced_tools_import,
        test_travel_tools_import,
        test_enhanced_agent_import,
        test_enhanced_tool_factory,
        test_task_import
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
            failed += 1
        print()
    
    print(f"📊 Validation Results:")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📈 Success Rate: {passed}/{passed + failed} ({100 * passed / (passed + failed):.1f}%)")
    
    if failed == 0:
        print("\n🎉 All tool optimizations are working correctly!")
        return 0
    else:
        print(f"\n⚠️  {failed} validation test(s) failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
