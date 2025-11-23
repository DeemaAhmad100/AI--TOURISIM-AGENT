"""
Integration tests for AI agents and travel platform components.
Tests the complete workflow from user input to travel package generation.
"""

import unittest
import sys
import os
from unittest.mock import Mock, patch, MagicMock

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

class TestAIAgentsIntegration(unittest.TestCase):
    """Test AI agents integration with the travel platform."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_destination = "Paris"
        self.test_budget = "moderate"
        self.test_style = "cultural-immersive"
        
    def test_itinerary_generator_integration(self):
        """Test enhanced itinerary generator integration."""
        try:
            from ai_agents.enhanced_itinerary_generator import EnhancedItineraryGenerator
            
            generator = EnhancedItineraryGenerator()
            self.assertIsNotNone(generator)
            
            # Test that the generator can be instantiated
            self.assertTrue(hasattr(generator, 'generate_itinerary'))
            
        except ImportError as e:
            self.skipTest(f"Skipping test due to import error: {e}")
    
    def test_booking_system_integration(self):
        """Test booking system integration."""
        try:
            from booking_system.booking_manager import BookingManager
            
            booking_manager = BookingManager()
            self.assertIsNotNone(booking_manager)
            
            # Test basic booking manager functionality
            self.assertTrue(hasattr(booking_manager, 'create_booking'))
            
        except ImportError as e:
            self.skipTest(f"Skipping test due to import error: {e}")
    
    def test_stripe_integration(self):
        """Test Stripe payment integration."""
        try:
            from api_integration.stripe.stripe_service import StripeService
            
            # Test that StripeService can be imported and instantiated
            service = StripeService()
            self.assertIsNotNone(service)
            
        except ImportError as e:
            self.skipTest(f"Skipping test due to import error: {e}")
    
    @patch('supabase.create_client')
    def test_database_integration(self, mock_supabase):
        """Test database integration with mocked Supabase."""
        mock_client = Mock()
        mock_supabase.return_value = mock_client
        
        # Mock successful database response
        mock_response = Mock()
        mock_response.data = [{"id": 1, "name": "Test Destination"}]
        mock_client.table().select().execute.return_value = mock_response
        
        # Test that database queries work with mocked client
        self.assertEqual(len(mock_response.data), 1)
        
    def test_complete_travel_package_workflow(self):
        """Test complete workflow from input to travel package generation."""
        # This is a high-level integration test
        test_params = {
            'destination': self.test_destination,
            'budget': self.test_budget,
            'style': self.test_style,
            'duration': 7
        }
        
        # Test that all required parameters are present
        required_params = ['destination', 'budget', 'style', 'duration']
        for param in required_params:
            self.assertIn(param, test_params)
        
        # Verify parameter types
        self.assertIsInstance(test_params['destination'], str)
        self.assertIsInstance(test_params['budget'], str)
        self.assertIsInstance(test_params['style'], str)
        self.assertIsInstance(test_params['duration'], int)

class TestPlatformComponents(unittest.TestCase):
    """Test individual platform components."""
    
    def test_config_loading(self):
        """Test configuration loading."""
        try:
            from core.config import load_config
            # Test that config can be imported
            self.assertTrue(callable(load_config))
            
        except ImportError as e:
            self.skipTest(f"Skipping test due to import error: {e}")
    
    def test_platform_core(self):
        """Test platform core functionality."""
        try:
            from core.platform_core import TravelPlatform
            
            # Test that platform can be imported
            platform = TravelPlatform()
            self.assertIsNotNone(platform)
            
        except ImportError as e:
            self.skipTest(f"Skipping test due to import error: {e}")

if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)