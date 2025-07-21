"""
Final Hotels Database Comprehensive Analysis
Complete overview of the massively expanded hotels database
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client

def main():
    load_dotenv()
    
    url = os.getenv('SUPABASE_URL')
    key = os.getenv('SUPABASE_KEY')
    
    if not url or not key:
        print("❌ Missing Supabase credentials")
        return
    
    try:
        supabase: Client = create_client(url, key)
        print("🏨 COMPREHENSIVE HOTELS DATABASE ANALYSIS")
        print("=" * 70)
        
        result = supabase.table('hotels').select('*').execute()
        hotels = result.data
        
        print(f"📊 TOTAL HOTELS: {len(hotels)}")
        print(f"🎯 Database Growth: From 11 → {len(hotels)} hotels ({len(hotels)-11:+d} added)")
        print("=" * 70)
        
        # Analyze by star rating
        star_analysis = {}
        price_analysis = {"Ultra-Luxury ($1000+)": [], "Luxury ($500-$999)": [], "Premium ($200-$499)": [], "Budget (<$200)": []}
        city_analysis = {}
        country_analysis = {}
        amenities_count = {}
        
        total_value = 0
        
        for hotel in hotels:
            # Star rating analysis
            stars = hotel.get('star_rating', 0)
            star_analysis[stars] = star_analysis.get(stars, 0) + 1
            
            # Price analysis
            price = hotel.get('price_per_night', 0)
            total_value += price
            hotel_name = hotel.get('name', 'Unknown')
            
            if price >= 1000:
                price_analysis["Ultra-Luxury ($1000+)"].append(hotel_name)
            elif price >= 500:
                price_analysis["Luxury ($500-$999)"].append(hotel_name)
            elif price >= 200:
                price_analysis["Premium ($200-$499)"].append(hotel_name)
            else:
                price_analysis["Budget (<$200)"].append(hotel_name)
            
            # Geographic analysis
            address = hotel.get('address', '')
            if ',' in address:
                parts = address.split(',')
                city = parts[-2].strip() if len(parts) > 2 else parts[-1].strip()
                country = parts[-1].strip()
                
                city_analysis[city] = city_analysis.get(city, 0) + 1
                country_analysis[country] = country_analysis.get(country, 0) + 1
            
            # Amenities analysis
            amenities = hotel.get('amenities', [])
            if isinstance(amenities, list):
                for amenity in amenities:
                    amenities_count[amenity] = amenities_count.get(amenity, 0) + 1
        
        # Display star rating breakdown
        print("⭐ STAR RATING DISTRIBUTION:")
        for stars in sorted(star_analysis.keys(), reverse=True):
            count = star_analysis[stars]
            percentage = (count / len(hotels)) * 100
            print(f"  {stars}⭐: {count:2d} hotels ({percentage:4.1f}%)")
        
        # Display price range analysis
        print(f"\n💰 PRICE RANGE ANALYSIS:")
        for range_name, hotel_list in price_analysis.items():
            count = len(hotel_list)
            percentage = (count / len(hotels)) * 100
            print(f"  {range_name}: {count:2d} hotels ({percentage:4.1f}%)")
        
        avg_price = total_value / len(hotels) if hotels else 0
        print(f"\n💵 PRICING STATISTICS:")
        print(f"  Average Price: ${avg_price:.2f} per night")
        print(f"  Total Portfolio Value: ${total_value:,.2f} per night")
        
        # Display geographic coverage
        print(f"\n🌍 GEOGRAPHIC COVERAGE:")
        print(f"  Countries: {len(country_analysis)} nations")
        print(f"  Cities: {len(city_analysis)} destinations")
        
        # Top countries by hotel count
        top_countries = sorted(country_analysis.items(), key=lambda x: x[1], reverse=True)[:10]
        print(f"\n🏙️ TOP DESTINATIONS BY HOTEL COUNT:")
        for i, (country, count) in enumerate(top_countries, 1):
            print(f"  {i:2d}. {country}: {count} hotels")
        
        # Top amenities
        top_amenities = sorted(amenities_count.items(), key=lambda x: x[1], reverse=True)[:15]
        print(f"\n🎯 MOST COMMON AMENITIES:")
        for i, (amenity, count) in enumerate(top_amenities, 1):
            percentage = (count / len(hotels)) * 100
            print(f"  {i:2d}. {amenity}: {count} hotels ({percentage:4.1f}%)")
        
        # Sample ultra-luxury hotels
        ultra_luxury = price_analysis["Ultra-Luxury ($1000+)"]
        if ultra_luxury:
            print(f"\n✨ ULTRA-LUXURY PROPERTIES (${1000}+ per night):")
            for i, hotel in enumerate(ultra_luxury, 1):
                print(f"  {i}. {hotel}")
        
        # Sample budget options
        budget_hotels = price_analysis["Budget (<$200)"][:5]
        if budget_hotels:
            print(f"\n💡 BUDGET-FRIENDLY OPTIONS (<$200 per night):")
            for i, hotel in enumerate(budget_hotels, 1):
                print(f"  {i}. {hotel}")
        
        print(f"\n" + "=" * 70)
        print("🎊 DATABASE EXPANSION SUCCESS SUMMARY")
        print("=" * 70)
        print(f"✅ Started with: 11 hotels")
        print(f"🚀 Expanded to: {len(hotels)} hotels")
        print(f"📈 Growth Rate: {((len(hotels)-11)/11)*100:.0f}% increase")
        print(f"🌟 Star Coverage: {min(star_analysis.keys())}⭐ to {max(star_analysis.keys())}⭐")
        print(f"💰 Price Range: ${min(h.get('price_per_night', 0) for h in hotels):.0f} - ${max(h.get('price_per_night', 0) for h in hotels):.0f}")
        print(f"🌍 Global Reach: {len(country_analysis)} countries, {len(city_analysis)} cities")
        print(f"🏨 Hotel Types: Luxury resorts, business hotels, boutique properties, budget options")
        
        print(f"\n🎯 YOUR AI TRAVEL AGENT NOW HAS ACCESS TO:")
        print(f"  • Comprehensive global hotel inventory")
        print(f"  • All price ranges and accommodation types")
        print(f"  • Detailed amenities and booking information")
        print(f"  • Complete contact details and policies")
        print(f"  • Geographic coordinates for location services")
        print(f"  • Professional hotel ratings and reviews")
        
        print(f"\n🚀 READY FOR ADVANCED TRAVEL PACKAGE GENERATION!")
        print(f"Your AI can now create sophisticated, diverse travel recommendations! ✈️🏨")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
