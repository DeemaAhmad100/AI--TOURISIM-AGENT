"""
🗃️ Simple Database Population Script
Basic script to populate existing Supabase tables with essential travel data
"""

import os
import json
import datetime
from typing import List, Dict, Any
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment
load_dotenv()

# Initialize Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    print("❌ Error: SUPABASE_URL and SUPABASE_KEY must be set in .env file")
    exit(1)

supabase: Client = create_client(supabase_url, supabase_key)

class SimpleDataPopulator:
    """Simple data population for existing tables"""
    
    def __init__(self):
        self.supabase = supabase
        
    def check_existing_tables(self):
        """Check what tables currently exist"""
        print("🔍 Checking existing tables...")
        
        tables_to_check = ["destinations", "attractions", "hotels", "restaurants", "user_profiles"]
        
        existing_data = {}
        for table in tables_to_check:
            try:
                result = self.supabase.table(table).select("*", count="exact").execute()
                count = result.count if hasattr(result, 'count') else len(result.data)
                existing_data[table] = {"count": count, "exists": True}
                print(f"✅ {table}: {count} records")
            except Exception as e:
                existing_data[table] = {"count": 0, "exists": False, "error": str(e)}
                print(f"❌ {table}: {str(e)}")
        
        return existing_data
    
    def add_basic_hotels(self):
        """Add basic hotel data to existing schema"""
        print("\n🏨 Adding basic hotels...")
        
        hotels = [
            {
                "name": "Four Seasons Hotel Beirut",
                "address": "Beirut Central District, Lebanon",
                "star_rating": 5,
                "customer_rating": 4.8,
                "price_per_night": 280.00,
                "currency": "USD",
                "amenities": ["Pool", "Spa", "Gym", "WiFi", "Restaurant", "Concierge"],
                "description": "Luxury hotel in the heart of Beirut with stunning sea views",
                "booking_url": "https://www.fourseasons.com/beirut/",
                "distance_to_center": 0.5,
                "wifi_available": True,
                "parking_available": True,
                "pet_friendly": False,
                "accessibility_features": ["Wheelchair Access", "Elevator", "Accessible Rooms"],
                "created_at": datetime.datetime.now().isoformat(),
                "updated_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Boutique Hotel Beirut",
                "address": "Hamra District, Beirut, Lebanon",
                "star_rating": 4,
                "customer_rating": 4.5,
                "price_per_night": 120.00,
                "currency": "USD",
                "amenities": ["WiFi", "Restaurant", "24h Reception", "Laundry"],
                "description": "Charming boutique hotel in vibrant Hamra neighborhood",
                "booking_url": "https://boutiquehotelbeirut.com",
                "distance_to_center": 2.1,
                "wifi_available": True,
                "parking_available": False,
                "pet_friendly": True,
                "accessibility_features": ["Elevator"],
                "created_at": datetime.datetime.now().isoformat(),
                "updated_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Kyoto Traditional Ryokan",
                "address": "Gion District, Kyoto, Japan",
                "star_rating": 5,
                "customer_rating": 4.9,
                "price_per_night": 450.00,
                "currency": "USD",
                "amenities": ["Traditional Rooms", "Kaiseki Dining", "Tea Ceremony", "Garden", "Onsen"],
                "description": "Authentic Japanese ryokan experience in historic Gion",
                "booking_url": "https://kyoto-ryokan.jp",
                "distance_to_center": 3.2,
                "wifi_available": True,
                "parking_available": False,
                "pet_friendly": False,
                "accessibility_features": [],
                "created_at": datetime.datetime.now().isoformat(),
                "updated_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("hotels").upsert(hotels).execute()
            print(f"✅ Successfully added {len(hotels)} hotels")
            return True
        except Exception as e:
            print(f"❌ Error adding hotels: {e}")
            return False
    
    def add_basic_restaurants(self):
        """Add basic restaurant data to existing schema"""
        print("\n🍽️ Adding basic restaurants...")
        
        restaurants = [
            {
                "name": "Tawlet Beirut",
                "cuisine_type": "Lebanese Traditional",
                "address": "Mar Mikhael, Beirut, Lebanon",
                "phone": "+961-1-448129",
                "price_per_person": 25.00,
                "currency": "USD",
                "rating": 4.7,
                "description": "Authentic Lebanese home cooking with fresh, local ingredients",
                "opening_hours": "12:00-22:00",
                "delivery_available": False,
                "reservation_required": True,
                "dietary_options": "Vegetarian, Vegan options available",
                "created_at": datetime.datetime.now().isoformat(),
                "updated_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Al Falamanki",
                "cuisine_type": "Lebanese Fusion",
                "address": "Gemmayzeh, Beirut, Lebanon", 
                "phone": "+961-1-445957",
                "price_per_person": 20.00,
                "currency": "USD",
                "rating": 4.5,
                "description": "Modern Lebanese cuisine in a cozy traditional setting",
                "opening_hours": "18:00-24:00",
                "delivery_available": True,
                "reservation_required": True,
                "dietary_options": "Vegetarian, Gluten-free options",
                "created_at": datetime.datetime.now().isoformat(),
                "updated_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Kikunoi Kyoto",
                "cuisine_type": "Kaiseki (Traditional Japanese)",
                "address": "Higashiyama, Kyoto, Japan",
                "phone": "+81-75-561-0015",
                "price_per_person": 200.00,
                "currency": "USD",
                "rating": 4.9,
                "description": "3-Michelin-star kaiseki restaurant with seasonal menu",
                "opening_hours": "17:00-21:00",
                "delivery_available": False,
                "reservation_required": True,
                "dietary_options": "Vegetarian kaiseki available with advance notice",
                "created_at": datetime.datetime.now().isoformat(),
                "updated_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("restaurants").upsert(restaurants).execute()
            print(f"✅ Successfully added {len(restaurants)} restaurants")
            return True
        except Exception as e:
            print(f"❌ Error adding restaurants: {e}")
            return False
    
    def add_enhanced_destinations(self):
        """Add more destinations with existing schema"""
        print("\n🌍 Adding enhanced destinations...")
        
        new_destinations = [
            {
                "name": "Dubai, UAE",
                "country": "United Arab Emirates",
                "continent": "Asia",
                "city": "Dubai",
                "description": "Futuristic city with luxury shopping, modern architecture, and desert adventures",
                "timezone": "Asia/Dubai",
                "currency": "AED",
                "language": "Arabic, English",
                "best_season": "November to March",
                "climate_type": "Desert",
                "visa_requirements": "Visa on arrival for most nationalities",
                "safety_rating": 4.8,
                "cost_level": "high",
                "popularity_score": 95,
                "tags": ["luxury", "shopping", "modern", "desert", "business"],
                "created_at": datetime.datetime.now().isoformat(),
                "updated_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Istanbul, Turkey",
                "country": "Turkey",
                "continent": "Europe/Asia",
                "city": "Istanbul",
                "description": "Historic city bridging Europe and Asia with rich Ottoman heritage",
                "timezone": "Europe/Istanbul",
                "currency": "TRY",
                "language": "Turkish, English",
                "best_season": "April to June, September to November",
                "climate_type": "Mediterranean",
                "visa_requirements": "E-visa required for most nationalities",
                "safety_rating": 4.2,
                "cost_level": "medium",
                "popularity_score": 88,
                "tags": ["historical", "cultural", "architecture", "food", "markets"],
                "created_at": datetime.datetime.now().isoformat(),
                "updated_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Marrakech, Morocco",
                "country": "Morocco",
                "continent": "Africa",
                "city": "Marrakech",
                "description": "Imperial city with bustling souks, palaces, and Atlas Mountain backdrop",
                "timezone": "Africa/Casablanca",
                "currency": "MAD",
                "language": "Arabic, French, Berber",
                "best_season": "October to April",
                "climate_type": "Semi-arid",
                "visa_requirements": "Visa-free for most nationalities up to 90 days",
                "safety_rating": 4.0,
                "cost_level": "low",
                "popularity_score": 78,
                "tags": ["cultural", "markets", "architecture", "desert", "adventure"],
                "created_at": datetime.datetime.now().isoformat(),
                "updated_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("destinations").upsert(new_destinations).execute()
            print(f"✅ Successfully added {len(new_destinations)} destinations")
            return True
        except Exception as e:
            print(f"❌ Error adding destinations: {e}")
            return False
    
    def run_simple_population(self):
        """Run simple data population"""
        print("🗃️ Simple Database Population")
        print("="*50)
        
        # Check existing tables
        existing_data = self.check_existing_tables()
        
        # Run operations based on what exists
        operations = []
        
        if existing_data.get("destinations", {}).get("exists", False):
            operations.append(("Enhanced Destinations", self.add_enhanced_destinations))
        
        if existing_data.get("hotels", {}).get("exists", False):
            operations.append(("Basic Hotels", self.add_basic_hotels))
        
        if existing_data.get("restaurants", {}).get("exists", False):
            operations.append(("Basic Restaurants", self.add_basic_restaurants))
        
        if not operations:
            print("❌ No suitable tables found for population")
            return
        
        success_count = 0
        for operation_name, operation_func in operations:
            try:
                if operation_func():
                    success_count += 1
            except Exception as e:
                print(f"❌ Failed {operation_name}: {e}")
        
        print(f"\n🎉 Simple population completed!")
        print(f"✅ Successfully completed {success_count}/{len(operations)} operations")
        
        # Final status check
        print("\n📊 Updated database status:")
        self.check_existing_tables()

def main():
    """Main execution function"""
    print("🗃️ Simple AI Travel Platform - Database Population")
    print("="*60)
    
    populator = SimpleDataPopulator()
    populator.run_simple_population()

if __name__ == "__main__":
    main()
