"""
🗃️ Enhanced Database Population Script
Comprehensive script to populate Supabase database with rich travel data
for advanced AI travel platform functionality
"""

import os
import json
import datetime
from typing import List, Dict, Any
from dotenv import load_dotenv
from supabase import create_client, Client
import random

# Load environment
load_dotenv()

# Initialize Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    print("❌ Error: SUPABASE_URL and SUPABASE_KEY must be set in .env file")
    exit(1)

supabase: Client = create_client(supabase_url, supabase_key)

class DatabasePopulator:
    """Comprehensive database population with travel intelligence data"""
    
    def __init__(self):
        self.supabase = supabase
        
    def check_database_status(self):
        """Check current database status and contents"""
        print("🔍 Checking database status...")
        
        tables_to_check = [
            "destinations", "attractions", "hotels", "restaurants", 
            "activities", "cultural_insights", "seasonal_data", 
            "travel_bookings", "user_profiles", "price_tracking"
        ]
        
        status = {}
        for table in tables_to_check:
            try:
                result = self.supabase.table(table).select("*", count="exact").execute()
                count = result.count if hasattr(result, 'count') else len(result.data)
                status[table] = count
                print(f"📊 {table}: {count} records")
            except Exception as e:
                status[table] = f"Error: {str(e)}"
                print(f"❌ {table}: {str(e)}")
        
        return status
    
    def populate_destinations(self):
        """Populate destinations with rich metadata"""
        print("\n🌍 Populating destinations...")
        
        destinations = [
            {
                "name": "Beirut, Lebanon",
                "country": "Lebanon",
                "region": "Middle East",
                "coordinates": {"lat": 33.8938, "lng": 35.5018},
                "timezone": "Asia/Beirut",
                "currency": "USD/LBP",
                "languages": ["Arabic", "English", "French"],
                "best_months": ["Mar", "Apr", "May", "Sep", "Oct", "Nov"],
                "peak_season": ["Jun", "Jul", "Aug"],
                "budget_range": {"low": 50, "mid": 120, "high": 300},
                "cultural_highlights": [
                    "Ancient Phoenician heritage",
                    "French colonial architecture", 
                    "Mediterranean cuisine",
                    "Vibrant nightlife",
                    "Art galleries and museums"
                ],
                "travel_warnings": [],
                "visa_requirements": {"US": "visa_free_90_days", "EU": "visa_free_90_days"},
                "accessibility_rating": 7,
                "family_friendly": True,
                "solo_travel_safe": True,
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Kyoto, Japan",
                "country": "Japan", 
                "region": "East Asia",
                "coordinates": {"lat": 35.0116, "lng": 135.7681},
                "timezone": "Asia/Tokyo",
                "currency": "JPY",
                "languages": ["Japanese", "English"],
                "best_months": ["Mar", "Apr", "May", "Sep", "Oct", "Nov"],
                "peak_season": ["Mar", "Apr", "Oct", "Nov"],
                "budget_range": {"low": 80, "mid": 200, "high": 500},
                "cultural_highlights": [
                    "Ancient temples and shrines",
                    "Traditional geisha districts",
                    "Zen gardens and meditation",
                    "Tea ceremony culture",
                    "Cherry blossom viewing"
                ],
                "travel_warnings": [],
                "visa_requirements": {"US": "visa_free_90_days", "EU": "visa_free_90_days"},
                "accessibility_rating": 9,
                "family_friendly": True,
                "solo_travel_safe": True,
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Paris, France",
                "country": "France",
                "region": "Western Europe", 
                "coordinates": {"lat": 48.8566, "lng": 2.3522},
                "timezone": "Europe/Paris",
                "currency": "EUR",
                "languages": ["French", "English"],
                "best_months": ["Apr", "May", "Jun", "Sep", "Oct"],
                "peak_season": ["Jun", "Jul", "Aug"],
                "budget_range": {"low": 70, "mid": 180, "high": 400},
                "cultural_highlights": [
                    "World-class museums",
                    "Gothic and baroque architecture",
                    "Haute cuisine and wine",
                    "Fashion and art",
                    "Romantic atmosphere"
                ],
                "travel_warnings": [],
                "visa_requirements": {"US": "visa_free_90_days", "non_EU": "schengen_visa"},
                "accessibility_rating": 8,
                "family_friendly": True,
                "solo_travel_safe": True,
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Bali, Indonesia",
                "country": "Indonesia",
                "region": "Southeast Asia",
                "coordinates": {"lat": -8.3405, "lng": 115.0920},
                "timezone": "Asia/Makassar", 
                "currency": "IDR",
                "languages": ["Indonesian", "English", "Balinese"],
                "best_months": ["Apr", "May", "Jun", "Jul", "Aug", "Sep"],
                "peak_season": ["Jul", "Aug", "Dec"],
                "budget_range": {"low": 30, "mid": 80, "high": 250},
                "cultural_highlights": [
                    "Hindu temples and ceremonies",
                    "Rice terrace landscapes",
                    "Traditional art and dance",
                    "Spiritual wellness culture",
                    "Tropical beaches"
                ],
                "travel_warnings": ["volcanic_activity"],
                "visa_requirements": {"US": "visa_on_arrival", "EU": "visa_on_arrival"},
                "accessibility_rating": 6,
                "family_friendly": True,
                "solo_travel_safe": True,
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "New York City, USA",
                "country": "United States",
                "region": "North America",
                "coordinates": {"lat": 40.7128, "lng": -74.0060},
                "timezone": "America/New_York",
                "currency": "USD",
                "languages": ["English", "Spanish"],
                "best_months": ["Apr", "May", "Jun", "Sep", "Oct", "Nov"],
                "peak_season": ["Dec", "Jun", "Jul", "Aug"],
                "budget_range": {"low": 100, "mid": 250, "high": 600},
                "cultural_highlights": [
                    "Broadway shows and theater",
                    "World-class museums",
                    "Diverse neighborhoods", 
                    "Food scene diversity",
                    "Urban architecture"
                ],
                "travel_warnings": [],
                "visa_requirements": {"EU": "ESTA_required", "others": "visa_required"},
                "accessibility_rating": 9,
                "family_friendly": True,
                "solo_travel_safe": True,
                "created_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("destinations").upsert(destinations).execute()
            print(f"✅ Successfully added {len(destinations)} destinations")
            return True
        except Exception as e:
            print(f"❌ Error populating destinations: {e}")
            return False
    
    def populate_attractions(self):
        """Populate attractions with detailed information"""
        print("\n🏛️ Populating attractions...")
        
        attractions = [
            # Beirut attractions
            {
                "name": "Pigeon Rocks (Raouché)",
                "destination": "Beirut, Lebanon",
                "category": "natural_landmark",
                "description": "Iconic natural rock formations off the Beirut coast",
                "coordinates": {"lat": 33.8938, "lng": 35.4780},
                "price_range": "free",
                "duration_hours": 2,
                "best_time": "sunset",
                "crowd_level": "moderate",
                "tourist_trap_score": 3,
                "local_authenticity": 8,
                "cultural_significance": 7,
                "photo_worthiness": 9,
                "accessibility_rating": 6,
                "seasonal_notes": {
                    "spring": "Perfect weather for walking",
                    "summer": "Crowded but beautiful sunsets", 
                    "autumn": "Ideal conditions",
                    "winter": "Can be windy"
                },
                "insider_tips": [
                    "Visit during sunset for best photos",
                    "Walk along the Corniche for multiple viewpoints",
                    "Try nearby seaside cafes"
                ],
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "National Museum of Beirut",
                "destination": "Beirut, Lebanon", 
                "category": "museum",
                "description": "Lebanon's principal museum showcasing archaeological treasures",
                "coordinates": {"lat": 33.8869, "lng": 35.5158},
                "price_range": "budget",
                "duration_hours": 3,
                "best_time": "morning",
                "crowd_level": "low",
                "tourist_trap_score": 1,
                "local_authenticity": 9,
                "cultural_significance": 10,
                "photo_worthiness": 7,
                "accessibility_rating": 8,
                "seasonal_notes": {
                    "year_round": "Indoor attraction, weather independent"
                },
                "insider_tips": [
                    "Start with the basement Phoenician artifacts",
                    "Ask for the audio guide in English",
                    "Allow extra time for the medieval collection"
                ],
                "created_at": datetime.datetime.now().isoformat()
            },
            # Kyoto attractions
            {
                "name": "Fushimi Inari Shrine",
                "destination": "Kyoto, Japan",
                "category": "religious_site",
                "description": "Famous shrine with thousands of vermillion torii gates",
                "coordinates": {"lat": 34.9671, "lng": 135.7727},
                "price_range": "free",
                "duration_hours": 3,
                "best_time": "early_morning",
                "crowd_level": "high",
                "tourist_trap_score": 6,
                "local_authenticity": 8,
                "cultural_significance": 10,
                "photo_worthiness": 10,
                "accessibility_rating": 5,
                "seasonal_notes": {
                    "spring": "Cherry blossoms nearby",
                    "summer": "Very hot, go early",
                    "autumn": "Beautiful fall colors",
                    "winter": "Fewer crowds, peaceful"
                },
                "insider_tips": [
                    "Start hiking at 6 AM to avoid crowds",
                    "Bring water for the mountain hike",
                    "The full hike takes 2-3 hours"
                ],
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Kinkaku-ji (Golden Pavilion)",
                "destination": "Kyoto, Japan",
                "category": "temple",
                "description": "Iconic golden temple reflecting in a peaceful pond",
                "coordinates": {"lat": 35.0394, "lng": 135.7292},
                "price_range": "budget",
                "duration_hours": 2,
                "best_time": "early_morning",
                "crowd_level": "very_high",
                "tourist_trap_score": 8,
                "local_authenticity": 6,
                "cultural_significance": 10,
                "photo_worthiness": 10,
                "accessibility_rating": 7,
                "seasonal_notes": {
                    "spring": "Cherry blossoms frame the temple",
                    "summer": "Lush green gardens",
                    "autumn": "Stunning red maple leaves",
                    "winter": "Snow creates magical atmosphere"
                },
                "insider_tips": [
                    "Arrive right when it opens at 8 AM",
                    "Best photos from the viewing platform",
                    "Combine with nearby Ryoan-ji temple"
                ],
                "created_at": datetime.datetime.now().isoformat()
            },
            # Paris attractions
            {
                "name": "Louvre Museum",
                "destination": "Paris, France",
                "category": "museum",
                "description": "World's largest art museum housing the Mona Lisa",
                "coordinates": {"lat": 48.8606, "lng": 2.3376},
                "price_range": "moderate",
                "duration_hours": 6,
                "best_time": "weekday_morning",
                "crowd_level": "very_high",
                "tourist_trap_score": 7,
                "local_authenticity": 6,
                "cultural_significance": 10,
                "photo_worthiness": 9,
                "accessibility_rating": 9,
                "seasonal_notes": {
                    "year_round": "Indoor attraction, book in advance"
                },
                "insider_tips": [
                    "Book timed entry tickets online",
                    "Use the less crowded Carrousel entrance",
                    "Focus on 2-3 sections per visit"
                ],
                "created_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("attractions").upsert(attractions).execute()
            print(f"✅ Successfully added {len(attractions)} attractions")
            return True
        except Exception as e:
            print(f"❌ Error populating attractions: {e}")
            return False
    
    def populate_cultural_insights(self):
        """Populate cultural insights for enhanced intelligence"""
        print("\n🎭 Populating cultural insights...")
        
        insights = [
            {
                "destination": "Beirut, Lebanon",
                "cultural_category": "social_etiquette",
                "insight_type": "greeting_customs",
                "content": "Lebanese people are very warm and hospitable. Expect multiple kisses on cheeks when greeting friends.",
                "importance_level": 7,
                "traveler_type": "all",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "destination": "Beirut, Lebanon", 
                "cultural_category": "dining_etiquette",
                "insight_type": "food_culture",
                "content": "Meals are social events meant to be shared. Don't refuse food offerings as it can be considered rude.",
                "importance_level": 8,
                "traveler_type": "all",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "destination": "Kyoto, Japan",
                "cultural_category": "temple_etiquette", 
                "insight_type": "religious_respect",
                "content": "Bow before entering temple gates, remove hats, speak quietly, and don't point at Buddha statues.",
                "importance_level": 9,
                "traveler_type": "all",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "destination": "Kyoto, Japan",
                "cultural_category": "social_etiquette",
                "insight_type": "public_behavior",
                "content": "Avoid eating while walking, don't talk loudly on trains, and always bow when greeting people.",
                "importance_level": 8,
                "traveler_type": "all", 
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "destination": "Paris, France",
                "cultural_category": "social_etiquette",
                "insight_type": "greeting_customs",
                "content": "Always say 'Bonjour/Bonsoir' when entering shops and 'Au revoir' when leaving. It's considered rude not to.",
                "importance_level": 7,
                "traveler_type": "all",
                "created_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("cultural_insights").upsert(insights).execute()
            print(f"✅ Successfully added {len(insights)} cultural insights")
            return True
        except Exception as e:
            print(f"❌ Error populating cultural insights: {e}")
            return False
    
    def populate_seasonal_data(self):
        """Populate seasonal intelligence data"""
        print("\n🌤️ Populating seasonal data...")
        
        seasonal_data = [
            {
                "destination": "Beirut, Lebanon",
                "month": "March",
                "temperature_avg": 18,
                "temperature_range": {"min": 13, "max": 23},
                "rainfall_mm": 70,
                "humidity_percent": 65,
                "daylight_hours": 12,
                "crowd_level": "moderate",
                "price_multiplier": 1.0,
                "seasonal_highlights": [
                    "Perfect weather for walking",
                    "Almond blossoms in bloom", 
                    "Outdoor dining season begins"
                ],
                "what_to_pack": ["Light jacket", "Comfortable shoes", "Sunglasses"],
                "local_events": ["Spring festivals", "Outdoor markets resume"],
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "destination": "Kyoto, Japan",
                "month": "April", 
                "temperature_avg": 16,
                "temperature_range": {"min": 9, "max": 23},
                "rainfall_mm": 120,
                "humidity_percent": 60,
                "daylight_hours": 13,
                "crowd_level": "very_high",
                "price_multiplier": 1.8,
                "seasonal_highlights": [
                    "Peak cherry blossom season",
                    "Hanami (flower viewing) parties",
                    "Perfect weather for sightseeing"
                ],
                "what_to_pack": ["Layers", "Rain jacket", "Comfortable walking shoes"],
                "local_events": ["Cherry blossom festivals", "Hanami celebrations"],
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "destination": "Paris, France",
                "month": "September",
                "temperature_avg": 17,
                "temperature_range": {"min": 12, "max": 22},
                "rainfall_mm": 55,
                "humidity_percent": 70,
                "daylight_hours": 12,
                "crowd_level": "moderate",
                "price_multiplier": 1.2,
                "seasonal_highlights": [
                    "Ideal weather for walking",
                    "Autumn colors begin",
                    "Cultural season resumes"
                ],
                "what_to_pack": ["Light sweater", "Comfortable shoes", "Light rain jacket"],
                "local_events": ["Fashion Week", "Cultural exhibitions", "Wine harvest"],
                "created_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("seasonal_data").upsert(seasonal_data).execute()
            print(f"✅ Successfully added {len(seasonal_data)} seasonal records")
            return True
        except Exception as e:
            print(f"❌ Error populating seasonal data: {e}")
            return False
    
    def populate_hotels(self):
        """Populate hotel data with detailed information"""
        print("\n🏨 Populating hotels...")
        
        hotels = [
            {
                "name": "Four Seasons Hotel Beirut",
                "destination": "Beirut, Lebanon",
                "category": "luxury",
                "price_per_night": 280,
                "currency": "USD",
                "rating": 4.8,
                "coordinates": {"lat": 33.8938, "lng": 35.5018},
                "amenities": ["Pool", "Spa", "Gym", "Sea View", "Concierge", "WiFi", "Restaurant"],
                "room_types": ["Standard", "Deluxe Sea View", "Suite", "Presidential Suite"],
                "booking_platforms": {
                    "booking.com": "https://booking.com/fourseasons-beirut",
                    "expedia": "https://expedia.com/fourseasons-beirut",
                    "hotel_direct": "https://fourseasons.com/beirut"
                },
                "customer_reviews": [
                    {"rating": 5, "comment": "Excellent service and beautiful sea views", "date": "2024-06-15"},
                    {"rating": 4, "comment": "Perfect location in downtown Beirut", "date": "2024-05-20"},
                    {"rating": 5, "comment": "Outstanding breakfast buffet", "date": "2024-04-10"}
                ],
                "distance_to_center": 0.5,
                "check_in_time": "15:00",
                "check_out_time": "12:00",
                "cancellation_policy": "free_24h",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Gion Yoshikawa",
                "destination": "Kyoto, Japan",
                "category": "luxury_ryokan",
                "price_per_night": 450,
                "currency": "USD",
                "rating": 4.9,
                "coordinates": {"lat": 35.0042, "lng": 135.7742},
                "amenities": ["Traditional Rooms", "Kaiseki Dining", "Tea Ceremony", "Garden View", "Onsen"],
                "room_types": ["Traditional Tatami", "Deluxe Garden View", "Suite with Private Garden"],
                "booking_platforms": {
                    "booking.com": "https://booking.com/gion-yoshikawa",
                    "ryokan.or.jp": "https://ryokan.or.jp/gion-yoshikawa"
                },
                "customer_reviews": [
                    {"rating": 5, "comment": "Authentic Japanese experience", "date": "2024-05-15"},
                    {"rating": 5, "comment": "Incredible kaiseki dinner", "date": "2024-04-22"},
                    {"rating": 4, "comment": "Beautiful traditional architecture", "date": "2024-03-18"}
                ],
                "distance_to_center": 2.1,
                "check_in_time": "16:00",
                "check_out_time": "10:00", 
                "cancellation_policy": "free_48h",
                "created_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("hotels").upsert(hotels).execute()
            print(f"✅ Successfully added {len(hotels)} hotels")
            return True
        except Exception as e:
            print(f"❌ Error populating hotels: {e}")
            return False
    
    def populate_restaurants(self):
        """Populate restaurant data with reviews and details"""
        print("\n🍽️ Populating restaurants...")
        
        restaurants = [
            {
                "name": "Tawlet",
                "destination": "Beirut, Lebanon",
                "cuisine_type": "Lebanese Traditional",
                "location": "Mar Mikhael", 
                "coordinates": {"lat": 33.9015, "lng": 35.5142},
                "price_range": "$$",
                "rating": 4.7,
                "phone": "+961-1-448129",
                "specialties": ["Meze", "Kibbeh", "Traditional Stews", "Fresh Bread"],
                "dietary_options": ["Vegetarian", "Vegan", "Gluten-Free Available"],
                "atmosphere": "Casual Traditional",
                "customer_reviews": [
                    {"rating": 5, "comment": "Authentic Lebanese home cooking", "date": "2024-06-01"},
                    {"rating": 4, "comment": "Fresh ingredients and traditional recipes", "date": "2024-05-15"},
                    {"rating": 5, "comment": "Great atmosphere and friendly staff", "date": "2024-04-20"}
                ],
                "opening_hours": {
                    "monday": "12:00-22:00",
                    "tuesday": "12:00-22:00", 
                    "wednesday": "12:00-22:00",
                    "thursday": "12:00-22:00",
                    "friday": "12:00-23:00",
                    "saturday": "12:00-23:00",
                    "sunday": "12:00-21:00"
                },
                "booking_required": True,
                "booking_url": "https://tawlet.com/reservations",
                "local_favorite": True,
                "tourist_trap_score": 2,
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Kikunoi",
                "destination": "Kyoto, Japan",
                "cuisine_type": "Kaiseki (Traditional Japanese)",
                "location": "Higashiyama",
                "coordinates": {"lat": 35.0036, "lng": 135.7814},
                "price_range": "$$$$",
                "rating": 4.9,
                "phone": "+81-75-561-0015",
                "specialties": ["Seasonal Kaiseki", "Tea Ceremony", "Traditional Presentation"],
                "dietary_options": ["Vegetarian Kaiseki", "Special Dietary Requests"],
                "atmosphere": "Formal Traditional",
                "customer_reviews": [
                    {"rating": 5, "comment": "Exceptional kaiseki experience", "date": "2024-05-10"},
                    {"rating": 5, "comment": "Art on a plate, incredible presentation", "date": "2024-04-25"},
                    {"rating": 4, "comment": "Expensive but worth every yen", "date": "2024-03-30"}
                ],
                "opening_hours": {
                    "tuesday": "17:00-21:00",
                    "wednesday": "17:00-21:00",
                    "thursday": "17:00-21:00",
                    "friday": "17:00-21:00",
                    "saturday": "17:00-21:00",
                    "sunday": "17:00-21:00",
                    "monday": "closed"
                },
                "booking_required": True,
                "booking_url": "https://kikunoi.jp/reservations",
                "local_favorite": True,
                "tourist_trap_score": 1,
                "michelin_stars": 3,
                "created_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("restaurants").upsert(restaurants).execute()
            print(f"✅ Successfully added {len(restaurants)} restaurants")
            return True
        except Exception as e:
            print(f"❌ Error populating restaurants: {e}")
            return False
    
    def populate_activities(self):
        """Populate activities with intelligence data"""
        print("\n🎯 Populating activities...")
        
        activities = [
            {
                "name": "Lebanese Cooking Class",
                "destination": "Beirut, Lebanon",
                "category": "cultural_experience",
                "description": "Learn to make traditional Lebanese dishes like hummus, tabbouleh, and kibbeh",
                "duration_hours": 4,
                "price_range": "$$",
                "difficulty_level": "beginner",
                "group_size": {"min": 2, "max": 12},
                "what_included": ["Ingredients", "Recipe cards", "Welcome drink", "Full meal"],
                "booking_required": True,
                "advance_booking_days": 2,
                "personality_match": {
                    "adventurous": 8,
                    "cultural": 10,
                    "foodie": 10,
                    "social": 9,
                    "relaxed": 7
                },
                "local_authenticity": 9,
                "tourist_trap_score": 2,
                "best_time": "morning",
                "seasonal_availability": "year_round",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Traditional Tea Ceremony",
                "destination": "Kyoto, Japan",
                "category": "cultural_experience",
                "description": "Authentic Japanese tea ceremony in a traditional tea house",
                "duration_hours": 2,
                "price_range": "$$$",
                "difficulty_level": "beginner",
                "group_size": {"min": 1, "max": 6},
                "what_included": ["Tea ceremony", "Traditional sweets", "Cultural explanation", "Kimono rental optional"],
                "booking_required": True,
                "advance_booking_days": 3,
                "personality_match": {
                    "cultural": 10,
                    "spiritual": 9,
                    "peaceful": 10,
                    "traditional": 10,
                    "mindful": 9
                },
                "local_authenticity": 10,
                "tourist_trap_score": 1,
                "best_time": "afternoon",
                "seasonal_availability": "year_round",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Hidden Alley Food Tour",
                "destination": "Beirut, Lebanon",
                "category": "food_experience",
                "description": "Explore local food spots that tourists rarely find",
                "duration_hours": 3,
                "price_range": "$$",
                "difficulty_level": "easy",
                "group_size": {"min": 4, "max": 8},
                "what_included": ["Local guide", "5 food stops", "Cultural stories", "Take-home recipes"],
                "booking_required": True,
                "advance_booking_days": 1,
                "personality_match": {
                    "adventurous": 9,
                    "foodie": 10,
                    "social": 8,
                    "curious": 9,
                    "authentic": 10
                },
                "local_authenticity": 10,
                "tourist_trap_score": 1,
                "best_time": "evening",
                "seasonal_availability": "year_round",
                "anti_tourist_trap": True,
                "created_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("activities").upsert(activities).execute()
            print(f"✅ Successfully added {len(activities)} activities")
            return True
        except Exception as e:
            print(f"❌ Error populating activities: {e}")
            return False
    
    def create_sample_user_profiles(self):
        """Create sample user profiles for testing"""
        print("\n👤 Creating sample user profiles...")
        
        profiles = [
            {
                "user_id": "demo_user_001",
                "name": "Alex Chen",
                "age": 28,
                "interests": ["culture", "food", "photography"],
                "travel_style": "authentic_explorer",
                "personality_traits": {
                    "adventurous": 8,
                    "cultural": 9,
                    "foodie": 9,
                    "social": 7,
                    "budget_conscious": 6
                },
                "budget_range": "moderate",
                "accessibility_needs": [],
                "dietary_restrictions": ["vegetarian"],
                "language_preferences": ["English", "Spanish"],
                "previous_destinations": ["Barcelona", "Istanbul", "Bangkok"],
                "travel_frequency": "3-4 trips per year",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "user_id": "demo_user_002", 
                "name": "Sarah Johnson",
                "age": 35,
                "interests": ["history", "art", "nature"],
                "travel_style": "cultural_immersion",
                "personality_traits": {
                    "cultural": 10,
                    "peaceful": 8,
                    "educational": 9,
                    "traditional": 7,
                    "mindful": 8
                },
                "budget_range": "luxury",
                "accessibility_needs": [],
                "dietary_restrictions": [],
                "language_preferences": ["English", "French"],
                "previous_destinations": ["Paris", "Rome", "Florence", "Vienna"],
                "travel_frequency": "2-3 trips per year",
                "created_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("user_profiles").upsert(profiles).execute()
            print(f"✅ Successfully added {len(profiles)} user profiles")
            return True
        except Exception as e:
            print(f"❌ Error creating user profiles: {e}")
            return False
    
    def run_full_population(self):
        """Run complete database population"""
        print("🚀 Starting comprehensive database population...")
        print("="*80)
        
        # Check initial status
        self.check_database_status()
        
        # Populate all tables
        operations = [
            ("Destinations", self.populate_destinations),
            ("Attractions", self.populate_attractions),
            ("Cultural Insights", self.populate_cultural_insights),
            ("Seasonal Data", self.populate_seasonal_data),
            ("Hotels", self.populate_hotels),
            ("Restaurants", self.populate_restaurants),
            ("Activities", self.populate_activities),
            ("User Profiles", self.create_sample_user_profiles)
        ]
        
        success_count = 0
        for operation_name, operation_func in operations:
            try:
                if operation_func():
                    success_count += 1
            except Exception as e:
                print(f"❌ Failed {operation_name}: {e}")
        
        print(f"\n🎉 Database population completed!")
        print(f"✅ Successfully completed {success_count}/{len(operations)} operations")
        
        # Final status check
        print("\n📊 Final database status:")
        self.check_database_status()
        
        print("\n🌟 Your AI Travel Platform is now ready with enhanced intelligence!")
        print("🔋 Database is fully populated for advanced features:")
        print("   • Personality-based recommendations")
        print("   • Cultural intelligence and etiquette")
        print("   • Seasonal optimization")
        print("   • Anti-tourist-trap suggestions")
        print("   • Local authenticity scoring")
        print("   • Comprehensive attraction data")

def main():
    """Main execution function"""
    print("🗃️ Enhanced AI Travel Platform - Database Population")
    print("="*80)
    
    populator = DatabasePopulator()
    populator.run_full_population()

if __name__ == "__main__":
    main()
