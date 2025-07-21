"""
Large-Scale Hotels Database Expansion
Adds 30+ premium hotels across multiple global destinations
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client
import time

def get_luxury_hotels_batch_1():
    """Premium 5-star hotels across major global destinations"""
    return [
        # MIDDLE EAST PREMIUM
        {
            "name": "Atlantis The Palm Dubai",
            "rating": 4.7,
            "price_per_night": 900.0,
            "amenities": ["Water park", "Aquarium", "Private beach", "Multiple restaurants", "Spa", "WiFi", "Pool"],
            "booking_url": "https://www.atlantis.com/dubai",
            "coordinates": "25.1308,55.1175",
            "star_rating": 5,
            "address": "Crescent Rd, The Palm Jumeirah, Dubai, UAE",
            "phone": "+971 4 426 2000",
            "email": "info@atlantisthepalm.com",
            "website": "https://www.atlantis.com/dubai",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 48 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "Four Seasons Resort Dubai at Jumeirah Beach",
            "rating": 4.8,
            "price_per_night": 850.0,
            "amenities": ["Private beach", "Spa", "Fine dining", "Pool", "Business center", "WiFi", "Fitness Center"],
            "booking_url": "https://www.fourseasons.com/dubai",
            "coordinates": "25.1004,55.1647",
            "star_rating": 5,
            "address": "Jumeirah Beach Rd, Dubai, UAE",
            "phone": "+971 4 270 7777",
            "email": "reservations.dubai@fourseasons.com",
            "website": "https://www.fourseasons.com/dubai",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "St. Regis Doha",
            "rating": 4.7,
            "price_per_night": 520.0,
            "amenities": ["Butler service", "Spa", "Fine dining", "Business center", "Pool", "WiFi", "Concierge"],
            "booking_url": "https://www.marriott.com/stregis-doha",
            "coordinates": "25.3548,51.5310",
            "star_rating": 5,
            "address": "Al Gassar Resort, Doha, Qatar",
            "phone": "+974 4446 0000",
            "email": "stregis.doha@stregis.com",
            "website": "https://www.marriott.com/stregis-doha",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        
        # EUROPEAN LUXURY
        {
            "name": "Claridge's London",
            "rating": 4.8,
            "price_per_night": 950.0,
            "amenities": ["Art Deco design", "Michelin dining", "Spa", "Butler service", "Business center", "WiFi"],
            "booking_url": "https://www.claridges.co.uk",
            "coordinates": "51.5130,-0.1479",
            "star_rating": 5,
            "address": "Brook St, Mayfair, London W1K 4HR, UK",
            "phone": "+44 20 7629 8860",
            "email": "info@claridges.co.uk",
            "website": "https://www.claridges.co.uk",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": False,
            "pet_friendly": True
        },
        {
            "name": "Le Bristol Paris",
            "rating": 4.9,
            "price_per_night": 1100.0,
            "amenities": ["Palace hotel", "Michelin restaurants", "Spa", "Garden", "Butler service", "WiFi"],
            "booking_url": "https://www.lebristolparis.com",
            "coordinates": "48.8682,2.3245",
            "star_rating": 5,
            "address": "112 Rue du Faubourg Saint-Honoré, 75008 Paris, France",
            "phone": "+33 1 53 43 43 00",
            "email": "resa@lebristolparis.com",
            "website": "https://www.lebristolparis.com",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 48 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "Hotel Adlon Kempinski Berlin",
            "rating": 4.8,
            "price_per_night": 720.0,
            "amenities": ["Brandenburg Gate views", "Spa", "Fine dining", "Business center", "Historic luxury", "WiFi"],
            "booking_url": "https://www.kempinski.com/berlin",
            "coordinates": "52.5163,13.3777",
            "star_rating": 5,
            "address": "Unter den Linden 77, 10117 Berlin, Germany",
            "phone": "+49 30 2261 0",
            "email": "reservations.adlon@kempinski.com",
            "website": "https://www.kempinski.com/berlin",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        }
    ]

def get_luxury_hotels_batch_2():
    """Asian luxury and premium hotels"""
    return [
        {
            "name": "Mandarin Oriental Tokyo",
            "rating": 4.8,
            "price_per_night": 950.0,
            "amenities": ["City views", "Michelin dining", "Spa", "Business facilities", "Fine dining", "WiFi"],
            "booking_url": "https://www.mandarinoriental.com/tokyo",
            "coordinates": "35.6795,139.7632",
            "star_rating": 5,
            "address": "2-1-1 Nihonbashi Muromachi, Chuo City, Tokyo 103-8328, Japan",
            "phone": "+81 3 3270 8800",
            "email": "motyo-reservations@mohg.com",
            "website": "https://www.mandarinoriental.com/tokyo",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "The St. Regis Bangkok",
            "rating": 4.7,
            "price_per_night": 420.0,
            "amenities": ["Butler service", "Spa", "Rooftop bar", "Fine dining", "Pool", "WiFi", "Business Center"],
            "booking_url": "https://www.marriott.com/stregis-bangkok",
            "coordinates": "13.7439,100.5417",
            "star_rating": 5,
            "address": "159 Rajadamri Rd, Lumphini, Pathum Wan District, Bangkok 10330, Thailand",
            "phone": "+66 2 207 7777",
            "email": "stregis.bangkok@stregis.com",
            "website": "https://www.marriott.com/stregis-bangkok",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "Shangri-La Hotel Singapore",
            "rating": 4.6,
            "price_per_night": 380.0,
            "amenities": ["Garden setting", "Pool", "Spa", "Multiple restaurants", "Business center", "WiFi"],
            "booking_url": "https://www.shangri-la.com/singapore",
            "coordinates": "1.3099,103.8256",
            "star_rating": 5,
            "address": "22 Orange Grove Rd, Singapore 258350",
            "phone": "+65 6737 3644",
            "email": "slsg@shangri-la.com",
            "website": "https://www.shangri-la.com/singapore",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "The Oberoi Mumbai",
            "rating": 4.7,
            "price_per_night": 320.0,
            "amenities": ["Ocean views", "Spa", "Fine dining", "Business center", "Pool", "WiFi", "Butler service"],
            "booking_url": "https://www.oberoihotels.com/mumbai",
            "coordinates": "19.0521,72.8239",
            "star_rating": 5,
            "address": "Nariman Point, Mumbai, Maharashtra 400021, India",
            "phone": "+91 22 6632 5757",
            "email": "reservations.mumbai@oberoigroup.com",
            "website": "https://www.oberoihotels.com/mumbai",
            "check_in_time": "14:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "Aman Tokyo",
            "rating": 4.9,
            "price_per_night": 1200.0,
            "amenities": ["Minimalist luxury", "Spa", "Fine dining", "City views", "Zen design", "WiFi"],
            "booking_url": "https://www.aman.com/resorts/aman-tokyo",
            "coordinates": "35.6762,139.7633",
            "star_rating": 5,
            "address": "1-5-6 Otemachi, Chiyoda City, Tokyo 100-0004, Japan",
            "phone": "+81 3 5224 3333",
            "email": "amantokyo@aman.com",
            "website": "https://www.aman.com/resorts/aman-tokyo",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 48 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "Grand Hyatt Hong Kong",
            "rating": 4.5,
            "price_per_night": 450.0,
            "amenities": ["Harbor views", "Multiple restaurants", "Spa", "Business center", "Pool", "WiFi"],
            "booking_url": "https://www.hyatt.com/grand-hyatt-hong-kong",
            "coordinates": "22.2783,114.1722",
            "star_rating": 5,
            "address": "1 Harbour Rd, Wan Chai, Hong Kong",
            "phone": "+852 2588 1234",
            "email": "hongkong.grand@hyatt.com",
            "website": "https://www.hyatt.com/grand-hyatt-hong-kong",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        }
    ]

def get_luxury_hotels_batch_3():
    """American luxury hotels"""
    return [
        {
            "name": "The St. Regis New York",
            "rating": 4.6,
            "price_per_night": 850.0,
            "amenities": ["Butler service", "Central location", "Spa", "Fine dining", "Business center", "WiFi"],
            "booking_url": "https://www.marriott.com/stregis-new-york",
            "coordinates": "40.7614,-73.9776",
            "star_rating": 5,
            "address": "2 E 55th St, New York, NY 10022, USA",
            "phone": "+1 212 753 4500",
            "email": "stregis.newyork@stregis.com",
            "website": "https://www.marriott.com/stregis-new-york",
            "check_in_time": "16:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "The Carlyle New York",
            "rating": 4.7,
            "price_per_night": 920.0,
            "amenities": ["Upper East Side", "Jazz club", "Spa", "Fine dining", "Art collection", "WiFi"],
            "booking_url": "https://www.rosewoodhotels.com/carlyle",
            "coordinates": "40.7740,-73.9631",
            "star_rating": 5,
            "address": "35 E 76th St, New York, NY 10021, USA",
            "phone": "+1 212 744 1600",
            "email": "reservations.carlyle@rosewoodhotels.com",
            "website": "https://www.rosewoodhotels.com/carlyle",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "The Ritz-Carlton San Francisco",
            "rating": 4.5,
            "price_per_night": 650.0,
            "amenities": ["Nob Hill location", "Spa", "Fine dining", "Business center", "City views", "WiFi"],
            "booking_url": "https://www.ritzcarlton.com/san-francisco",
            "coordinates": "37.7919,-122.4104",
            "star_rating": 5,
            "address": "600 Stockton St, San Francisco, CA 94108, USA",
            "phone": "+1 415 296 7465",
            "email": "sanfrancisco@ritzcarlton.com",
            "website": "https://www.ritzcarlton.com/san-francisco",
            "check_in_time": "16:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "Four Seasons Seattle",
            "rating": 4.7,
            "price_per_night": 620.0,
            "amenities": ["Waterfront views", "Spa", "Fine dining", "Business center", "Modern luxury", "WiFi"],
            "booking_url": "https://www.fourseasons.com/seattle",
            "coordinates": "47.6089,-122.3357",
            "star_rating": 5,
            "address": "99 Union St, Seattle, WA 98101, USA",
            "phone": "+1 206 749 7000",
            "email": "reservations.seattle@fourseasons.com",
            "website": "https://www.fourseasons.com/seattle",
            "check_in_time": "16:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "The Breakers Palm Beach",
            "rating": 4.6,
            "price_per_night": 580.0,
            "amenities": ["Oceanfront", "Golf course", "Spa", "Multiple restaurants", "Beach access", "WiFi"],
            "booking_url": "https://www.thebreakers.com",
            "coordinates": "26.7056,-80.0364",
            "star_rating": 5,
            "address": "1 S County Rd, Palm Beach, FL 33480, USA",
            "phone": "+1 561 655 6611",
            "email": "reservations@thebreakers.com",
            "website": "https://www.thebreakers.com",
            "check_in_time": "16:00",
            "check_out_time": "11:00",
            "cancellation_policy": "Free cancellation up to 48 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        }
    ]

def get_business_hotels_batch():
    """4-star business and premium hotels"""
    return [
        {
            "name": "Novotel London Canary Wharf",
            "rating": 4.2,
            "price_per_night": 220.0,
            "amenities": ["Business district", "Modern rooms", "Restaurant", "Fitness center", "WiFi", "River views"],
            "booking_url": "https://www.novotel.com/london-canary-wharf",
            "coordinates": "51.5074,-0.0278",
            "star_rating": 4,
            "address": "40 Marsh Wall, London E14 9TP, UK",
            "phone": "+44 20 7660 0777",
            "email": "h5309@accor.com",
            "website": "https://www.novotel.com/london-canary-wharf",
            "check_in_time": "14:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "Renaissance Paris Republique Hotel",
            "rating": 4.4,
            "price_per_night": 280.0,
            "amenities": ["Central location", "Modern design", "Restaurant", "Business center", "WiFi", "Fitness center"],
            "booking_url": "https://www.marriott.com/renaissance-paris-republique",
            "coordinates": "48.8675,2.3633",
            "star_rating": 4,
            "address": "40 Rue René Boulanger, 75010 Paris, France",
            "phone": "+33 1 71 18 79 79",
            "email": "renaissance.parisrepublique@marriott.com",
            "website": "https://www.marriott.com/renaissance-paris-republique",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "Hyatt Regency Tokyo",
            "rating": 4.3,
            "price_per_night": 350.0,
            "amenities": ["Shinjuku location", "Multiple restaurants", "Business center", "Fitness center", "WiFi", "City views"],
            "booking_url": "https://www.hyatt.com/regency-tokyo",
            "coordinates": "35.6938,139.7036",
            "star_rating": 4,
            "address": "2-7-2 Nishi Shinjuku, Shinjuku City, Tokyo 160-0023, Japan",
            "phone": "+81 3 3348 1234",
            "email": "tokyo.regency@hyatt.com",
            "website": "https://www.hyatt.com/regency-tokyo",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "InterContinental Sydney",
            "rating": 4.5,
            "price_per_night": 420.0,
            "amenities": ["Harbour views", "Opera House location", "Multiple restaurants", "Spa", "Business center", "WiFi"],
            "booking_url": "https://www.ihg.com/intercontinental/sydney",
            "coordinates": "-33.8634,151.2109",
            "star_rating": 4,
            "address": "117 Macquarie St, Sydney NSW 2000, Australia",
            "phone": "+61 2 9253 9000",
            "email": "sydney@ihg.com",
            "website": "https://www.ihg.com/intercontinental/sydney",
            "check_in_time": "15:00",
            "check_out_time": "11:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "Grand Hyatt Singapore",
            "rating": 4.4,
            "price_per_night": 320.0,
            "amenities": ["Orchard Road", "Shopping access", "Multiple restaurants", "Spa", "Pool", "WiFi"],
            "booking_url": "https://www.hyatt.com/grand-hyatt-singapore",
            "coordinates": "1.3048,103.8318",
            "star_rating": 4,
            "address": "10 Scotts Rd, Singapore 228211",
            "phone": "+65 6738 1234",
            "email": "singapore.grand@hyatt.com",
            "website": "https://www.hyatt.com/grand-hyatt-singapore",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "Courtyard by Marriott Frankfurt Airport",
            "rating": 4.3,
            "price_per_night": 180.0,
            "amenities": ["Airport shuttle", "Business center", "Restaurant", "Fitness center", "WiFi", "Meeting rooms"],
            "booking_url": "https://www.marriott.com/courtyard-frankfurt-airport",
            "coordinates": "50.0369,8.5622",
            "star_rating": 4,
            "address": "Unterschweinstiege 16, 60549 Frankfurt, Germany",
            "phone": "+49 69 69 71 99 0",
            "email": "reservations.frankfurtairport@marriott.com",
            "website": "https://www.marriott.com/courtyard-frankfurt-airport",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 6 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        }
    ]

def get_budget_hotels_batch():
    """Budget and mid-range hotels"""
    return [
        {
            "name": "citizenM London Shoreditch",
            "rating": 4.4,
            "price_per_night": 180.0,
            "amenities": ["Modern design", "Tech-savvy rooms", "Restaurant", "24/7 gym", "WiFi", "Business center"],
            "booking_url": "https://www.citizenm.com/london-shoreditch",
            "coordinates": "51.5211,-0.0825",
            "star_rating": 4,
            "address": "6 Holywell Ln, London EC2A 3ET, UK",
            "phone": "+44 20 3519 1680",
            "email": "shoreditch@citizenm.com",
            "website": "https://www.citizenm.com/london-shoreditch",
            "check_in_time": "14:00",
            "check_out_time": "11:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": False,
            "pet_friendly": False
        },
        {
            "name": "Moxy NYC Times Square",
            "rating": 4.2,
            "price_per_night": 250.0,
            "amenities": ["Times Square location", "Modern design", "Restaurant", "Fitness center", "WiFi", "24/7 market"],
            "booking_url": "https://www.marriott.com/moxy-nyc-times-square",
            "coordinates": "40.7614,-73.9847",
            "star_rating": 4,
            "address": "485 7th Ave, New York, NY 10018, USA",
            "phone": "+1 212 967 6699",
            "email": "moxy.nytimessquare@marriott.com",
            "website": "https://www.marriott.com/moxy-nyc-times-square",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": True
        },
        {
            "name": "ibis Dubai Al Barsha",
            "rating": 4.1,
            "price_per_night": 120.0,
            "amenities": ["Mall access", "Restaurant", "Business center", "WiFi", "Pool", "Family-friendly"],
            "booking_url": "https://www.ibis.com/dubai-al-barsha",
            "coordinates": "25.1138,55.2053",
            "star_rating": 3,
            "address": "Sheikh Zayed Rd, Al Barsha, Dubai, UAE",
            "phone": "+971 4 704 4444",
            "email": "h9321@accor.com",
            "website": "https://www.ibis.com/dubai-al-barsha",
            "check_in_time": "14:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "Hampton by Hilton Berlin City Centre",
            "rating": 4.3,
            "price_per_night": 140.0,
            "amenities": ["Central location", "Free breakfast", "Fitness center", "WiFi", "Business center", "Modern rooms"],
            "booking_url": "https://www.hilton.com/hampton-berlin",
            "coordinates": "52.5200,13.4050",
            "star_rating": 3,
            "address": "Mauerstraße 81-82, 10117 Berlin, Germany",
            "phone": "+49 30 259 269 0",
            "email": "berlin@hamptoninn.com",
            "website": "https://www.hilton.com/hampton-berlin",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "Holiday Inn Express Singapore Katong",
            "rating": 4.2,
            "price_per_night": 160.0,
            "amenities": ["Cultural district", "Free breakfast", "Business center", "WiFi", "Fitness center", "Local area"],
            "booking_url": "https://www.ihg.com/holidayinnexpress/singapore-katong",
            "coordinates": "1.3048,103.9048",
            "star_rating": 3,
            "address": "21 Joo Chiat Rd, Singapore 427131",
            "phone": "+65 6723 7001",
            "email": "info@hiekatong.com.sg",
            "website": "https://www.ihg.com/holidayinnexpress/singapore-katong",
            "check_in_time": "15:00",
            "check_out_time": "12:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": True,
            "pet_friendly": False
        },
        {
            "name": "Best Western Plus Tokyo Nippori",
            "rating": 4.0,
            "price_per_night": 140.0,
            "amenities": ["Station access", "Restaurant", "Business center", "WiFi", "Compact rooms", "Local transport"],
            "booking_url": "https://www.bestwestern.com/tokyo-nippori",
            "coordinates": "35.7281,139.7714",
            "star_rating": 3,
            "address": "2-20-1 Higashinippori, Arakawa City, Tokyo 116-0014, Japan",
            "phone": "+81 3 5615 7700",
            "email": "info@bw-nippori.com",
            "website": "https://www.bestwestern.com/tokyo-nippori",
            "check_in_time": "15:00",
            "check_out_time": "11:00",
            "cancellation_policy": "Free cancellation up to 24 hours before check-in",
            "wifi_available": True,
            "parking_available": False,
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
        print("🏨 LARGE-SCALE HOTELS DATABASE EXPANSION")
        print("=" * 60)
        print("Adding 30+ premium hotels across global destinations...")
        
        total_successful = 0
        
        # Add luxury hotels batch 1
        total_successful += add_hotels_batch(supabase, get_luxury_hotels_batch_1(), "Luxury Hotels Batch 1: Middle East & Europe")
        
        # Add luxury hotels batch 2
        total_successful += add_hotels_batch(supabase, get_luxury_hotels_batch_2(), "Luxury Hotels Batch 2: Asia Pacific")
        
        # Add luxury hotels batch 3
        total_successful += add_hotels_batch(supabase, get_luxury_hotels_batch_3(), "Luxury Hotels Batch 3: Americas")
        
        # Add business hotels
        total_successful += add_hotels_batch(supabase, get_business_hotels_batch(), "Business & 4-Star Hotels")
        
        # Add budget hotels
        total_successful += add_hotels_batch(supabase, get_budget_hotels_batch(), "Budget & Mid-Range Hotels")
        
        # Final verification
        print("\n" + "=" * 60)
        print("📊 EXPANDED DATABASE SUMMARY")
        print("=" * 60)
        
        result = supabase.table('hotels').select('*').execute()
        total_hotels = len(result.data)
        
        print(f"🏨 TOTAL HOTELS IN DATABASE: {total_hotels}")
        print(f"✅ Successfully added in this session: {total_successful}")
        
        # Show distribution by star rating
        star_counts = {}
        cities = set()
        price_ranges = {"Luxury ($500+)": 0, "Premium ($200-$500)": 0, "Budget (<$200)": 0}
        
        for hotel in result.data:
            star = hotel.get('star_rating', 'Unknown')
            price = hotel.get('price_per_night', 0)
            
            # Extract city from address or coordinates
            address = hotel.get('address', '')
            if ',' in address:
                city_part = address.split(',')[-2].strip() if len(address.split(',')) > 2 else address.split(',')[-1].strip()
                cities.add(city_part)
            
            star_counts[star] = star_counts.get(star, 0) + 1
            
            if price >= 500:
                price_ranges["Luxury ($500+)"] += 1
            elif price >= 200:
                price_ranges["Premium ($200-$500)"] += 1
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
        
        print(f"\n🎯 Your expanded hotel database now includes:")
        print(f"  • World-class luxury resorts and 5-star hotels")
        print(f"  • Premium business hotels in major cities")
        print(f"  • Budget-friendly options for all travelers")
        print(f"  • Hotels across multiple continents and time zones")
        print(f"  • Complete amenities and booking information")
        
        print(f"\n✅ HOTELS DATABASE SIGNIFICANTLY EXPANDED!")
        print(f"Ready for enhanced travel package generation! 🎉")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
