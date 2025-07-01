"""
🗃️ Compatible Database Population Script
Script that works with the current database schema structure
"""

import os
import datetime
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

class CompatibleDataPopulator:
    """Data population that works with current schema"""
    
    def __init__(self):
        self.supabase = supabase
        
    def check_database_status(self):
        """Check current database status"""
        print("🔍 Checking database status...")
        
        tables = ["destinations", "attractions", "hotels", "restaurants", "user_profiles"]
        
        for table in tables:
            try:
                result = self.supabase.table(table).select("*", count="exact").execute()
                count = result.count if hasattr(result, 'count') else len(result.data)
                print(f"📊 {table}: {count} records")
            except Exception as e:
                print(f"❌ {table}: {str(e)}")
    
    def add_compatible_destinations(self):
        """Add destinations using current schema"""
        print("\n🌍 Adding destinations (compatible format)...")
        
        # Current schema: name, country, continent, best_season, average_cost_per_day, currency, language, description
        new_destinations = [
            {
                "name": "Beirut",
                "country": "Lebanon",
                "continent": "Asia",
                "best_season": "Spring/Fall",
                "average_cost_per_day": 80.0,
                "currency": "USD",
                "language": "Arabic/English",
                "description": "Historic Mediterranean city with vibrant culture, delicious cuisine, and rich heritage",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Kyoto",
                "country": "Japan",
                "continent": "Asia", 
                "best_season": "Spring/Fall",
                "average_cost_per_day": 120.0,
                "currency": "JPY",
                "language": "Japanese",
                "description": "Ancient capital with beautiful temples, traditional culture, and cherry blossoms",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Dubai",
                "country": "UAE",
                "continent": "Asia",
                "best_season": "Winter",
                "average_cost_per_day": 200.0,
                "currency": "AED",
                "language": "Arabic/English",
                "description": "Futuristic city with luxury shopping, modern architecture, and desert adventures",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Istanbul",
                "country": "Turkey",
                "continent": "Europe",
                "best_season": "Spring/Fall", 
                "average_cost_per_day": 70.0,
                "currency": "TRY",
                "language": "Turkish",
                "description": "Historic city bridging Europe and Asia with Ottoman heritage and vibrant bazaars",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Marrakech",
                "country": "Morocco",
                "continent": "Africa",
                "best_season": "Winter/Spring",
                "average_cost_per_day": 60.0,
                "currency": "MAD",
                "language": "Arabic/French",
                "description": "Imperial city with bustling souks, palaces, and Atlas Mountain backdrop",
                "created_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("destinations").upsert(new_destinations).execute()
            print(f"✅ Successfully added {len(new_destinations)} destinations")
            return True
        except Exception as e:
            print(f"❌ Error adding destinations: {e}")
            return False
    
    def add_compatible_attractions(self):
        """Add attractions using current schema"""
        print("\n🏛️ Adding attractions (compatible format)...")
        
        # First, get destination IDs for our new destinations
        destinations_map = {}
        try:
            result = self.supabase.table("destinations").select("id, name").execute()
            for dest in result.data:
                destinations_map[dest['name']] = dest['id']
        except Exception as e:
            print(f"⚠️ Could not map destinations: {e}")
            return False
        
        # Current schema: destination_id, type, description, cost, duration_hours, rating, best_time
        new_attractions = []
        
        # Beirut attractions
        if "Beirut" in destinations_map:
            beirut_id = destinations_map["Beirut"]
            new_attractions.extend([
                {
                    "name": "Pigeon Rocks (Raouché)",
                    "destination_id": beirut_id,
                    "type": "Natural Landmark",
                    "description": "Iconic natural rock formations off the Beirut coast with stunning sunset views",
                    "cost": 0.0,
                    "duration_hours": 2,
                    "rating": 4.6,
                    "best_time": "Evening",
                    "created_at": datetime.datetime.now().isoformat()
                },
                {
                    "name": "National Museum of Beirut",
                    "destination_id": beirut_id,
                    "type": "Museum",
                    "description": "Lebanon's principal museum showcasing archaeological treasures and Phoenician artifacts",
                    "cost": 8.0,
                    "duration_hours": 3,
                    "rating": 4.4,
                    "best_time": "Morning",
                    "created_at": datetime.datetime.now().isoformat()
                },
                {
                    "name": "Beirut Souks",
                    "destination_id": beirut_id,
                    "type": "Shopping",
                    "description": "Modern shopping district built on historic souk foundations",
                    "cost": 0.0,
                    "duration_hours": 3,
                    "rating": 4.2,
                    "best_time": "Afternoon",
                    "created_at": datetime.datetime.now().isoformat()
                }
            ])
        
        # Kyoto attractions
        if "Kyoto" in destinations_map:
            kyoto_id = destinations_map["Kyoto"]
            new_attractions.extend([
                {
                    "name": "Fushimi Inari Shrine",
                    "destination_id": kyoto_id,
                    "type": "Religious",
                    "description": "Famous shrine with thousands of vermillion torii gates leading up the mountain",
                    "cost": 0.0,
                    "duration_hours": 3,
                    "rating": 4.8,
                    "best_time": "Early Morning",
                    "created_at": datetime.datetime.now().isoformat()
                },
                {
                    "name": "Kinkaku-ji (Golden Pavilion)",
                    "destination_id": kyoto_id,
                    "type": "Temple",
                    "description": "Iconic golden temple reflecting in a peaceful pond, UNESCO World Heritage site",
                    "cost": 5.0,
                    "duration_hours": 2,
                    "rating": 4.7,
                    "best_time": "Morning",
                    "created_at": datetime.datetime.now().isoformat()
                },
                {
                    "name": "Arashiyama Bamboo Grove",
                    "destination_id": kyoto_id,
                    "type": "Natural",
                    "description": "Mystical bamboo forest creating natural cathedral of green light",
                    "cost": 0.0,
                    "duration_hours": 2,
                    "rating": 4.5,
                    "best_time": "Morning",
                    "created_at": datetime.datetime.now().isoformat()
                }
            ])
        
        # Dubai attractions
        if "Dubai" in destinations_map:
            dubai_id = destinations_map["Dubai"]
            new_attractions.extend([
                {
                    "name": "Burj Khalifa",
                    "destination_id": dubai_id,
                    "type": "Landmark",
                    "description": "World's tallest building with observation decks offering panoramic city views",
                    "cost": 45.0,
                    "duration_hours": 3,
                    "rating": 4.6,
                    "best_time": "Sunset",
                    "created_at": datetime.datetime.now().isoformat()
                },
                {
                    "name": "Dubai Mall",
                    "destination_id": dubai_id,
                    "type": "Shopping",
                    "description": "World's largest shopping mall with aquarium, ice rink, and fountain shows",
                    "cost": 0.0,
                    "duration_hours": 4,
                    "rating": 4.4,
                    "best_time": "Evening",
                    "created_at": datetime.datetime.now().isoformat()
                },
                {
                    "name": "Desert Safari",
                    "destination_id": dubai_id,
                    "type": "Adventure",
                    "description": "Thrilling desert experience with dune bashing, camel riding, and Bedouin camp",
                    "cost": 80.0,
                    "duration_hours": 6,
                    "rating": 4.7,
                    "best_time": "Afternoon",
                    "created_at": datetime.datetime.now().isoformat()
                }
            ])
        
        if new_attractions:
            try:
                result = self.supabase.table("attractions").upsert(new_attractions).execute()
                print(f"✅ Successfully added {len(new_attractions)} attractions")
                return True
            except Exception as e:
                print(f"❌ Error adding attractions: {e}")
                return False
        else:
            print("⚠️ No attractions to add (destinations not found)")
            return False
    
    def add_basic_hotels(self):
        """Add hotels using current schema"""
        print("\n🏨 Adding hotels (compatible format)...")
        
        # Check if hotels table exists and what columns it has
        try:
            # Try to get the structure first
            result = self.supabase.table("hotels").select("*").limit(1).execute()
            print("ℹ️ Hotels table exists and is accessible")
        except Exception as e:
            print(f"❌ Hotels table issue: {e}")
            return False
        
        # Add basic hotel data - we'll use minimal fields that likely exist
        hotels = [
            {
                "name": "Four Seasons Hotel Beirut",
                "star_rating": 5,
                "price_per_night": 280.00,
                "currency": "USD",
                "description": "Luxury hotel in the heart of Beirut with stunning sea views",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Kyoto Traditional Ryokan", 
                "star_rating": 5,
                "price_per_night": 450.00,
                "currency": "USD",
                "description": "Authentic Japanese ryokan experience in historic Gion district",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Burj Al Arab Dubai",
                "star_rating": 5,
                "price_per_night": 800.00,
                "currency": "USD", 
                "description": "Iconic sail-shaped luxury hotel on private island",
                "created_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("hotels").upsert(hotels).execute()
            print(f"✅ Successfully added {len(hotels)} hotels")
            return True
        except Exception as e:
            print(f"❌ Error adding hotels: {e}")
            print(f"   Details: {e}")
            return False
    
    def add_basic_restaurants(self):
        """Add restaurants using current schema"""
        print("\n🍽️ Adding restaurants (compatible format)...")
        
        # Check restaurants table structure
        try:
            result = self.supabase.table("restaurants").select("*").limit(1).execute()
            print("ℹ️ Restaurants table exists and is accessible")
        except Exception as e:
            print(f"❌ Restaurants table issue: {e}")
            return False
        
        # Add basic restaurant data
        restaurants = [
            {
                "name": "Tawlet Beirut",
                "cuisine_type": "Lebanese Traditional",
                "price_per_person": 25.00,
                "currency": "USD",
                "rating": 4.7,
                "description": "Authentic Lebanese home cooking with fresh, local ingredients from village cooperatives",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Kikunoi Kyoto",
                "cuisine_type": "Kaiseki Traditional",
                "price_per_person": 200.00,
                "currency": "USD",
                "rating": 4.9,
                "description": "3-Michelin-star kaiseki restaurant offering seasonal Japanese haute cuisine",
                "created_at": datetime.datetime.now().isoformat()
            },
            {
                "name": "Nobu Dubai",
                "cuisine_type": "Japanese Fusion",
                "price_per_person": 120.00,
                "currency": "USD",
                "rating": 4.6,
                "description": "World-renowned Japanese-Peruvian fusion restaurant with innovative dishes",
                "created_at": datetime.datetime.now().isoformat()
            }
        ]
        
        try:
            result = self.supabase.table("restaurants").upsert(restaurants).execute()
            print(f"✅ Successfully added {len(restaurants)} restaurants")
            return True
        except Exception as e:
            print(f"❌ Error adding restaurants: {e}")
            return False
    
    def run_compatible_population(self):
        """Run complete compatible data population"""
        print("🗃️ Compatible Database Population")
        print("="*60)
        
        # Check initial status
        self.check_database_status()
        
        # Run population operations
        operations = [
            ("New Destinations", self.add_compatible_destinations),
            ("Enhanced Attractions", self.add_compatible_attractions),
            ("Basic Hotels", self.add_basic_hotels),
            ("Basic Restaurants", self.add_basic_restaurants)
        ]
        
        success_count = 0
        for operation_name, operation_func in operations:
            try:
                if operation_func():
                    success_count += 1
            except Exception as e:
                print(f"❌ Failed {operation_name}: {e}")
        
        print(f"\n🎉 Compatible population completed!")
        print(f"✅ Successfully completed {success_count}/{len(operations)} operations")
        
        # Final status check
        print("\n📊 Final database status:")
        self.check_database_status()
        
        print("\n🌟 Your database now has enhanced travel data!")
        print("✨ Ready for improved AI travel recommendations!")

def main():
    """Main execution function"""
    print("🗃️ Compatible AI Travel Platform - Database Population")
    print("="*70)
    
    populator = CompatibleDataPopulator()
    populator.run_compatible_population()

if __name__ == "__main__":
    main()
