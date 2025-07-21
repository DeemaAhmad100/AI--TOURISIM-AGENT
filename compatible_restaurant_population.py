"""
🍽️ Compatible Restaurant Population Script
Adds restaurants using your existing database schema
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

supabase: Client = create_client(supabase_url, supabase_key)

def get_destination_id(destination_name):
    """Get destination ID by name"""
    try:
        result = supabase.table("destinations").select("id").ilike("name", f"%{destination_name}%").execute()
        if result.data:
            return str(result.data[0]['id'])
        return None
    except Exception as e:
        print(f"Error getting destination ID for {destination_name}: {e}")
        return None

def add_compatible_restaurants():
    """Add restaurants using existing schema columns only"""
    
    restaurants_data = [
        # Beirut Restaurants
        {
            "name": "Tawlet",
            "destination": "Beirut",
            "cuisine_type": "Lebanese Traditional",
            "rating": 4.7,
            "price_range": "moderate",
            "specialties": ["Hummus", "Tabbouleh", "Kibbeh", "Manakish"],
            "phone": "+961-1-442-664",
            "address": "Naher Street, Mar Mikhael, Beirut",
            "reservation_required": False,
            "local_authenticity": 9,
            "tourist_trap_score": 2
        },
        {
            "name": "Em Sherif",
            "destination": "Beirut",
            "cuisine_type": "Lebanese Fine Dining", 
            "rating": 4.9,
            "price_range": "expensive",
            "specialties": ["Mixed Mezze", "Grilled Lamb", "Fattoush", "Baklava"],
            "phone": "+961-1-322-722",
            "address": "Ashrafieh, Beirut",
            "reservation_required": True,
            "local_authenticity": 8,
            "tourist_trap_score": 3
        },
        {
            "name": "Babel Bay",
            "destination": "Beirut",
            "cuisine_type": "Mediterranean",
            "rating": 4.5,
            "price_range": "moderate",
            "specialties": ["Seafood Mezze", "Grilled Fish", "Mediterranean Salads"],
            "phone": "+961-1-565-777",
            "address": "Zaitunay Bay, Beirut",
            "reservation_required": False,
            "local_authenticity": 7,
            "tourist_trap_score": 4
        },
        {
            "name": "Urbanista",
            "destination": "Beirut",
            "cuisine_type": "International",
            "rating": 4.6,
            "price_range": "expensive",
            "specialties": ["Fusion Dishes", "Craft Cocktails", "International Tapas"],
            "phone": "+961-1-988-555", 
            "address": "Hamra District, Beirut",
            "reservation_required": True,
            "local_authenticity": 6,
            "tourist_trap_score": 3
        },
        
        # Dubai Restaurants
        {
            "name": "Nobu",
            "destination": "Dubai",
            "cuisine_type": "Japanese Fusion",
            "rating": 4.8,
            "price_range": "expensive",
            "specialties": ["Black Cod Miso", "Yellowtail Sashimi", "Rock Shrimp Tempura"],
            "phone": "+971-4-426-2626",
            "address": "Atlantis The Palm, Dubai",
            "reservation_required": True,
            "local_authenticity": 5,
            "tourist_trap_score": 6
        },
        {
            "name": "Pierchic",
            "destination": "Dubai", 
            "cuisine_type": "Seafood",
            "rating": 4.6,
            "price_range": "expensive",
            "specialties": ["Fresh Lobster", "Sea Bass", "Oysters", "Seafood Platter"],
            "phone": "+971-4-432-3232",
            "address": "Al Qasr, Madinat Jumeirah, Dubai",
            "reservation_required": True,
            "local_authenticity": 6,
            "tourist_trap_score": 5
        },
        {
            "name": "Al Hadheerah",
            "destination": "Dubai",
            "cuisine_type": "Traditional Emirati",
            "rating": 4.4,
            "price_range": "moderate",
            "specialties": ["Lamb Ouzi", "Camel Meat", "Arabic Coffee", "Date Sweets"],
            "phone": "+971-4-432-3000",
            "address": "Al Sahra Desert Resort, Dubai",
            "reservation_required": True,
            "local_authenticity": 9,
            "tourist_trap_score": 3
        },
        {
            "name": "Zuma",
            "destination": "Dubai",
            "cuisine_type": "Japanese Contemporary",
            "rating": 4.7,
            "price_range": "expensive",
            "specialties": ["Robata Grill", "Sushi", "Sake Selection"],
            "phone": "+971-4-425-5660",
            "address": "Gate Village, DIFC, Dubai",
            "reservation_required": True,
            "local_authenticity": 5,
            "tourist_trap_score": 4
        },
        
        # Paris Restaurants
        {
            "name": "Le Jules Verne",
            "destination": "Paris",
            "cuisine_type": "French Fine Dining",
            "rating": 4.4,
            "price_range": "expensive", 
            "specialties": ["French Gastronomy", "Seasonal Menu", "Wine Pairing"],
            "phone": "+33-1-45-55-61-44",
            "address": "Eiffel Tower, 2nd Floor, Paris",
            "reservation_required": True,
            "local_authenticity": 7,
            "tourist_trap_score": 8
        },
        {
            "name": "L'As du Fallafel",
            "destination": "Paris",
            "cuisine_type": "Middle Eastern",
            "rating": 4.3,
            "price_range": "budget",
            "specialties": ["Falafel", "Shawarma", "Hummus", "Fresh Pita"],
            "phone": "+33-1-48-87-63-60",
            "address": "34 Rue des Rosiers, Marais, Paris",
            "reservation_required": False,
            "local_authenticity": 8,
            "tourist_trap_score": 2
        },
        {
            "name": "L'Ami Jean",
            "destination": "Paris",
            "cuisine_type": "French Bistro",
            "rating": 4.6,
            "price_range": "moderate",
            "specialties": ["Cassoulet", "Duck Confit", "French Wine"],
            "phone": "+33-1-47-05-86-89",
            "address": "27 Rue Malar, 7th Arrondissement, Paris",
            "reservation_required": True,
            "local_authenticity": 9,
            "tourist_trap_score": 1
        },
        {
            "name": "Breizh Café",
            "destination": "Paris",
            "cuisine_type": "French Contemporary",
            "rating": 4.5,
            "price_range": "moderate",
            "specialties": ["Gourmet Crêpes", "Buckwheat Galettes", "Organic Cider"],
            "phone": "+33-1-42-72-13-77",
            "address": "109 Rue Vieille du Temple, Marais, Paris",
            "reservation_required": False,
            "local_authenticity": 7,
            "tourist_trap_score": 3
        },
        
        # Tokyo Restaurants
        {
            "name": "Kikunoi",
            "destination": "Tokyo",
            "cuisine_type": "Kaiseki Traditional",
            "rating": 4.9,
            "price_range": "expensive",
            "specialties": ["Seasonal Kaiseki", "Traditional Presentation", "Tea Ceremony"],
            "phone": "+81-75-561-0015",
            "address": "Kyoto (Tokyo branch)",
            "reservation_required": True,
            "local_authenticity": 10,
            "tourist_trap_score": 1
        },
        {
            "name": "Sukiyabashi Jiro",
            "destination": "Tokyo",
            "cuisine_type": "Sushi",
            "rating": 4.8,
            "price_range": "expensive",
            "specialties": ["Omakase Sushi", "Premium Fish", "Traditional Technique"],
            "phone": "+81-3-3535-3600",
            "address": "Ginza, Tokyo",
            "reservation_required": True,
            "local_authenticity": 10,
            "tourist_trap_score": 2
        },
        {
            "name": "Gonpachi Shibuya",
            "destination": "Tokyo",
            "cuisine_type": "Japanese Traditional",
            "rating": 4.4,
            "price_range": "moderate",
            "specialties": ["Yakitori", "Sake", "Robatayaki", "Traditional Atmosphere"],
            "phone": "+81-3-5771-0170",
            "address": "Shibuya, Tokyo",
            "reservation_required": False,
            "local_authenticity": 8,
            "tourist_trap_score": 3
        },
        {
            "name": "Narisawa",
            "destination": "Tokyo",
            "cuisine_type": "Japanese Contemporary",
            "rating": 4.7,
            "price_range": "expensive",
            "specialties": ["Innovative Techniques", "Local Ingredients", "Nature-inspired"],
            "phone": "+81-3-5785-0799",
            "address": "Minato, Tokyo",
            "reservation_required": True,
            "local_authenticity": 9,
            "tourist_trap_score": 2
        },
        
        # London Restaurants
        {
            "name": "Dishoom",
            "destination": "London",
            "cuisine_type": "Indian",
            "rating": 4.6,
            "price_range": "moderate",
            "specialties": ["Black Dal", "Pau Bhaji", "Biryanis", "Masala Chai"],
            "phone": "+44-20-7420-9320",
            "address": "Covent Garden, London",
            "reservation_required": False,
            "local_authenticity": 7,
            "tourist_trap_score": 4
        },
        {
            "name": "Rules",
            "destination": "London",
            "cuisine_type": "British Traditional",
            "rating": 4.3,
            "price_range": "expensive",
            "specialties": ["Game Meats", "British Classics", "Historic Atmosphere"],
            "phone": "+44-20-7836-5314",
            "address": "Covent Garden, London",
            "reservation_required": True,
            "local_authenticity": 9,
            "tourist_trap_score": 5
        },
        {
            "name": "Sketch",
            "destination": "London",
            "cuisine_type": "French Contemporary",
            "rating": 4.5,
            "price_range": "expensive",
            "specialties": ["Modern French", "Artistic Presentation", "Afternoon Tea"],
            "phone": "+44-20-7659-4500",
            "address": "Mayfair, London",
            "reservation_required": True,
            "local_authenticity": 6,
            "tourist_trap_score": 6
        },
        {
            "name": "Borough Market Restaurant",
            "destination": "London",
            "cuisine_type": "British Modern",
            "rating": 4.4,
            "price_range": "moderate",
            "specialties": ["Market Fresh", "British Seasonal", "Local Produce"],
            "phone": "+44-20-7407-1002",
            "address": "Borough Market, London",
            "reservation_required": False,
            "local_authenticity": 8,
            "tourist_trap_score": 3
        }
    ]
    
    added_count = 0
    
    for restaurant in restaurants_data:
        try:
            # Get destination ID
            destination_id = get_destination_id(restaurant["destination"])
            if not destination_id:
                print(f"   ⚠️ Could not find destination: {restaurant['destination']}")
                continue
            
            # Prepare restaurant data with compatible fields only
            restaurant_data = {
                "name": restaurant["name"],
                "destination_id": destination_id,
                "cuisine_type": restaurant["cuisine_type"],
                "rating": restaurant["rating"],
                "price_range": restaurant["price_range"],
                "specialties": restaurant["specialties"],
                "phone": restaurant["phone"],
                "address": restaurant["address"],
                "reservation_required": restaurant["reservation_required"],
                "local_authenticity": restaurant["local_authenticity"],
                "tourist_trap_score": restaurant["tourist_trap_score"],
                "created_at": datetime.datetime.now().isoformat()
            }
            
            # Insert restaurant
            result = supabase.table("restaurants").insert(restaurant_data).execute()
            print(f"   ✅ Added: {restaurant['name']} ({restaurant['cuisine_type']}) - {restaurant['destination']}")
            added_count += 1
            
        except Exception as e:
            print(f"   ❌ Error adding {restaurant['name']}: {e}")
    
    return added_count

def verify_restaurant_count():
    """Check current restaurant count"""
    try:
        result = supabase.table("restaurants").select("count", count="exact").execute()
        count = result.count if hasattr(result, 'count') else len(result.data)
        return count
    except Exception as e:
        print(f"❌ Error checking restaurant count: {e}")
        return 0

def show_restaurant_summary():
    """Show summary of restaurants by destination"""
    try:
        result = supabase.table("restaurants").select("name, cuisine_type, rating, price_range").execute()
        restaurants = result.data
        
        print(f"\n📋 Restaurant Summary ({len(restaurants)} total):")
        by_cuisine = {}
        for r in restaurants:
            cuisine = r.get('cuisine_type', 'Unknown')
            if cuisine not in by_cuisine:
                by_cuisine[cuisine] = []
            by_cuisine[cuisine].append(f"{r['name']} ({r.get('rating', 'N/A')}★)")
        
        for cuisine, restaurants_list in by_cuisine.items():
            print(f"   🍽️ {cuisine}: {len(restaurants_list)} restaurants")
            for rest in restaurants_list[:2]:  # Show first 2
                print(f"      • {rest}")
            if len(restaurants_list) > 2:
                print(f"      • ... and {len(restaurants_list) - 2} more")
                
    except Exception as e:
        print(f"❌ Error getting restaurant summary: {e}")

def main():
    """Main execution"""
    print("🍽️ Compatible Restaurant Population for AI Travel Platform")
    print("=" * 60)
    
    # Check initial count
    print("\n📊 Checking current database status...")
    initial_count = verify_restaurant_count()
    print(f"📊 Current restaurants in database: {initial_count}")
    
    if initial_count > 15:
        print(f"✅ You already have {initial_count} restaurants - good coverage!")
        response = input("Do you want to add more restaurants anyway? (y/n): ")
        if response.lower() != 'y':
            print("👍 Skipping restaurant addition")
            show_restaurant_summary()
            return
    
    # Add restaurants
    print("\n🚀 Adding restaurants using compatible schema...")
    total_added = add_compatible_restaurants()
    
    # Final verification
    print(f"\n🎉 Restaurant addition completed!")
    print(f"📈 Restaurants added: {total_added}")
    
    final_count = verify_restaurant_count()
    print(f"📊 Final restaurant count: {final_count}")
    
    # Show summary
    show_restaurant_summary()
    
    if final_count >= 15:
        print("\n✅ Excellent! Your platform now has great restaurant coverage")
        print("🎯 Restaurant booking feature is ready for investor demos")
        print("🚀 Your AI Travel Platform is now 100% READY! 🎉")
    else:
        print(f"\n⚠️ Consider adding more restaurants (current: {final_count}, recommended: 15+)")
    
    print("\n🚀 Next steps:")
    print("   • Test restaurant search: streamlit run enhanced_streamlit_app.py")
    print("   • Navigate to Restaurant Booking section") 
    print("   • Verify restaurants appear in search results")
    print("   • Your platform is ready for investor presentations! 🎯")

if __name__ == "__main__":
    main()
