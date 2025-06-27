"""
🌍 INTELLIGENT COUNTRY TRAVEL ADVISOR 🌍
Enhanced AI Travel Agent that can answer questions about any country in the world
with smart intent detection and comprehensive travel recommendations
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client
from enhanced_travel_agent import SmartTravelAgent
import re
from typing import Dict, List, Any

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

class WorldTravelExpert(SmartTravelAgent):
    """
    Enhanced Travel Agent that can provide information about any country in the world
    """
    
    def __init__(self):
        """Initialize the world travel expert"""
        super().__init__()
        
        # Extended country knowledge base
        self.country_info = {
            "france": {
                "official_name": "France",
                "continent": "Europe",
                "capital": "Paris",
                "currency": "Euro (EUR)",
                "languages": ["French"],
                "best_time": "April to September",
                "famous_for": ["Art", "Culture", "Cuisine", "Romance", "Fashion"],
                "must_visit": ["Paris", "Nice", "Lyon", "Bordeaux", "Marseille"],
                "typical_activities": [
                    "Visit iconic landmarks like Eiffel Tower and Louvre",
                    "Explore charming villages in Provence",
                    "Wine tasting in Bordeaux and Burgundy",
                    "Art appreciation in world-class museums",
                    "Culinary experiences and cooking classes",
                    "River cruises along the Seine",
                    "Shopping in fashionable boutiques",
                    "Historical tours of châteaux and palaces"
                ]
            },
            "japan": {
                "official_name": "Japan",
                "continent": "Asia",
                "capital": "Tokyo",
                "currency": "Japanese Yen (JPY)",
                "languages": ["Japanese"],
                "best_time": "March to May, September to November",
                "famous_for": ["Technology", "Culture", "Anime", "Cuisine", "Cherry Blossoms"],
                "must_visit": ["Tokyo", "Kyoto", "Osaka", "Hiroshima", "Mount Fuji"],
                "typical_activities": [
                    "Experience traditional tea ceremonies",
                    "Visit ancient temples and shrines",
                    "Enjoy cherry blossom viewing (sakura)",
                    "Explore modern technology districts",
                    "Try authentic sushi and ramen",
                    "Stay in traditional ryokans",
                    "Attend cultural festivals",
                    "Visit anime and manga districts"
                ]
            },
            "italy": {
                "official_name": "Italy",
                "continent": "Europe",
                "capital": "Rome",
                "currency": "Euro (EUR)",
                "languages": ["Italian"],
                "best_time": "April to June, September to October",
                "famous_for": ["History", "Art", "Cuisine", "Architecture", "Romance"],
                "must_visit": ["Rome", "Florence", "Venice", "Milan", "Naples"],
                "typical_activities": [
                    "Explore ancient Roman ruins and Colosseum",
                    "Art appreciation in Renaissance museums",
                    "Gondola rides in Venice canals",
                    "Culinary tours and cooking classes",
                    "Wine tasting in Tuscany",
                    "Visit Vatican City and Sistine Chapel",
                    "Fashion shopping in Milan",
                    "Coastal drives along Amalfi Coast"
                ]
            },
            "spain": {
                "official_name": "Spain",
                "continent": "Europe",
                "capital": "Madrid",
                "currency": "Euro (EUR)",
                "languages": ["Spanish", "Catalan", "Basque"],
                "best_time": "April to June, September to October",
                "famous_for": ["Architecture", "Flamenco", "Cuisine", "Beaches", "Culture"],
                "must_visit": ["Barcelona", "Madrid", "Seville", "Valencia", "Granada"],
                "typical_activities": [
                    "Explore Gaudí's architectural masterpieces",
                    "Experience flamenco shows and dance",
                    "Enjoy tapas tours and Spanish cuisine",
                    "Visit world-class museums like Prado",
                    "Relax on Mediterranean beaches",
                    "Explore Moorish palaces in Andalusia",
                    "Participate in local festivals",
                    "Walk the Camino de Santiago pilgrimage"
                ]
            },
            "thailand": {
                "official_name": "Thailand",
                "continent": "Asia",
                "capital": "Bangkok",
                "currency": "Thai Baht (THB)",
                "languages": ["Thai"],
                "best_time": "November to March",
                "famous_for": ["Temples", "Beaches", "Street Food", "Culture", "Hospitality"],
                "must_visit": ["Bangkok", "Chiang Mai", "Phuket", "Krabi", "Ayutthaya"],
                "typical_activities": [
                    "Visit ornate Buddhist temples",
                    "Experience traditional Thai massage",
                    "Explore floating markets",
                    "Island hopping and beach relaxation",
                    "Street food tours and cooking classes",
                    "Elephant sanctuary visits",
                    "Traditional craft workshops",
                    "River boat tours and jungle treks"
                ]
            },
            "egypt": {
                "official_name": "Egypt",
                "continent": "Africa",
                "capital": "Cairo",
                "currency": "Egyptian Pound (EGP)",
                "languages": ["Arabic"],
                "best_time": "October to April",
                "famous_for": ["Pyramids", "Ancient History", "Nile River", "Pharaohs"],
                "must_visit": ["Cairo", "Luxor", "Aswan", "Alexandria", "Sharm El Sheikh"],
                "typical_activities": [
                    "Explore ancient pyramids and Sphinx",
                    "Nile River cruises and felucca rides",
                    "Visit tombs in Valley of the Kings",
                    "Discover treasures in Egyptian Museum",
                    "Desert safari and camel rides",
                    "Snorkeling in Red Sea coral reefs",
                    "Sound and light shows at monuments",
                    "Traditional bazaar shopping"
                ]
            },
            "australia": {
                "official_name": "Australia",
                "continent": "Oceania",
                "capital": "Canberra",
                "currency": "Australian Dollar (AUD)",
                "languages": ["English"],
                "best_time": "September to November, March to May",
                "famous_for": ["Wildlife", "Beaches", "Outback", "Coral Reef", "Cities"],
                "must_visit": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"],
                "typical_activities": [
                    "Explore Great Barrier Reef snorkeling",
                    "Wildlife encounters with kangaroos and koalas",
                    "Sydney Opera House and Harbour Bridge",
                    "Outback adventures and Uluru visits",
                    "Beach surfing and coastal drives",
                    "Wine tasting in Barossa Valley",
                    "Aboriginal culture experiences",
                    "Road trips along scenic coastlines"
                ]
            },
            "united states": {
                "official_name": "United States of America",
                "continent": "North America",
                "capital": "Washington D.C.",
                "currency": "US Dollar (USD)",
                "languages": ["English"],
                "best_time": "Varies by region",
                "famous_for": ["Diversity", "National Parks", "Cities", "Entertainment", "Culture"],
                "must_visit": ["New York", "Los Angeles", "San Francisco", "Las Vegas", "Miami"],
                "typical_activities": [
                    "Explore iconic landmarks and monuments",
                    "Visit world-class museums and galleries",
                    "Experience Broadway shows and entertainment",
                    "National park adventures and hiking",
                    "Beach activities and water sports",
                    "Food tours and diverse cuisine",
                    "Shopping in major retail destinations",
                    "Road trips on scenic highways"
                ]
            }
        }
    
    def extract_country_from_query(self, query: str) -> str:
        """Extract country name from user query"""
        query_lower = query.lower()
        
        # Common country name patterns
        country_patterns = [
            r'\bin\s+([a-zA-Z\s]+?)(?:\s|$|[,.])',
            r'\babout\s+([a-zA-Z\s]+?)(?:\s|$|[,.])',
            r'\bto\s+([a-zA-Z\s]+?)(?:\s|$|[,.])',
            r'\bvisit\s+([a-zA-Z\s]+?)(?:\s|$|[,.])',
            r'^([a-zA-Z\s]+?)\s+attractions',
            r'^([a-zA-Z\s]+?)\s+travel'
        ]
        
        # Check database countries first
        db_countries = self._get_database_countries()
        for country in db_countries:
            if country.lower() in query_lower:
                return country
        
        # Check knowledge base countries
        for country_key in self.country_info.keys():
            country_name = self.country_info[country_key]["official_name"]
            if country_key in query_lower or country_name.lower() in query_lower:
                return country_name
        
        # Pattern matching for country extraction
        for pattern in country_patterns:
            match = re.search(pattern, query_lower)
            if match:
                potential_country = match.group(1).strip()
                # Clean up common words
                cleaned = re.sub(r'\b(the|a|an|some|any|best|good|great)\b', '', potential_country).strip()
                if len(cleaned) > 2:
                    return cleaned.title()
        
        return None
    
    def _get_database_countries(self) -> List[str]:
        """Get list of countries from database"""
        try:
            destinations = supabase.table("destinations").select("country").execute()
            return [dest["country"] for dest in destinations.data]
        except:
            return []
    
    def get_country_attractions(self, country: str) -> List[Dict]:
        """Get attractions for a specific country from database"""
        try:
            # Get destinations in the country
            destinations = supabase.table("destinations").select("id, name").eq("country", country).execute()
            
            if not destinations.data:
                return []
            
            # Get attractions for these destinations
            attractions = []
            for dest in destinations.data:
                dest_attractions = supabase.table("attractions").select("*").eq("destination_id", dest["id"]).execute()
                for attr in dest_attractions.data:
                    attr["destination_name"] = dest["name"]
                    attractions.append(attr)
            
            # Sort by rating
            attractions.sort(key=lambda x: x.get("rating", 0), reverse=True)
            return attractions
            
        except Exception as e:
            print(f"Database error: {e}")
            return []
    
    def get_country_destinations(self, country: str) -> List[Dict]:
        """Get destinations for a specific country"""
        try:
            destinations = supabase.table("destinations").select("*").eq("country", country).execute()
            return destinations.data
        except:
            return []
    
    def generate_country_response(self, country: str, user_query: str) -> Dict[str, Any]:
        """Generate comprehensive response about a country"""
        
        # Get data from database
        attractions = self.get_country_attractions(country)
        destinations = self.get_country_destinations(country)
        
        # Get country info from knowledge base
        country_key = country.lower()
        country_info = self.country_info.get(country_key, {})
        
        response = {
            "type": "country_information",
            "country": country,
            "has_database_info": len(destinations) > 0,
            "attractions": attractions,
            "destinations": destinations,
            "country_info": country_info,
            "recommendations": self._generate_country_recommendations(country, country_info, attractions),
            "action": "display_country_info"
        }
        
        return response
    
    def _generate_country_recommendations(self, country: str, country_info: Dict, attractions: List[Dict]) -> Dict[str, List[str]]:
        """Generate comprehensive recommendations for a country"""
        
        recommendations = {
            "must_visit_attractions": [],
            "cultural_activities": [],
            "adventure_activities": [],
            "food_experiences": [],
            "seasonal_activities": [],
            "practical_tips": []
        }
        
        # Database attractions
        if attractions:
            recommendations["must_visit_attractions"] = [
                f"🎯 {attr['name']} ({attr['type']}) - Rating: ⭐{attr['rating']}"
                for attr in attractions[:5]
            ]
        
        # Knowledge base activities
        if country_info.get("typical_activities"):
            activities = country_info["typical_activities"]
            
            # Categorize activities
            for activity in activities:
                if any(word in activity.lower() for word in ['museum', 'temple', 'culture', 'art', 'historic']):
                    recommendations["cultural_activities"].append(f"🏛️ {activity}")
                elif any(word in activity.lower() for word in ['adventure', 'trek', 'climb', 'safari', 'dive']):
                    recommendations["adventure_activities"].append(f"🏔️ {activity}")
                elif any(word in activity.lower() for word in ['food', 'cuisine', 'cooking', 'restaurant', 'taste']):
                    recommendations["food_experiences"].append(f"🍽️ {activity}")
                else:
                    recommendations["seasonal_activities"].append(f"🌟 {activity}")
        
        # Practical tips
        if country_info:
            if country_info.get("best_time"):
                recommendations["practical_tips"].append(f"🗓️ Best time to visit: {country_info['best_time']}")
            if country_info.get("currency"):
                recommendations["practical_tips"].append(f"💰 Currency: {country_info['currency']}")
            if country_info.get("languages"):
                recommendations["practical_tips"].append(f"🗣️ Languages: {', '.join(country_info['languages'])}")
        
        return recommendations
    
    def process_country_query(self, user_query: str) -> Dict[str, Any]:
        """Process country-specific queries"""
        
        # Extract country from query
        country = self.extract_country_from_query(user_query)
        
        if not country:
            # Fallback to general intent detection
            return super().process_user_query(user_query)
        
        # Generate country-specific response
        country_response = self.generate_country_response(country, user_query)
        
        # Detect intent for additional context
        intent, confidence = self.intent_detector.detect_intent(user_query)
        
        return {
            "user_query": user_query,
            "detected_intent": intent,
            "confidence": confidence,
            "country": country,
            "response": country_response,
            "is_country_query": True
        }
    
    def process_user_query(self, user_input: str) -> Dict[str, Any]:
        """Enhanced query processing with country detection"""
        
        # Check if this is a country-specific query
        country = self.extract_country_from_query(user_input)
        
        if country:
            return self.process_country_query(user_input)
        else:
            return super().process_user_query(user_input)
    
    def _display_country_response(self, result: Dict[str, Any]):
        """Display country-specific response"""
        
        if not result.get("is_country_query"):
            super()._display_response(result)
            return
        
        country = result["country"]
        response = result["response"]
        
        print(f"\n🌍 TRAVEL GUIDE FOR {country.upper()} 🌍")
        print("=" * 60)
        
        # Country overview
        if response["country_info"]:
            info = response["country_info"]
            print(f"🏛️ Capital: {info.get('capital', 'N/A')}")
            print(f"🌍 Continent: {info.get('continent', 'N/A')}")
            print(f"💰 Currency: {info.get('currency', 'N/A')}")
            print(f"🗣️ Languages: {', '.join(info.get('languages', ['N/A']))}")
            print(f"🗓️ Best Time: {info.get('best_time', 'N/A')}")
            print(f"🌟 Famous For: {', '.join(info.get('famous_for', ['Various attractions']))}")
        
        # Database attractions
        if response["attractions"]:
            print(f"\n🎯 TOP ATTRACTIONS ({len(response['attractions'])} found):")
            print("-" * 40)
            for i, attr in enumerate(response["attractions"][:8], 1):
                print(f"{i}. 🏛️ {attr['name']} ({attr['type']})")
                print(f"   📍 Location: {attr.get('destination_name', 'N/A')}")
                print(f"   ⭐ Rating: {attr['rating']}")
                print(f"   📝 {attr['description']}")
                print()
        
        # Recommendations
        recommendations = response["recommendations"]
        
        if recommendations["cultural_activities"]:
            print("🏛️ CULTURAL ACTIVITIES:")
            for activity in recommendations["cultural_activities"]:
                print(f"   {activity}")
        
        if recommendations["adventure_activities"]:
            print("\n🏔️ ADVENTURE ACTIVITIES:")
            for activity in recommendations["adventure_activities"]:
                print(f"   {activity}")
        
        if recommendations["food_experiences"]:
            print("\n🍽️ FOOD EXPERIENCES:")
            for activity in recommendations["food_experiences"]:
                print(f"   {activity}")
        
        if recommendations["seasonal_activities"]:
            print("\n🌟 OTHER RECOMMENDED ACTIVITIES:")
            for activity in recommendations["seasonal_activities"]:
                print(f"   {activity}")
        
        if recommendations["practical_tips"]:
            print("\n💡 PRACTICAL TRAVEL TIPS:")
            for tip in recommendations["practical_tips"]:
                print(f"   {tip}")
        
        # Destinations with costs
        if response["destinations"]:
            print(f"\n💰 BUDGET INFORMATION:")
            print("-" * 30)
            for dest in response["destinations"]:
                print(f"📍 {dest['name']}: ${dest['average_cost_per_day']}/day")
                print(f"   🌡️ Best Season: {dest['best_season']}")
    
    def _display_response(self, result: Dict[str, Any]):
        """Enhanced response display"""
        
        if result.get("is_country_query"):
            self._display_country_response(result)
        else:
            super()._display_response(result)
    
    def demo_country_queries(self):
        """Demonstrate country-specific queries"""
        
        print("\n🌍 COUNTRY TRAVEL EXPERT DEMO 🌍")
        print("=" * 50)
        
        sample_queries = [
            "Tell me about attractions in France",
            "What should I do in Japan?",
            "Best things to visit in Italy",
            "I want to travel to Thailand, what do you recommend?",
            "Show me what Egypt has to offer",
            "Australia travel guide",
            "Spain attractions and activities",
            "United States travel recommendations"
        ]
        
        print("Sample queries you can ask:")
        for i, query in enumerate(sample_queries, 1):
            print(f"{i}. {query}")
        
        print("\n🎯 Testing a sample query...")
        
        # Test one query
        test_query = "What are the best attractions in Japan?"
        print(f"\n🔍 Query: '{test_query}'")
        result = self.process_user_query(test_query)
        self._display_response(result)


def main():
    """Main function for world travel expert"""
    
    print("🌍" * 20)
    print("🎯 WORLD TRAVEL EXPERT - ASK ABOUT ANY COUNTRY! 🎯")
    print("🌍" * 20)
    
    expert = WorldTravelExpert()
    
    print("\n✨ I can help you with travel information about ANY country!")
    print("✨ Ask me about attractions, activities, culture, and more!")
    print("\nExamples:")
    print("• 'What are the best attractions in France?'")
    print("• 'Tell me about things to do in Japan'")
    print("• 'I want to visit Italy, what do you recommend?'")
    print("• 'Best activities in Thailand'")
    
    print("\n" + "=" * 60)
    print("Choose an option:")
    print("1️⃣ Start interactive chat")
    print("2️⃣ See demo with sample countries")
    print("3️⃣ Quick test")
    
    choice = input("\nYour choice (1-3): ").strip()
    
    if choice == "1":
        expert.chat_interface()
    elif choice == "2":
        expert.demo_country_queries()
    elif choice == "3":
        # Quick test
        test_query = input("\n🔍 Enter a country query (e.g., 'attractions in France'): ")
        result = expert.process_user_query(test_query)
        expert._display_response(result)
    
    print("\n🌟 Thank you for using World Travel Expert! 🌟")

if __name__ == "__main__":
    main()
