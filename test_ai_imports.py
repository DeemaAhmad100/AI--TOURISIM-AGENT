"""
Quick test script to verify AI module imports
"""
import sys
from pathlib import Path

# Add src to path
current_dir = Path(__file__).parent
src_path = current_dir / "src"
sys.path.append(str(src_path))

print("🧪 Testing Enhanced AI Module Imports...")

try:
    from ai_agents.integration.advanced_ai_integrator import ai_integrator
    print("✅ AI Integrator imported successfully!")
    
    # Test basic functionality
    result = ai_integrator.process_user_input_with_ai("I love adventure travel!", "test_user")
    print("✅ AI processing test completed!")
    print(f"📊 Result keys: {list(result.keys())}")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Runtime error: {e}")

print("🎉 Test completed!")
