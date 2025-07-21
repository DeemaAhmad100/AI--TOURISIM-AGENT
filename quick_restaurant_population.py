"""
🍽️ Quick Restaurant Population Script
Adds essential restaurants to complete your AI Travel Platform
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

def add_restaurants_by_destination():
    """Add restaurants organized by destination"""
    
    restaurants_data = {
        "Beirut": [
            {
                "name": "Tawlet",
                "cuisine_type": "Lebanese Traditional",
                "rating": 4.7,
                "price_range": "$$",
                "description": "Authentic Lebanese home cooking with changing daily menu from different regions",
                "specialties": ["Hummus", "Tabbouleh", "Kibbeh", "Manakish"],
                "atmosphere": "Casual traditional",
                "booking_required": False,
                "phone": "+961-1-442-664",
                "address": "Naher Street, Mar Mikhael, Beirut"
            },
            {
                "name": "Em Sherif",
                "cuisine_type": "Lebanese Fine Dining", 
                "rating": 4.9,
                "price_range": "$$$",
                "description": "Upscale Lebanese cuisine in elegant traditional setting",
                "specialties": ["Mixed Mezze", "Grilled Lamb", "Fattoush", "Baklava"],
                "atmosphere": "Fine dining",
                "booking_required": True,
                "phone": "+961-1-322-722",
                "address": "Ashrafieh, Beirut"
            },
            {
                "name": "Babel Bay",
                "cuisine_type": "Mediterranean",
                "rating": 4.5,
                "price_range": "$$",
                "description": "Waterfront Mediterranean dining with Lebanese influences",
                "specialties": ["Seafood Mezze", "Grilled Fish", "Mediterranean Salads"],
                "atmosphere": "Waterfront casual",
                "booking_required": False,
                "phone": "+961-1-565-777",
                "address": "Zaitunay Bay, Beirut"
            },
            {
                "name": "Urbanista",
                "cuisine_type": "International",
                "rating": 4.6,
                "price_range": "$$$",
                "description": "Modern international cuisine with local ingredients",
                "specialties": ["Fusion Dishes", "Craft Cocktails", "International Tapas"],
                "atmosphere": "Modern upscale",
                "booking_required": True,
                "phone": "+961-1-988-555",
                "address": "Hamra District, Beirut"
            }
        ],
        "Dubai": [
            {
                "name": "Nobu",
                "cuisine_type": "Japanese Fusion",
                "rating": 4.8,
                "price_range": "$$$$",
                "description": "World-renowned Japanese restaurant with signature dishes",
                "specialties": ["Black Cod Miso", "Yellowtail Sashimi", "Rock Shrimp Tempura"],
                "atmosphere": "Upscale modern",
                "booking_required": True,
                "phone": "+971-4-426-2626",
                "address": "Atlantis The Palm, Dubai"
            },
            {
                "name": "Pierchic", 
                "cuisine_type": "Seafood",
                "rating": 4.6,
                "price_range": "$$$",
                "description": "Overwater seafood restaurant with ocean views",
                "specialties": ["Fresh Lobster", "Sea Bass", "Oysters", "Seafood Platter"],
                "atmosphere": "Romantic waterfront",
                "booking_required": True,
                "phone": "+971-4-432-3232",
                "address": "Al Qasr, Madinat Jumeirah, Dubai"
            },
            {
                "name": "Al Hadheerah",
                "cuisine_type": "Traditional Emirati",
                "rating": 4.4,
                "price_range": "$$",
                "description": "Desert dining experience with traditional Emirati cuisine",
                "specialties": ["Lamb Ouzi", "Camel Meat", "Arabic Coffee", "Date Sweets"],
                "atmosphere": "Traditional desert",
                "booking_required": True,
                "phone": "+971-4-432-3000",
                "address": "Al Sahra Desert Resort, Dubai"
            },
            {
                "name": "Zuma",
                "cuisine_type": "Japanese Contemporary",
                "rating": 4.7,
                "price_range": "$$$", 
                "description": "Contemporary Japanese izakaya-style dining",
                "specialties": ["Robata Grill", "Sushi", "Sake Selection"],
                "atmosphere": "Modern Japanese",
                "booking_required": True,
                "phone": "+971-4-425-5660",
                "address": "Gate Village, DIFC, Dubai"
            }
        ],
        "Paris": [
            {
                "name": "Le Jules Verne",
                "cuisine_type": "French Fine Dining",
                "rating": 4.4,
                "price_range": "$$$$",
                "description": "Michelin-starred restaurant in the Eiffel Tower",
                "specialties": ["French Gastronomy", "Seasonal Menu", "Wine Pairing"],
                "atmosphere": "Iconic fine dining",
                "booking_required": True,
                "phone": "+33-1-45-55-61-44",
                "address": "Eiffel Tower, 2nd Floor, Paris"
            },
            {
                "name": "L'As du Fallafel",
                "cuisine_type": "Middle Eastern",
                "rating": 4.3,
                "price_range": "$",
                "description": "Famous falafel spot in the Marais district",
                "specialties": ["Falafel", "Shawarma", "Hummus", "Fresh Pita"],
                "atmosphere": "Casual street food",
                "booking_required": False,
                "phone": "+33-1-48-87-63-60",
                "address": "34 Rue des Rosiers, Marais, Paris"
            },
            {
                "name": "L'Ami Jean",
                "cuisine_type": "French Bistro",
                "rating": 4.6,
                "price_range": "$$", 
                "description": "Traditional French bistro with Basque influences",
                "specialties": ["Cassoulet", "Duck Confit", "French Wine"],
                "atmosphere": "Traditional bistro",
                "booking_required": True,
                "phone": "+33-1-47-05-86-89",
                "address": "27 Rue Malar, 7th Arrondissement, Paris"
            },
            {
                "name": "Breizh Café",
                "cuisine_type": "French Contemporary",
                "rating": 4.5,
                "price_range": "$$",
                "description": "Modern crêperie with Japanese influences",
                "specialties": ["Gourmet Crêpes", "Buckwheat Galettes", "Organic Cider"],
                "atmosphere": "Modern casual",
                "booking_required": False,
                "phone": "+33-1-42-72-13-77",
                "address": "109 Rue Vieille du Temple, Marais, Paris"
            }
        ],
        "Tokyo": [
            {
                "name": "Kikunoi",
                "cuisine_type": "Kaiseki Traditional",
                "rating": 4.9,
                "price_range": "$$$$",
                "description": "3-Michelin-star kaiseki restaurant with seasonal menu",
                "specialties": ["Seasonal Kaiseki", "Traditional Presentation", "Tea Ceremony"],
                "atmosphere": "Traditional Japanese",
                "booking_required": True,
                "phone": "+81-75-561-0015",
                "address": "Kyoto (Tokyo branch planned)"
            },
            {
                "name": "Sukiyabashi Jiro",
                "cuisine_type": "Sushi",
                "rating": 4.8,
                "price_range": "$$$$",
                "description": "World-famous sushi master's restaurant",
                "specialties": ["Omakase Sushi", "Premium Fish", "Traditional Technique"],
                "atmosphere": "Exclusive sushi counter",
                "booking_required": True,
                "phone": "+81-3-3535-3600",
                "address": "Ginza, Tokyo"
            },
            {
                "name": "Gonpachi Shibuya",
                "cuisine_type": "Japanese Traditional",
                "rating": 4.4,
                "price_range": "$$",
                "description": "Traditional izakaya with rustic atmosphere",
                "specialties": ["Yakitori", "Sake", "Robatayaki", "Traditional Atmosphere"],
                "atmosphere": "Traditional rustic",
                "booking_required": False,
                "phone": "+81-3-5771-0170",
                "address": "Shibuya, Tokyo"
            },
            {
                "name": "Narisawa",
                "cuisine_type": "Japanese Contemporary",
                "rating": 4.7,
                "price_range": "$$$",
                "description": "Innovative Japanese cuisine with local ingredients",
                "specialties": ["Innovative Techniques", "Local Ingredients", "Nature-inspired"],
                "atmosphere": "Modern fine dining",
                "booking_required": True,
                "phone": "+81-3-5785-0799",
                "address": "Minato, Tokyo"
            }
        ],
        "London": [
            {
                "name": "Dishoom",
                "cuisine_type": "Indian",
                "rating": 4.6,
                "price_range": "$$",
                "description": "Bombay-style café with vintage charm",
                "specialties": ["Black Dal", "Pau Bhaji", "Biryanis", "Masala Chai"],
                "atmosphere": "Vintage Indian café",
                "booking_required": False,
                "phone": "+44-20-7420-9320",
                "address": "Covent Garden, London"
            },
            {
                "name": "Rules",
                "cuisine_type": "British Traditional",
                "rating": 4.3,
                "price_range": "$$$",
                "description": "London's oldest restaurant serving traditional British fare",
                "specialties": ["Game Meats", "British Classics", "Historic Atmosphere"],
                "atmosphere": "Historic traditional",
                "booking_required": True,
                "phone": "+44-20-7836-5314",
                "address": "Covent Garden, London"
            },
            {
                "name": "Sketch",
                "cuisine_type": "French Contemporary",
                "rating": 4.5,
                "price_range": "$$$",
                "description": "Artistic restaurant with unique pod-shaped dining rooms",
                "specialties": ["Modern French", "Artistic Presentation", "Afternoon Tea"],
                "atmosphere": "Artistic modern",
                "booking_required": True,
                "phone": "+44-20-7659-4500",
                "address": "Mayfair, London"
            },
            {
                "name": "Borough Market Restaurant",
                "cuisine_type": "British Modern",
                "rating": 4.4,
                "price_range": "$$",
                "description": "Market-fresh British cuisine in historic setting",
                "specialties": ["Market Fresh", "British Seasonal", "Local Produce"],
                "atmosphere": "Market casual",
                "booking_required": False,
                "phone": "+44-20-7407-1002",
                "address": "Borough Market, London"
            }
        ]
    }
    
    total_added = 0
    
    for destination_name, restaurants in restaurants_data.items():
        print(f"\n🍽️ Adding restaurants for {destination_name}...")
        
        # Get destination ID
        destination_id = get_destination_id(destination_name)
        if not destination_id:
            print(f"   ⚠️ Could not find destination: {destination_name}")
            continue
        
        for restaurant in restaurants:
            try:
                # Add destination_id and timestamps
                restaurant_data = {
                    **restaurant,
                    "destination_id": destination_id,
                    "created_at": datetime.datetime.now().isoformat(),
                    "updated_at": datetime.datetime.now().isoformat()
                }
                
                # Insert restaurant
                result = supabase.table("restaurants").insert(restaurant_data).execute()
                print(f"   ✅ Added: {restaurant['name']} ({restaurant['cuisine_type']})")
                total_added += 1
                
            except Exception as e:
                print(f"   ❌ Error adding {restaurant['name']}: {e}")
    
    return total_added

def verify_restaurant_count():
    """Check current restaurant count"""
    try:
        result = supabase.table("restaurants").select("count", count="exact").execute()
        count = result.count if hasattr(result, 'count') else len(result.data)
        print(f"📊 Total restaurants in database: {count}")
        return count
    except Exception as e:
        print(f"❌ Error checking restaurant count: {e}")
        return 0

def main():
    """Main execution"""
    print("🍽️ Quick Restaurant Population for AI Travel Platform")
    print("=" * 55)
    
    # Check initial count
    print("\n📊 Checking current database status...")
    initial_count = verify_restaurant_count()
    
    if initial_count > 15:
        print(f"✅ You already have {initial_count} restaurants - good coverage!")
        print("💡 This script adds premium restaurants for major destinations")
        response = input("Do you want to add more restaurants anyway? (y/n): ")
        if response.lower() != 'y':
            print("👍 Skipping restaurant addition")
            return
    
    # Add restaurants
    print("\n🚀 Adding restaurants by destination...")
    total_added = add_restaurants_by_destination()
    
    # Final verification
    print(f"\n🎉 Restaurant addition completed!")
    print(f"📈 Restaurants added: {total_added}")
    
    final_count = verify_restaurant_count()
    print(f"📊 Final restaurant count: {final_count}")
    
    if final_count >= 15:
        print("✅ Excellent! Your platform now has great restaurant coverage")
        print("🎯 Restaurant booking feature is ready for demos")
    else:
        print("⚠️ Consider adding more restaurants for better coverage")
    
    print("\n🚀 Next steps:")
    print("   • Test restaurant search: streamlit run enhanced_streamlit_app.py")
    print("   • Navigate to Restaurant Booking section")
    print("   • Verify restaurants appear in search results")

if __name__ == "__main__":
    main()
