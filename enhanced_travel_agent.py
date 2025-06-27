"""
🎯 ENHANCED INTENT DETECTION & INTEGRATION SYSTEM
Advanced intent detection with database integration for AI Travel Agent
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client
from intent_detection import TravelIntentDetector
from typing import Dict, List, Any
import json

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

class SmartTravelAgent:
    """
    Enhanced Travel Agent with Intent Detection and Database Integration
    """
    
    def __init__(self):
        """Initialize the smart travel agent"""
        print("🚀 Initializing Smart Travel Agent with Intent Detection...")
        
        # Initialize intent detector
        self.intent_detector = TravelIntentDetector()
        self.intent_detector.setup()
        
        # Lower the confidence threshold for better detection
        self.intent_detector.threshold = 0.4
        
        print("✅ Smart Travel Agent ready!")
    
    def process_user_query(self, user_input: str) -> Dict[str, Any]:
        """
        Process user input with intent detection and provide intelligent responses
        
        Args:
            user_input: The user's query
            
        Returns:
            Dictionary containing intent, confidence, and intelligent response
        """
        # Detect intent
        intent, confidence = self.intent_detector.detect_intent(user_input)
        
        # Generate intelligent response based on intent
        response_data = {
            "user_query": user_input,
            "detected_intent": intent,
            "confidence": confidence,
            "response": self._generate_response(intent, user_input, confidence),
            "suggestions": []
        }
        
        # Add suggestions if confidence is low
        if confidence < 0.5:
            suggestions = self.intent_detector.get_intent_suggestions(user_input, top_k=3)
            response_data["suggestions"] = [intent for intent, score in suggestions]
        
        return response_data
    
    def _generate_response(self, intent: str, user_input: str, confidence: float) -> Dict[str, Any]:
        """
        Generate intelligent response based on detected intent
        """
        if intent == "destination_search":
            return self._handle_destination_search(user_input)
        
        elif intent == "budget_planning":
            return self._handle_budget_planning(user_input)
        
        elif intent == "activity_recommendations":
            return self._handle_activity_recommendations(user_input)
        
        elif intent == "trip_planning":
            return self._handle_trip_planning(user_input)
        
        elif intent == "weather_information":
            return self._handle_weather_information(user_input)
        
        elif intent == "transportation":
            return self._handle_transportation(user_input)
        
        elif intent == "accommodation":
            return self._handle_accommodation(user_input)
        
        elif intent == "cultural_information":
            return self._handle_cultural_information(user_input)
        
        else:
            return self._handle_unknown_intent(user_input, confidence)
    
    def _handle_destination_search(self, user_input: str) -> Dict[str, Any]:
        """Handle destination search queries"""
        
        # Extract keywords from user input
        keywords = user_input.lower()
        
        # Smart destination search based on keywords
        destinations = []
        
        try:
            if "romantic" in keywords or "honeymoon" in keywords:
                # Search for romantic destinations
                result = supabase.table("destinations").select("*").execute()
                for dest in result.data:
                    desc = dest.get('description', '').lower()
                    if any(word in desc for word in ['romantic', 'art', 'culture', 'historic']):
                        destinations.append(dest)
            
            elif "budget" in keywords or "cheap" in keywords:
                # Search for budget destinations
                result = supabase.table("destinations").select("*").lt("average_cost_per_day", 100).execute()
                destinations = result.data
            
            elif "beach" in keywords:
                # Search for beach destinations
                result = supabase.table("destinations").select("*").execute()
                for dest in result.data:
                    desc = dest.get('description', '').lower()
                    if any(word in desc for word in ['beach', 'coast', 'island', 'ocean']):
                        destinations.append(dest)
            
            elif "europe" in keywords:
                # Search for European destinations
                result = supabase.table("destinations").select("*").eq("continent", "Europe").execute()
                destinations = result.data
            
            elif "asia" in keywords:
                # Search for Asian destinations
                result = supabase.table("destinations").select("*").eq("continent", "Asia").execute()
                destinations = result.data
            
            else:
                # General destination search
                result = supabase.table("destinations").select("*").limit(5).execute()
                destinations = result.data
            
        except Exception as e:
            print(f"Database error: {e}")
            destinations = []
        
        return {
            "type": "destination_search",
            "message": f"Found {len(destinations)} destinations matching your criteria!",
            "destinations": destinations[:5],  # Limit to top 5
            "action": "display_destinations"
        }
    
    def _handle_budget_planning(self, user_input: str) -> Dict[str, Any]:
        """Handle budget planning queries"""
        
        try:
            # Get budget statistics
            all_destinations = supabase.table("destinations").select("name, country, average_cost_per_day, continent").execute()
            
            budget_ranges = {
                "budget": [d for d in all_destinations.data if d['average_cost_per_day'] < 75],
                "mid_range": [d for d in all_destinations.data if 75 <= d['average_cost_per_day'] <= 150],
                "luxury": [d for d in all_destinations.data if d['average_cost_per_day'] > 150]
            }
            
            # Calculate average costs by continent
            continent_costs = {}
            for dest in all_destinations.data:
                cont = dest['continent']
                if cont not in continent_costs:
                    continent_costs[cont] = []
                continent_costs[cont].append(dest['average_cost_per_day'])
            
            continent_averages = {
                cont: sum(costs) / len(costs) 
                for cont, costs in continent_costs.items()
            }
            
            return {
                "type": "budget_planning",
                "message": "Here's your budget breakdown and recommendations:",
                "budget_ranges": budget_ranges,
                "continent_averages": continent_averages,
                "action": "display_budget_info"
            }
            
        except Exception as e:
            print(f"Database error: {e}")
            return {
                "type": "budget_planning",
                "message": "I can help you with budget planning! Please specify your budget range or destination.",
                "action": "ask_budget_details"
            }
    
    def _handle_activity_recommendations(self, user_input: str) -> Dict[str, Any]:
        """Handle activity and attraction recommendations"""
        
        try:
            keywords = user_input.lower()
            attractions = []
            
            if "museum" in keywords:
                result = supabase.table("attractions").select("*").ilike("type", "%museum%").execute()
                attractions = result.data
            elif "restaurant" in keywords or "food" in keywords:
                result = supabase.table("attractions").select("*").ilike("type", "%restaurant%").execute()
                attractions = result.data
            else:
                # Get top-rated attractions
                result = supabase.table("attractions").select("*").order("rating", desc=True).limit(10).execute()
                attractions = result.data
            
            return {
                "type": "activity_recommendations",
                "message": f"Found {len(attractions)} great activities for you!",
                "attractions": attractions,
                "action": "display_attractions"
            }
            
        except Exception as e:
            print(f"Database error: {e}")
            return {
                "type": "activity_recommendations",
                "message": "I can recommend amazing activities! What type of activities interest you?",
                "action": "ask_activity_preferences"
            }
    
    def _handle_trip_planning(self, user_input: str) -> Dict[str, Any]:
        """Handle trip planning queries"""
        return {
            "type": "trip_planning",
            "message": "I'd love to help you plan your trip! Let me gather some information:",
            "questions": [
                "What's your destination?",
                "How many days are you planning to stay?",
                "What's your budget range?",
                "What activities interest you most?"
            ],
            "action": "start_trip_planning"
        }
    
    def _handle_weather_information(self, user_input: str) -> Dict[str, Any]:
        """Handle weather information queries"""
        return {
            "type": "weather_information",
            "message": "For current weather information, I recommend checking a weather service. However, I can provide general seasonal advice for different destinations!",
            "seasonal_tips": {
                "Europe": "Best visited April-September for warm weather",
                "Asia": "Varies by region - avoid monsoon seasons",
                "Americas": "Depends on hemisphere and altitude"
            },
            "action": "provide_seasonal_advice"
        }
    
    def _handle_transportation(self, user_input: str) -> Dict[str, Any]:
        """Handle transportation queries"""
        return {
            "type": "transportation",
            "message": "I can help with transportation planning! Here are general options:",
            "transport_options": [
                "✈️ Flights - Compare prices on booking sites",
                "🚂 Trains - Great for scenic routes in Europe/Asia",
                "🚌 Buses - Budget-friendly option",
                "🚗 Car rentals - For flexibility and road trips",
                "🚇 Local transport - Metro, buses, taxis in cities"
            ],
            "action": "provide_transport_info"
        }
    
    def _handle_accommodation(self, user_input: str) -> Dict[str, Any]:
        """Handle accommodation queries"""
        return {
            "type": "accommodation",
            "message": "Here are accommodation options to consider:",
            "accommodation_types": [
                "🏨 Hotels - Full service and amenities",
                "🏠 Vacation rentals - Like home away from home",
                "🏕️ Hostels - Budget-friendly, great for meeting people",
                "🏖️ Resorts - All-inclusive luxury options",
                "🏡 B&Bs - Personal touch and local experience"
            ],
            "action": "provide_accommodation_info"
        }
    
    def _handle_cultural_information(self, user_input: str) -> Dict[str, Any]:
        """Handle cultural information queries"""
        return {
            "type": "cultural_information",
            "message": "Cultural awareness is important for great travel experiences!",
            "cultural_tips": [
                "Research local customs and etiquette",
                "Learn basic phrases in the local language",
                "Understand tipping practices",
                "Respect religious and cultural sites",
                "Try local cuisine and experiences"
            ],
            "action": "provide_cultural_tips"
        }
    
    def _handle_unknown_intent(self, user_input: str, confidence: float) -> Dict[str, Any]:
        """Handle unknown or low-confidence intents"""
        
        # Get intent suggestions
        suggestions = self.intent_detector.get_intent_suggestions(user_input, top_k=3)
        
        return {
            "type": "clarification",
            "message": f"I'm not entirely sure what you're looking for (confidence: {confidence:.2f}). Here are some things I can help with:",
            "suggestions": [
                "🔍 Find destinations that match your preferences",
                "💰 Plan your travel budget",
                "🎯 Recommend activities and attractions",
                "📅 Help organize your trip itinerary",
                "🌤️ Provide seasonal travel advice",
                "🚗 Give transportation options",
                "🏨 Suggest accommodation types",
                "🏛️ Share cultural information"
            ],
            "intent_suggestions": [(intent, f"{score:.2f}") for intent, score in suggestions],
            "action": "ask_clarification"
        }
    
    def chat_interface(self):
        """Interactive chat interface for the travel agent"""
        
        print("\n🌍 SMART AI TRAVEL AGENT 🌍")
        print("=" * 50)
        print("Hello! I'm your intelligent travel agent.")
        print("I can help you with destinations, budgets, activities, and more!")
        print("Type 'quit' to exit.\n")
        
        while True:
            try:
                user_input = input("💬 You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("🌟 Thank you for using Smart Travel Agent! Safe travels! 🌟")
                    break
                
                if not user_input:
                    continue
                
                print("\n🤔 Processing your request...")
                
                # Process the query
                result = self.process_user_query(user_input)
                
                # Display results
                self._display_response(result)
                
                print("\n" + "-" * 50 + "\n")
                
            except KeyboardInterrupt:
                print("\n\n🌟 Thank you for using Smart Travel Agent! Safe travels! 🌟")
                break
            except Exception as e:
                print(f"❌ Sorry, I encountered an error: {e}")
                print("Please try rephrasing your question.\n")
    
    def _display_response(self, result: Dict[str, Any]):
        """Display the agent's response in a formatted way"""
        
        print(f"\n🎯 Intent: {result['detected_intent'].replace('_', ' ').title()}")
        print(f"📊 Confidence: {result['confidence']:.2f}")
        
        response = result['response']
        print(f"\n🤖 Agent: {response['message']}")
        
        # Display specific content based on response type
        if response['type'] == 'destination_search' and response.get('destinations'):
            print("\n📍 Recommended Destinations:")
            for i, dest in enumerate(response['destinations'], 1):
                print(f"   {i}. {dest['name']}, {dest['country']}")
                print(f"      💰 ${dest['average_cost_per_day']}/day")
                print(f"      📝 {dest['description'][:80]}...")
                print()
        
        elif response['type'] == 'budget_planning' and response.get('budget_ranges'):
            print("\n💰 Budget Categories:")
            ranges = response['budget_ranges']
            print(f"   💚 Budget (under $75): {len(ranges['budget'])} destinations")
            print(f"   💛 Mid-range ($75-150): {len(ranges['mid_range'])} destinations")
            print(f"   💜 Luxury (over $150): {len(ranges['luxury'])} destinations")
            
            if response.get('continent_averages'):
                print("\n🌍 Average costs by continent:")
                for continent, avg in response['continent_averages'].items():
                    print(f"   • {continent}: ${avg:.0f}/day")
        
        elif response['type'] == 'activity_recommendations' and response.get('attractions'):
            print("\n🎯 Top Attractions:")
            for i, attr in enumerate(response['attractions'][:5], 1):
                print(f"   {i}. {attr['name']} ({attr['type']})")
                print(f"      ⭐ Rating: {attr['rating']}")
                print(f"      📝 {attr['description'][:60]}...")
                print()
        
        # Display suggestions for low confidence
        if result.get('suggestions'):
            print("\n💡 Did you mean to ask about:")
            for suggestion in result['suggestions']:
                print(f"   • {suggestion.replace('_', ' ').title()}")


def demonstration():
    """Demonstration of the enhanced travel agent"""
    
    print("🎯 ENHANCED TRAVEL AGENT DEMONSTRATION")
    print("=" * 50)
    
    agent = SmartTravelAgent()
    
    # Test queries
    test_queries = [
        "I want to find romantic destinations in Europe",
        "What are some budget-friendly places to visit?",
        "Show me museums in Paris",
        "Can you help me plan a 7-day trip to Japan?",
        "What's the weather like in Bali in December?",
        "Where should I stay in New York?",
        "Tell me about local customs in Thailand",
        "I need help with something"
    ]
    
    print("\n🧪 TESTING ENHANCED TRAVEL AGENT:")
    print("-" * 50)
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{i}. Testing: '{query}'")
        result = agent.process_user_query(query)
        
        print(f"   🎯 Intent: {result['detected_intent']}")
        print(f"   📊 Confidence: {result['confidence']:.3f}")
        print(f"   💬 Response: {result['response']['message'][:80]}...")
        
        if result.get('suggestions'):
            print(f"   💡 Suggestions: {', '.join(result['suggestions'])}")


if __name__ == "__main__":
    # Run demonstration
    demonstration()
    
    print("\n\n🚀 Ready for interactive chat!")
    print("You can now start the interactive chat interface:")
    print("agent = SmartTravelAgent()")
    print("agent.chat_interface()")
