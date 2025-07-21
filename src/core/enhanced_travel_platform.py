"""
🌍 Enhanced AI Travel Platform - Complete Travel Booking System
Advanced travel platform with integrated booking, recommendations, and personal assistant
"""

import os
import json
import datetime
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from .config import config, get_openai_config, get_supabase_config, get_stripe_config

# Import CrewAI with proper handling
try:
    from crewai import Agent, Task, Crew, tool
except ImportError:
    print("⚠️ CrewAI not found. Please install: pip install crewai")
    # Create mock classes for development
    class Agent: pass
    class Task: pass
    class Crew: pass
    def tool(name=None, description=None):
        def decorator(func): return func
        return decorator

from langchain_community.tools.tavily_search import TavilySearchResults
from supabase import create_client, Client
import requests
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import asyncio
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Remove duplicate environment loading since it's done in config
# load_dotenv()

# Initialize services using centralized config
openai_config = get_openai_config()
supabase_config = get_supabase_config()
stripe_config = get_stripe_config()

# Initialize clients
supabase: Client = create_client(
    supabase_config["url"], 
    supabase_config["key"]
) if supabase_config["url"] and supabase_config["key"] else None

llm = ChatOpenAI(
    model=openai_config["model"], 
    temperature=openai_config["temperature"]
) if openai_config["api_key"] else None

@dataclass
class UserProfile:
    """User profile with preferences and travel history"""
    user_id: str
    age: int
    interests: List[str]
    travel_style: str  # luxury, budget, adventure, cultural, family
    accessibility_needs: List[str]
    budget_range: str
    preferred_airlines: List[str]
    dietary_restrictions: List[str]
    language_preferences: List[str]
    previous_destinations: List[str]
    calendar_integration: bool = False

@dataclass
class FlightOption:
    """Flight booking option"""
    airline: str
    departure_time: str
    arrival_time: str
    duration: str
    price: float
    stops: int
    booking_url: str
    rating: float
    amenities: List[str]

@dataclass
class HotelOption:
    """Hotel booking option"""
    name: str
    location: str
    price_per_night: float
    rating: float
    customer_reviews: List[str]
    amenities: List[str]
    booking_url: str
    photos: List[str]
    distance_to_center: float

@dataclass
class RestaurantOption:
    """Restaurant recommendation"""
    name: str
    cuisine_type: str
    location: str
    rating: float
    price_range: str
    customer_reviews: List[str]
    specialties: List[str]
    booking_url: Optional[str]
    phone: str

@dataclass
class CarRentalOption:
    """Car rental option"""
    company: str
    car_model: str
    price_per_day: float
    features: List[str]
    pickup_location: str
    booking_url: str
    insurance_included: bool

@dataclass
class TravelPackage:
    """Complete travel package"""
    destination: str
    duration: int
    flight: FlightOption
    hotel: HotelOption
    restaurants: List[RestaurantOption]
    car_rental: Optional[CarRentalOption]
    total_price: float
    savings: float
    activities: List[str]
    travel_guide_pdf: str

class PriceTracker:
    """Advanced price tracking and alerts system"""
    
    def __init__(self):
        self.tracked_items = {}
        
    def track_price(self, item_type: str, item_id: str, current_price: float, user_email: str, target_price: float = None):
        """Track price changes for flights, hotels, etc."""
        self.tracked_items[f"{item_type}_{item_id}"] = {
            "type": item_type,
            "id": item_id,
            "current_price": current_price,
            "user_email": user_email,
            "target_price": target_price,
            "price_history": [{"date": datetime.datetime.now().isoformat(), "price": current_price}],
            "alerts_sent": 0
        }
        
    def check_price_changes(self):
        """Check for price changes and send alerts"""
        for item_key, item_data in self.tracked_items.items():
            # Simulate price checking (in real implementation, call actual APIs)
            new_price = self._get_updated_price(item_data["type"], item_data["id"])
            
            if new_price != item_data["current_price"]:
                price_change = new_price - item_data["current_price"]
                self._send_price_alert(item_data, new_price, price_change)
                item_data["current_price"] = new_price
                item_data["price_history"].append({
                    "date": datetime.datetime.now().isoformat(),
                    "price": new_price
                })
    
    def _get_updated_price(self, item_type: str, item_id: str) -> float:
        """Simulate getting updated price from external APIs"""
        # In real implementation, call actual booking APIs
        import random
        base_price = self.tracked_items[f"{item_type}_{item_id}"]["current_price"]
        return base_price * (0.9 + random.random() * 0.2)  # ±10% variation
    
    def _send_price_alert(self, item_data: dict, new_price: float, price_change: float):
        """Send price alert email"""
        try:
            subject = f"🚨 Price Alert: {item_data['type'].title()} Price Changed!"
            change_type = "📉 Decreased" if price_change < 0 else "📈 Increased"
            body = f"""
            Price Alert for your tracked {item_data['type']}:
            
            {change_type} by ${abs(price_change):.2f}
            New Price: ${new_price:.2f}
            Previous Price: ${item_data['current_price']:.2f}
            
            Check now to book at the best price!
            """
            
            self._send_email(item_data["user_email"], subject, body)
            item_data["alerts_sent"] += 1
            
        except Exception as e:
            print(f"Error sending price alert: {e}")
    
    def _send_email(self, to_email: str, subject: str, body: str):
        """Send email notification"""
        if not config.SMTP_PASSWORD:
            print(f"Email alert (no email configured): {subject}")
            return
            
        try:
            msg = MIMEMultipart()
            msg['From'] = "travel.platform@example.com"
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            # Note: Configure with your actual email provider
            print(f"Email sent to {to_email}: {subject}")
        except Exception as e:
            print(f"Email error: {e}")

class CalendarIntegration:
    """Calendar integration for travel planning"""
    
    def __init__(self):
        self.calendar_events = {}
    
    def add_travel_to_calendar(self, user_id: str, travel_package: TravelPackage, start_date: str):
        """Add travel itinerary to user's calendar"""
        events = []
        
        # Flight events
        events.append({
            "title": f"✈️ Flight to {travel_package.destination}",
            "start": travel_package.flight.departure_time,
            "end": travel_package.flight.arrival_time,
            "type": "flight",
            "details": f"Airline: {travel_package.flight.airline}"
        })
        
        # Hotel check-in/out
        check_in = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        check_out = check_in + datetime.timedelta(days=travel_package.duration)
        
        events.append({
            "title": f"🏨 Hotel: {travel_package.hotel.name}",
            "start": check_in.isoformat(),
            "end": check_out.isoformat(),
            "type": "accommodation",
            "details": f"Location: {travel_package.hotel.location}"
        })
        
        # Restaurant reservations
        for i, restaurant in enumerate(travel_package.restaurants):
            dinner_date = check_in + datetime.timedelta(days=i)
            dinner_time = dinner_date.replace(hour=19, minute=0)  # 7 PM
            
            events.append({
                "title": f"🍽️ Dinner at {restaurant.name}",
                "start": dinner_time.isoformat(),
                "end": (dinner_time + datetime.timedelta(hours=2)).isoformat(),
                "type": "dining",
                "details": f"Cuisine: {restaurant.cuisine_type}, Phone: {restaurant.phone}"
            })
        
        self.calendar_events[user_id] = events
        return events
    
    def get_user_calendar(self, user_id: str) -> List[dict]:
        """Get user's travel calendar events"""
        return self.calendar_events.get(user_id, [])
    
    def check_availability(self, user_id: str, start_date: str, end_date: str) -> bool:
        """Check if user is available for travel dates"""
        events = self.get_user_calendar(user_id)
        
        for event in events:
            event_start = datetime.datetime.fromisoformat(event["start"])
            event_end = datetime.datetime.fromisoformat(event["end"])
            travel_start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            travel_end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            
            # Check for conflicts
            if (travel_start <= event_end and travel_end >= event_start):
                return False
        
        return True

class GroupBookingManager:
    """Manage group travel bookings and coordination"""
    
    def __init__(self):
        self.group_bookings = {}
    
    def create_group_booking(self, group_leader_id: str, destination: str, travel_dates: Tuple[str, str], max_participants: int = 10):
        """Create a new group booking"""
        group_id = f"group_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        self.group_bookings[group_id] = {
            "group_id": group_id,
            "leader_id": group_leader_id,
            "destination": destination,
            "travel_dates": travel_dates,
            "max_participants": max_participants,
            "participants": [group_leader_id],
            "status": "open",
            "created_at": datetime.datetime.now().isoformat(),
            "preferences": {},
            "group_discounts": {}
        }
        
        return group_id
    
    def join_group_booking(self, group_id: str, user_id: str) -> bool:
        """Add user to group booking"""
        if group_id not in self.group_bookings:
            return False
        
        group = self.group_bookings[group_id]
        
        if len(group["participants"]) >= group["max_participants"]:
            return False
        
        if user_id not in group["participants"]:
            group["participants"].append(user_id)
        
        return True
    
    def calculate_group_discounts(self, group_id: str, base_package: TravelPackage) -> TravelPackage:
        """Calculate group discounts and return updated package"""
        if group_id not in self.group_bookings:
            return base_package
        
        group = self.group_bookings[group_id]
        participant_count = len(group["participants"])
        
        # Group discount logic
        if participant_count >= 5:
            discount_rate = min(0.15, 0.03 * participant_count)  # Up to 15% discount
        elif participant_count >= 3:
            discount_rate = 0.05  # 5% for smaller groups
        else:
            discount_rate = 0
        
        # Apply discount
        discounted_price = base_package.total_price * (1 - discount_rate)
        additional_savings = base_package.total_price - discounted_price
        
        # Create new package with group pricing
        group_package = TravelPackage(
            destination=base_package.destination,
            duration=base_package.duration,
            flight=base_package.flight,
            hotel=base_package.hotel,
            restaurants=base_package.restaurants,
            car_rental=base_package.car_rental,
            total_price=discounted_price,
            savings=base_package.savings + additional_savings,
            activities=base_package.activities + [f"Group discount: {discount_rate*100:.1f}%"],
            travel_guide_pdf=base_package.travel_guide_pdf
        )
        
        return group_package

class SmartTravelAssistant:
    """AI Personal Travel Assistant with advanced features"""
    
    def __init__(self):
        self.search_tool = self._create_search_tool()
        self.price_tracker = PriceTracker()
        self.calendar_integration = CalendarIntegration()
        
    def _create_search_tool(self):
        @tool
        def search_travel_info(query: str) -> str:
            """Search for travel information including flights, hotels, restaurants"""
            search = TavilySearchResults(api_key=config.TAVILY_API_KEY, max_results=10)
            try:
                results = search.invoke(query)
                return self._format_search_results(results)
            except Exception as e:
                return f"Search error: {str(e)}"
        return search_travel_info
    
    def _format_search_results(self, results):
        """Format search results for travel information"""
        formatted = ""
        for res in results:
            formatted += f"🔍 {res.get('title', 'No Title')}\n"
            formatted += f"📍 {res.get('url', 'No URL')}\n"
            formatted += f"📝 {res.get('content', 'No Content')[:200]}...\n\n"
        return formatted
    
    def create_personalized_itinerary(self, 
                                    destination: str, 
                                    user_profile: UserProfile,
                                    travel_dates: Tuple[str, str],
                                    duration: int) -> TravelPackage:
        """Create a complete personalized travel package"""
        
        print(f"🤖 Creating personalized itinerary for {destination}...")
        
        # Get flight options
        flights = self._search_flights(destination, travel_dates, user_profile)
        
        # Get hotel options
        hotels = self._search_hotels(destination, user_profile, duration)
        
        # Get restaurant recommendations
        restaurants = self._search_restaurants(destination, user_profile)
        
        # Get car rental options
        car_rentals = self._search_car_rentals(destination, user_profile)
        
        # Create optimized packages
        packages = self._create_packages(flights, hotels, restaurants, car_rentals, user_profile)
        
        # Select best package
        best_package = self._select_best_package(packages, user_profile)
        
        # Generate travel guide PDF
        pdf_path = self._generate_travel_guide(best_package, destination, user_profile)
        best_package.travel_guide_pdf = pdf_path
        
        return best_package
    
    def _search_flights(self, destination: str, dates: Tuple[str, str], profile: UserProfile) -> List[FlightOption]:
        """Search for flight options based on user preferences"""
        
        query = f"flights to {destination} from user location {dates[0]} to {dates[1]} {profile.budget_range} budget"
        results = self.search_tool.invoke(query)
        
        # Mock flight data (in real implementation, integrate with flight APIs)
        flights = [
            FlightOption(
                airline="Emirates",
                departure_time="2025-07-01 14:30",
                arrival_time="2025-07-01 23:45",
                duration="9h 15m",
                price=850.0,
                stops=1,
                booking_url="https://emirates.com/booking",
                rating=4.7,
                amenities=["Wi-Fi", "Entertainment", "Meals"]
            ),
            FlightOption(
                airline="Qatar Airways",
                departure_time="2025-07-01 10:15",
                arrival_time="2025-07-01 20:30",
                duration="10h 15m",
                price=920.0,
                stops=1,
                booking_url="https://qatarairways.com/booking",
                rating=4.8,
                amenities=["Wi-Fi", "Premium Entertainment", "Gourmet Meals"]
            )
        ]
        
        # Filter by user preferences
        if profile.preferred_airlines:
            flights = [f for f in flights if f.airline in profile.preferred_airlines]
        
        # Sort by price and rating
        flights.sort(key=lambda x: (x.price, -x.rating))
        
        return flights[:5]  # Return top 5 options
    
    def _search_hotels(self, destination: str, profile: UserProfile, duration: int) -> List[HotelOption]:
        """Search for hotel options with customer feedback"""
        
        query = f"best hotels in {destination} {profile.budget_range} {profile.travel_style} customer reviews"
        results = self.search_tool.invoke(query)
        
        # Mock hotel data (integrate with booking APIs)
        hotels = [
            HotelOption(
                name="Four Seasons Hotel Beirut",
                location="Beirut Central District",
                price_per_night=280.0,
                rating=4.8,
                customer_reviews=[
                    "Excellent service and beautiful sea views",
                    "Perfect location in downtown Beirut",
                    "Outstanding breakfast buffet"
                ],
                amenities=["Pool", "Spa", "Gym", "Sea View", "Concierge"],
                booking_url="https://booking.com/fourseasons",
                photos=["hotel1.jpg", "hotel2.jpg"],
                distance_to_center=0.5
            ),
            HotelOption(
                name="InterContinental Phoenicia Beirut",
                location="Ain Mreisseh",
                price_per_night=220.0,
                rating=4.6,
                customer_reviews=[
                    "Historic hotel with great character",
                    "Excellent location near the sea",
                    "Professional staff and clean rooms"
                ],
                amenities=["Pool", "Business Center", "Restaurant", "Sea View"],
                booking_url="https://booking.com/intercontinental",
                photos=["hotel3.jpg", "hotel4.jpg"],
                distance_to_center=1.2
            )
        ]
        
        # Filter by accessibility needs
        if "wheelchair_accessible" in profile.accessibility_needs:
            hotels = [h for h in hotels if "Accessible" in h.amenities]
        
        return hotels
    
    def _search_restaurants(self, destination: str, profile: UserProfile) -> List[RestaurantOption]:
        """Search for restaurant recommendations with reviews"""
        
        query = f"best restaurants in {destination} {' '.join(profile.interests)} cuisine customer reviews"
        results = self.search_tool.invoke(query)
        
        # Mock restaurant data
        restaurants = [
            RestaurantOption(
                name="Tawlet",
                cuisine_type="Lebanese Traditional",
                location="Mar Mikhael",
                rating=4.7,
                price_range="$$",
                customer_reviews=[
                    "Authentic Lebanese home cooking",
                    "Fresh ingredients and traditional recipes",
                    "Great atmosphere and friendly staff"
                ],
                specialties=["Meze", "Kibbeh", "Traditional Stews"],
                booking_url="https://tawlet.com/reservations",
                phone="+961-1-448129"
            ),
            RestaurantOption(
                name="Em Sherif",
                cuisine_type="Lebanese Fine Dining",
                location="Ashrafieh",
                rating=4.9,
                price_range="$$$$",
                customer_reviews=[
                    "Exceptional Lebanese cuisine",
                    "Beautiful presentation and service",
                    "Must-try for special occasions"
                ],
                specialties=["Gourmet Meze", "Lamb Ouzi", "Traditional Sweets"],
                booking_url="https://emsherif.com/booking",
                phone="+961-1-200043"
            )
        ]
        
        # Filter by dietary restrictions
        if profile.dietary_restrictions:
            # Filter restaurants that can accommodate restrictions
            pass
        
        return restaurants
    
    def _search_car_rentals(self, destination: str, profile: UserProfile) -> List[CarRentalOption]:
        """Search for car rental options"""
        
        rentals = [
            CarRentalOption(
                company="Budget",
                car_model="Toyota Corolla",
                price_per_day=35.0,
                features=["GPS", "AC", "Automatic"],
                pickup_location="Beirut Airport",
                booking_url="https://budget.com/beirut",
                insurance_included=True
            ),
            CarRentalOption(
                company="Hertz",
                car_model="BMW 3 Series",
                price_per_day=85.0,
                features=["GPS", "Premium Audio", "Automatic", "Leather Seats"],
                pickup_location="Downtown Beirut",
                booking_url="https://hertz.com/beirut",
                insurance_included=True
            )
        ]
        
        return rentals
    
    def _create_packages(self, flights: List[FlightOption], 
                        hotels: List[HotelOption], 
                        restaurants: List[RestaurantOption],
                        car_rentals: List[CarRentalOption],
                        profile: UserProfile) -> List[TravelPackage]:
        """Create optimized travel packages"""
        
        packages = []
        
        for flight in flights[:2]:  # Top 2 flights
            for hotel in hotels[:2]:  # Top 2 hotels
                # Calculate package price
                car_rental = car_rentals[0] if car_rentals else None
                
                duration = 7  # Example duration
                total_price = (flight.price * 2 + 
                             hotel.price_per_night * duration + 
                             (car_rental.price_per_day * duration if car_rental else 0))
                
                # Calculate savings (package discount)
                individual_price = total_price * 1.15  # 15% markup for individual booking
                savings = individual_price - total_price
                
                package = TravelPackage(
                    destination="Beirut, Lebanon",
                    duration=duration,
                    flight=flight,
                    hotel=hotel,
                    restaurants=restaurants,
                    car_rental=car_rental,
                    total_price=total_price,
                    savings=savings,
                    activities=self._get_activities_for_profile(profile),
                    travel_guide_pdf=""
                )
                
                packages.append(package)
        
        return packages
    
    def _select_best_package(self, packages: List[TravelPackage], profile: UserProfile) -> TravelPackage:
        """Select the best package based on user preferences"""
        
        def score_package(package: TravelPackage) -> float:
            score = 0
            
            # Price factor (lower is better for budget travelers)
            if profile.budget_range == "budget":
                score += (1000 - package.total_price) / 100
            elif profile.budget_range == "luxury":
                score += package.hotel.rating * 20
            
            # Rating factors
            score += package.flight.rating * 10
            score += package.hotel.rating * 10
            
            # Savings factor
            score += package.savings / 10
            
            return score
        
        packages.sort(key=score_package, reverse=True)
        return packages[0]
    
    def _get_activities_for_profile(self, profile: UserProfile) -> List[str]:
        """Get personalized activities based on user profile"""
        
        activities = []
        
        if "culture" in profile.interests:
            activities.extend([
                "Visit the National Museum of Beirut",
                "Explore the ancient Roman Baths",
                "Walk through the historic Gemmayzeh district"
            ])
        
        if "food" in profile.interests:
            activities.extend([
                "Take a Lebanese cooking class",
                "Food tour in Souk el Gharb",
                "Visit traditional markets"
            ])
        
        if "nature" in profile.interests:
            activities.extend([
                "Day trip to Jeita Grotto",
                "Hiking in the Chouf Mountains",
                "Visit Baatara Gorge Waterfall"
            ])
        
        return activities
    
    def _generate_travel_guide(self, package: TravelPackage, destination: str, profile: UserProfile) -> str:
        """Generate a comprehensive PDF travel guide"""
        
        filename = f"travel_guide_{destination.replace(' ', '_')}_{datetime.datetime.now().strftime('%Y%m%d')}.pdf"
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()
        content = []
        
        # Title
        title = Paragraph(f"Complete Travel Guide: {destination}", styles['Title'])
        content.append(title)
        content.append(Spacer(1, 12))
        
        # Package summary
        summary = f"""
        <b>Your Travel Package Summary:</b><br/>
        Destination: {package.destination}<br/>
        Duration: {package.duration} days<br/>
        Total Cost: ${package.total_price:.2f}<br/>
        Savings: ${package.savings:.2f}<br/>
        """
        content.append(Paragraph(summary, styles['Normal']))
        content.append(Spacer(1, 12))
        
        # Activities and recommendations
        activities_text = "<b>Recommended Activities:</b><br/>"
        for activity in package.activities:
            activities_text += f"• {activity}<br/>"
        
        content.append(Paragraph(activities_text, styles['Normal']))
        
        # Build PDF
        doc.build(content)
        
        return filename

class TravelPlatformUI:
    """Main travel platform interface"""
    
    def __init__(self):
        self.assistant = SmartTravelAssistant()
        self.price_tracker = PriceTracker()
        self.calendar_integration = CalendarIntegration()
        self.group_booking = GroupBookingManager()
        
    def main_menu(self):
        """Display main platform menu"""
        
        print("\n" + "="*80)
        print("🌍 ✈️  ENHANCED AI TRAVEL PLATFORM  🏨 🍽️")
        print("="*80)
        print("🎯 Complete Travel Solutions with AI Personal Assistant")
        print("-"*80)
        print("1. 🗺️  Create Complete Travel Package (Flight + Hotel + Car + Guide)")
        print("2. 📊 Track Price Trends & Get Notifications")
        print("3. 📅 Calendar Integration & Date Suggestions")
        print("4. 👥 Smart Group Booking")
        print("5. 🤖 AI Personal Travel Assistant Chat")
        print("6. 📱 User Profile Management")
        print("7. 📈 Travel Analytics & Insights")
        print("8. 🔍 Hidden Gems & Local Experiences")
        print("9. 📰 Latest Travel News & Updates")
        print("10. 🚪 Exit")
        print("="*80)
    
    def create_travel_package_flow(self):
        """Complete travel package creation flow"""
        
        print("\n🌟 CREATE YOUR COMPLETE TRAVEL PACKAGE")
        print("="*60)
        
        # Get user input
        destination = input("🎯 Enter destination (e.g., Beirut, Lebanon): ").strip()
        
        print("\n📅 Select travel dates:")
        start_date = input("Start date (YYYY-MM-DD): ").strip()
        end_date = input("End date (YYYY-MM-DD): ").strip()
        
        # Calculate duration
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        duration = (end - start).days
        
        # Create user profile (simplified)
        user_profile = UserProfile(
            user_id="user_001",
            age=30,
            interests=["culture", "food", "nature"],
            travel_style="moderate",
            accessibility_needs=[],
            budget_range="moderate",
            preferred_airlines=[],
            dietary_restrictions=[],
            language_preferences=["English"],
            previous_destinations=[]
        )
        
        print("\n🤖 AI is creating your personalized travel package...")
        print("⏳ Searching flights, hotels, restaurants, and activities...")
        
        # Create package
        package = self.assistant.create_personalized_itinerary(
            destination, user_profile, (start_date, end_date), duration
        )
        
        # Display package
        self._display_travel_package(package)
        
        # Booking confirmation
        if input("\n💳 Proceed to booking? (y/n): ").lower() == 'y':
            self._process_booking(package)
    
    def _display_travel_package(self, package: TravelPackage):
        """Display travel package details"""
        
        print("\n" + "🎉"*20)
        print("✈️ YOUR PERSONALIZED TRAVEL PACKAGE")
        print("🎉"*20)
        
        print(f"\n📍 Destination: {package.destination}")
        print(f"⏰ Duration: {package.duration} days")
        print(f"💰 Total Price: ${package.total_price:.2f}")
        print(f"💵 You Save: ${package.savings:.2f}")
        
        print(f"\n✈️ FLIGHT DETAILS:")
        print(f"   Airline: {package.flight.airline}")
        print(f"   Departure: {package.flight.departure_time}")
        print(f"   Duration: {package.flight.duration}")
        print(f"   Price: ${package.flight.price}")
        print(f"   Rating: ⭐ {package.flight.rating}/5")
        
        print(f"\n🏨 HOTEL DETAILS:")
        print(f"   Name: {package.hotel.name}")
        print(f"   Location: {package.hotel.location}")
        print(f"   Price/night: ${package.hotel.price_per_night}")
        print(f"   Rating: ⭐ {package.hotel.rating}/5")
        print(f"   Reviews: {package.hotel.customer_reviews[0]}")
        
        print(f"\n🍽️ RECOMMENDED RESTAURANTS:")
        for restaurant in package.restaurants:
            print(f"   • {restaurant.name} ({restaurant.cuisine_type})")
            print(f"     Rating: ⭐ {restaurant.rating}/5 | {restaurant.price_range}")
        
        if package.car_rental:
            print(f"\n🚗 CAR RENTAL:")
            print(f"   Company: {package.car_rental.company}")
            print(f"   Model: {package.car_rental.car_model}")
            print(f"   Price/day: ${package.car_rental.price_per_day}")
        
        print(f"\n🎯 RECOMMENDED ACTIVITIES:")
        for activity in package.activities:
            print(f"   • {activity}")
        
        print(f"\n📄 Travel Guide: {package.travel_guide_pdf}")
    
    def _process_booking(self, package: TravelPackage):
        """Process the booking payment"""
        
        print("\n💳 BOOKING CONFIRMATION")
        print("="*40)
        
        print("📋 Booking Summary:")
        print(f"   Total Amount: ${package.total_price:.2f}")
        print(f"   Savings: ${package.savings:.2f}")
        
        # Mock payment process
        print("\n💳 Payment Information:")
        card_number = input("Card Number: ")
        expiry = input("Expiry (MM/YY): ")
        cvv = input("CVV: ")
        name = input("Cardholder Name: ")
        
        print("\n⏳ Processing payment...")
        print("✅ Payment successful!")
        print("📧 Confirmation emails sent!")
        print("📱 Booking details saved to your account!")
        print(f"📄 Travel guide saved: {package.travel_guide_pdf}")
        
        # Save booking to database
        self._save_booking_to_database(package)
    
    def _save_booking_to_database(self, package: TravelPackage):
        """Save booking to Supabase database"""
        try:
            booking_data = {
                "destination": package.destination,
                "duration": package.duration,
                "total_price": package.total_price,
                "savings": package.savings,
                "flight_details": asdict(package.flight),
                "hotel_details": asdict(package.hotel),
                "booking_date": datetime.datetime.now().isoformat(),
                "status": "confirmed"
            }
            
            supabase.table("travel_bookings").insert(booking_data).execute()
            print("✅ Booking saved to database!")
            
        except Exception as e:
            print(f"⚠️ Error saving booking: {e}")

def main():
    """Main application entry point"""
    
    platform = TravelPlatformUI()
    
    print("🌍 Welcome to the Enhanced AI Travel Platform!")
    print("🤖 Your Personal AI Travel Assistant is ready!")
    
    while True:
        platform.main_menu()
        choice = input("\n🎯 Select an option (1-10): ").strip()
        
        if choice == '1':
            platform.create_travel_package_flow()
        elif choice == '2':
            print("📊 Price tracking features coming soon!")
        elif choice == '3':
            print("📅 Calendar integration features coming soon!")
        elif choice == '4':
            print("👥 Group booking features coming soon!")
        elif choice == '5':
            print("🤖 AI Chat features coming soon!")
        elif choice == '6':
            print("📱 Profile management coming soon!")
        elif choice == '7':
            print("📈 Analytics features coming soon!")
        elif choice == '8':
            print("🔍 Hidden gems features coming soon!")
        elif choice == '9':
            print("📰 Travel news features coming soon!")
        elif choice == '10':
            print("\n👋 Thank you for using Enhanced AI Travel Platform!")
            print("🌍 Safe travels! ✈️")
            break
        else:
            print("❌ Invalid option. Please select 1-10.")
        
        input("\n🔄 Press Enter to continue...")

if __name__ == "__main__":
    main()
