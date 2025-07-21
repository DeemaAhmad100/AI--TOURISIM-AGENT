"""
Extended Global Hotels Database Expansion - Phase 2
Adds another 25+ hotels covering more destinations and hotel categories
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client
import time

def get_european_hotels_expansion():
    """Additional European hotels in new cities"""
    return [
        {
            "name": "Hotel Villa San Martino Rome",
            "rating": 4.5,
            "price_per_night": 320.0,
            "amenities": ["Historic villa", "Garden", "Restaurant", "Business center", "WiFi", "Concierge"],
            "booking_url": "https://www.villasanmartino.com",
            "coordinates": "41.9028,12.4964",
            "star_rating": 4,
            "address": "Via Massimo D'Azeglio 16, 00184 Rome, Italy",
            "phone": "+39 06 4827 4171",
            "email": "info@villasanmartino.com",
            "website": "https://www.villasanmartino.com",
            "check_in_time": "14:00",
            "check_out_time": "11:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "The Westin Palace Madrid",
            "rating": 4.6,
            "price_per_night": 420.0,
            "amenities": ["Belle Époque architecture", "Spa", "Fine dining", "Business center", "WiFi", "Historic"],
            "booking_url": "https://www.marriott.com/westin-palace-madrid",
            "coordinates": "40.4168,-3.6936",
            "star_rating": 5,
            "address": "Plaza de las Cortes 7, 28014 Madrid, Spain",
            "phone": "+34 91 360 8000",
            "email": "palace.madrid@westin.com",
            "website": "https://www.marriott.com/westin-palace-madrid",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "Hotel d'Angleterre Copenhagen",
            "rating": 4.7,
            "price_per_night": 480.0,
            "amenities": ["Royal Square location", "Michelin dining", "Spa", "Business center", "WiFi", "Historic luxury"],
            "booking_url": "https://www.dangleterre.com",
            "coordinates": "55.6761,12.5683",
            "star_rating": 5,
            "address": "Kongens Nytorv 34, 1050 Copenhagen, Denmark",
            "phone": "+45 33 12 00 95",
            "email": "hotel@dangleterre.com",
            "website": "https://www.dangleterre.com",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": False,
            "pet_friendly": True
        },
        {
            "name": "Grand Hotel Stockholm",
            "rating": 4.6,
            "price_per_night": 520.0,
            "amenities": ["Royal Palace views", "Spa", "Fine dining", "Business center", "WiFi", "Historic elegance"],
            "booking_url": "https://www.grandhotel.se",
            "coordinates": "59.3293,18.0686",
            "star_rating": 5,
            "address": "Södra Blasieholmshamnen 8, 103 27 Stockholm, Sweden",
            "phone": "+46 8 679 35 00",
            "email": "info@grandhotel.se",
            "website": "https://www.grandhotel.se",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "The Shelbourne Dublin",
            "rating": 4.5,
            "price_per_night": 380.0,
            "amenities": ["St. Stephen's Green", "Historic hotel", "Spa", "Fine dining", "Business center", "WiFi"],
            "booking_url": "https://www.marriott.com/shelbourne-dublin",
            "coordinates": "53.3398,-6.2603",
            "star_rating": 5,
            "address": "27 St Stephen's Green, Dublin 2, Ireland",
            "phone": "+353 1 663 4500",
            "email": "shelbourne.dublin@marriott.com",
            "website": "https://www.marriott.com/shelbourne-dublin",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        }
    ]

def get_asian_hotels_expansion():
    """Additional Asian hotels in new destinations"""
    return [
        {
            "name": "The Fullerton Hotel Singapore",
            "rating": 4.6,
            "price_per_night": 420.0,
            "amenities": ["Heritage building", "River views", "Spa", "Fine dining", "Business center", "WiFi"],
            "booking_url": "https://www.fullertonhotels.com/singapore",
            "coordinates": "1.2862,103.8545",
            "star_rating": 5,
            "address": "1 Fullerton Square, Singapore 049178",
            "phone": "+65 6733 8388",
            "email": "enquiries@fullertonhotel.com",
            "website": "https://www.fullertonhotels.com/singapore",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "Shangri-La Hotel Bangkok",
            "rating": 4.5,
            "price_per_night": 280.0,
            "amenities": ["River location", "Multiple restaurants", "Spa", "Pool", "Business center", "WiFi"],
            "booking_url": "https://www.shangri-la.com/bangkok",
            "coordinates": "13.7249,100.5369",
            "star_rating": 5,
            "address": "89 Soi Wat Suan Plu, New Road, Bangkok 10500, Thailand",
            "phone": "+66 2 236 7777",
            "email": "slbk@shangri-la.com",
            "website": "https://www.shangri-la.com/bangkok",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "The Imperial Hotel Tokyo",
            "rating": 4.4,
            "price_per_night": 450.0,
            "amenities": ["Imperial Palace views", "Traditional service", "Multiple restaurants", "Spa", "WiFi"],
            "booking_url": "https://www.imperialhotel.co.jp",
            "coordinates": "35.6751,139.7594",
            "star_rating": 5,
            "address": "1-1-1 Uchisaiwaicho, Chiyoda City, Tokyo 100-8558, Japan",
            "phone": "+81 3 3504 1111",
            "email": "hotel@imperialhotel.co.jp",
            "website": "https://www.imperialhotel.co.jp",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "Conrad Seoul",
            "rating": 4.5,
            "price_per_night": 320.0,
            "amenities": ["Han River views", "Modern luxury", "Spa", "Business center", "Multiple restaurants", "WiFi"],
            "booking_url": "https://www.hilton.com/conrad-seoul",
            "coordinates": "37.5326,126.9652",
            "star_rating": 5,
            "address": "10 Gukjegeumyung-ro, Yeongdeungpo-gu, Seoul 07326, South Korea",
            "phone": "+82 2 6137 7000",
            "email": "seoul_reservations@conradhotels.com",
            "website": "https://www.hilton.com/conrad-seoul",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "JW Marriott Hotel Jakarta",
            "rating": 4.3,
            "price_per_night": 180.0,
            "amenities": ["Business district", "Pool", "Spa", "Multiple restaurants", "Business center", "WiFi"],
            "booking_url": "https://www.marriott.com/jw-marriott-jakarta",
            "coordinates": "-6.2088,106.8456",
            "star_rating": 5,
            "address": "Jl. Dr. Ide Anak Agung Gde Agung, Mega Kuningan, Jakarta 12950, Indonesia",
            "phone": "+62 21 2551 5888",
            "email": "mhrs.cgkjw.reservations@marriott.com",
            "website": "https://www.marriott.com/jw-marriott-jakarta",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        }
    ]

def get_american_hotels_expansion():
    """Additional American hotels in new cities"""
    return [
        {
            "name": "The Ritz-Carlton Chicago",
            "rating": 4.5,
            "price_per_night": 520.0,
            "amenities": ["Magnificent Mile", "Spa", "Fine dining", "Business center", "City views", "WiFi"],
            "booking_url": "https://www.ritzcarlton.com/chicago",
            "coordinates": "41.8955,-87.6255",
            "star_rating": 5,
            "address": "160 E Pearson St, Chicago, IL 60611, USA",
            "phone": "+1 312 266 1000",
            "email": "chicago@ritzcarlton.com",
            "website": "https://www.ritzcarlton.com/chicago",
            "check_in_time": "16:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "Four Seasons Hotel Boston",
            "rating": 4.6,
            "price_per_night": 620.0,
            "amenities": ["Back Bay location", "Spa", "Fine dining", "Business center", "City views", "WiFi"],
            "booking_url": "https://www.fourseasons.com/boston",
            "coordinates": "42.3496,-71.0746",
            "star_rating": 5,
            "address": "200 Boylston St, Boston, MA 02116, USA",
            "phone": "+1 617 338 4400",
            "email": "reservations.boston@fourseasons.com",
            "website": "https://www.fourseasons.com/boston",
            "check_in_time": "16:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "The St. Regis Atlanta",
            "rating": 4.4,
            "price_per_night": 480.0,
            "amenities": ["Buckhead district", "Spa", "Fine dining", "Business center", "Butler service", "WiFi"],
            "booking_url": "https://www.marriott.com/stregis-atlanta",
            "coordinates": "33.8439,-84.3781",
            "star_rating": 5,
            "address": "88 W Paces Ferry Rd NW, Atlanta, GA 30305, USA",
            "phone": "+1 404 563 7900",
            "email": "stregis.atlanta@stregis.com",
            "website": "https://www.marriott.com/stregis-atlanta",
            "check_in_time": "16:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "Hotel Vancouver",
            "rating": 4.3,
            "price_per_night": 350.0,
            "amenities": ["Downtown location", "Historic hotel", "Spa", "Restaurant", "Business center", "WiFi"],
            "booking_url": "https://www.fairmont.com/hotel-vancouver",
            "coordinates": "49.2827,-123.1207",
            "star_rating": 4,
            "address": "900 W Georgia St, Vancouver, BC V6C 2W6, Canada",
            "phone": "+1 604 684 3131",
            "email": "vancouver@fairmont.com",
            "website": "https://www.fairmont.com/hotel-vancouver",
            "check_in_time": "16:00",
            "check_out_time": "11:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "The Westin Peachtree Plaza Atlanta",
            "rating": 4.2,
            "price_per_night": 220.0,
            "amenities": ["Downtown location", "Revolving restaurant", "Pool", "Business center", "WiFi", "City views"],
            "booking_url": "https://www.marriott.com/westin-peachtree-atlanta",
            "coordinates": "33.7601,-84.3871",
            "star_rating": 4,
            "address": "210 Peachtree St NW, Atlanta, GA 30303, USA",
            "phone": "+1 404 659 1400",
            "email": "westin.peachtree@westin.com",
            "website": "https://www.marriott.com/westin-peachtree-atlanta",
            "check_in_time": "16:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        }
    ]

def get_resort_hotels_expansion():
    """Resort and destination hotels"""
    return [
        {
            "name": "The Resort at Pedregal Cabo",
            "rating": 4.8,
            "price_per_night": 850.0,
            "amenities": ["Cliffside location", "Private beach", "Spa", "Multiple restaurants", "Pool", "WiFi"],
            "booking_url": "https://www.rosewoodhotels.com/pedregal",
            "coordinates": "22.8905,-109.9167",
            "star_rating": 5,
            "address": "Camino del Mar 1, Pedregal, Cabo San Lucas 23455, Mexico",
            "phone": "+52 624 163 4300",
            "email": "reservations.pedregal@rosewoodhotels.com",
            "website": "https://www.rosewoodhotels.com/pedregal",
            "check_in_time": "16:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 48 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "Four Seasons Resort Bali at Sayan",
            "rating": 4.9,
            "price_per_night": 750.0,
            "amenities": ["Rainforest setting", "River views", "Spa", "Infinity pool", "Fine dining", "WiFi"],
            "booking_url": "https://www.fourseasons.com/sayan",
            "coordinates": "-8.5069,115.2624",
            "star_rating": 5,
            "address": "Sayan, Ubud, Gianyar Regency, Bali 80571, Indonesia",
            "phone": "+62 361 977 577",
            "email": "reservations.sayan@fourseasons.com",
            "website": "https://www.fourseasons.com/sayan",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 48 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "The Oberoi Udaivilas",
            "rating": 4.8,
            "price_per_night": 680.0,
            "amenities": ["Palace architecture", "Lake views", "Spa", "Fine dining", "Boat transfers", "WiFi"],
            "booking_url": "https://www.oberoihotels.com/udaivilas",
            "coordinates": "24.5854,73.6897",
            "star_rating": 5,
            "address": "Haridasji Ki Magri, Udaipur, Rajasthan 313001, India",
            "phone": "+91 294 243 3300",
            "email": "reservations.udaivilas@oberoigroup.com",
            "website": "https://www.oberoihotels.com/udaivilas",
            "check_in_time": "14:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 48 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "Amangiri Utah",
            "rating": 4.9,
            "price_per_night": 1500.0,
            "amenities": ["Desert luxury", "Spa", "Adventure activities", "Fine dining", "Pool", "WiFi"],
            "booking_url": "https://www.aman.com/resorts/amangiri",
            "coordinates": "37.0625,-111.3991",
            "star_rating": 5,
            "address": "1 Kayenta Rd, Canyon Point, UT 84741, USA",
            "phone": "+1 435 675 3999",
            "email": "amangiri@aman.com",
            "website": "https://www.aman.com/resorts/amangiri",
            "check_in_time": "16:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 72 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "Belmond Hotel Caruso Ravello",
            "rating": 4.7,
            "price_per_night": 920.0,
            "amenities": ["Amalfi Coast views", "Historic palace", "Infinity pool", "Fine dining", "Spa", "WiFi"],
            "booking_url": "https://www.belmond.com/caruso",
            "coordinates": "40.6518,14.6116",
            "star_rating": 5,
            "address": "Piazza San Giovanni del Toro 2, 84010 Ravello SA, Italy",
            "phone": "+39 089 858 801",
            "email": "reservations.hca@belmond.com",
            "website": "https://www.belmond.com/caruso",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 48 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        }
    ]

def get_budget_expansion_hotels():
    """Additional budget and mid-range options"""
    return [
        {
            "name": "Pod Hotels Brooklyn",
            "rating": 4.1,
            "price_per_night": 150.0,
            "amenities": ["Modern design", "Rooftop bar", "Compact rooms", "WiFi", "24/7 front desk", "Local area"],
            "booking_url": "https://www.podhotels.com/brooklyn",
            "coordinates": "40.6892,-73.9442",
            "star_rating": 3,
            "address": "247 Metropolitan Ave, Brooklyn, NY 11211, USA",
            "phone": "+1 718 387 8181",
            "email": "brooklyn@podhotels.com",
            "website": "https://www.podhotels.com/brooklyn",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": False,
            "pet_friendly": False
        },
        {
            "name": "Generator London",
            "rating": 4.0,
            "price_per_night": 120.0,
            "amenities": ["Hostel-style", "Social spaces", "Bar", "WiFi", "24/7 reception", "Young travelers"],
            "booking_url": "https://www.generatorhostels.com/london",
            "coordinates": "51.5074,-0.1322",
            "star_rating": 3,
            "address": "37 Tavistock Pl, London WC1H 9SE, UK",
            "phone": "+44 20 7388 7666",
            "email": "london@generatorhostels.com",
            "website": "https://www.generatorhostels.com/london",
            "check_in_time": "15:00",
            "check_out_time": "11:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": False,
            "pet_friendly": False
        },
        {
            "name": "Hotel Zephyr San Francisco",
            "rating": 4.2,
            "price_per_night": 280.0,
            "amenities": ["Fisherman's Wharf", "Nautical theme", "Restaurant", "Business center", "WiFi", "Bay views"],
            "booking_url": "https://www.hotelzephyrsf.com",
            "coordinates": "37.8085,-122.4156",
            "star_rating": 4,
            "address": "250 Beach St, San Francisco, CA 94133, USA",
            "phone": "+1 415 617 6565",
            "email": "info@hotelzephyrsf.com",
            "website": "https://www.hotelzephyrsf.com",
            "check_in_time": "16:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "Ace Hotel Portland",
            "rating": 4.3,
            "price_per_night": 200.0,
            "amenities": ["Boutique style", "Local art", "Restaurant", "WiFi", "24/7 front desk", "Downtown"],
            "booking_url": "https://www.acehotel.com/portland",
            "coordinates": "45.5245,-122.6762",
            "star_rating": 4,
            "address": "1022 SW Stark St, Portland, OR 97205, USA",
            "phone": "+1 503 228 2277",
            "email": "portland@acehotel.com",
            "website": "https://www.acehotel.com/portland",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "Aloft Bangkok Sukhumvit 11",
            "rating": 4.1,
            "price_per_night": 140.0,
            "amenities": ["Modern design", "Pool", "Fitness center", "Restaurant", "WiFi", "Business center"],
            "booking_url": "https://www.marriott.com/aloft-bangkok-sukhumvit",
            "coordinates": "13.7440,100.5510",
            "star_rating": 4,
            "address": "35 Sukhumvit Soi 11, Klongtoey Nua, Wattana, Bangkok 10110, Thailand",
            "phone": "+66 2 207 7000",
            "email": "aloft.bangkoksukhumvit@marriott.com",
            "website": "https://www.marriott.com/aloft-bangkok-sukhumvit",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        }
    ]

def add_hotels_batch(supabase: Client, hotels_data: list, batch_name: str):
    """Add a batch of hotels with progress tracking"""
    print(f"\n🏨 Adding {batch_name} ({len(hotels_data)} hotels)...")
    successful = 0
    
    for i, hotel in enumerate(hotels_data):
        try:
            print(f"  {i+1:2d}. Adding: {hotel['name']}")
            result = supabase.table("hotels").insert(hotel).execute()
            if result.data:
                print(f"      ✅ Success")
                successful += 1
            else:
                print(f"      ❌ Failed - no data returned")
            time.sleep(0.5)  # Small delay to avoid overwhelming
        except Exception as e:
            print(f"      ❌ Error: {str(e)[:60]}...")
    
    print(f"✅ {batch_name}: {successful}/{len(hotels_data)} hotels added successfully")
    return successful

def main():
    load_dotenv()
    
    url = os.getenv('SUPABASE_URL')
    key = os.getenv('SUPABASE_KEY')
    
    if not url or not key:
        print("❌ Missing Supabase credentials")
        return
    
    try:
        supabase: Client = create_client(url, key)
        print("🏨 HOTELS DATABASE EXPANSION - PHASE 2")
        print("=" * 60)
        print("Adding 25+ additional hotels across new destinations...")
        
        total_successful = 0
        
        # Add European expansion
        total_successful += add_hotels_batch(supabase, get_european_hotels_expansion(), "European Hotels Expansion")
        
        # Add Asian expansion
        total_successful += add_hotels_batch(supabase, get_asian_hotels_expansion(), "Asian Hotels Expansion")
        
        # Add American expansion
        total_successful += add_hotels_batch(supabase, get_american_hotels_expansion(), "American Hotels Expansion")
        
        # Add resort hotels
        total_successful += add_hotels_batch(supabase, get_resort_hotels_expansion(), "Luxury Resort Hotels")
        
        # Add budget expansion
        total_successful += add_hotels_batch(supabase, get_budget_expansion_hotels(), "Budget & Boutique Hotels")
        
        # Final verification
        print("\n" + "=" * 60)
        print("📊 COMPREHENSIVE DATABASE SUMMARY")
        print("=" * 60)
        
        result = supabase.table('hotels').select('*').execute()
        total_hotels = len(result.data)
        
        print(f"🏨 TOTAL HOTELS IN DATABASE: {total_hotels}")
        print(f"✅ Successfully added in this session: {total_successful}")
        
        # Show distribution by star rating
        star_counts = {}
        cities = set()
        price_ranges = {"Ultra-Luxury ($1000+)": 0, "Luxury ($500-$999)": 0, "Premium ($200-$499)": 0, "Budget (<$200)": 0}
        
        for hotel in result.data:
            star = hotel.get('star_rating', 'Unknown')
            price = hotel.get('price_per_night', 0)
            
            # Extract city from address
            address = hotel.get('address', '')
            if ',' in address:
                city_part = address.split(',')[-2].strip() if len(address.split(',')) > 2 else address.split(',')[-1].strip()
                cities.add(city_part)
            
            star_counts[star] = star_counts.get(star, 0) + 1
            
            if price >= 1000:
                price_ranges["Ultra-Luxury ($1000+)"] += 1
            elif price >= 500:
                price_ranges["Luxury ($500-$999)"] += 1
            elif price >= 200:
                price_ranges["Premium ($200-$499)"] += 1
            else:
                price_ranges["Budget (<$200)"] += 1
        
        print(f"\n📊 Hotels by Star Rating:")
        for star in sorted(star_counts.keys(), reverse=True):
            print(f"  {star}⭐: {star_counts[star]} hotels")
        
        print(f"\n💰 Hotels by Price Range:")
        for range_name, count in price_ranges.items():
            print(f"  {range_name}: {count} hotels")
        
        print(f"\n🌍 Global Coverage:")
        print(f"  Cities/Regions: {len(cities)} destinations")
        
        print(f"\n🎯 Your massively expanded hotel database now includes:")
        print(f"  • Ultra-luxury resorts and exclusive properties")
        print(f"  • 5-star hotels in major global cities")
        print(f"  • Premium business and boutique hotels")
        print(f"  • Budget-friendly options across all destinations")
        print(f"  • Resort properties in exotic locations")
        print(f"  • Complete global coverage for travel packages")
        
        print(f"\n✅ HOTELS DATABASE MASSIVELY EXPANDED!")
        print(f"🚀 Ready for sophisticated AI travel package generation!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
