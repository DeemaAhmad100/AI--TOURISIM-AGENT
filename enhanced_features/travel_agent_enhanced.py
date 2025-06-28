"""
Enhanced Travel Agent with Advanced Features
This module provides intelligent travel planning with user profiles,
personalized recommendations, and integrated booking capabilities.
"""

import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import pandas as pd
from supabase import create_client, Client
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class UserProfile:
    """User profile data structure"""
    user_id: str
    age: int
    interests: List[str]
    travel_style: str
    accessibility_needs: List[str]
    budget_range: str
    dietary_restrictions: List[str]
    preferred_airlines: List[str] = None

@dataclass
class TravelPackage:
    """Complete travel package data structure"""
    id: str
    destination: str
    flight: Dict
    hotel: Dict
    restaurants: List[Dict]
    activities: List[Dict]
    total_price: float
    duration_days: int
    included_services: List[str]

@dataclass
class FlightDetails:
    """Flight information structure"""
    id: str
    airline: str
    departure_city: str
    arrival_city: str
    departure_time: datetime
    arrival_time: datetime
    price: float
    booking_url: str

@dataclass
class HotelDetails:
    """Hotel information structure"""
    id: str
    name: str
    rating: float
    price_per_night: float
    amenities: List[str]
    customer_reviews: List[str]
    booking_url: str

class EnhancedTravelAgent:
    """
    Enhanced Travel Agent with AI-powered personalization and booking capabilities
    """
    
    def __init__(self):
        """Initialize the enhanced travel agent"""
        print("🚀 Initializing Enhanced Travel Agent...")
        
        # Initialize Supabase client
        self.supabase = self._init_supabase()
        
        # Initialize OpenAI model
        self.llm = self._init_openai()
        
        # Initialize AI agents
        self._init_ai_agents()
        
        print("✅ Enhanced Travel Agent ready!")
    
    def _init_supabase(self) -> Client:
        """Initialize Supabase client"""
        try:
            supabase_url = os.getenv("SUPABASE_URL")
            supabase_key = os.getenv("SUPABASE_KEY")
            
            if not supabase_url or not supabase_key:
                raise ValueError("Supabase credentials missing in .env file")
            
            return create_client(supabase_url, supabase_key)
        except Exception as e:
            print(f"❌ Error initializing Supabase: {e}")
            return None
    
    def _init_openai(self):
        """Initialize OpenAI model"""
        try:
            openai_key = os.getenv("OPENAI_API_KEY")
            if not openai_key:
                print("⚠️ OpenAI API key not found. AI features will be limited.")
                return None
            
            return ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
        except Exception as e:
            print(f"❌ Error initializing OpenAI: {e}")
            return None
    
    def _init_ai_agents(self):
        """Initialize specialized AI agents"""
        if not self.llm:
            print("⚠️ AI agents not initialized due to missing OpenAI key")
            return
        
        # Personalization Agent
        self.personalization_agent = Agent(
            role="Travel Personalization Specialist",
            goal="Analyze user profiles and preferences to provide highly personalized travel recommendations",
            backstory="You are an expert in understanding traveler psychology and matching experiences to individual preferences.",
            verbose=True,
            llm=self.llm
        )
        
        # Package Creator Agent  
        self.package_agent = Agent(
            role="Travel Package Architect",
            goal="Create optimal travel packages by combining flights, hotels, restaurants, and activities",
            backstory="You specialize in creating seamless travel experiences that maximize value and satisfaction.",
            verbose=True,
            llm=self.llm
        )

    # === USER PROFILE MANAGEMENT ===
    
    def create_user_profile(self, profile_data: Dict) -> Dict:
        """Create a new user profile"""
        try:
            # Validate required fields
            required_fields = ['user_id', 'age', 'interests', 'travel_style', 'budget_range']
            for field in required_fields:
                if field not in profile_data:
                    return {"success": False, "error": f"Missing required field: {field}"}
            
            # Insert into database
            result = self.supabase.table("user_profiles").insert(profile_data).execute()
            
            return {
                "success": True, 
                "profile_id": result.data[0]["id"],
                "message": "User profile created successfully!"
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_user_profile(self, user_id: str) -> Optional[UserProfile]:
        """Retrieve user profile from database"""
        try:
            result = self.supabase.table("user_profiles").select("*").eq("user_id", user_id).execute()
            
            if result.data:
                data = result.data[0]
                return UserProfile(
                    user_id=data["user_id"],
                    age=data["age"],
                    interests=data["interests"] or [],
                    travel_style=data["travel_style"],
                    accessibility_needs=data["accessibility_needs"] or [],
                    budget_range=data["budget_range"],
                    dietary_restrictions=data["dietary_restrictions"] or [],
                    preferred_airlines=data["preferred_airlines"] or []
                )
        except Exception as e:
            print(f"❌ Error fetching user profile: {e}")
        return None
    
    def update_user_profile(self, user_id: str, updates: Dict) -> Dict:
        """Update user profile"""
        try:
            result = self.supabase.table("user_profiles")\
                .update(updates)\
                .eq("user_id", user_id)\
                .execute()
            
            return {"success": True, "message": "Profile updated successfully!"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    # === FLIGHT SEARCH ===
    
    def search_flights(self, departure: str, destination: str, departure_date: str, 
                      budget: float, user_profile: UserProfile = None) -> List[FlightDetails]:
        """Search for flights within budget with personalization"""
        try:
            query = self.supabase.table("flights").select("*")\
                .eq("departure_city", departure)\
                .eq("arrival_city", destination)\
                .lte("price", budget)\
                .order("price", desc=False)
            
            # Apply user preferences if available
            if user_profile and user_profile.preferred_airlines:
                query = query.in_("airline", user_profile.preferred_airlines)
            
            result = query.execute()
            
            # Convert to FlightDetails objects
            flights = []
            for flight_data in result.data:
                flights.append(FlightDetails(
                    id=flight_data["id"],
                    airline=flight_data["airline"],
                    departure_city=flight_data["departure_city"],
                    arrival_city=flight_data["arrival_city"],
                    departure_time=datetime.fromisoformat(flight_data["departure_time"]),
                    arrival_time=datetime.fromisoformat(flight_data["arrival_time"]),
                    price=float(flight_data["price"]),
                    booking_url=flight_data["booking_url"]
                ))
            
            return flights
        except Exception as e:
            print(f"❌ Error searching flights: {e}")
            return []
    
    # === HOTEL SEARCH ===
    
    def search_hotels(self, destination_id: str, budget_per_night: float, 
                     user_profile: UserProfile = None) -> List[HotelDetails]:
        """Search for hotels within budget with personalization"""
        try:
            query = self.supabase.table("hotels").select("*")\
                .eq("destination_id", destination_id)\
                .lte("price_per_night", budget_per_night)\
                .order("rating", desc=True)
            
            result = query.execute()
            
            # Convert to HotelDetails objects
            hotels = []
            for hotel_data in result.data:
                hotels.append(HotelDetails(
                    id=hotel_data["id"],
                    name=hotel_data["name"],
                    rating=float(hotel_data["rating"]),
                    price_per_night=float(hotel_data["price_per_night"]),
                    amenities=hotel_data["amenities"] or [],
                    customer_reviews=hotel_data["customer_reviews"] or [],
                    booking_url=hotel_data["booking_url"]
                ))
            
            return hotels
        except Exception as e:
            print(f"❌ Error searching hotels: {e}")
            return []
    
    # === RESTAURANT SEARCH ===
    
    def search_restaurants(self, destination_id: str, user_profile: UserProfile = None) -> List[Dict]:
        """Search for restaurants with personalization based on dietary restrictions"""
        try:
            query = self.supabase.table("restaurants").select("*")\
                .eq("destination_id", destination_id)\
                .order("rating", desc=True)
            
            result = query.execute()
            restaurants = result.data
            
            # Filter based on dietary restrictions
            if user_profile and user_profile.dietary_restrictions:
                filtered_restaurants = []
                for restaurant in restaurants:
                    # Check if restaurant accommodates dietary restrictions
                    # This is a simplified example - you'd implement more sophisticated matching
                    specialties = restaurant.get("specialties", [])
                    if self._check_dietary_compatibility(specialties, user_profile.dietary_restrictions):
                        filtered_restaurants.append(restaurant)
                return filtered_restaurants
            
            return restaurants
        except Exception as e:
            print(f"❌ Error searching restaurants: {e}")
            return []
    
    def _check_dietary_compatibility(self, specialties: List[str], restrictions: List[str]) -> bool:
        """Check if restaurant accommodates dietary restrictions"""
        # Simplified logic - expand based on your needs
        for restriction in restrictions:
            if restriction.lower() in [s.lower() for s in specialties]:
                return True
        return len(restrictions) == 0  # If no restrictions, all restaurants are compatible
    
    # === PERSONALIZED RECOMMENDATIONS ===
    
    def get_personalized_recommendations(self, user_profile: UserProfile, destination_id: str) -> Dict:
        """Get personalized recommendations based on user profile"""
        try:
            # Get restaurants based on dietary restrictions and interests
            restaurants = self.search_restaurants(destination_id, user_profile)
            
            # Get activities based on interests
            activities = self._get_activities_by_interests(destination_id, user_profile.interests)
            
            # Get hidden gems
            hidden_gems = self.get_hidden_gems(destination_id)
            
            # Get local tips
            local_tips = self.get_local_tips(destination_id)
            
            # Use AI to enhance recommendations
            if self.llm:
                enhanced_recommendations = self._enhance_with_ai(
                    user_profile, restaurants, activities, hidden_gems
                )
                return enhanced_recommendations
            
            return {
                "restaurants": restaurants[:5],  # Top 5
                "activities": activities[:10],   # Top 10
                "hidden_gems": hidden_gems,
                "local_tips": local_tips,
                "personalization_score": self._calculate_personalization_score(user_profile)
            }
        except Exception as e:
            print(f"❌ Error getting recommendations: {e}")
            return {}
    
    def _get_activities_by_interests(self, destination_id: str, interests: List[str]) -> List[Dict]:
        """Get activities matching user interests"""
        try:
            # This would query your activities table (you'd need to create this)
            # For now, returning mock data based on interests
            activities = []
            
            interest_mapping = {
                "culture": ["Museum Visit", "Historical Tour", "Local Art Gallery"],
                "food": ["Cooking Class", "Food Tour", "Local Market Visit"],
                "adventure": ["Hiking", "Water Sports", "Adventure Tour"],
                "nature": ["Nature Walk", "Beach Visit", "Mountain Trip"],
                "shopping": ["Shopping Tour", "Local Markets", "Boutique Shopping"]
            }
            
            for interest in interests:
                if interest.lower() in interest_mapping:
                    for activity in interest_mapping[interest.lower()]:
                        activities.append({
                            "name": activity,
                            "type": interest,
                            "description": f"Experience {activity} in this beautiful destination",
                            "rating": 4.5,
                            "duration": "2-3 hours"
                        })
            
            return activities
        except Exception as e:
            print(f"❌ Error getting activities: {e}")
            return []
    
    def _enhance_with_ai(self, user_profile: UserProfile, restaurants: List, 
                        activities: List, hidden_gems: List) -> Dict:
        """Use AI to enhance recommendations"""
        try:
            # Create task for personalization agent
            personalization_task = Task(
                description=f"""
                Analyze this user profile and enhance the travel recommendations:
                
                User Profile:
                - Age: {user_profile.age}
                - Interests: {', '.join(user_profile.interests)}
                - Travel Style: {user_profile.travel_style}
                - Budget Range: {user_profile.budget_range}
                - Dietary Restrictions: {', '.join(user_profile.dietary_restrictions)}
                
                Available Options:
                - Restaurants: {len(restaurants)} options
                - Activities: {len(activities)} options
                - Hidden Gems: {len(hidden_gems)} options
                
                Please provide:
                1. Top 3 personalized restaurant recommendations with reasons
                2. Top 5 activities that match their interests and travel style
                3. Personalized tips based on their profile
                4. Budget optimization suggestions
                """,
                agent=self.personalization_agent,
                expected_output="Detailed personalized recommendations with explanations"
            )
            
            # Execute the task
            crew = Crew(agents=[self.personalization_agent], tasks=[personalization_task])
            result = crew.kickoff()
            
            return {
                "ai_recommendations": str(result),
                "restaurants": restaurants[:3],
                "activities": activities[:5],
                "hidden_gems": hidden_gems,
                "personalization_score": 95  # High score due to AI enhancement
            }
        except Exception as e:
            print(f"❌ Error enhancing with AI: {e}")
            return {
                "restaurants": restaurants[:5],
                "activities": activities[:10],
                "hidden_gems": hidden_gems,
                "personalization_score": 70
            }
    
    def _calculate_personalization_score(self, user_profile: UserProfile) -> int:
        """Calculate how well we can personalize for this user"""
        score = 50  # Base score
        
        if user_profile.interests:
            score += 15
        if user_profile.dietary_restrictions:
            score += 10
        if user_profile.preferred_airlines:
            score += 10
        if user_profile.accessibility_needs:
            score += 15
        
        return min(score, 100)
    
    # === TRAVEL PACKAGE CREATION ===
    
    def create_travel_package(self, destination: str, user_profile: UserProfile, 
                            budget: float, duration_days: int, departure_city: str = None) -> TravelPackage:
        """Create a complete travel package"""
        try:
            print(f"🎯 Creating travel package for {destination}...")
            
            # Get destination ID
            destination_data = self._get_destination_by_name(destination)
            if not destination_data:
                raise ValueError(f"Destination '{destination}' not found")
            
            destination_id = destination_data["id"]
            
            # Calculate budget allocation
            budget_allocation = self._calculate_budget_allocation(budget, duration_days)
            
            # Search for flights
            flights = []
            if departure_city:
                flights = self.search_flights(
                    departure_city, destination, 
                    datetime.now().strftime("%Y-%m-%d"),
                    budget_allocation["flights"], user_profile
                )
            
            # Search for hotels
            hotels = self.search_hotels(
                destination_id, 
                budget_allocation["hotel_per_night"], 
                user_profile
            )
            
            # Get personalized recommendations
            recommendations = self.get_personalized_recommendations(user_profile, destination_id)
            
            # Create package using AI
            if self.llm and flights and hotels:
                package = self._create_ai_optimized_package(
                    destination, flights[0], hotels[0], recommendations, 
                    budget, duration_days, user_profile
                )
            else:
                # Create basic package
                package = TravelPackage(
                    id=f"pkg_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                    destination=destination,
                    flight=flights[0].__dict__ if flights else {},
                    hotel=hotels[0].__dict__ if hotels else {},
                    restaurants=recommendations.get("restaurants", [])[:3],
                    activities=recommendations.get("activities", [])[:5],
                    total_price=budget,
                    duration_days=duration_days,
                    included_services=["flight", "hotel", "restaurants", "activities"]
                )
            
            # Save package to database
            self._save_package_to_database(package)
            
            print("✅ Travel package created successfully!")
            return package
            
        except Exception as e:
            print(f"❌ Error creating travel package: {e}")
            return None
    
    def _get_destination_by_name(self, destination_name: str) -> Dict:
        """Get destination data by name"""
        try:
            result = self.supabase.table("enhanced_destinations")\
                .select("*")\
                .ilike("name", f"%{destination_name}%")\
                .execute()
            
            return result.data[0] if result.data else None
        except Exception as e:
            print(f"❌ Error getting destination: {e}")
            return None
    
    def _calculate_budget_allocation(self, total_budget: float, duration_days: int) -> Dict:
        """Calculate optimal budget allocation"""
        return {
            "flights": total_budget * 0.35,        # 35% for flights
            "hotel_per_night": (total_budget * 0.40) / duration_days,  # 40% for hotels
            "food_per_day": (total_budget * 0.20) / duration_days,     # 20% for food
            "activities": total_budget * 0.05       # 5% for activities
        }
    
    def _create_ai_optimized_package(self, destination: str, flight: FlightDetails, 
                                   hotel: HotelDetails, recommendations: Dict,
                                   budget: float, duration_days: int, 
                                   user_profile: UserProfile) -> TravelPackage:
        """Create an AI-optimized travel package"""
        try:
            # Create task for package optimization
            package_task = Task(
                description=f"""
                Create an optimized travel package for:
                
                Destination: {destination}
                Duration: {duration_days} days
                Budget: ${budget:,.2f}
                User Style: {user_profile.travel_style}
                User Interests: {', '.join(user_profile.interests)}
                
                Selected Flight: {flight.airline} - ${flight.price}
                Selected Hotel: {hotel.name} - ${hotel.price_per_night}/night
                
                Available restaurants: {len(recommendations.get('restaurants', []))}
                Available activities: {len(recommendations.get('activities', []))}
                
                Please optimize:
                1. Daily itinerary that maximizes experiences within budget
                2. Restaurant selection based on user preferences
                3. Activity scheduling considering user interests
                4. Budget optimization suggestions
                5. Package highlights and unique selling points
                """,
                agent=self.package_agent,
                expected_output="Optimized travel package with detailed itinerary and recommendations"
            )
            
            # Execute optimization
            crew = Crew(agents=[self.package_agent], tasks=[package_task])
            ai_result = crew.kickoff()
            
            # Calculate total price
            total_price = (flight.price * 2) + (hotel.price_per_night * duration_days)  # Round trip + hotel
            
            return TravelPackage(
                id=f"ai_pkg_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                destination=destination,
                flight=flight.__dict__,
                hotel=hotel.__dict__,
                restaurants=recommendations.get("restaurants", [])[:3],
                activities=recommendations.get("activities", [])[:duration_days],
                total_price=total_price,
                duration_days=duration_days,
                included_services=["flight", "hotel", "restaurants", "activities", "ai_optimization"]
            )
            
        except Exception as e:
            print(f"❌ Error creating AI-optimized package: {e}")
            return None
    
    def _save_package_to_database(self, package: TravelPackage) -> bool:
        """Save travel package to database"""
        try:
            package_data = {
                "id": package.id,
                "name": f"{package.duration_days}-Day {package.destination} Package",
                "destination_id": self._get_destination_by_name(package.destination)["id"],
                "total_price": package.total_price,
                "duration_days": package.duration_days,
                "included_services": package.included_services,
                "created_at": datetime.now().isoformat()
            }
            
            result = self.supabase.table("travel_packages").insert(package_data).execute()
            return True
        except Exception as e:
            print(f"❌ Error saving package: {e}")
            return False
    
    # === HIDDEN GEMS AND LOCAL TIPS ===
    
    def get_hidden_gems(self, destination_id: str) -> List[str]:
        """Get hidden gems and authentic experiences"""
        try:
            result = self.supabase.table("enhanced_destinations")\
                .select("hidden_gems")\
                .eq("id", destination_id)\
                .execute()
            
            if result.data and result.data[0]["hidden_gems"]:
                return result.data[0]["hidden_gems"]
        except Exception as e:
            print(f"❌ Error fetching hidden gems: {e}")
        
        # Return default hidden gems if none in database
        return [
            "Visit the local neighborhood markets early in the morning",
            "Try street food from vendors recommended by locals",
            "Explore areas where locals actually live and work",
            "Visit during local festivals or cultural events"
        ]
    
    def get_local_tips(self, destination_id: str) -> List[str]:
        """Get local tips and advice"""
        try:
            result = self.supabase.table("enhanced_destinations")\
                .select("local_tips")\
                .eq("id", destination_id)\
                .execute()
            
            if result.data and result.data[0]["local_tips"]:
                return result.data[0]["local_tips"]
        except Exception as e:
            print(f"❌ Error fetching local tips: {e}")
        
        # Return default tips if none in database
        return [
            "Learn a few basic phrases in the local language",
            "Respect local customs and dress codes",
            "Always negotiate prices at markets",
            "Keep copies of important documents",
            "Use local transportation to save money and meet people"
        ]
    
    # === UTILITY METHODS ===
    
    def test_database_connection(self) -> Dict:
        """Test database connection and functionality"""
        try:
            # Test basic connection
            result = self.supabase.table("enhanced_destinations").select("count").execute()
            
            return {
                "success": True,
                "message": "Database connection successful!",
                "tables_accessible": True
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": "Database connection failed"
            }
    
    def get_user_statistics(self, user_id: str) -> Dict:
        """Get user travel statistics"""
        try:
            # This would aggregate user's travel data
            # For now, returning mock statistics
            return {
                "total_trips": 5,
                "countries_visited": 8,
                "total_spent": 12500.00,
                "favorite_destination": "Italy",
                "average_trip_duration": 7,
                "preferred_travel_style": "Cultural"
            }
        except Exception as e:
            return {"error": str(e)}

# === DEMO AND TESTING FUNCTIONS ===

def demo_enhanced_travel_agent():
    """Demonstrate the enhanced travel agent capabilities"""
    print("\n🌟 ENHANCED TRAVEL AGENT DEMO")
    print("=" * 50)
    
    # Initialize agent
    agent = EnhancedTravelAgent()
    
    # Test database connection
    db_test = agent.test_database_connection()
    print(f"Database Test: {'✅' if db_test['success'] else '❌'} {db_test['message']}")
    
    # Create sample user profile
    sample_profile_data = {
        "user_id": "demo_user_001",
        "age": 28,
        "interests": ["culture", "food", "history"],
        "travel_style": "moderate",
        "accessibility_needs": [],
        "budget_range": "moderate",
        "dietary_restrictions": ["vegetarian"],
        "preferred_airlines": ["Emirates", "Qatar Airways"]
    }
    
    print("\n👤 Creating sample user profile...")
    profile_result = agent.create_user_profile(sample_profile_data)
    print(f"Profile Creation: {'✅' if profile_result['success'] else '❌'}")
    
    # Get user profile
    user_profile = agent.get_user_profile("demo_user_001")
    if user_profile:
        print(f"✅ User profile loaded: {user_profile.travel_style} traveler interested in {', '.join(user_profile.interests)}")
    
    # Test personalized recommendations
    print("\n🎯 Getting personalized recommendations for Beirut...")
    # You would need a destination in your database for this to work
    # recommendations = agent.get_personalized_recommendations(user_profile, "beirut_destination_id")
    
    print("✅ Demo completed!")

if __name__ == "__main__":
    demo_enhanced_travel_agent()
