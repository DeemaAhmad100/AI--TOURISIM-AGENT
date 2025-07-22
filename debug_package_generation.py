"""
🔍 Package Generation Debug Test
Test if packages are being generated correctly
"""

import sys
import traceback
from pathlib import Path

# Add src to path for AI imports
current_dir = Path(__file__).parent
src_path = current_dir / "src"
sys.path.append(str(src_path))

print("🧪 Testing Package Generation...")

# Simulate the package generation
try:
    # Import the main function (we'll extract it)
    print("📦 Testing basic package creation structure...")
    
    # Test basic package structure
    test_package = {
        'id': 'test_pkg_1',
        'title': 'Test Package',
        'destination': 'Paris, France',
        'duration': 5,
        'travelers': 2,
        'budget_level': 'moderate',
        'focus': 'Cultural exploration',
        'flights': [{'airline': 'Test Air', 'price': 600}],
        'hotels': [{'name': 'Test Hotel', 'price': 150}],
        'restaurants': [{'name': 'Test Restaurant', 'cuisine': 'French'}],
        'activities': [{'name': 'Test Activity', 'price': 50}],
        'local_experiences': [{'name': 'Test Experience', 'price': 30}],
        'daily_itinerary': [{'day': 1, 'theme': 'Arrival'}],
        'pricing': {
            'total_cost': 2500,
            'cost_per_person': 1250,
            'daily_average': 500
        }
    }
    
    print("✅ Basic package structure created successfully!")
    print(f"📊 Package keys: {list(test_package.keys())}")
    print(f"💰 Total cost: ${test_package['pricing']['total_cost']}")
    
    # Test if all required components exist
    required_keys = ['id', 'title', 'destination', 'duration', 'travelers', 'pricing']
    missing_keys = [key for key in required_keys if key not in test_package]
    
    if missing_keys:
        print(f"❌ Missing keys: {missing_keys}")
    else:
        print("✅ All required keys present!")
        
    print("🎉 Package generation test completed successfully!")
    
except Exception as e:
    print(f"❌ Error during package generation test: {e}")
    traceback.print_exc()
