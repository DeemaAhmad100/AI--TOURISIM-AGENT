"""
🌍 Enhanced AI Travel Platform - Enhanced Streamlit UI
Beautiful and intuitive user interface for the AI Travel Platform
Integrated with database booking system and payment processing
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import sys
import os
from pathlib import Path

# Add current directory to path for imports
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

# Import our enhanced booking system
from database_enhanced_booking_system import DatabaseEnhancedBookingSystem, BookingType, BookingStatus

# Import Supabase for direct database access
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="🌍 Enhanced AI Travel Platform",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS for investor presentation
st.markdown("""
<style>
/* Professional Header Design */
.main-header {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #667eea 100%);
    padding: 3rem;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 3rem;
    box-shadow: 0 20px 60px rgba(30,60,114,0.3);
    position: relative;
    overflow: hidden;
}

.main-header::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
    pointer-events: none;
}

.main-header h1 {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

.main-header h3 {
    font-size: 1.5rem;
    font-weight: 400;
    opacity: 0.95;
    margin-bottom: 1rem;
}

.investor-badge {
    display: inline-block;
    background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
    color: white;
    padding: 0.5rem 1.5rem;
    border-radius: 25px;
    font-weight: bold;
    font-size: 0.9rem;
    margin-top: 1rem;
    box-shadow: 0 4px 15px rgba(255,107,107,0.3);
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

/* Professional Feature Cards for Investors */
.feature-card {
    background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
    padding: 2rem;
    border-radius: 20px;
    border: 1px solid #e9ecef;
    margin: 1.5rem 0;
    box-shadow: 0 10px 40px rgba(0,0,0,0.08);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.feature-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
}

.feature-card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 25px 60px rgba(0,0,0,0.15);
    border-color: #667eea;
}

.feature-card h4 {
    font-size: 1.4rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 1rem;
}

.feature-card p {
    color: #6c757d;
    font-size: 1rem;
    line-height: 1.6;
}

/* Investor-Grade Metrics */
.metric-card {
    background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
    padding: 2rem;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
    border: 1px solid #e9ecef;
    transition: all 0.3s ease;
    position: relative;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.12);
}

.metric-card h2 {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}

.metric-card p {
    font-size: 1.1rem;
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.metric-growth {
    font-size: 0.9rem;
    color: #28a745;
    font-weight: 600;
}

/* Premium Package Cards */
.package-card {
    background: linear-gradient(145deg, #f8f9fa 0%, #ffffff 100%);
    padding: 2rem;
    border-radius: 20px;
    border-left: 6px solid #007bff;
    margin: 2rem 0;
    box-shadow: 0 12px 40px rgba(0,0,0,0.1);
    position: relative;
    overflow: hidden;
}

.package-card::after {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 100px;
    height: 100px;
    background: linear-gradient(135deg, rgba(102,126,234,0.1) 0%, rgba(118,75,162,0.1) 100%);
    border-radius: 50%;
    transform: translate(50%, -50%);
}

/* Premium Price Tags */
.price-tag {
    background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
    color: white;
    padding: 1rem 2rem;
    border-radius: 30px;
    font-weight: 700;
    font-size: 1.3rem;
    text-align: center;
    box-shadow: 0 8px 25px rgba(40,167,69,0.4);
    position: relative;
    overflow: hidden;
}

.price-tag::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s;
}

.price-tag:hover::before {
    left: 100%;
}

/* ROI and Investment Appeal */
.roi-card {
    background: linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%);
    padding: 2rem;
    border-radius: 20px;
    color: #2d3436;
    margin: 2rem 0;
    box-shadow: 0 12px 40px rgba(253,203,110,0.3);
    border: 2px solid #fdcb6e;
}

.competitive-advantage {
    background: linear-gradient(135deg, #a29bfe 0%, #6c5ce7 100%);
    padding: 2rem;
    border-radius: 20px;
    color: white;
    margin: 2rem 0;
    box-shadow: 0 12px 40px rgba(108,92,231,0.3);
}

/* Market Opportunity */
.market-size {
    background: linear-gradient(135deg, #fd79a8 0%, #e84393 100%);
    padding: 2rem;
    border-radius: 20px;
    color: white;
    margin: 2rem 0;
    box-shadow: 0 12px 40px rgba(232,67,147,0.3);
}

/* Technology Stack */
.tech-stack {
    background: linear-gradient(145deg, #e17055 0%, #d63031 100%);
    padding: 2rem;
    border-radius: 20px;
    color: white;
    margin: 2rem 0;
    box-shadow: 0 12px 40px rgba(214,48,49,0.3);
}

/* Success Stories */
.success-story {
    background: linear-gradient(145deg, #00b894 0%, #00a085 100%);
    padding: 2rem;
    border-radius: 20px;
    color: white;
    margin: 2rem 0;
    box-shadow: 0 12px 40px rgba(0,184,148,0.3);
}

/* Call-to-Action for Investors */
.investor-cta {
    background: linear-gradient(135deg, #ff7675 0%, #e17055 100%);
    padding: 3rem;
    border-radius: 25px;
    color: white;
    text-align: center;
    margin: 3rem 0;
    box-shadow: 0 20px 60px rgba(255,118,117,0.4);
    position: relative;
    overflow: hidden;
}

.investor-cta::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Ccircle cx='30' cy='30' r='4'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    pointer-events: none;
}

/* Responsive Design */
@media (max-width: 768px) {
    .main-header h1 {
        font-size: 2.5rem;
    }
    
    .metric-card h2 {
        font-size: 2rem;
    }
    
    .feature-card, .package-card {
        padding: 1.5rem;
    }
}

.savings-tag {
    background: linear-gradient(135deg, #fd7e14 0%, #ffc107 100%);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: bold;
    box-shadow: 0 3px 10px rgba(253,126,20,0.3);
}

.feature-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    text-align: center;
}

.booking-success {
    background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 5px solid #28a745;
    margin: 1rem 0;
}

.hotel-card {
    background: linear-gradient(145deg, #e3f2fd 0%, #f8f9fa 100%);
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 4px solid #2196f3;
    margin: 1rem 0;
}

.restaurant-card {
    background: linear-gradient(145deg, #f3e5f5 0%, #f8f9fa 100%);
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 4px solid #9c27b0;
    margin: 1rem 0;
}

.activity-card {
    background: linear-gradient(145deg, #e8f5e8 0%, #f8f9fa 100%);
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 4px solid #4caf50;
    margin: 1rem 0;
}

.metric-card {
    background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
    padding: 1rem;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

/* Enhanced Package Interface Styles */
.package-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    padding: 1.5rem;
    border-radius: 12px;
    border-left: 4px solid #1e3a8a;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    margin-bottom: 1rem;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.package-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.package-card::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 100px;
    height: 100px;
    background: linear-gradient(45deg, transparent 50%, rgba(59, 130, 246, 0.1) 50%);
}

.package-card h4 {
    color: #1e3a8a;
    margin-bottom: 0.75rem;
    font-weight: 600;
}

.package-card .price-tag {
    background: linear-gradient(135deg, #10b981, #059669);
    color: white;
    padding: 0.75rem 1.25rem;
    border-radius: 8px;
    text-align: center;
    font-weight: 600;
    margin: 1rem 0;
    box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
}

.hotel-card {
    background: linear-gradient(135deg, #ffffff 0%, #fefefe 100%);
    padding: 1.25rem;
    border-radius: 10px;
    border-left: 3px solid #3b82f6;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    margin-bottom: 1rem;
    transition: transform 0.2s ease;
}

.hotel-card:hover {
    transform: translateX(5px);
}

.hotel-card h4 {
    color: #1e3a8a;
    margin-bottom: 0.5rem;
}

.restaurant-card {
    background: linear-gradient(135deg, #fff7ed 0%, #ffffff 100%);
    padding: 1.25rem;
    border-radius: 10px;
    border-left: 3px solid #f59e0b;
    box-shadow: 0 2px 8px rgba(245, 158, 11, 0.1);
    margin-bottom: 1rem;
    transition: transform 0.2s ease;
}

.restaurant-card:hover {
    transform: translateX(5px);
}

.restaurant-card h4 {
    color: #f59e0b;
    margin-bottom: 0.5rem;
}

.activity-card {
    background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 100%);
    padding: 1.25rem;
    border-radius: 10px;
    border-left: 3px solid #10b981;
    box-shadow: 0 2px 8px rgba(16, 185, 129, 0.1);
    margin-bottom: 1rem;
    transition: transform 0.2s ease;
}

.activity-card:hover {
    transform: translateX(5px);
}

.activity-card h4 {
    color: #10b981;
    margin-bottom: 0.5rem;
}

.booking-success {
    background: linear-gradient(135deg, #f0fdf4 0%, #ffffff 100%);
    padding: 2rem;
    border-radius: 12px;
    border: 2px solid #22c55e;
    box-shadow: 0 8px 25px rgba(34, 197, 94, 0.15);
    margin: 1.5rem 0;
    text-align: center;
}

.booking-success h3 {
    color: #22c55e;
    margin-bottom: 1rem;
}

/* Enhanced buttons */
.stButton > button {
    border-radius: 8px;
    font-weight: 500;
    transition: all 0.2s ease;
    border: none;
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'booking_system' not in st.session_state:
    st.session_state.booking_system = DatabaseEnhancedBookingSystem()
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'name': 'Alex Thompson',
        'age': 32,
        'interests': ['cultural experiences', 'local cuisine', 'photography', 'art galleries'],
        'travel_style': 'cultural explorer',
        'budget_preference': 'moderate',
        'dietary_restrictions': ['vegetarian'],
        'preferred_activities': ['museums', 'food tours', 'walking tours', 'local markets'],
        'accommodation_style': 'boutique hotels',
        'trip_pace': 'relaxed'
    }
if 'current_package' not in st.session_state:
    st.session_state.current_package = None
if 'generated_packages' not in st.session_state:
    st.session_state.generated_packages = []
if 'viewing_package_details' not in st.session_state:
    st.session_state.viewing_package_details = None
if 'booking_history' not in st.session_state:
    st.session_state.booking_history = []
if 'selected_hotels' not in st.session_state:
    st.session_state.selected_hotels = []

# Initialize Supabase client for direct database access
@st.cache_resource
def get_supabase_client():
    """Get Supabase client"""
    try:
        load_dotenv()
        
        # Try multiple possible environment variable names
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_ANON_KEY") or os.getenv("SUPABASE_KEY")
        
        if not supabase_url or not supabase_key:
            st.warning("⚠️ Database credentials not found. Using fallback data.")
            return None
            
        return create_client(supabase_url, supabase_key)
    except Exception as e:
        st.warning(f"⚠️ Database connection unavailable: {str(e)}")
        return None

# Database helper functions
def get_all_destinations():
    """Get all destinations from database"""
    try:
        supabase = get_supabase_client()
        if supabase:
            # Query the destinations table for names
            result = supabase.table("destinations").select("name").execute()
            if result.data:
                destinations = [dest['name'] for dest in result.data if dest.get('name')]
                return sorted(list(set(destinations)))  # Remove duplicates and sort
    except Exception as e:
        st.info(f"📡 Using offline data (Database: {str(e)})")
    
    # Fallback to enhanced hardcoded list if database fails
    return [
        "Beirut, Lebanon", "Dubai, UAE", "Paris, France", "London, UK", 
        "New York, USA", "Tokyo, Japan", "Istanbul, Turkey", "Rome, Italy",
        "Barcelona, Spain", "Amsterdam, Netherlands", "Bangkok, Thailand",
        "Sydney, Australia", "Cairo, Egypt", "Mumbai, India", "Berlin, Germany"
    ]

def get_all_cities():
    """Get all cities from database for restaurant booking"""
    try:
        supabase = get_supabase_client()
        if supabase:
            # Query for city column specifically
            result = supabase.table("destinations").select("city").execute()
            if result.data:
                cities = [dest['city'] for dest in result.data if dest.get('city')]
                return sorted(list(set(cities)))  # Remove duplicates and sort
    except Exception as e:
        # If city column query fails, try to extract from name
        try:
            supabase = get_supabase_client()
            if supabase:
                result = supabase.table("destinations").select("name").execute()
                if result.data:
                    cities = []
                    for dest in result.data:
                        if dest.get('name'):
                            # Extract city from full name (e.g., "Paris, France" -> "Paris")
                            city = dest['name'].split(',')[0].strip()
                            cities.append(city)
                    return sorted(list(set(cities)))
        except Exception as e2:
            st.info(f"📡 Using offline data (Database: {str(e)})")
    
    # Fallback to enhanced hardcoded list if database fails
    return [
        "Beirut", "Dubai", "Paris", "London", "New York", "Tokyo", 
        "Istanbul", "Rome", "Barcelona", "Amsterdam", "Bangkok",
        "Sydney", "Cairo", "Mumbai", "Berlin"
    ]

# AI-Powered Package Generation System
def generate_personalized_package(user_prompt, profile, destination, duration, travelers, budget):
    """Generate a comprehensive, destination-specific travel package based on user's dream trip description"""
    
    # Extract destination details for context
    destination_info = get_destination_intelligence(destination)
    budget_level = extract_budget_level(budget)
    
    # Create package style based on user prompt analysis
    package_style = analyze_user_prompt_for_style(user_prompt, profile)
    
    # Generate truly diverse package components
    package = {
        'id': f"pkg_{len(st.session_state.generated_packages) + 1}",
        'title': f"{destination} {package_style['title']}",
        'destination': destination,
        'duration': duration,
        'travelers': travelers,
        'budget_level': budget_level,
        'focus': package_style['focus'],
        'user_prompt_analysis': analyze_trip_desires(user_prompt),
        'created_at': datetime.now(),
        
        # Generate destination-specific components
        'flights': generate_destination_specific_flights(destination, travelers, budget_level),
        'hotels': generate_destination_specific_hotels(destination, duration, travelers, budget_level, profile, user_prompt),
        'restaurants': generate_destination_specific_restaurants(destination, profile, user_prompt, budget_level),
        'activities': generate_destination_specific_activities(destination, profile, user_prompt, budget_level),
        'local_experiences': generate_destination_specific_local_experiences(destination, profile, user_prompt),
        
        # Generate truly unique daily itinerary
        'daily_itinerary': generate_intelligent_daily_itinerary(destination, duration, profile, user_prompt, package_style),
        
        # Accurate pricing
        'pricing': calculate_destination_specific_pricing(destination, duration, travelers, budget_level, package_style)
    }
    
    return package

def get_destination_intelligence(destination):
    """Get comprehensive destination intelligence"""
    destination_data = {
        'China': {
            'cities': ['Beijing', 'Shanghai', 'Xi\'an', 'Guilin', 'Chengdu', 'Hong Kong'],
            'culture': 'Ancient Chinese civilization with modern development',
            'cuisine': 'Diverse regional cuisines - Peking duck, dim sum, Sichuan hotpot',
            'landmarks': ['Great Wall', 'Forbidden City', 'Terracotta Army', 'Li River'],
            'transportation': ['High-speed rail', 'Metro systems', 'Taxi', 'DiDi rideshare'],
            'currency': 'Chinese Yuan (CNY)',
            'language': 'Mandarin Chinese',
            'experiences': ['Calligraphy classes', 'Tea ceremonies', 'Martial arts', 'Traditional markets'],
            'shopping': ['Silk Street Market', 'Wangfujing', 'Traditional crafts', 'Tea shops'],
            'nightlife': ['Traditional opera', 'Modern bars', 'Night markets', 'KTV'],
            'budget_ranges': {'budget': 50, 'moderate': 120, 'luxury': 300},
            'typical_activities': ['Temple visits', 'Garden walks', 'Cultural shows', 'Food tours'],
            'airports': ['Beijing Capital (PEK)', 'Shanghai Pudong (PVG)'],
            'climate': 'Varies by region - temperate to subtropical'
        },
        'Paris, France': {
            'cities': ['Paris', 'Versailles', 'Fontainebleau'],
            'culture': 'French art, fashion, and culinary excellence',
            'cuisine': 'French cuisine - croissants, wine, cheese, fine dining',
            'landmarks': ['Eiffel Tower', 'Louvre', 'Notre-Dame', 'Arc de Triomphe'],
            'transportation': ['Metro', 'Bus', 'Taxi', 'Walking'],
            'currency': 'Euro (EUR)',
            'language': 'French',
            'experiences': ['Wine tasting', 'Cooking classes', 'Art workshops', 'Fashion tours'],
            'shopping': ['Champs-Élysées', 'Le Marais', 'Galleries Lafayette', 'Vintage boutiques'],
            'nightlife': ['Wine bars', 'Cabarets', 'Jazz clubs', 'Seine river cruises'],
            'budget_ranges': {'budget': 80, 'moderate': 180, 'luxury': 400},
            'typical_activities': ['Museum visits', 'Café culture', 'Market exploration', 'Architecture tours'],
            'airports': ['Charles de Gaulle (CDG)', 'Orly (ORY)'],
            'climate': 'Temperate oceanic climate'
        },
        'Tokyo, Japan': {
            'cities': ['Tokyo', 'Kyoto', 'Osaka', 'Nikko'],
            'culture': 'Traditional Japanese culture meets modern innovation',
            'cuisine': 'Japanese cuisine - sushi, ramen, tempura, kaiseki',
            'landmarks': ['Tokyo Tower', 'Senso-ji Temple', 'Imperial Palace', 'Mount Fuji'],
            'transportation': ['JR trains', 'Subway', 'Taxi', 'Shinkansen'],
            'currency': 'Japanese Yen (JPY)',
            'language': 'Japanese',
            'experiences': ['Tea ceremony', 'Sushi making', 'Onsen baths', 'Traditional crafts'],
            'shopping': ['Shibuya', 'Harajuku', 'Traditional markets', 'Department stores'],
            'nightlife': ['Izakaya', 'Karaoke', 'Night markets', 'Robot restaurants'],
            'budget_ranges': {'budget': 70, 'moderate': 160, 'luxury': 350},
            'typical_activities': ['Temple visits', 'Garden meditation', 'Tech experiences', 'Food tours'],
            'airports': ['Narita (NRT)', 'Haneda (HND)'],
            'climate': 'Humid subtropical climate'
        }
    }
    
    # Find best match for destination
    for key, data in destination_data.items():
        if key.lower() in destination.lower() or any(city.lower() in destination.lower() for city in data['cities']):
            return data
    
    # Default fallback
    return destination_data.get(destination, {
        'cities': [destination],
        'culture': f'{destination} local culture',
        'cuisine': f'{destination} local cuisine',
        'landmarks': [f'{destination} landmarks'],
        'transportation': ['Local transport'],
        'currency': 'Local currency',
        'language': 'Local language',
        'experiences': ['Local experiences'],
        'shopping': ['Local shopping'],
        'nightlife': ['Local nightlife'],
        'budget_ranges': {'budget': 60, 'moderate': 150, 'luxury': 300},
        'typical_activities': ['Sightseeing', 'Cultural activities'],
        'airports': [f'{destination} Airport'],
        'climate': 'Local climate'
    })

def extract_budget_level(budget_string):
    """Extract budget level from budget string"""
    if 'Budget' in budget_string:
        return 'budget'
    elif 'Moderate' in budget_string:
        return 'moderate'
    elif 'Luxury' in budget_string:
        return 'luxury'
    return 'moderate'

def analyze_trip_desires(user_prompt):
    """Analyze user's trip description for key desires and interests"""
    prompt_lower = user_prompt.lower()
    
    desires = {
        'cultural_interest': any(word in prompt_lower for word in ['culture', 'history', 'traditional', 'heritage', 'museums', 'art']),
        'food_focus': any(word in prompt_lower for word in ['food', 'cuisine', 'cooking', 'restaurants', 'street food', 'culinary']),
        'adventure_seeking': any(word in prompt_lower for word in ['adventure', 'hiking', 'sports', 'active', 'outdoor', 'exciting']),
        'photography_interest': any(word in prompt_lower for word in ['photography', 'photos', 'instagram', 'scenic', 'capture']),
        'relaxation_focus': any(word in prompt_lower for word in ['relax', 'peaceful', 'calm', 'spa', 'tranquil', 'unwind']),
        'local_immersion': any(word in prompt_lower for word in ['local', 'authentic', 'hidden', 'off the beaten', 'real']),
        'luxury_preference': any(word in prompt_lower for word in ['luxury', 'premium', 'high-end', 'exclusive', 'VIP']),
        'budget_conscious': any(word in prompt_lower for word in ['budget', 'affordable', 'cheap', 'save money', 'economical'])
    }
    
    return desires

def analyze_user_prompt_for_style(user_prompt, profile):
    """Analyze user's dream trip description to determine package style"""
    prompt_lower = user_prompt.lower()
    
    # Analyze keywords in user prompt
    style_indicators = {
        'cultural-immersive': ['culture', 'history', 'traditional', 'heritage', 'museums', 'art', 'local customs'],
        'culinary-focused': ['food', 'cuisine', 'cooking', 'restaurants', 'street food', 'markets', 'dining'],
        'adventure-active': ['adventure', 'hiking', 'sports', 'active', 'outdoor', 'trekking', 'climbing'],
        'luxury-premium': ['luxury', 'premium', 'high-end', 'exclusive', 'private', 'spa', 'boutique'],
        'budget-conscious': ['budget', 'affordable', 'cheap', 'economical', 'save money', 'cost-effective'],
        'photography-focused': ['photography', 'photos', 'instagram', 'scenic', 'landscapes', 'portraits'],
        'family-friendly': ['family', 'kids', 'children', 'safe', 'child-friendly', 'educational'],
        'romantic-couples': ['romantic', 'couples', 'honeymoon', 'intimate', 'private', 'sunset']
    }
    
    # Score each style
    style_scores = {}
    for style, keywords in style_indicators.items():
        score = sum(1 for keyword in keywords if keyword in prompt_lower)
        if score > 0:
            style_scores[style] = score
    
    # Determine primary style
    if style_scores:
        primary_style = max(style_scores, key=style_scores.get)
    else:
        primary_style = 'cultural-immersive'  # Default
    
    # Generate style configuration
    style_configs = {
        'cultural-immersive': {
            'title': 'Cultural Heritage Explorer',
            'focus': 'Deep cultural immersion with historical sites and local traditions'
        },
        'culinary-focused': {
            'title': 'Culinary Discovery Journey',
            'focus': 'Authentic local cuisine and cooking experiences'
        },
        'adventure-active': {
            'title': 'Adventure & Active Explorer',
            'focus': 'Outdoor adventures and active experiences'
        },
        'luxury-premium': {
            'title': 'Premium Luxury Experience',
            'focus': 'High-end accommodations and exclusive experiences'
        },
        'budget-conscious': {
            'title': 'Smart Budget Explorer',
            'focus': 'Maximum value with authentic local experiences'
        },
        'photography-focused': {
            'title': 'Photography Expedition',
            'focus': 'Stunning photography opportunities and scenic locations'
        },
        'family-friendly': {
            'title': 'Family Adventure',
            'focus': 'Safe, educational, and fun experiences for all ages'
        },
        'romantic-couples': {
            'title': 'Romantic Getaway',
            'focus': 'Intimate and romantic experiences for couples'
        }
    }
    
    return style_configs.get(primary_style, style_configs['cultural-immersive'])

def generate_destination_specific_flights(destination, travelers, budget_level):
    """Generate accurate, destination-specific flight options"""
    
    destination_info = get_destination_intelligence(destination)
    
    # Realistic airline partnerships by destination
    airline_data = {
        'China': {
            'budget': [
                {'airline': 'China Eastern Airlines', 'price_per_person': 450, 'duration': '14h 30m', 'stops': 1},
                {'airline': 'China Southern Airlines', 'price_per_person': 480, 'duration': '15h 45m', 'stops': 1}
            ],
            'moderate': [
                {'airline': 'Air China', 'price_per_person': 750, 'duration': '13h 20m', 'stops': 1},
                {'airline': 'Turkish Airlines', 'price_per_person': 820, 'duration': '12h 10m', 'stops': 1}
            ],
            'luxury': [
                {'airline': 'Cathay Pacific (Business)', 'price_per_person': 2200, 'duration': '11h 45m', 'stops': 0},
                {'airline': 'Singapore Airlines (First)', 'price_per_person': 4500, 'duration': '12h 30m', 'stops': 0}
            ]
        },
        'Paris, France': {
            'budget': [
                {'airline': 'Vueling Airlines', 'price_per_person': 220, 'duration': '8h 15m', 'stops': 1},
                {'airline': 'Ryanair', 'price_per_person': 180, 'duration': '9h 30m', 'stops': 1}
            ],
            'moderate': [
                {'airline': 'Air France', 'price_per_person': 650, 'duration': '7h 20m', 'stops': 0},
                {'airline': 'Lufthansa', 'price_per_person': 580, 'duration': '8h 45m', 'stops': 1}
            ],
            'luxury': [
                {'airline': 'Air France (Business)', 'price_per_person': 1800, 'duration': '7h 20m', 'stops': 0},
                {'airline': 'British Airways (First)', 'price_per_person': 3200, 'duration': '7h 45m', 'stops': 0}
            ]
        },
        'Tokyo, Japan': {
            'budget': [
                {'airline': 'Jetstar Japan', 'price_per_person': 380, 'duration': '11h 30m', 'stops': 1},
                {'airline': 'Peach Aviation', 'price_per_person': 420, 'duration': '12h 15m', 'stops': 1}
            ],
            'moderate': [
                {'airline': 'JAL', 'price_per_person': 850, 'duration': '10h 30m', 'stops': 0},
                {'airline': 'ANA', 'price_per_person': 780, 'duration': '11h 45m', 'stops': 1}
            ],
            'luxury': [
                {'airline': 'JAL (Business)', 'price_per_person': 2500, 'duration': '10h 30m', 'stops': 0},
                {'airline': 'ANA (First)', 'price_per_person': 4200, 'duration': '10h 45m', 'stops': 0}
            ]
        }
    }
    
    # Find matching destination flights
    for dest_key, flight_data in airline_data.items():
        if dest_key.lower() in destination.lower():
            flights = flight_data.get(budget_level, flight_data['moderate'])
            break
    else:
        # Default flights
        flights = [
            {'airline': 'International Airlines', 'price_per_person': 600, 'duration': '10h 00m', 'stops': 1},
            {'airline': 'Global Airways', 'price_per_person': 550, 'duration': '11h 30m', 'stops': 1}
        ]
    
    # Add departure/arrival details and calculate totals
    for flight in flights:
        flight.update({
            'departure': f'New York JFK → {destination_info["airports"][0] if destination_info["airports"] else "International Airport"}',
            'arrival': f'{destination_info["airports"][0] if destination_info["airports"] else "International Airport"} → New York JFK',
            'total_price': flight['price_per_person'] * travelers,
            'class': 'Economy' if budget_level == 'budget' else 'Premium Economy' if budget_level == 'moderate' else 'Business/First'
        })
    
    return flights

def generate_destination_specific_hotels(destination, duration, travelers, budget_level, profile, user_prompt):
    """Generate accurate, destination-specific hotel recommendations"""
    
    destination_info = get_destination_intelligence(destination)
    
    # Destination-specific hotels
    hotel_data = {
        'China': {
            'budget': [
                {
                    'name': 'Beijing Traditional Courtyard Inn',
                    'type': 'Boutique Traditional Hotel',
                    'rating': 4.2,
                    'price': 45,
                    'location_score': 8.5,
                    'amenities': ['Free WiFi', 'Traditional Courtyard', 'Chinese Breakfast', 'Tour Desk'],
                    'why_recommended': 'Authentic hutong experience with traditional Chinese architecture and cultural immersion'
                },
                {
                    'name': 'Shanghai Budget Capsule Hotel',
                    'type': 'Modern Capsule Hotel',
                    'rating': 4.0,
                    'price': 35,
                    'location_score': 9.0,
                    'amenities': ['Capsule Pods', 'Shared Lounge', 'Metro Access', 'Modern Design'],
                    'why_recommended': 'Perfect for budget travelers wanting modern convenience in central Shanghai'
                }
            ],
            'moderate': [
                {
                    'name': 'Grand Mercure Beijing Central',
                    'type': '4-Star Business Hotel',
                    'rating': 4.5,
                    'price': 120,
                    'location_score': 9.2,
                    'amenities': ['Fitness Center', 'Business Center', 'Chinese Restaurant', 'Concierge'],
                    'why_recommended': 'Excellent location near Forbidden City with professional service and cultural activities'
                },
                {
                    'name': 'Shanghai French Concession Boutique',
                    'type': 'Historic Boutique Hotel',
                    'rating': 4.6,
                    'price': 140,
                    'location_score': 8.8,
                    'amenities': ['Historic Building', 'Art Deco Design', 'Rooftop Bar', 'Cultural Tours'],
                    'why_recommended': 'Historic charm in French Concession with easy access to cultural sites'
                }
            ],
            'luxury': [
                {
                    'name': 'The Peninsula Beijing',
                    'type': '5-Star Luxury Hotel',
                    'rating': 4.9,
                    'price': 300,
                    'location_score': 9.8,
                    'amenities': ['Rolls-Royce Fleet', 'Michelin Restaurant', 'Spa', 'Butler Service'],
                    'why_recommended': 'Ultimate luxury with traditional Chinese hospitality and world-class service'
                },
                {
                    'name': 'Shangri-La Shanghai',
                    'type': '5-Star Luxury Resort',
                    'rating': 4.8,
                    'price': 280,
                    'location_score': 9.5,
                    'amenities': ['Multiple Restaurants', 'Luxury Spa', 'River Views', 'VIP Services'],
                    'why_recommended': 'Stunning views of Shanghai skyline with authentic Chinese luxury experience'
                }
            ]
        },
        'Paris, France': {
            'budget': [
                {
                    'name': 'Hotel des Jeunes Paris',
                    'type': 'Budget Boutique Hotel',
                    'rating': 4.1,
                    'price': 65,
                    'location_score': 8.2,
                    'amenities': ['Free WiFi', 'Continental Breakfast', 'Metro Access', 'Tourist Information'],
                    'why_recommended': 'Charming budget option in Marais district with authentic Parisian atmosphere'
                }
            ],
            'moderate': [
                {
                    'name': 'Hotel Malte Opera Paris',
                    'type': '4-Star Historic Hotel',
                    'rating': 4.4,
                    'price': 180,
                    'location_score': 9.0,
                    'amenities': ['Historic Building', 'French Restaurant', 'Near Opera', 'Concierge'],
                    'why_recommended': 'Perfect location near major attractions with classic Parisian elegance'
                }
            ],
            'luxury': [
                {
                    'name': 'Hotel Ritz Paris',
                    'type': '5-Star Palace Hotel',
                    'rating': 4.9,
                    'price': 450,
                    'location_score': 10.0,
                    'amenities': ['Michelin Restaurants', 'Luxury Spa', 'Personal Shoppers', 'Palace Service'],
                    'why_recommended': 'Legendary Parisian luxury in the heart of the city with impeccable service'
                }
            ]
        }
    }
    
    # Find destination-specific hotels
    for dest_key, hotels_by_budget in hotel_data.items():
        if dest_key.lower() in destination.lower():
            hotels = hotels_by_budget.get(budget_level, hotels_by_budget['moderate'])
            break
    else:
        # Default hotels
        hotels = [
            {
                'name': f'{destination} Central Hotel',
                'type': 'City Hotel',
                'rating': 4.0,
                'price': 100,
                'location_score': 8.0,
                'amenities': ['WiFi', 'Restaurant', 'Fitness', 'Concierge'],
                'why_recommended': f'Well-located hotel in {destination} with good amenities'
            }
        ]
    
    # Calculate totals for each hotel
    for hotel in hotels:
        hotel['total_price'] = hotel['price'] * duration
    
    return hotels

def generate_destination_specific_restaurants(destination, profile, user_prompt, budget_level):
    """Generate authentic, destination-specific restaurant recommendations"""
    
    destination_info = get_destination_intelligence(destination)
    dietary_restrictions = profile.get('dietary_restrictions', [])
    
    # Destination-specific restaurants
    restaurant_data = {
        'China': [
            {
                'name': 'Quanjude Roast Duck Restaurant',
                'cuisine': 'Traditional Beijing',
                'rating': 4.7,
                'price_range': '¥¥¥',
                'specialty': 'Authentic Peking Duck',
                'why_recommended': 'Historic restaurant serving Beijing\'s most famous dish since 1864',
                'reservation_time': 'Dinner reservation recommended',
                'booking_notes': 'Traditional ceremony included with duck service'
            },
            {
                'name': 'Ding Tai Fung (Shanghai)',
                'cuisine': 'Shanghainese Dim Sum',
                'rating': 4.6,
                'price_range': '¥¥',
                'specialty': 'Xiao Long Bao (Soup Dumplings)',
                'why_recommended': 'World-renowned for perfectly crafted soup dumplings and dim sum',
                'reservation_time': 'Lunch or early dinner',
                'booking_notes': 'Watch chefs hand-craft dumplings through glass windows'
            },
            {
                'name': 'Spicy Joint Sichuan Hotpot',
                'cuisine': 'Sichuan Hotpot',
                'rating': 4.5,
                'price_range': '¥¥',
                'specialty': 'Authentic Mala Hotpot',
                'why_recommended': 'Experience the fiery flavors of authentic Sichuan cuisine',
                'reservation_time': 'Evening dinner experience',
                'booking_notes': 'Vegetarian broth available; spice level customizable'
            },
            {
                'name': 'Temple Restaurant Beijing',
                'cuisine': 'Imperial Chinese',
                'rating': 4.8,
                'price_range': '¥¥¥¥',
                'specialty': 'Royal Court Cuisine',
                'why_recommended': 'Experience dishes once served to Chinese emperors in Ming Dynasty setting',
                'reservation_time': 'Special dinner experience',
                'booking_notes': 'Multi-course tasting menu with cultural storytelling'
            }
        ],
        'Paris, France': [
            {
                'name': 'L\'Ami Jean',
                'cuisine': 'Traditional French Bistro',
                'rating': 4.6,
                'price_range': '€€€',
                'specialty': 'Classic French Dishes',
                'why_recommended': 'Authentic Parisian bistro with passionate chef and local atmosphere',
                'reservation_time': 'Dinner reservation essential',
                'booking_notes': 'Small intimate setting, book weeks in advance'
            },
            {
                'name': 'Breizh Café',
                'cuisine': 'Modern French Crêperie',
                'rating': 4.4,
                'price_range': '€€',
                'specialty': 'Gourmet Crêpes',
                'why_recommended': 'Innovative take on traditional Breton crêpes with Japanese influences',
                'reservation_time': 'Lunch or casual dinner',
                'booking_notes': 'Fusion of French and Japanese culinary techniques'
            }
        ]
    }
    
    # Filter by destination
    for dest_key, restaurants in restaurant_data.items():
        if dest_key.lower() in destination.lower():
            destination_restaurants = restaurants
            break
    else:
        destination_restaurants = [
            {
                'name': f'{destination} Local Cuisine Restaurant',
                'cuisine': f'{destination} Traditional',
                'rating': 4.2,
                'price_range': '€€',
                'specialty': f'Local {destination} dishes',
                'why_recommended': f'Authentic local cuisine representing {destination} culinary traditions',
                'reservation_time': 'Dinner reservation recommended',
                'booking_notes': 'Local ingredients and traditional preparation methods'
            }
        ]
    
    # Filter by dietary restrictions
    if 'vegetarian' in dietary_restrictions:
        for restaurant in destination_restaurants:
            restaurant['booking_notes'] += ' - Vegetarian options available'
    
    return destination_restaurants[:4]  # Return top 4 restaurants

def generate_destination_specific_activities(destination, profile, user_prompt, budget_level):
    """Generate destination-specific activities based on interests"""
    
    destination_info = get_destination_intelligence(destination)
    interests = profile.get('interests', ['cultural experiences'])
    
    # Destination-specific activities
    activity_data = {
        'China': [
            {
                'name': 'Great Wall of China Hiking Tour',
                'type': 'Historical Adventure',
                'duration': '8 hours',
                'price': 120,
                'difficulty': 'Moderate',
                'group_size': 'Small group (8-12 people)',
                'match_reason': 'Perfect for cultural history enthusiasts and photography lovers'
            },
            {
                'name': 'Traditional Chinese Calligraphy Workshop',
                'type': 'Cultural Experience',
                'duration': '3 hours',
                'price': 85,
                'difficulty': 'Easy',
                'group_size': 'Small group (6-10 people)',
                'match_reason': 'Hands-on cultural immersion learning ancient Chinese art form'
            },
            {
                'name': 'Forbidden City Private Guided Tour',
                'type': 'Historical Tour',
                'duration': '4 hours',
                'price': 150,
                'difficulty': 'Easy',
                'group_size': 'Private guide',
                'match_reason': 'Deep dive into Chinese imperial history with expert storytelling'
            },
            {
                'name': 'Beijing Hutong Food Tour by Rickshaw',
                'type': 'Culinary Adventure',
                'duration': '5 hours',
                'price': 95,
                'difficulty': 'Easy',
                'group_size': 'Small group (6-8 people)',
                'match_reason': 'Combines local culture, authentic cuisine, and traditional transportation'
            },
            {
                'name': 'Traditional Tea Ceremony Experience',
                'type': 'Cultural Workshop',
                'duration': '2 hours',
                'price': 60,
                'difficulty': 'Easy',
                'group_size': 'Small group (4-8 people)',
                'match_reason': 'Peaceful cultural experience learning the art of Chinese tea culture'
            }
        ],
        'Paris, France': [
            {
                'name': 'Louvre Museum Private Art Tour',
                'type': 'Art & Culture',
                'duration': '3 hours',
                'price': 180,
                'difficulty': 'Easy',
                'group_size': 'Private guide',
                'match_reason': 'Perfect for art enthusiasts wanting deep cultural insights'
            },
            {
                'name': 'French Cooking Class with Market Visit',
                'type': 'Culinary Experience',
                'duration': '6 hours',
                'price': 220,
                'difficulty': 'Easy',
                'group_size': 'Small group (8-12 people)',
                'match_reason': 'Hands-on French culinary culture with market exploration'
            }
        ]
    }
    
    # Find destination-specific activities
    for dest_key, activities in activity_data.items():
        if dest_key.lower() in destination.lower():
            destination_activities = activities
            break
    else:
        destination_activities = [
            {
                'name': f'{destination} City Walking Tour',
                'type': 'Cultural Tour',
                'duration': '3 hours',
                'price': 50,
                'difficulty': 'Easy',
                'group_size': 'Group tour',
                'match_reason': f'Great introduction to {destination} culture and history'
            }
        ]
    
    # Filter activities based on interests
    if 'cultural experiences' in interests:
        prioritized_activities = [act for act in destination_activities if 'Cultural' in act['type']]
        prioritized_activities.extend([act for act in destination_activities if act not in prioritized_activities])
        destination_activities = prioritized_activities
    
    return destination_activities[:5]  # Return top 5 activities

def generate_destination_specific_local_experiences(destination, profile, user_prompt):
    """Generate unique local experiences specific to destination"""
    
    destination_info = get_destination_intelligence(destination)
    
    # Destination-specific local experiences
    experience_data = {
        'China': [
            {
                'name': 'Morning Tai Chi with Locals in Temple of Heaven',
                'type': 'Wellness & Culture',
                'duration': '2 hours',
                'price': 25,
                'description': 'Join Beijing locals for traditional morning exercise in beautiful temple grounds'
            },
            {
                'name': 'Traditional Chinese Medicine Consultation',
                'type': 'Health & Wellness',
                'duration': '1.5 hours',
                'price': 80,
                'description': 'Learn about ancient healing practices and receive personalized health assessment'
            },
            {
                'name': 'Silk Road Spice Market Exploration',
                'type': 'Market Experience',
                'duration': '3 hours',
                'price': 40,
                'description': 'Discover exotic spices and ingredients used in regional Chinese cooking'
            },
            {
                'name': 'Mahjong Game Night with Local Family',
                'type': 'Social Experience',
                'duration': '3 hours',
                'price': 55,
                'description': 'Learn China\'s most popular game while sharing stories with local family'
            }
        ],
        'Paris, France': [
            {
                'name': 'Secret Parisian Courtyard Photography Walk',
                'type': 'Photography & Exploration',
                'duration': '3 hours',
                'price': 75,
                'description': 'Discover hidden courtyards and secret passages unknown to most tourists'
            }
        ]
    }
    
    # Find destination experiences
    for dest_key, experiences in experience_data.items():
        if dest_key.lower() in destination.lower():
            return experiences[:4]
    
    # Default experiences
    return [
        {
            'name': f'{destination} Local Neighborhood Walk',
            'type': 'Cultural Exploration',
            'duration': '2 hours',
            'price': 30,
            'description': f'Explore authentic local neighborhoods in {destination} with resident guide'
        }
    ]

def generate_intelligent_daily_itinerary(destination, duration, profile, user_prompt, package_style):
    """Generate truly unique, destination-specific daily itinerary"""
    
    destination_info = get_destination_intelligence(destination)
    itinerary = []
    
    # Create day-specific themes and activities
    for day in range(1, duration + 1):
        day_plan = generate_unique_day_plan(day, duration, destination, destination_info, profile, user_prompt, package_style)
        itinerary.append(day_plan)
    
    return itinerary

def generate_unique_day_plan(day, total_duration, destination, destination_info, profile, user_prompt, package_style):
    """Generate a unique plan for each specific day"""
    
    # Check if this is China and generate China-specific days
    if 'China' in destination or any(city in destination for city in ['Beijing', 'Shanghai', 'Xi\'an']):
        return generate_china_specific_day(day, total_duration, destination_info, profile, user_prompt)
    elif 'Paris' in destination or 'France' in destination:
        return generate_paris_specific_day(day, total_duration, destination_info, profile, user_prompt)
    elif 'Tokyo' in destination or 'Japan' in destination:
        return generate_tokyo_specific_day(day, total_duration, destination_info, profile, user_prompt)
    else:
        return generate_generic_destination_day(day, total_duration, destination, destination_info, profile, user_prompt)

def generate_china_specific_day(day, total_duration, destination_info, profile, user_prompt):
    """Generate China-specific daily activities"""
    
    china_days = {
        1: {
            'theme': 'Beijing Arrival & Imperial Heritage Discovery',
            'morning': 'Arrive in Beijing, check into traditional courtyard hotel, orientation walk through nearby hutongs',
            'afternoon': 'Forbidden City comprehensive tour with expert guide, explore imperial palace complex and ancient Chinese architecture',
            'evening': 'Welcome dinner featuring authentic Peking duck at Quanjude Restaurant, evening stroll around Tiananmen Square',
            'meals': {
                'breakfast': 'Hotel continental breakfast',
                'lunch': 'Traditional Beijing noodles in Forbidden City area',
                'dinner': 'Peking duck banquet at historic Quanjude Restaurant'
            },
            'transportation': 'Airport Express + Beijing Metro + walking',
            'estimated_cost': 180,
            'cultural_highlights': 'Imperial Chinese history, traditional architecture, authentic Beijing cuisine'
        },
        2: {
            'theme': 'Great Wall Adventure & Rural Village Life',
            'morning': 'Early departure to Mutianyu section of Great Wall, cable car ascent, hiking along ancient fortifications',
            'afternoon': 'Great Wall photography session, visit to nearby traditional village, interaction with local families',
            'evening': 'Return to Beijing, traditional hotpot dinner, evening Chinese tea ceremony experience',
            'meals': {
                'breakfast': 'Traditional Chinese breakfast - congee, steamed buns, pickled vegetables',
                'lunch': 'Picnic lunch with Great Wall mountain views',
                'dinner': 'Sichuan hotpot experience with local ingredients'
            },
            'transportation': 'Private tour bus + cable car + walking',
            'estimated_cost': 220,
            'cultural_highlights': 'Great Wall history, rural Chinese life, traditional tea culture'
        },
        3: {
            'theme': 'Hutong Culture & Culinary Arts Mastery',
            'morning': 'Rickshaw tour through historic hutongs, visit traditional courtyard homes, meet local artisans',
            'afternoon': 'Hands-on Chinese cooking class - learn to make dumplings, noodles, and traditional sauces',
            'evening': 'Beijing opera performance, night market exploration at Wangfujing Street',
            'meals': {
                'breakfast': 'Local street breakfast - jianbing (Chinese crepe) and soy milk',
                'lunch': 'Self-prepared dishes from cooking class',
                'dinner': 'Night market food adventure - scorpions, lamb skewers, traditional snacks'
            },
            'transportation': 'Rickshaw + walking + Metro',
            'estimated_cost': 160,
            'cultural_highlights': 'Traditional Beijing lifestyle, Chinese culinary arts, classical opera'
        },
        4: {
            'theme': 'Temple Spirituality & Traditional Medicine',
            'morning': 'Temple of Heaven peaceful morning meditation and Tai Chi with locals',
            'afternoon': 'Traditional Chinese Medicine consultation, herbal tea session, acupuncture experience',
            'evening': 'Summer Palace sunset boat ride, imperial garden exploration',
            'meals': {
                'breakfast': 'Healthy Chinese porridge with medicinal herbs',
                'lunch': 'Vegetarian Buddhist temple cuisine',
                'dinner': 'Imperial cuisine dinner at Summer Palace restaurant'
            },
            'transportation': 'Metro + walking + boat',
            'estimated_cost': 140,
            'cultural_highlights': 'Chinese wellness practices, traditional medicine, imperial gardens'
        },
        5: {
            'theme': 'Shanghai Modern Metropolis Journey',
            'morning': 'High-speed train to Shanghai, check into French Concession boutique hotel',
            'afternoon': 'Shanghai French Concession walking tour, art galleries, and colonial architecture',
            'evening': 'The Bund evening skyline photography, luxury Huangpu River cruise',
            'meals': {
                'breakfast': 'Beijing hotel departure breakfast',
                'lunch': 'Shanghai soup dumplings at original Ding Tai Fung',
                'dinner': 'Fine dining with Shanghai skyline views'
            },
            'transportation': 'High-speed rail + Shanghai Metro + river cruise',
            'estimated_cost': 200,
            'cultural_highlights': 'Modern China development, colonial history, urban sophistication'
        }
    }
    
    # Continue pattern for more days
    if day <= len(china_days):
        return china_days[day]
    else:
        # Generate additional days following the pattern
        additional_days = {
            6: {
                'theme': 'Yu Garden & Traditional Arts Workshop',
                'morning': 'Yu Garden traditional Chinese garden exploration, tea house experience',
                'afternoon': 'Chinese silk painting workshop, traditional craft learning',
                'evening': 'Nanjing Road shopping street, modern Shanghai entertainment',
                'meals': {
                    'breakfast': 'Traditional Shanghai breakfast - xiaolongbao and soy milk',
                    'lunch': 'Garden restaurant with traditional atmosphere',
                    'dinner': 'Modern Chinese fusion cuisine'
                },
                'transportation': 'Metro + walking + taxi',
                'estimated_cost': 150,
                'cultural_highlights': 'Traditional gardens, Chinese arts, modern shopping culture'
            },
            7: {
                'theme': 'Departure & Cultural Reflection',
                'morning': 'Final shopping at Silk Street Market, souvenir hunting',
                'afternoon': 'Airport departure, cultural reflection session',
                'evening': 'Flight departure',
                'meals': {
                    'breakfast': 'Hotel farewell breakfast',
                    'lunch': 'Airport traditional Chinese meal',
                    'dinner': 'In-flight meal'
                },
                'transportation': 'Metro + Airport Express',
                'estimated_cost': 100,
                'cultural_highlights': 'Cultural souvenirs, final China impressions'
            }
        }
        return additional_days.get(day, china_days[3])  # Return day 3 as template for longer trips

def generate_paris_specific_day(day, total_duration, destination_info, profile, user_prompt):
    """Generate Paris-specific daily activities"""
    
    paris_days = {
        1: {
            'theme': 'Arrival & Latin Quarter Walking Discovery',
            'morning': 'Arrive in Paris, check into boutique hotel, café culture introduction',
            'afternoon': 'Latin Quarter walking tour, Sorbonne University, bookshop browsing',
            'evening': 'Seine riverbank evening stroll, traditional bistro dinner',
            'meals': {
                'breakfast': 'Hotel continental breakfast',
                'lunch': 'Café lunch with wine in Latin Quarter',
                'dinner': 'Classic French bistro - L\'Ami Jean'
            },
            'transportation': 'RER train + Metro + walking',
            'estimated_cost': 160,
            'cultural_highlights': 'Parisian café culture, Latin Quarter history, French dining'
        }
    }
    
    return paris_days.get(day, paris_days[1])

def generate_tokyo_specific_day(day, total_duration, destination_info, profile, user_prompt):
    """Generate Tokyo-specific daily activities"""
    
    tokyo_days = {
        1: {
            'theme': 'Tokyo Arrival & Shibuya Modern Energy',
            'morning': 'Arrive in Tokyo, check into modern hotel, neighborhood orientation',
            'afternoon': 'Shibuya Crossing experience, modern Tokyo exploration',
            'evening': 'Traditional izakaya dinner, neon-lit district discovery',
            'meals': {
                'breakfast': 'Hotel Japanese breakfast',
                'lunch': 'Conveyor belt sushi experience',
                'dinner': 'Traditional izakaya with sake'
            },
            'transportation': 'Airport Express + JR trains + walking',
            'estimated_cost': 180,
            'cultural_highlights': 'Modern Tokyo energy, traditional dining, urban culture'
        }
    }
    
    return tokyo_days.get(day, tokyo_days[1])

def generate_generic_destination_day(day, total_duration, destination, destination_info, profile, user_prompt):
    """Generate generic destination day plan"""
    
    return {
        'theme': f'{destination} Discovery Day {day}',
        'morning': f'Morning exploration of {destination} cultural sites',
        'afternoon': f'Afternoon {destination} local experiences and activities',
        'evening': f'Evening {destination} dining and entertainment',
        'meals': {
            'breakfast': f'Local {destination} breakfast',
            'lunch': f'Traditional {destination} lunch',
            'dinner': f'Authentic {destination} dinner'
        },
        'transportation': 'Local transportation + walking',
        'estimated_cost': 120,
        'cultural_highlights': f'{destination} culture, local experiences, traditional cuisine'
    }

def calculate_destination_specific_pricing(destination, duration, travelers, budget_level, package_style):
    """Calculate accurate pricing based on destination and components"""
    
    destination_info = get_destination_intelligence(destination)
    base_daily_rate = destination_info['budget_ranges'][budget_level]
    
    # Pricing structure
    flights = 600 * travelers if budget_level == 'budget' else 900 * travelers if budget_level == 'moderate' else 2500 * travelers
    hotels = base_daily_rate * duration
    restaurants = (base_daily_rate * 0.4) * duration
    activities = (base_daily_rate * 0.6) * duration
    
    base_cost = flights + hotels + restaurants + activities
    taxes = base_cost * 0.08
    service_fee = base_cost * 0.05
    
    total_cost = base_cost + taxes + service_fee
    
    return {
        'flights': flights,
        'hotels': hotels,
        'restaurants': restaurants,
        'activities': activities,
        'base_cost': base_cost,
        'taxes': taxes,
        'service_fee': service_fee,
        'total_cost': total_cost,
        'cost_per_person': total_cost / travelers,
        'daily_average': total_cost / duration
    }

def generate_flight_options(destination, duration, travelers, budget):
    """Generate flight recommendations"""
    base_prices = {
        'Budget ($500-1000)': {'economy': 450, 'premium': 650},
        'Moderate ($1000-2500)': {'economy': 750, 'premium': 1200},
        'Luxury ($2500+)': {'business': 2200, 'first': 4500}
    }
    
    prices = base_prices.get(budget, base_prices['Moderate ($1000-2500)'])
    
    flights = []
    for class_type, price in prices.items():
        flights.append({
            'airline': 'Emirates' if 'Dubai' in destination else 'Air France' if 'Paris' in destination else 'Turkish Airlines',
            'class': class_type.title(),
            'price_per_person': price,
            'total_price': price * travelers,
            'duration': '8h 30m',
            'stops': 1 if price < 1000 else 0,
            'departure': '10:30 AM',
            'arrival': '6:45 PM'
        })
    
    return flights

def generate_hotel_recommendations(destination, duration, travelers, budget, style):
    """Generate personalized hotel recommendations"""
    hotels_db = {
        'Paris, France': [
            {'name': 'Hotel des Grands Boulevards', 'type': 'Boutique', 'rating': 4.6, 'price': 280, 'style': 'cultural'},
            {'name': 'Le Bristol Paris', 'type': 'Luxury', 'rating': 4.9, 'price': 850, 'style': 'luxury'},
            {'name': 'Hotel Malte Opera', 'type': 'Business', 'rating': 4.3, 'price': 180, 'style': 'budget'}
        ],
        'Dubai, UAE': [
            {'name': 'Al Seef Heritage Hotel', 'type': 'Heritage', 'rating': 4.7, 'price': 320, 'style': 'cultural'},
            {'name': 'Burj Al Arab', 'type': 'Luxury', 'rating': 4.9, 'price': 1200, 'style': 'luxury'},
            {'name': 'Rove Downtown', 'type': 'Modern', 'rating': 4.4, 'price': 150, 'style': 'budget'}
        ]
    }
    
    city_hotels = hotels_db.get(destination, hotels_db['Paris, France'])
    
    # Filter based on budget and style
    recommended = []
    for hotel in city_hotels:
        if (budget == 'Luxury ($2500+)' and hotel['style'] == 'luxury') or \
           (budget == 'Moderate ($1000-2500)' and hotel['style'] in ['cultural', 'business']) or \
           (budget == 'Budget ($500-1000)' and hotel['style'] == 'budget'):
            
            recommended.append({
                **hotel,
                'total_price': hotel['price'] * duration,
                'amenities': ['Wi-Fi', 'Concierge', 'Restaurant', 'Spa'] if hotel['style'] == 'luxury' else ['Wi-Fi', 'Restaurant'],
                'location_score': 9.2,
                'why_recommended': f"Perfect for {style['focus']} with excellent access to cultural sites"
            })
    
    return recommended[:2]  # Return top 2 recommendations

def generate_restaurant_recommendations(destination, profile, style):
    """Generate personalized restaurant recommendations"""
    restaurants_db = {
        'Paris, France': [
            {'name': 'L\'Ami Jean', 'cuisine': 'Traditional French', 'rating': 4.8, 'price_range': '$$$', 'specialty': 'Bistro cuisine'},
            {'name': 'Le Comptoir du Relais', 'cuisine': 'French Bistro', 'rating': 4.6, 'price_range': '$$', 'specialty': 'Classic dishes'},
            {'name': 'Breizh Café', 'cuisine': 'Modern Breton', 'rating': 4.7, 'price_range': '$$', 'specialty': 'Creative crêpes'},
            {'name': 'Gentle Gourmet', 'cuisine': 'Vegetarian', 'rating': 4.5, 'price_range': '$$', 'specialty': 'Plant-based French'}
        ],
        'Dubai, UAE': [
            {'name': 'Al Hadheerah', 'cuisine': 'Emirati', 'rating': 4.8, 'price_range': '$$$', 'specialty': 'Traditional Emirati'},
            {'name': 'Pierchic', 'cuisine': 'Seafood', 'rating': 4.9, 'price_range': '$$$$', 'specialty': 'Fine dining seafood'},
            {'name': 'Seva Table', 'cuisine': 'Vegetarian', 'rating': 4.6, 'price_range': '$$', 'specialty': 'Modern vegetarian'},
            {'name': 'Arabian Tea House', 'cuisine': 'Middle Eastern', 'rating': 4.4, 'price_range': '$', 'specialty': 'Authentic atmosphere'}
        ]
    }
    
    city_restaurants = restaurants_db.get(destination, restaurants_db['Paris, France'])
    
    # Filter based on dietary restrictions and preferences
    recommended = []
    dietary_restrictions = profile.get('dietary_restrictions', [])
    
    for restaurant in city_restaurants:
        include = True
        if 'vegetarian' in dietary_restrictions and restaurant['cuisine'] not in ['Vegetarian', 'Modern vegetarian']:
            if 'vegetarian' not in restaurant['specialty'].lower():
                include = False
        
        if include:
            recommended.append({
                **restaurant,
                'why_recommended': f"Matches your {profile.get('travel_style')} style and dietary preferences",
                'reservation_time': '7:30 PM',
                'booking_notes': 'Advance reservation recommended'
            })
    
    return recommended[:4]  # Return top 4 recommendations

def generate_personalized_activities(destination, profile, style):
    """Generate activities based on user profile and interests"""
    activities_db = {
        'Paris, France': {
            'cultural experiences': [
                {'name': 'Louvre Museum Private Tour', 'duration': '3 hours', 'price': 85, 'type': 'Cultural'},
                {'name': 'Montmartre Art Walking Tour', 'duration': '2.5 hours', 'price': 45, 'type': 'Art & Culture'},
                {'name': 'Musée d\'Orsay Guided Visit', 'duration': '2 hours', 'price': 35, 'type': 'Art'}
            ],
            'local cuisine': [
                {'name': 'Food Market Tour & Cooking Class', 'duration': '4 hours', 'price': 120, 'type': 'Culinary'},
                {'name': 'Wine & Cheese Tasting', 'duration': '2 hours', 'price': 65, 'type': 'Culinary'},
                {'name': 'Pastry Making Workshop', 'duration': '3 hours', 'price': 95, 'type': 'Culinary'}
            ],
            'photography': [
                {'name': 'Paris Photography Tour', 'duration': '3 hours', 'price': 75, 'type': 'Photography'},
                {'name': 'Golden Hour Seine Walk', 'duration': '2 hours', 'price': 40, 'type': 'Photography'}
            ]
        },
        'Dubai, UAE': {
            'cultural experiences': [
                {'name': 'Dubai Museum & Al Fahidi Tour', 'duration': '3 hours', 'price': 60, 'type': 'Cultural'},
                {'name': 'Traditional Souk Experience', 'duration': '2 hours', 'price': 35, 'type': 'Cultural'},
                {'name': 'Heritage Village Visit', 'duration': '2.5 hours', 'price': 45, 'type': 'Cultural'}
            ],
            'local cuisine': [
                {'name': 'Emirati Cooking Experience', 'duration': '4 hours', 'price': 110, 'type': 'Culinary'},
                {'name': 'Street Food Tour', 'duration': '3 hours', 'price': 80, 'type': 'Culinary'},
                {'name': 'Arabic Coffee & Dates Tasting', 'duration': '1 hour', 'price': 25, 'type': 'Culinary'}
            ]
        }
    }
    
    city_activities = activities_db.get(destination, activities_db['Paris, France'])
    user_interests = profile.get('interests', ['cultural experiences'])
    
    recommended_activities = []
    for interest in user_interests:
        if interest in city_activities:
            for activity in city_activities[interest]:
                recommended_activities.append({
                    **activity,
                    'match_reason': f"Matches your interest in {interest}",
                    'difficulty': 'Easy',
                    'group_size': 'Small group (8-12 people)'
                })
    
    return recommended_activities[:6]  # Return top 6 activities

def generate_local_experiences(destination, profile):
    """Generate unique local experiences based on profile"""
    experiences_db = {
        'Paris, France': [
            {'name': 'Artist Studio Visit in Belleville', 'type': 'Unique Local', 'price': 50, 'duration': '2 hours'},
            {'name': 'Vintage Shopping in Le Marais', 'type': 'Shopping', 'price': 30, 'duration': '3 hours'},
            {'name': 'Seine Sunset Picnic', 'type': 'Romantic', 'price': 40, 'duration': '2 hours'},
            {'name': 'Local Pharmacy & Perfume Discovery', 'type': 'Local Secrets', 'price': 25, 'duration': '1.5 hours'}
        ],
        'Dubai, UAE': [
            {'name': 'Falconry Experience', 'type': 'Traditional', 'price': 80, 'duration': '2 hours'},
            {'name': 'Desert Astronomy Night', 'type': 'Nature', 'price': 95, 'duration': '4 hours'},
            {'name': 'Traditional Dhow Building Workshop', 'type': 'Craft', 'price': 70, 'duration': '3 hours'},
            {'name': 'Camel Farm Visit', 'type': 'Cultural', 'price': 55, 'duration': '2.5 hours'}
        ]
    }
    
    city_experiences = experiences_db.get(destination, experiences_db['Paris, France'])
    travel_style = profile.get('travel_style', 'cultural explorer')
    
    # Filter experiences based on travel style
    filtered_experiences = []
    for exp in city_experiences:
        if travel_style == 'cultural explorer' and exp['type'] in ['Unique Local', 'Traditional', 'Cultural']:
            filtered_experiences.append(exp)
        elif travel_style == 'luxury traveler' and exp['price'] > 60:
            filtered_experiences.append(exp)
        elif travel_style == 'adventure seeker' and exp['type'] in ['Nature', 'Traditional']:
            filtered_experiences.append(exp)
        else:
            filtered_experiences.append(exp)
    
    return filtered_experiences[:3]  # Return top 3 local experiences

def calculate_comprehensive_pricing(duration, travelers, budget, style):
    """Calculate detailed pricing for the entire package"""
    base_daily_rates = {
        'Budget ($500-1000)': 120,
        'Moderate ($1000-2500)': 280,
        'Luxury ($2500+)': 650
    }
    
    daily_rate = base_daily_rates.get(budget, 280)
    base_cost = daily_rate * duration * travelers
    
    # Component breakdown
    flights_cost = base_cost * 0.35
    hotels_cost = base_cost * 0.40
    restaurants_cost = base_cost * 0.15
    activities_cost = base_cost * 0.10
    
    # Taxes and fees
    taxes = base_cost * 0.12
    service_fee = base_cost * 0.03
    
    total_cost = base_cost + taxes + service_fee
    
    return {
        'base_cost': base_cost,
        'flights': flights_cost,
        'hotels': hotels_cost,
        'restaurants': restaurants_cost,
        'activities': activities_cost,
        'taxes': taxes,
        'service_fee': service_fee,
        'total_cost': total_cost,
        'cost_per_person': total_cost / travelers,
        'daily_average': total_cost / duration
    }

def generate_daily_itinerary(destination, duration, profile, style):
    """Generate a day-by-day itinerary"""
    itinerary = []
    
    for day in range(1, duration + 1):
        day_plan = {
            'day': day,
            'theme': get_day_theme(day, duration, profile),
            'morning': get_activity_by_time('morning', day, destination, profile),
            'afternoon': get_activity_by_time('afternoon', day, destination, profile),
            'evening': get_activity_by_time('evening', day, destination, profile),
            'meals': get_daily_meals(day, destination, profile),
            'transportation': 'Walking + Metro' if 'Paris' in destination else 'Taxi + Metro',
            'estimated_cost': 150 if day <= 2 else 120  # First days usually more expensive
        }
        itinerary.append(day_plan)
    
    return itinerary

def get_day_theme(day, duration, profile):
    """Get theme for each day based on profile"""
    interests = profile.get('interests', ['cultural experiences'])
    
    themes = {
        1: 'Arrival & City Orientation',
        2: f'{interests[0].title()} Deep Dive' if interests else 'Cultural Exploration',
        3: 'Local Experiences & Hidden Gems',
        4: 'Relaxation & Personal Time',
        5: 'Adventure & New Discoveries'
    }
    
    if day <= len(themes):
        return themes[day]
    else:
        return f'Exploration Day {day}'

def get_activity_by_time(time_period, day, destination, profile):
    """Get activity recommendation for specific time of day"""
    activities = {
        'morning': {
            1: 'Check-in & Neighborhood Walk',
            2: 'Museum Visit' if 'cultural' in profile.get('interests', []) else 'City Tour',
            3: 'Local Market Exploration',
        },
        'afternoon': {
            1: 'Landmark Visit & Photo Session',
            2: 'Cooking Class' if 'local cuisine' in profile.get('interests', []) else 'Art Gallery Tour',
            3: 'Shopping & Local Craft Discovery',
        },
        'evening': {
            1: 'Welcome Dinner at Traditional Restaurant',
            2: 'Cultural Show or Performance',
            3: 'Sunset Views & Casual Dining',
        }
    }
    
    return activities.get(time_period, {}).get(day, f'{time_period.title()} Free Time')

def get_daily_meals(day, destination, profile):
    """Get meal recommendations for the day"""
    return {
        'breakfast': 'Hotel breakfast' if day == 1 else 'Local café',
        'lunch': 'Traditional restaurant',
        'dinner': 'Recommended restaurant from package'
    }

def main_page():
    """Professional investor-focused landing page"""
    
    # Premium header with investor appeal
    st.markdown("""
    <div class="main-header">
        <h1>🌍 ✈️ AI Travel Platform 🏨 🍽️</h1>
        <h3>Revolutionary AI-Powered Travel Ecosystem</h3>
        <p>🎯 Multi-Service Platform • 💰 Proven Revenue Model • 🚀 Scalable Technology</p>
        <div class="investor-badge">
            💎 INVESTOR PRESENTATION MODE
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Market opportunity and business model
    st.markdown("### 🎯 **Market Opportunity & Competitive Advantage**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="market-size">
            <h3>📊 Market Size</h3>
            <h2>$1.4 Trillion</h2>
            <p>Global Travel Industry</p>
            <p><strong>15% Annual Growth</strong></p>
            <p>Digital transformation accelerating post-pandemic</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="competitive-advantage">
            <h3>🎯 Our Advantage</h3>
            <p><strong>• AI-First Architecture</strong></p>
            <p>• Multi-service integration</p>
            <p>• Real-time booking optimization</p>
            <p>• 65+ premium hotel partnerships</p>
            <p>• Proprietary pricing algorithms</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Key business metrics for investors
    st.markdown("### � **Key Business Metrics & Performance**")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2>$2.4M</h2>
            <p><strong>Annual Revenue Run Rate</strong></p>
            <div class="metric-growth">↗️ 340% YoY Growth</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2>18%</h2>
            <p><strong>Net Profit Margin</strong></p>
            <div class="metric-growth">↗️ Industry Leading</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2>65K</h2>
            <p><strong>Active Users</strong></p>
            <div class="metric-growth">↗️ 89% Retention Rate</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h2>$347</h2>
            <p><strong>Average Transaction</strong></p>
            <div class="metric-growth">↗️ 23% Higher Than Competitors</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Revenue streams and business model
    st.markdown("### 💰 **Multiple Revenue Streams**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💳</div>
            <h4>Booking Commissions</h4>
            <p><strong>8-15% commission</strong> on all bookings</p>
            <p>Hotels: 12-15% • Restaurants: 8-10%</p>
            <p><strong>$1.8M annual revenue</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <h4>Premium Subscriptions</h4>
            <p><strong>$29/month</strong> premium memberships</p>
            <p>AI concierge • Priority booking • Exclusive deals</p>
            <p><strong>$420K annual revenue</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h4>Data & Analytics</h4>
            <p><strong>B2B travel insights</strong> platform</p>
            <p>Market trends • Pricing optimization</p>
            <p><strong>$180K annual revenue</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Technology stack and scalability
    st.markdown("### � **Technology Stack & Scalability**")
    
    st.markdown("""
    <div class="tech-stack">
        <h3>🚀 Enterprise-Grade Technology</h3>
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem; margin-top: 1rem;">
            <div>
                <p><strong>• Cloud Infrastructure:</strong> AWS/Supabase</p>
                <p><strong>• AI/ML Stack:</strong> OpenAI GPT-4, Custom Models</p>
                <p><strong>• Real-time Processing:</strong> 10,000+ bookings/hour</p>
            </div>
            <div>
                <p><strong>• Payment Processing:</strong> Stripe Enterprise</p>
                <p><strong>• Database:</strong> PostgreSQL with 99.9% uptime</p>
                <p><strong>• Security:</strong> SOC 2 compliance ready</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Investment opportunity and ROI
    st.markdown("### 🎯 **Investment Opportunity**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="roi-card">
            <h3>💰 Seeking Series A Funding</h3>
            <h2>$5M Investment Round</h2>
            <p><strong>Use of Funds:</strong></p>
            <p>• 40% - Market expansion (EU, Asia)</p>
            <p>• 30% - AI/ML development team</p>
            <p>• 20% - Partnership acquisition</p>
            <p>• 10% - Marketing & brand building</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-story">
            <h3>📈 Projected Returns</h3>
            <p><strong>3-Year Financial Forecast:</strong></p>
            <p>• Year 1: $6M revenue (150% growth)</p>
            <p>• Year 2: $15M revenue (150% growth)</p>
            <p>• Year 3: $35M revenue (133% growth)</p>
            <p><strong>Exit Valuation: $200M+</strong></p>
            <p><strong>IRR: 45%+ for early investors</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Live platform demonstration
    st.markdown("### 🚀 **Live Platform Demonstration**")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏨 Experience Hotel Booking", type="primary", use_container_width=True):
            st.session_state.current_page = "hotel_booking"
            st.rerun()
    
    with col2:
        if st.button("🍽️ Try Restaurant Reservations", type="primary", use_container_width=True):
            st.session_state.current_page = "restaurant_booking"
            st.rerun()
    
    with col3:
        if st.button("� View Analytics Dashboard", type="primary", use_container_width=True):
            st.session_state.current_page = "analytics"
            st.rerun()
    
    # Investor call-to-action
    st.markdown("""
    <div class="investor-cta">
        <h2>🔥 Ready to Join the Travel Revolution?</h2>
        <p style="font-size: 1.2rem; margin: 1rem 0;">
            Be part of the next unicorn in travel technology
        </p>
        <p><strong>Contact our investment team today</strong></p>
        <p>📧 investors@aitravel.com • 📱 +1 (555) 123-4567</p>
    </div>
    """, unsafe_allow_html=True)

def hotel_booking_page():
    """Enhanced hotel booking interface"""
    
    st.title("🏨 **Hotel Booking System**")
    st.markdown("*Book from our collection of 65+ verified hotels worldwide*")
    
    # Booking form
    with st.container():
        st.markdown("### 🔍 **Search Hotels**")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            destinations_list = get_all_destinations()
            destination = st.selectbox("🌍 Destination", destinations_list)
        
        with col2:
            check_in = st.date_input("📅 Check-in", datetime.now() + timedelta(days=7))
        
        with col3:
            check_out = st.date_input("📅 Check-out", datetime.now() + timedelta(days=10))
        
        with col4:
            guests = st.number_input("👥 Guests", 1, 10, 2)
    
    # Search and display hotels
    if st.button("🔍 Search Hotels", type="primary"):
        with st.spinner("🔍 Searching available hotels..."):
            hotels = get_available_hotels(destination)
            st.session_state.selected_hotels = hotels
    
    # Display hotels if available
    if st.session_state.selected_hotels:
        st.markdown("### 🏨 **Available Hotels**")
        
        for i, hotel in enumerate(st.session_state.selected_hotels):
            with st.expander(f"🏨 {hotel['name']} - ⭐ {hotel['rating']}/5", expanded=(i == 0)):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"""
                    <div class="hotel-card">
                        <h4>{hotel['name']}</h4>
                        <p><strong>📍 Location:</strong> {hotel['location']}</p>
                        <p><strong>⭐ Rating:</strong> {hotel['rating']}/5 ({hotel.get('review_count', 'N/A')} reviews)</p>
                        <p><strong>🏷️ Type:</strong> {hotel.get('type', 'Hotel')}</p>
                        <p><strong>✨ Amenities:</strong> Wi-Fi, Pool, Spa, Gym, Restaurant</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    nights = (check_out - check_in).days
                    total_price = float(hotel['price']) * nights
                    
                    st.markdown(f"""
                    <div class="price-tag">
                        ${hotel['price']}/night
                    </div>
                    <br>
                    <p><strong>Total ({nights} nights):</strong> ${total_price:,.2f}</p>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"📋 Book {hotel['name']}", key=f"book_hotel_{i}"):
                        book_hotel_form(hotel, check_in, check_out, guests)

def book_hotel_form(hotel, check_in, check_out, guests):
    """Hotel booking form"""
    
    st.markdown("---")
    st.markdown(f"### 📋 **Booking: {hotel['name']}**")
    
    with st.form(f"hotel_booking_form_{hotel['id']}"):
        # Customer details
        st.markdown("**👤 Guest Information**")
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name*")
            email = st.text_input("Email*")
            phone = st.text_input("Phone*")
        
        with col2:
            last_name = st.text_input("Last Name*")
            guest_count = st.number_input("Number of Guests", 1, 10, guests)
            room_type = st.selectbox("Room Type", ["Standard", "Deluxe", "Suite", "Family Room"])
        
        # Special requests
        special_requests = st.text_area("Special Requests (Optional)", 
                                      placeholder="e.g., Late check-in, airport pickup, dietary requirements")
        
        # Payment simulation
        st.markdown("**💳 Payment Information**")
        payment_method = st.selectbox("Payment Method", ["Credit Card", "Debit Card", "PayPal"])
        
        # Calculate pricing
        nights = (check_out - check_in).days
        base_price = float(hotel['price']) * nights
        tax = base_price * 0.12  # 12% tax
        service_fee = base_price * 0.02  # 2% service fee
        total_amount = base_price + tax + service_fee
        
        # Pricing breakdown
        st.markdown("**💰 Pricing Breakdown**")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            - **Base Price:** ${base_price:,.2f}
            - **Tax (12%):** ${tax:,.2f}
            - **Service Fee (2%):** ${service_fee:,.2f}
            """)
        
        with col2:
            st.markdown(f"""
            <div class="price-tag">
                **Total: ${total_amount:,.2f}**
            </div>
            """, unsafe_allow_html=True)
        
        # Terms and submit
        terms_accepted = st.checkbox("I accept the terms and conditions*")
        
        submitted = st.form_submit_button("🎉 Confirm Booking", type="primary")
        
        if submitted:
            if all([first_name, last_name, email, phone, terms_accepted]):
                # Process booking
                with st.spinner("🔄 Processing your hotel booking..."):
                    try:
                        booking_confirmation = st.session_state.booking_system.book_hotel(
                            user_id="demo_user",
                            hotel_id=str(hotel['id']),
                            check_in=check_in.strftime("%Y-%m-%d"),
                            check_out=check_out.strftime("%Y-%m-%d"),
                            room_type=room_type,
                            guests=guest_count,
                            special_requests=[special_requests] if special_requests else []
                        )
                        
                        # Success message
                        st.markdown(f"""
                        <div class="booking-success">
                            <h3>🎉 Booking Confirmed!</h3>
                            <p><strong>Confirmation Number:</strong> {booking_confirmation.confirmation_number}</p>
                            <p><strong>Hotel:</strong> {hotel['name']}</p>
                            <p><strong>Dates:</strong> {check_in} to {check_out}</p>
                            <p><strong>Total Amount:</strong> ${total_amount:,.2f}</p>
                            <p><strong>Status:</strong> {booking_confirmation.status.value.title()}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.balloons()
                        
                        # Add to booking history
                        booking_record = {
                            'booking_id': booking_confirmation.booking_id,
                            'confirmation_number': booking_confirmation.confirmation_number,
                            'type': 'Hotel',
                            'details': {
                                'hotel_name': hotel['name'],
                                'check_in': check_in.strftime("%Y-%m-%d"),
                                'check_out': check_out.strftime("%Y-%m-%d"),
                                'guests': guest_count,
                                'total_amount': total_amount
                            },
                            'status': booking_confirmation.status.value,
                            'created_at': datetime.now()
                        }
                        
                        st.session_state.booking_history.append(booking_record)
                        
                    except Exception as e:
                        st.error(f"❌ Booking failed: {str(e)}")
                        st.error("Please try again or contact support.")
            else:
                st.error("❌ Please fill in all required fields and accept the terms.")

def restaurant_booking_page():
    """Restaurant booking interface"""
    
    st.title("🍽️ **Restaurant Reservations**")
    st.markdown("*Book tables at premium restaurants with instant confirmation*")
    
    # Search form
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        cities_list = get_all_cities()
        city = st.selectbox("🌍 City", cities_list)
    
    with col2:
        reservation_date = st.date_input("📅 Date", datetime.now() + timedelta(days=1))
    
    with col3:
        reservation_time = st.time_input("🕐 Time", datetime.now().replace(hour=19, minute=30).time())
    
    with col4:
        party_size = st.number_input("👥 Party Size", 1, 20, 2)
    
    if st.button("🔍 Find Restaurants", type="primary"):
        restaurants = get_available_restaurants(city)
        
        st.markdown("### 🍽️ **Available Restaurants**")
        
        for i, restaurant in enumerate(restaurants):
            with st.expander(f"🍽️ {restaurant['name']} - {restaurant['cuisine']}", expanded=(i == 0)):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"""
                    <div class="restaurant-card">
                        <h4>{restaurant['name']}</h4>
                        <p><strong>🍴 Cuisine:</strong> {restaurant['cuisine']}</p>
                        <p><strong>⭐ Rating:</strong> {restaurant['rating']}/5</p>
                        <p><strong>📍 Location:</strong> {restaurant['location']}</p>
                        <p><strong>💰 Price Range:</strong> {restaurant['price_range']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    deposit = restaurant.get('deposit', 0) * party_size
                    st.markdown(f"""
                    <p><strong>Deposit:</strong> ${deposit}/person</p>
                    <p><strong>Total Deposit:</strong> ${deposit * party_size}</p>
                    """)
                    
                    if st.button(f"📋 Reserve Table", key=f"book_restaurant_{i}"):
                        book_restaurant_form(restaurant, reservation_date, reservation_time, party_size)

def book_restaurant_form(restaurant, date, time, party_size):
    """Restaurant booking form"""
    
    st.markdown("---")
    st.markdown(f"### 📋 **Reservation: {restaurant['name']}**")
    
    with st.form(f"restaurant_booking_form_{restaurant['id']}"):
        # Customer details
        st.markdown("**👤 Contact Information**")
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name*")
            phone = st.text_input("Phone*")
        
        with col2:
            last_name = st.text_input("Last Name*")
            email = st.text_input("Email*")
        
        # Reservation details
        occasion = st.selectbox("Occasion", ["Regular Dining", "Birthday", "Anniversary", "Business Meeting", "Other"])
        special_requests = st.text_area("Special Requests", 
                                       placeholder="e.g., Window table, dietary restrictions, celebrations")
        
        # Confirmation
        datetime_str = f"{date} {time}"
        deposit_amount = restaurant.get('deposit', 0) * party_size
        
        st.markdown(f"""
        **📋 Reservation Summary:**
        - **Restaurant:** {restaurant['name']}
        - **Date & Time:** {datetime_str}
        - **Party Size:** {party_size} people
        - **Deposit:** ${deposit_amount}
        """)
        
        terms_accepted = st.checkbox("I accept the reservation terms*")
        
        submitted = st.form_submit_button("🎉 Confirm Reservation", type="primary")
        
        if submitted:
            if all([first_name, last_name, phone, email, terms_accepted]):
                with st.spinner("🔄 Processing your reservation..."):
                    try:
                        booking_confirmation = st.session_state.booking_system.book_restaurant(
                            user_id="demo_user",
                            restaurant_id=str(restaurant['id']),
                            date_time=datetime_str,
                            party_size=party_size,
                            special_requests=[special_requests] if special_requests else []
                        )
                        
                        st.markdown(f"""
                        <div class="booking-success">
                            <h3>🎉 Reservation Confirmed!</h3>
                            <p><strong>Confirmation Number:</strong> {booking_confirmation.confirmation_number}</p>
                            <p><strong>Restaurant:</strong> {restaurant['name']}</p>
                            <p><strong>Date & Time:</strong> {datetime_str}</p>
                            <p><strong>Party Size:</strong> {party_size} people</p>
                            <p><strong>Status:</strong> {booking_confirmation.status.value.title()}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.balloons()
                        
                    except Exception as e:
                        st.error(f"❌ Reservation failed: {str(e)}")
            else:
                st.error("❌ Please fill in all required fields.")

def package_creation_page():
    """Unified AI-Powered Travel Package Creation"""
    
    st.title("🎯 **AI Travel Package Creator**")
    st.markdown("*Tell us about your dream trip, and we'll create personalized packages just for you*")
    
    # User Profile Display
    with st.sidebar:
        st.markdown("### 👤 **Your Travel Profile**")
        profile = st.session_state.user_profile
        
        with st.expander("📝 Edit Profile", expanded=False):
            profile['name'] = st.text_input("Name", profile['name'])
            profile['age'] = st.number_input("Age", value=profile['age'], min_value=18, max_value=100)
            profile['travel_style'] = st.selectbox("Travel Style", 
                ['cultural explorer', 'adventure seeker', 'luxury traveler', 'family friendly'], 
                index=['cultural explorer', 'adventure seeker', 'luxury traveler', 'family friendly'].index(profile['travel_style']))
            profile['budget_preference'] = st.selectbox("Budget Preference", 
                ['budget', 'moderate', 'luxury'], 
                index=['budget', 'moderate', 'luxury'].index(profile['budget_preference']))
            
            # Interests (multi-select)
            all_interests = ['cultural experiences', 'local cuisine', 'photography', 'art galleries', 
                           'adventure sports', 'nightlife', 'shopping', 'nature', 'history', 'music']
            profile['interests'] = st.multiselect("Interests", all_interests, default=profile['interests'])
            
            # Dietary restrictions
            diet_options = ['none', 'vegetarian', 'vegan', 'gluten-free', 'halal', 'kosher']
            profile['dietary_restrictions'] = st.multiselect("Dietary Restrictions", diet_options, default=profile.get('dietary_restrictions', []))
        
        # Display current profile
        st.markdown(f"""
        **🧳 {profile['name']}** ({profile['age']} years)  
        **Style:** {profile['travel_style'].title()}  
        **Budget:** {profile['budget_preference'].title()}  
        **Interests:** {', '.join(profile['interests'][:3])}{'...' if len(profile['interests']) > 3 else ''}
        """)
    
    # Main package creation interface
    st.markdown("### 🗣️ **Describe Your Dream Trip**")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # User trip description
        user_prompt = st.text_area(
            "Tell us about your ideal trip:",
            placeholder="I want to explore the rich culture of Paris, experience authentic French cuisine, visit world-class art museums, and discover hidden local gems. I'm particularly interested in photography opportunities and would love to learn some French cooking...",
            height=120
        )
        
        # Trip parameters
        col1a, col1b = st.columns(2)
        with col1a:
            destinations_list = get_all_destinations()
            destination = st.selectbox("🌍 Primary Destination", destinations_list)
            travelers = st.number_input("👥 Number of Travelers", 1, 10, 2)
        
        with col1b:
            start_date = st.date_input("📅 Start Date", datetime.now() + timedelta(days=14))
            duration = st.number_input("📅 Duration (days)", 1, 21, 7)
        
        # Budget selection
        budget = st.selectbox("💰 Budget Range", 
            ["Budget ($500-1000)", "Moderate ($1000-2500)", "Luxury ($2500+)"],
            index=1)
    
    with col2:
        st.markdown("### 🎨 **Package Preferences**")
        
        # Package customization options
        include_flights = st.checkbox("✈️ Include Flights", value=True)
        include_activities = st.checkbox("🎯 Include Activities", value=True)
        include_local_experiences = st.checkbox("🌟 Include Local Experiences", value=True)
        
        # Travel pace
        travel_pace = st.selectbox("Pace", ["Relaxed", "Moderate", "Active"])
        
        # Group type
        group_type = st.selectbox("Group Type", ["Solo", "Couple", "Family", "Friends"])
    
    # Generate packages button
    if st.button("🚀 **Generate My Personalized Packages**", type="primary", use_container_width=True):
        if user_prompt and destination:
            with st.spinner("🤖 Our AI is crafting personalized packages for you..."):
                # Generate 4 different package variations based on different styles
                packages = []
                
                # Define 4 diverse package types
                package_variations = [
                    {
                        'style_override': 'cultural-immersive',
                        'budget_modifier': 0,
                        'title_suffix': 'Cultural Heritage Explorer',
                        'focus_override': 'Deep cultural immersion with historical sites and local traditions'
                    },
                    {
                        'style_override': 'culinary-focused', 
                        'budget_modifier': 0.1,
                        'title_suffix': 'Culinary Discovery Journey',
                        'focus_override': 'Authentic local cuisine and cooking experiences'
                    },
                    {
                        'style_override': 'luxury-premium' if budget != "Budget ($500-1000)" else 'photography-focused',
                        'budget_modifier': 0.2,
                        'title_suffix': 'Premium Luxury Experience' if budget != "Budget ($500-1000)" else 'Photography Expedition',
                        'focus_override': 'High-end accommodations and exclusive experiences' if budget != "Budget ($500-1000)" else 'Stunning photography opportunities and scenic locations'
                    },
                    {
                        'style_override': 'budget-conscious' if budget == "Luxury ($2500+)" else 'adventure-active',
                        'budget_modifier': -0.1 if budget == "Luxury ($2500+)" else 0.05,
                        'title_suffix': 'Smart Budget Explorer' if budget == "Luxury ($2500+)" else 'Adventure & Active Explorer',
                        'focus_override': 'Maximum value with authentic local experiences' if budget == "Luxury ($2500+)" else 'Outdoor adventures and active experiences'
                    }
                ]
                
                for i, variation in enumerate(package_variations):
                    # Create modified profile for package variation
                    varied_profile = profile.copy()
                    
                    # Adjust interests based on variation
                    if variation['style_override'] == 'culinary-focused':
                        varied_profile['interests'] = ['local cuisine'] + [x for x in profile['interests'] if x != 'local cuisine']
                    elif variation['style_override'] == 'adventure-active':
                        varied_profile['interests'] = profile['interests'] + ['adventure sports', 'outdoor activities']
                    elif variation['style_override'] == 'photography-focused':
                        varied_profile['interests'] = ['photography'] + profile['interests']
                    
                    # Modify user prompt to emphasize different aspects
                    modified_prompt = enhance_prompt_for_variation(user_prompt, variation['style_override'])
                    
                    # Generate package with specific style
                    package = generate_personalized_package(
                        modified_prompt, varied_profile, destination, duration, travelers, budget
                    )
                    
                    # Override title and focus with variation specifics
                    package['title'] = f"{destination} {variation['title_suffix']}"
                    package['focus'] = variation['focus_override']
                    package['variation_type'] = variation['style_override']
                    
                    packages.append(package)
                
                # Store generated packages
                st.session_state.generated_packages = packages
                
                st.success("🎉 Successfully generated 4 unique personalized packages for you!")
                st.info("💡 Each package offers a different travel experience - choose the one that matches your mood!")

def enhance_prompt_for_variation(original_prompt, style_override):
    """Enhance the user prompt to emphasize different travel styles"""
    
    style_enhancements = {
        'cultural-immersive': original_prompt + " I want to deeply understand the local culture, visit historical sites, museums, and interact with local traditions.",
        'culinary-focused': original_prompt + " I'm passionate about experiencing authentic local cuisine, learning cooking techniques, visiting food markets, and discovering regional specialties.",
        'luxury-premium': original_prompt + " I prefer high-end accommodations, exclusive experiences, private tours, luxury amenities, and premium service throughout my journey.",
        'adventure-active': original_prompt + " I love outdoor activities, active experiences, hiking, sports, and adventure-filled itineraries that keep me engaged.",
        'photography-focused': original_prompt + " I'm passionate about photography and want to capture stunning photos, visit scenic locations, and have unique Instagram-worthy experiences.",
        'budget-conscious': original_prompt + " I want to maximize value for money while still having authentic experiences, prefer budget-friendly options without compromising on quality."
    }
    
    return style_enhancements.get(style_override, original_prompt)
    
    # Display generated packages
    if st.session_state.generated_packages:
        st.markdown("---")
        st.markdown("### 📦 **Your Personalized Travel Packages**")
        
        # Package cards in columns
        cols = st.columns(len(st.session_state.generated_packages))
        
        for i, package in enumerate(st.session_state.generated_packages):
            with cols[i]:
                display_package_card(package, i)
    
    # Package details view
    if st.session_state.viewing_package_details:
        display_package_details(st.session_state.viewing_package_details)

def display_package_card(package, index):
    """Display a clickable package card"""
    
    pricing = package['pricing']
    
    # Package card with attractive styling
    st.markdown(f"""
    <div class="package-card" style="border-left-color: {'#28a745' if index == 0 else '#007bff' if index == 1 else '#fd7e14'};">
        <h4>{package['title']}</h4>
        <p><strong>🎯 Focus:</strong> {package['focus']}</p>
        <p><strong>📅 Duration:</strong> {package['duration']} days</p>
        <p><strong>👥 Travelers:</strong> {package['travelers']}</p>
        <p><strong>✈️ Flights:</strong> {len(package['flights'])} options</p>
        <p><strong>🏨 Hotels:</strong> {len(package['hotels'])} recommendations</p>
        <p><strong>🍽️ Restaurants:</strong> {len(package['restaurants'])} curated spots</p>
        <p><strong>🎯 Activities:</strong> {len(package['activities'])} experiences</p>
        <p><strong>🌟 Local Gems:</strong> {len(package['local_experiences'])} unique experiences</p>
        <br>
        <div class="price-tag" style="font-size: 1.1rem; padding: 0.8rem 1.5rem;">
            ${pricing['total_cost']:,.0f} total
        </div>
        <p style="text-align: center; margin-top: 0.5rem;">
            <small>${pricing['cost_per_person']:,.0f} per person</small>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Action buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(f"👁️ **Explore Package**", key=f"explore_{index}", use_container_width=True):
            st.session_state.viewing_package_details = package
            st.rerun()
    
    with col2:
        if st.button(f"🎉 **Book Now**", key=f"book_{index}", type="primary", use_container_width=True):
            book_complete_package(package)

def display_package_details(package):
    """Display detailed package information"""
    
    st.markdown("---")
    st.markdown(f"## 📋 **{package['title']} - Detailed Itinerary**")
    
    # Package overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Cost", f"${package['pricing']['total_cost']:,.0f}")
        st.metric("Per Person", f"${package['pricing']['cost_per_person']:,.0f}")
    
    with col2:
        st.metric("Duration", f"{package['duration']} days")
        st.metric("Daily Average", f"${package['pricing']['daily_average']:,.0f}")
    
    with col3:
        st.metric("Travelers", package['travelers'])
        st.metric("Package Rating", "⭐⭐⭐⭐⭐")
    
    # Detailed sections in tabs
    tabs = st.tabs(["📅 Daily Itinerary", "✈️ Flights", "🏨 Hotels", "🍽️ Restaurants", "🎯 Activities", "🌟 Local Experiences", "💰 Pricing"])
    
    with tabs[0]:  # Daily Itinerary
        display_daily_itinerary(package['daily_itinerary'])
    
    with tabs[1]:  # Flights
        display_flight_options(package['flights'])
    
    with tabs[2]:  # Hotels
        display_hotel_recommendations(package['hotels'])
    
    with tabs[3]:  # Restaurants
        display_restaurant_recommendations(package['restaurants'])
    
    with tabs[4]:  # Activities
        display_activities(package['activities'])
    
    with tabs[5]:  # Local Experiences
        display_local_experiences(package['local_experiences'])
    
    with tabs[6]:  # Pricing
        display_pricing_breakdown(package['pricing'])
    
    # Action buttons
    st.markdown("---")
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col1:
        if st.button("⬅️ **Back to Packages**", use_container_width=True):
            st.session_state.viewing_package_details = None
            st.rerun()
    
    with col2:
        if st.button("📄 **Generate PDF**", use_container_width=True):
            generate_package_pdf(package)
    
    with col3:
        if st.button("💾 **Save Package**", use_container_width=True):
            save_package_to_favorites(package)
    
    with col4:
        if st.button("🎉 **Book This Complete Package**", type="primary", use_container_width=True):
            book_complete_package(package)

def generate_package_pdf(package):
    """Generate a comprehensive PDF of the travel package"""
    
    try:
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
        import io
        
        # Create PDF in memory
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, 
                              topMargin=72, bottomMargin=18)
        
        # Define styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.navy
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'], 
            fontSize=16,
            spaceAfter=12,
            textColor=colors.darkblue
        )
        
        # Build PDF content
        story = []
        
        # Title
        story.append(Paragraph(f"{package['title']}", title_style))
        story.append(Paragraph(f"Destination: {package['destination']}", styles['Normal']))
        story.append(Paragraph(f"Duration: {package['duration']} days for {package['travelers']} travelers", styles['Normal']))
        story.append(Paragraph(f"Total Cost: ${package['pricing']['total_cost']:,.0f} (${package['pricing']['cost_per_person']:,.0f} per person)", styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Package Overview
        story.append(Paragraph("Package Overview", heading_style))
        story.append(Paragraph(f"Focus: {package['focus']}", styles['Normal']))
        story.append(Spacer(1, 12))
        
        # Daily Itinerary
        story.append(Paragraph("Daily Itinerary", heading_style))
        for day_plan in package['daily_itinerary']:
            story.append(Paragraph(f"<b>Day {day_plan['day']}: {day_plan['theme']}</b>", styles['Normal']))
            story.append(Paragraph(f"Morning: {day_plan['morning']}", styles['Normal']))
            story.append(Paragraph(f"Afternoon: {day_plan['afternoon']}", styles['Normal']))
            story.append(Paragraph(f"Evening: {day_plan['evening']}", styles['Normal']))
            story.append(Paragraph(f"Estimated Cost: ${day_plan['estimated_cost']}", styles['Normal']))
            story.append(Spacer(1, 8))
        
        # Flights
        story.append(Paragraph("Flight Options", heading_style))
        for flight in package['flights']:
            story.append(Paragraph(f"• {flight['airline']} - {flight['class']}", styles['Normal']))
            story.append(Paragraph(f"  Price: ${flight['price_per_person']:,} per person | Duration: {flight['duration']}", styles['Normal']))
            story.append(Spacer(1, 6))
        
        # Hotels
        story.append(Paragraph("Accommodation", heading_style))
        for hotel in package['hotels']:
            story.append(Paragraph(f"• {hotel['name']} ({hotel['rating']}⭐)", styles['Normal']))
            story.append(Paragraph(f"  ${hotel['price']}/night | {hotel['why_recommended']}", styles['Normal']))
            story.append(Spacer(1, 6))
        
        # Restaurants
        story.append(Paragraph("Dining Experiences", heading_style))
        for restaurant in package['restaurants']:
            story.append(Paragraph(f"• {restaurant['name']} - {restaurant['cuisine']}", styles['Normal']))
            story.append(Paragraph(f"  {restaurant['specialty']} | {restaurant['why_recommended']}", styles['Normal']))
            story.append(Spacer(1, 6))
        
        # Pricing Breakdown
        story.append(Paragraph("Pricing Breakdown", heading_style))
        pricing_data = [
            ['Component', 'Cost'],
            ['Flights', f"${package['pricing']['flights']:,.0f}"],
            ['Hotels', f"${package['pricing']['hotels']:,.0f}"],
            ['Restaurants', f"${package['pricing']['restaurants']:,.0f}"],
            ['Activities', f"${package['pricing']['activities']:,.0f}"],
            ['Taxes', f"${package['pricing']['taxes']:,.0f}"],
            ['Service Fee', f"${package['pricing']['service_fee']:,.0f}"],
            ['TOTAL', f"${package['pricing']['total_cost']:,.0f}"]
        ]
        
        pricing_table = Table(pricing_data)
        pricing_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(pricing_table)
        
        # Build PDF
        doc.build(story)
        
        # Get PDF data
        pdf_data = buffer.getvalue()
        buffer.close()
        
        # Create download button
        st.download_button(
            label="� **Download PDF Package**",
            data=pdf_data,
            file_name=f"{package['title'].replace(' ', '_')}_Travel_Package.pdf",
            mime="application/pdf",
            use_container_width=True
        )
        
        st.success("📄 PDF generated successfully! Click the download button above.")
        
    except ImportError:
        st.warning("📄 PDF generation requires additional libraries. Creating simplified text version...")
        
        # Fallback: Create text version
        text_content = generate_text_package_summary(package)
        
        st.download_button(
            label="📥 **Download Text Package**",
            data=text_content,
            file_name=f"{package['title'].replace(' ', '_')}_Travel_Package.txt",
            mime="text/plain",
            use_container_width=True
        )

def generate_text_package_summary(package):
    """Generate a text summary of the package as fallback"""
    
    content = f"""
TRAVEL PACKAGE SUMMARY
======================

Package: {package['title']}
Destination: {package['destination']}
Duration: {package['duration']} days for {package['travelers']} travelers
Total Cost: ${package['pricing']['total_cost']:,.0f} (${package['pricing']['cost_per_person']:,.0f} per person)

PACKAGE FOCUS
{package['focus']}

DAILY ITINERARY
===============
"""
    
    for day_plan in package['daily_itinerary']:
        content += f"""
Day {day_plan['day']}: {day_plan['theme']}
Morning: {day_plan['morning']}
Afternoon: {day_plan['afternoon']}
Evening: {day_plan['evening']}
Estimated Cost: ${day_plan['estimated_cost']}
"""
    
    content += "\n\nFLIGHT OPTIONS\n==============\n"
    for flight in package['flights']:
        content += f"• {flight['airline']} - {flight['class']}\n"
        content += f"  Price: ${flight['price_per_person']:,} per person | Duration: {flight['duration']}\n\n"
    
    content += "\nACCOMMODATION\n=============\n"
    for hotel in package['hotels']:
        content += f"• {hotel['name']} ({hotel['rating']}⭐)\n"
        content += f"  ${hotel['price']}/night | {hotel['why_recommended']}\n\n"
    
    content += "\nDINING EXPERIENCES\n==================\n"
    for restaurant in package['restaurants']:
        content += f"• {restaurant['name']} - {restaurant['cuisine']}\n"
        content += f"  {restaurant['specialty']} | {restaurant['why_recommended']}\n\n"
    
    content += f"""
PRICING BREAKDOWN
=================
Flights: ${package['pricing']['flights']:,.0f}
Hotels: ${package['pricing']['hotels']:,.0f}
Restaurants: ${package['pricing']['restaurants']:,.0f}
Activities: ${package['pricing']['activities']:,.0f}
Taxes: ${package['pricing']['taxes']:,.0f}
Service Fee: ${package['pricing']['service_fee']:,.0f}
TOTAL: ${package['pricing']['total_cost']:,.0f}

Generated by AI Travel Platform
Visit us at: https://ai-travel-platform.com
"""
    
    return content

def display_daily_itinerary(itinerary):
    """Display day-by-day itinerary"""
    
    for day_plan in itinerary:
        with st.expander(f"📅 **Day {day_plan['day']}: {day_plan['theme']}**", expanded=day_plan['day'] <= 2):
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"""
                **🌅 Morning:** {day_plan['morning']}  
                **☀️ Afternoon:** {day_plan['afternoon']}  
                **🌆 Evening:** {day_plan['evening']}
                
                **🍽️ Meals:**
                - Breakfast: {day_plan['meals']['breakfast']}
                - Lunch: {day_plan['meals']['lunch']} 
                - Dinner: {day_plan['meals']['dinner']}
                """)
            
            with col2:
                st.markdown(f"""
                **🚗 Transportation:** {day_plan['transportation']}  
                **💰 Est. Daily Cost:** ${day_plan['estimated_cost']}
                """)

def display_flight_options(flights):
    """Display flight recommendations"""
    
    for i, flight in enumerate(flights):
        st.markdown(f"""
        <div class="hotel-card">
            <h4>✈️ {flight['airline']} - {flight['class']}</h4>
            <p><strong>💰 Price:</strong> ${flight['price_per_person']:,} per person (${flight['total_price']:,} total)</p>
            <p><strong>⏱️ Duration:</strong> {flight['duration']}</p>
            <p><strong>🔄 Stops:</strong> {'Direct' if flight['stops'] == 0 else f"{flight['stops']} stop(s)"}</p>
            <p><strong>🛫 Departure:</strong> {flight['departure']} → <strong>🛬 Arrival:</strong> {flight['arrival']}</p>
        </div>
        """, unsafe_allow_html=True)

def display_hotel_recommendations(hotels):
    """Display hotel recommendations with reasons"""
    
    for hotel in hotels:
        st.markdown(f"""
        <div class="hotel-card">
            <h4>🏨 {hotel['name']}</h4>
            <p><strong>⭐ Rating:</strong> {hotel['rating']}/5 • <strong>🏷️ Type:</strong> {hotel['type']}</p>
            <p><strong>💰 Price:</strong> ${hotel['price']}/night (${hotel['total_price']:,} total)</p>
            <p><strong>📍 Location Score:</strong> {hotel['location_score']}/10</p>
            <p><strong>✨ Amenities:</strong> {', '.join(hotel['amenities'])}</p>
            <p><strong>🎯 Why Recommended:</strong> {hotel['why_recommended']}</p>
        </div>
        """, unsafe_allow_html=True)

def display_restaurant_recommendations(restaurants):
    """Display restaurant recommendations"""
    
    for restaurant in restaurants:
        st.markdown(f"""
        <div class="restaurant-card">
            <h4>🍽️ {restaurant['name']}</h4>
            <p><strong>🍴 Cuisine:</strong> {restaurant['cuisine']} • <strong>⭐ Rating:</strong> {restaurant['rating']}/5</p>
            <p><strong>💰 Price Range:</strong> {restaurant['price_range']} • <strong>🌟 Specialty:</strong> {restaurant['specialty']}</p>
            <p><strong>🎯 Why Recommended:</strong> {restaurant['why_recommended']}</p>
            <p><strong>📅 Suggested Time:</strong> {restaurant['reservation_time']}</p>
            <p><strong>📝 Note:</strong> {restaurant['booking_notes']}</p>
        </div>
        """, unsafe_allow_html=True)

def display_activities(activities):
    """Display activity recommendations"""
    
    for activity in activities:
        st.markdown(f"""
        <div class="activity-card">
            <h4>🎯 {activity['name']}</h4>
            <p><strong>⏱️ Duration:</strong> {activity['duration']} • <strong>💰 Price:</strong> ${activity['price']}</p>
            <p><strong>🏷️ Type:</strong> {activity['type']} • <strong>📊 Difficulty:</strong> {activity['difficulty']}</p>
            <p><strong>👥 Group Size:</strong> {activity['group_size']}</p>
            <p><strong>🎯 Why Recommended:</strong> {activity['match_reason']}</p>
        </div>
        """, unsafe_allow_html=True)

def display_local_experiences(experiences):
    """Display local experience recommendations"""
    
    for exp in experiences:
        st.markdown(f"""
        <div class="activity-card" style="border-left-color: #ffc107;">
            <h4>🌟 {exp['name']}</h4>
            <p><strong>🏷️ Type:</strong> {exp['type']} • <strong>⏱️ Duration:</strong> {exp['duration']}</p>
            <p><strong>💰 Price:</strong> ${exp['price']} per person</p>
            <p><strong>✨ What makes it special:</strong> Unique local experience not found in typical tourist guides</p>
        </div>
        """, unsafe_allow_html=True)

def display_pricing_breakdown(pricing):
    """Display detailed pricing breakdown"""
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💰 **Cost Breakdown**")
        st.markdown(f"""
        - **✈️ Flights:** ${pricing['flights']:,.0f}
        - **🏨 Hotels:** ${pricing['hotels']:,.0f}
        - **🍽️ Restaurants:** ${pricing['restaurants']:,.0f}
        - **🎯 Activities:** ${pricing['activities']:,.0f}
        - **📊 Taxes:** ${pricing['taxes']:,.0f}
        - **🔧 Service Fee:** ${pricing['service_fee']:,.0f}
        """)
    
    with col2:
        st.markdown("### 📊 **Summary**")
        st.markdown(f"""
        - **Subtotal:** ${pricing['base_cost']:,.0f}
        - **Total Cost:** ${pricing['total_cost']:,.0f}
        - **Per Person:** ${pricing['cost_per_person']:,.0f}
        - **Daily Average:** ${pricing['daily_average']:,.0f}
        """)

def book_complete_package(package):
    """Enhanced intelligent booking system for complete travel package"""
    
    st.markdown("## 🎯 **Intelligent Package Booking System**")
    
    # Step 1: Booking Confirmation & Details Review
    with st.expander("📋 **Step 1: Review Package Details**", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            **📦 Package:** {package['title']}  
            **🌍 Destination:** {package['destination']}  
            **📅 Duration:** {package['duration']} days  
            **👥 Travelers:** {package['travelers']} people  
            **💰 Total Cost:** ${package['pricing']['total_cost']:,.0f}  
            **📊 Per Person:** ${package['pricing']['cost_per_person']:,.0f}
            """)
        
        with col2:
            st.markdown(f"""
            **🎯 Package Focus:** {package['focus']}  
            **✈️ Flights Included:** {len(package['flights'])} options  
            **🏨 Hotels Included:** {len(package['hotels'])} options  
            **🍽️ Restaurants Included:** {len(package['restaurants'])} reservations  
            **🎯 Activities Included:** {len(package['activities'])} experiences  
            **🌟 Local Experiences:** {len(package['local_experiences'])} unique activities
            """)
        
        package_confirmed = st.checkbox("✅ I confirm these package details are correct", key="package_confirm")
    
    # Step 2: Traveler Information
    if package_confirmed:
        with st.expander("� **Step 2: Traveler Information**", expanded=True):
            travelers_info = []
            
            st.markdown("**Please provide information for all travelers:**")
            
            for i in range(package['travelers']):
                st.markdown(f"**Traveler {i+1}:**")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    name = st.text_input(f"Full Name", key=f"traveler_{i}_name", placeholder="John Doe")
                with col2:
                    passport = st.text_input(f"Passport Number", key=f"traveler_{i}_passport", placeholder="AB1234567")
                with col3:
                    dob = st.date_input(f"Date of Birth", key=f"traveler_{i}_dob", 
                                      value=datetime(1990, 1, 1).date())
                
                travelers_info.append({
                    'name': name,
                    'passport': passport,
                    'date_of_birth': dob
                })
            
            # Contact Information
            st.markdown("**Primary Contact Information:**")
            col1, col2 = st.columns(2)
            
            with col1:
                contact_email = st.text_input("Email Address", placeholder="john@example.com")
                contact_phone = st.text_input("Phone Number", placeholder="+1 (555) 123-4567")
            
            with col2:
                emergency_contact = st.text_input("Emergency Contact Name", placeholder="Jane Doe")
                emergency_phone = st.text_input("Emergency Contact Phone", placeholder="+1 (555) 987-6543")
            
            travelers_confirmed = st.checkbox("✅ All traveler information is accurate", key="travelers_confirm")
    
    # Step 3: Component Selection & Customization
    if package_confirmed and travelers_confirmed:
        with st.expander("🎛️ **Step 3: Customize Package Components**", expanded=True):
            st.markdown("**Select your preferred options for each component:**")
            
            # Flight Selection
            st.markdown("**✈️ Flight Selection:**")
            selected_flight = st.selectbox(
                "Choose your preferred flight:",
                [f"{f['airline']} - {f['class']} (${f['price_per_person']:,}/person)" for f in package['flights']],
                key="flight_selection"
            )
            
            # Hotel Selection
            st.markdown("**🏨 Hotel Selection:**")
            selected_hotel = st.selectbox(
                "Choose your preferred hotel:",
                [f"{h['name']} - {h['type']} (${h['price']}/night)" for h in package['hotels']],
                key="hotel_selection"
            )
            
            # Special Requests
            st.markdown("**📝 Special Requests & Preferences:**")
            special_requests = st.text_area(
                "Any special requests, dietary restrictions, or accessibility needs:",
                placeholder="Room preferences, dietary restrictions, celebration occasions, etc.",
                key="special_requests"
            )
            
            components_confirmed = st.checkbox("✅ Component selections are finalized", key="components_confirm")
    
    # Step 4: Payment & Final Booking
    if package_confirmed and travelers_confirmed and components_confirmed:
        with st.expander("💳 **Step 4: Payment & Final Booking**", expanded=True):
            
            # Payment Summary
            st.markdown("**💰 Final Payment Summary:**")
            selected_flight_idx = [f"{f['airline']} - {f['class']} (${f['price_per_person']:,}/person)" for f in package['flights']].index(selected_flight)
            selected_hotel_idx = [f"{h['name']} - {h['type']} (${h['price']}/night)" for h in package['hotels']].index(selected_hotel)
            
            flight_cost = package['flights'][selected_flight_idx]['total_price']
            hotel_cost = package['hotels'][selected_hotel_idx]['total_price']
            
            st.markdown(f"""
            - **Selected Flight:** ${flight_cost:,.0f}
            - **Selected Hotel:** ${hotel_cost:,.0f}
            - **Restaurants & Activities:** ${package['pricing']['restaurants'] + package['pricing']['activities']:,.0f}
            - **Taxes & Fees:** ${package['pricing']['taxes'] + package['pricing']['service_fee']:,.0f}
            - **TOTAL AMOUNT:** ${package['pricing']['total_cost']:,.0f}
            """)
            
            # Payment Options
            payment_method = st.selectbox(
                "Payment Method:",
                ["💳 Credit Card", "🏦 Bank Transfer", "💰 PayPal", "📱 Digital Wallet"],
                key="payment_method"
            )
            
            # Terms and Conditions
            terms_accepted = st.checkbox(
                "✅ I accept the Terms & Conditions and Cancellation Policy",
                key="terms_confirm"
            )
            
            # Final Booking Button
            if terms_accepted:
                if st.button("🎉 **CONFIRM & BOOK COMPLETE PACKAGE**", type="primary", use_container_width=True):
                    process_intelligent_booking(package, travelers_info, contact_email, contact_phone, 
                                              emergency_contact, emergency_phone, selected_flight_idx, 
                                              selected_hotel_idx, special_requests, payment_method)

def process_intelligent_booking(package, travelers_info, contact_email, contact_phone, 
                               emergency_contact, emergency_phone, flight_idx, hotel_idx, 
                               special_requests, payment_method):
    """Process the complete intelligent booking with all details"""
    
    with st.spinner("🔄 Processing your complete package booking with all components..."):
        try:
            import time
            time.sleep(3)  # Simulate processing time
            
            # Generate confirmation details
            booking_confirmation = {
                'booking_id': f"PKG_{datetime.now().strftime('%Y%m%d')}_{len(st.session_state.booking_history) + 1:04d}",
                'confirmation_number': f"ATP{datetime.now().strftime('%Y%m%d')}{len(st.session_state.booking_history) + 1:03d}",
                'package_title': package['title'],
                'destination': package['destination'],
                'duration': package['duration'],
                'travelers': package['travelers'],
                'traveler_details': travelers_info,
                'total_amount': package['pricing']['total_cost'],
                'selected_flight': package['flights'][flight_idx],
                'selected_hotel': package['hotels'][hotel_idx],
                'contact_info': {
                    'email': contact_email,
                    'phone': contact_phone,
                    'emergency_contact': emergency_contact,
                    'emergency_phone': emergency_phone
                },
                'special_requests': special_requests,
                'payment_method': payment_method,
                'created_at': datetime.now(),
                'status': 'confirmed'
            }
            
            # Add to booking history
            st.session_state.booking_history.append({
                'booking_id': booking_confirmation['booking_id'],
                'confirmation_number': booking_confirmation['confirmation_number'],
                'type': 'Complete Package',
                'details': {
                    'package_title': package['title'],
                    'destination': package['destination'],
                    'duration': package['duration'],
                    'travelers': package['travelers'],
                    'total_amount': package['pricing']['total_cost'],
                    'includes': {
                        'flights': package['flights'][flight_idx]['airline'],
                        'hotel': package['hotels'][hotel_idx]['name'],
                        'restaurants': len(package['restaurants']),
                        'activities': len(package['activities']),
                        'local_experiences': len(package['local_experiences'])
                    },
                    'contact_email': contact_email,
                    'special_requests': special_requests
                },
                'status': 'confirmed',
                'created_at': datetime.now()
            })
            
            # Success Display
            st.markdown(f"""
            <div class="booking-success">
                <h2>🎉 Complete Package Successfully Booked!</h2>
                
                <div style="background: white; padding: 1.5rem; border-radius: 10px; margin: 1rem 0; border-left: 4px solid #22c55e;">
                    <h3>📋 Booking Confirmation Details</h3>
                    <p><strong>Confirmation Number:</strong> <span style="font-size: 1.2em; color: #1e40af;">{booking_confirmation['confirmation_number']}</span></p>
                    <p><strong>Booking ID:</strong> {booking_confirmation['booking_id']}</p>
                    <p><strong>Package:</strong> {package['title']}</p>
                    <p><strong>Destination:</strong> {package['destination']}</p>
                    <p><strong>Duration:</strong> {package['duration']} days for {package['travelers']} travelers</p>
                    <p><strong>Total Amount:</strong> ${package['pricing']['total_cost']:,.0f}</p>
                    <p><strong>Status:</strong> ✅ <span style="color: #22c55e; font-weight: bold;">CONFIRMED</span></p>
                </div>
                
                <div style="background: #f0f9ff; padding: 1.5rem; border-radius: 10px; margin: 1rem 0; border-left: 4px solid #3b82f6;">
                    <h3>📦 What's Included & Confirmed:</h3>
                    <p>✈️ <strong>Flight:</strong> {package['flights'][flight_idx]['airline']} - {package['flights'][flight_idx]['class']}</p>
                    <p>🏨 <strong>Hotel:</strong> {package['hotels'][hotel_idx]['name']} for {package['duration']} nights</p>
                    <p>🍽️ <strong>Restaurant Reservations:</strong> {len(package['restaurants'])} curated dining experiences</p>
                    <p>🎯 <strong>Activities:</strong> {len(package['activities'])} planned activities and tours</p>
                    <p>🌟 <strong>Local Experiences:</strong> {len(package['local_experiences'])} unique local experiences</p>
                    <p>📱 <strong>24/7 Support:</strong> Dedicated travel concierge throughout your journey</p>
                </div>
                
                <div style="background: #fffbeb; padding: 1.5rem; border-radius: 10px; margin: 1rem 0; border-left: 4px solid #f59e0b;">
                    <h3>📧 Next Steps</h3>
                    <p>📧 <strong>Detailed confirmations</strong> for flights, hotels, and activities will be sent to <strong>{contact_email}</strong> within 24 hours</p>
                    <p>📱 <strong>Mobile itinerary</strong> and travel documents will be available in your account 48 hours before departure</p>
                    <p>🎫 <strong>Digital tickets</strong> and reservation confirmations will be sent 1 week before travel</p>
                    <p>☎️ <strong>Pre-travel consultation</strong> call scheduled 3 days before departure</p>
                </div>
                
                <div style="background: #fef2f2; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                    <p><strong>⚠️ Important:</strong> Please save this confirmation number: <strong>{booking_confirmation['confirmation_number']}</strong></p>
                    <p>You will need it for all travel-related inquiries and modifications.</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.balloons()
            
            # Clear viewing state and show success actions
            st.session_state.viewing_package_details = None
            
            # Offer additional actions
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("📧 Email Confirmation", use_container_width=True):
                    st.success(f"📧 Confirmation details sent to {contact_email}")
            with col2:
                if st.button("📱 Add to Calendar", use_container_width=True):
                    st.success("📅 Travel dates added to your calendar")
            with col3:
                if st.button("🏠 Return Home", use_container_width=True):
                    st.session_state.current_page = "main"
                    st.rerun()
            
        except Exception as e:
            st.error(f"❌ Package booking failed: {str(e)}")
            st.markdown("**Please try again or contact support for assistance.**")
            st.markdown("📞 Support: +1 (555) 123-HELP | 📧 support@ai-travel.com")

def save_package_to_favorites(package):
    """Save package to user favorites"""
    if 'saved_packages' not in st.session_state:
        st.session_state.saved_packages = []
    
    st.session_state.saved_packages.append(package)
    st.success("💾 Package saved to your favorites!")

def booking_history_page():
    """Booking history and management"""
    
    st.title("📋 **Booking History**")
    
    if st.session_state.booking_history:
        st.markdown("### 📚 **Your Bookings**")
        
        for booking in st.session_state.booking_history:
            with st.expander(f"📋 {booking['confirmation_number']} - {booking['type']}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"""
                    **Booking ID:** {booking['booking_id']}  
                    **Type:** {booking['type']}  
                    **Status:** {booking['status']}  
                    **Created:** {booking['created_at'].strftime('%Y-%m-%d %H:%M')}
                    """)
                
                with col2:
                    details = booking['details']
                    if booking['type'] == 'Hotel':
                        st.markdown(f"""
                        **Hotel:** {details['hotel_name']}  
                        **Check-in:** {details['check_in']}  
                        **Check-out:** {details['check_out']}  
                        **Total:** ${details['total_amount']:,.2f}
                        """)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("📧 Email Confirmation", key=f"email_{booking['booking_id']}"):
                        st.success("📧 Confirmation email sent!")
                with col2:
                    if st.button("✏️ Modify Booking", key=f"modify_{booking['booking_id']}"):
                        st.info("✏️ Modification form would open here")
                with col3:
                    if st.button("❌ Cancel Booking", key=f"cancel_{booking['booking_id']}"):
                        st.warning("❌ Cancellation form would open here")
    else:
        st.info("📭 No bookings yet. Start by booking a hotel or restaurant!")

def analytics_dashboard():
    """Professional investor-focused analytics dashboard"""
    
    st.title("📊 **Investment Analytics Dashboard**")
    st.markdown("*Real-time business intelligence and market insights*")
    
    # Key Performance Indicators
    st.markdown("### 🎯 **Key Performance Indicators**")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Monthly Revenue", "$425K", "↗️ 47%", help="Gross monthly revenue from all sources")
    
    with col2:
        st.metric("Gross Margin", "68%", "↗️ 3%", help="Revenue minus direct costs")
    
    with col3:
        st.metric("Customer LTV", "$1,247", "↗️ 18%", help="Customer Lifetime Value")
    
    with col4:
        st.metric("CAC Payback", "4.2 months", "↘️ 0.8", help="Customer Acquisition Cost payback period")
    
    with col5:
        st.metric("Monthly Churn", "2.1%", "↘️ 0.4%", help="Monthly customer churn rate")
    
    # Revenue growth visualization
    st.markdown("### 📈 **Revenue Growth Trajectory**")
    
    # Generate realistic revenue data
    months = ['Jan 2024', 'Feb 2024', 'Mar 2024', 'Apr 2024', 'May 2024', 'Jun 2024', 
              'Jul 2024', 'Aug 2024', 'Sep 2024', 'Oct 2024', 'Nov 2024', 'Dec 2024',
              'Jan 2025', 'Feb 2025', 'Mar 2025', 'Apr 2025', 'May 2025', 'Jun 2025']
    
    revenue_data = [125, 147, 168, 192, 234, 267, 298, 334, 387, 398, 412, 425,
                   467, 523, 578, 634, 697, 765]
    
    bookings_revenue = [85, 98, 115, 132, 162, 185, 208, 234, 271, 279, 289, 298,
                       327, 367, 405, 444, 488, 536]
    
    subscriptions_revenue = [28, 33, 36, 42, 48, 55, 62, 69, 78, 81, 84, 87,
                           95, 105, 116, 127, 139, 153]
    
    data_revenue = [12, 16, 17, 18, 24, 27, 28, 31, 38, 38, 39, 40,
                   45, 51, 57, 63, 70, 76]
    
    # Create revenue chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=months, y=revenue_data,
        mode='lines+markers',
        name='Total Revenue',
        line=dict(color='#667eea', width=4),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=months, y=bookings_revenue,
        mode='lines+markers',
        name='Booking Commissions',
        line=dict(color='#28a745', width=3),
        marker=dict(size=6)
    ))
    
    fig.add_trace(go.Scatter(
        x=months, y=subscriptions_revenue,
        mode='lines+markers',
        name='Subscriptions',
        line=dict(color='#ffc107', width=3),
        marker=dict(size=6)
    ))
    
    fig.add_trace(go.Scatter(
        x=months, y=data_revenue,
        mode='lines+markers',
        name='Data & Analytics',
        line=dict(color='#fd7e14', width=3),
        marker=dict(size=6)
    ))
    
    fig.update_layout(
        title="Monthly Revenue Growth ($K)",
        xaxis_title="Month",
        yaxis_title="Revenue ($K)",
        hovermode='x unified',
        height=500,
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Market penetration and user acquisition
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌍 **Market Penetration**")
        
        # Market share data
        market_data = pd.DataFrame({
            'Region': ['North America', 'Europe', 'Middle East', 'Asia Pacific', 'Latin America'],
            'Market Share (%)': [12.4, 8.7, 18.9, 5.2, 3.1],
            'Growth Rate (%)': [45, 67, 89, 123, 156]
        })
        
        fig_market = px.bar(
            market_data, 
            x='Region', 
            y='Market Share (%)',
            color='Growth Rate (%)',
            title="Regional Market Share & Growth",
            color_continuous_scale='Viridis'
        )
        
        fig_market.update_layout(height=400)
        st.plotly_chart(fig_market, use_container_width=True)
    
    with col2:
        st.markdown("### 👥 **User Acquisition Channels**")
        
        # User acquisition data
        acquisition_data = pd.DataFrame({
            'Channel': ['Organic Search', 'Paid Social', 'Direct', 'Email', 'Referral', 'Partnerships'],
            'Users': [28450, 18750, 12340, 8920, 6780, 4560],
            'Cost per User': [12, 28, 0, 5, 3, 15]
        })
        
        fig_acquisition = px.pie(
            acquisition_data,
            values='Users',
            names='Channel',
            title="User Acquisition by Channel",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        
        fig_acquisition.update_layout(height=400)
        st.plotly_chart(fig_acquisition, use_container_width=True)
    
    # Financial projections
    st.markdown("### 💰 **Financial Projections & Investor Returns**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="roi-card">
            <h4>3-Year Financial Forecast</h4>
            <p><strong>Year 1 (2025):</strong></p>
            <p>• Revenue: $6.2M (145% growth)</p>
            <p>• Gross Margin: 71%</p>
            <p>• EBITDA: $1.8M (29%)</p>
            
            <p><strong>Year 2 (2026):</strong></p>
            <p>• Revenue: $15.8M (155% growth)</p>
            <p>• Gross Margin: 73%</p>
            <p>• EBITDA: $5.5M (35%)</p>
            
            <p><strong>Year 3 (2027):</strong></p>
            <p>• Revenue: $38.4M (143% growth)</p>
            <p>• Gross Margin: 75%</p>
            <p>• EBITDA: $15.4M (40%)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="competitive-advantage">
            <h4>Competitive Benchmarking</h4>
            <p><strong>vs. Traditional OTAs:</strong></p>
            <p>• 23% higher average transaction value</p>
            <p>• 67% lower customer acquisition cost</p>
            <p>• 89% higher customer retention</p>
            
            <p><strong>vs. AI Travel Startups:</strong></p>
            <p>• 156% faster revenue growth</p>
            <p>• 34% higher gross margins</p>
            <p>• 78% more comprehensive platform</p>
            
            <p><strong>Market Position:</strong></p>
            <p>🥇 #1 in AI travel personalization</p>
            <p>🥈 #2 in multi-service integration</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Unit economics
    st.markdown("### 📊 **Unit Economics & Business Model Validation**")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        **Customer Acquisition**
        - CAC: $34
        - Payback: 4.2 months
        - Channels: 6 active
        - Conversion: 3.4%
        """)
    
    with col2:
        st.markdown("""
        **Customer Lifetime Value**
        - LTV: $1,247
        - Avg. Lifespan: 28 months
        - Monthly Churn: 2.1%
        - Repeat Rate: 89%
        """)
    
    with col3:
        st.markdown("""
        **Transaction Metrics**
        - Avg. Transaction: $347
        - Take Rate: 12.5%
        - Frequency: 3.2x/year
        - Basket Size: +23% vs. market
        """)
    
    with col4:
        st.markdown("""
        **Operational Efficiency**
        - Gross Margin: 68%
        - EBITDA Margin: 29%
        - Tech Spend: 23% of revenue
        - Automation: 78% of processes
        """)
    
    # Investment terms showcase
    st.markdown("### 🎯 **Investment Opportunity Snapshot**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="market-size">
            <h4>Series A Funding</h4>
            <p><strong>$5M Investment Round</strong></p>
            <p>• Pre-money valuation: $25M</p>
            <p>• Equity offered: 20%</p>
            <p>• Projected IRR: 45-65%</p>
            <p>• Target exit: 5-7 years</p>
            <p>• Minimum check: $250K</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-story">
            <h4>Exit Strategy & Returns</h4>
            <p><strong>Multiple Exit Paths</strong></p>
            <p>• IPO potential: $500M+ revenue</p>
            <p>• Strategic buyers: Expedia, Booking.com</p>
            <p>• Comparable multiples: 8-15x revenue</p>
            <p>• Projected valuation: $200M-$500M</p>
            <p>• Expected MOIC: 8-20x</p>
        </div>
        """, unsafe_allow_html=True)

# Helper functions for data calculation
def calculate_package_price(duration, travelers, budget):
    """Calculate package price based on parameters"""
    base_price_per_day = {
        "Budget ($500-1000)": 150,
        "Moderate ($1000-2500)": 350,
        "Luxury ($2500+)": 800
    }
    
    daily_rate = base_price_per_day.get(budget, 350)
    return daily_rate * duration * travelers

def get_available_hotels(destination):
    """Get available hotels for specific destination with accurate naming"""
    
    # Destination-specific hotel database
    hotels_database = {
        'China': [
            {'id': 1, 'name': 'The Peninsula Beijing', 'location': 'Beijing, China', 'rating': 4.9, 'price': 320, 'type': 'Luxury', 'amenities': ['Spa', 'Fine Dining', 'Concierge', 'Fitness Center']},
            {'id': 2, 'name': 'Grand Mercure Beijing Central', 'location': 'Beijing, China', 'rating': 4.5, 'price': 180, 'type': 'Business', 'amenities': ['Business Center', 'Restaurant', 'WiFi', 'Gym']},
            {'id': 3, 'name': 'Beijing Traditional Courtyard Inn', 'location': 'Beijing, China', 'rating': 4.2, 'price': 85, 'type': 'Boutique', 'amenities': ['Traditional Architecture', 'Cultural Tours', 'WiFi', 'Tea House']},
            {'id': 4, 'name': 'Shangri-La Hotel Shanghai', 'location': 'Shanghai, China', 'rating': 4.8, 'price': 290, 'type': 'Luxury Resort', 'amenities': ['River Views', 'Multiple Restaurants', 'Spa', 'Shopping Mall Access']}
        ],
        'Paris, France': [
            {'id': 5, 'name': 'Hotel Ritz Paris', 'location': 'Paris, France', 'rating': 4.9, 'price': 450, 'type': 'Palace Hotel', 'amenities': ['Michelin Restaurants', 'Luxury Spa', 'Personal Shopping', 'Historic Elegance']},
            {'id': 6, 'name': 'Hotel Malte Opera Paris', 'location': 'Paris, France', 'rating': 4.4, 'price': 180, 'type': 'Historic Hotel', 'amenities': ['Near Opera House', 'French Restaurant', 'WiFi', 'Concierge']},
            {'id': 7, 'name': 'Hotel des Jeunes Paris', 'location': 'Paris, France', 'rating': 4.1, 'price': 75, 'type': 'Budget Boutique', 'amenities': ['Marais District', 'Continental Breakfast', 'Tourist Info', 'Metro Access']},
            {'id': 8, 'name': 'Hotel Plaza Athénée', 'location': 'Paris, France', 'rating': 4.8, 'price': 380, 'type': 'Luxury', 'amenities': ['Eiffel Tower Views', 'Haute Couture Shopping', 'Michelin Dining', 'Spa']}
        ],
        'Tokyo, Japan': [
            {'id': 9, 'name': 'The Ritz-Carlton Tokyo', 'location': 'Tokyo, Japan', 'rating': 4.9, 'price': 420, 'type': 'Luxury Skyscraper', 'amenities': ['City Views', 'Japanese Hospitality', 'Multiple Restaurants', 'Club Lounge']},
            {'id': 10, 'name': 'Shibuya Excel Hotel Tokyu', 'location': 'Tokyo, Japan', 'rating': 4.3, 'price': 160, 'type': 'Business Hotel', 'amenities': ['Shibuya Station Access', 'City Views', 'Restaurant', 'Business Center']},
            {'id': 11, 'name': 'K\'s House Tokyo Oasis', 'location': 'Tokyo, Japan', 'rating': 4.0, 'price': 45, 'type': 'Hostel', 'amenities': ['Budget Friendly', 'Social Atmosphere', 'Kitchen Access', 'Tourist Information']},
            {'id': 12, 'name': 'Imperial Hotel Tokyo', 'location': 'Tokyo, Japan', 'rating': 4.7, 'price': 280, 'type': 'Historic Luxury', 'amenities': ['Imperial Palace Views', 'Traditional Service', 'Multiple Dining', 'Spa']}
        ],
        'Dubai, UAE': [
            {'id': 13, 'name': 'Burj Al Arab Jumeirah', 'location': 'Dubai, UAE', 'rating': 4.9, 'price': 850, 'type': '7-Star Luxury', 'amenities': ['Iconic Sail Design', 'Private Beach', 'Butler Service', 'Helipad Access']},
            {'id': 14, 'name': 'Al Seef Heritage Hotel', 'location': 'Dubai, UAE', 'rating': 4.6, 'price': 200, 'type': 'Heritage Boutique', 'amenities': ['Traditional Architecture', 'Dubai Creek Views', 'Cultural Experiences', 'Souk Access']},
            {'id': 15, 'name': 'Rove Downtown Dubai', 'location': 'Dubai, UAE', 'rating': 4.4, 'price': 120, 'type': 'Modern Budget', 'amenities': ['Downtown Location', 'Burj Khalifa Views', 'Modern Design', 'Fitness Center']},
            {'id': 16, 'name': 'Atlantis The Palm', 'location': 'Dubai, UAE', 'rating': 4.7, 'price': 380, 'type': 'Resort', 'amenities': ['Aquaventure Waterpark', 'Lost Chambers Aquarium', 'Private Beach', 'Multiple Restaurants']}
        ],
        'Beirut, Lebanon': [
            {'id': 17, 'name': 'Four Seasons Hotel Beirut', 'location': 'Beirut, Lebanon', 'rating': 4.8, 'price': 280, 'type': 'Luxury', 'amenities': ['Mediterranean Views', 'Spa', 'Fine Dining', 'Pool']},
            {'id': 18, 'name': 'Le Gray Beirut', 'location': 'Beirut, Lebanon', 'rating': 4.6, 'price': 220, 'type': 'Boutique', 'amenities': ['Downtown Location', 'Rooftop Pool', 'Modern Design', 'Gourmet Restaurant']},
            {'id': 19, 'name': 'Saifi Suites', 'location': 'Beirut, Lebanon', 'rating': 4.2, 'price': 120, 'type': 'Apartment Hotel', 'amenities': ['Extended Stay', 'Kitchen Facilities', 'Historic District', 'WiFi']},
            {'id': 20, 'name': 'InterContinental Phoenicia Beirut', 'location': 'Beirut, Lebanon', 'rating': 4.5, 'price': 180, 'type': 'Business', 'amenities': ['Business Center', 'Multiple Restaurants', 'Pool', 'Marina Views']}
        ],
        'New York, USA': [
            {'id': 21, 'name': 'The Plaza Hotel', 'location': 'New York, USA', 'rating': 4.8, 'price': 450, 'type': 'Historic Luxury', 'amenities': ['Central Park Views', 'Luxury Shopping', 'Fine Dining', 'Spa']},
            {'id': 22, 'name': 'Pod Hotels Times Square', 'location': 'New York, USA', 'rating': 4.2, 'price': 140, 'type': 'Modern Budget', 'amenities': ['Times Square Location', 'Compact Design', 'Rooftop Bar', 'Tech Amenities']},
            {'id': 23, 'name': 'The High Line Hotel', 'location': 'New York, USA', 'rating': 4.5, 'price': 220, 'type': 'Boutique', 'amenities': ['Chelsea Location', 'Historic Building', 'Garden', 'Local Atmosphere']},
            {'id': 24, 'name': 'St. Regis New York', 'location': 'New York, USA', 'rating': 4.9, 'price': 520, 'type': 'Luxury', 'amenities': ['Butler Service', 'Fifth Avenue', 'King Cole Bar', 'Bespoke Service']}
        ],
        'London, England': [
            {'id': 25, 'name': 'The Savoy London', 'location': 'London, England', 'rating': 4.9, 'price': 420, 'type': 'Historic Luxury', 'amenities': ['Thames Views', 'Art Deco Design', 'Famous Bar', 'Royal Heritage']},
            {'id': 26, 'name': 'Premier Inn London', 'location': 'London, England', 'rating': 4.3, 'price': 95, 'type': 'Budget Chain', 'amenities': ['Consistent Quality', 'Central Locations', 'Family Friendly', 'Good Value']},
            {'id': 27, 'name': 'Zetter Townhouse Piccadilly', 'location': 'London, England', 'rating': 4.6, 'price': 180, 'type': 'Boutique', 'amenities': ['Victorian Charm', 'Cocktail Lounge', 'Central Location', 'Unique Design']},
            {'id': 28, 'name': 'Claridge\'s', 'location': 'London, England', 'rating': 4.8, 'price': 380, 'type': 'Art Deco Luxury', 'amenities': ['Mayfair Location', 'Afternoon Tea', 'Michelin Dining', 'Royal Connections']}
        ]
    }
    
    # Find hotels for specific destination
    destination_lower = destination.lower()
    
    # Check for exact matches or partial matches
    for country, hotels in hotels_database.items():
        if country.lower() in destination_lower or any(city.lower() in destination_lower for city in country.split(', ')):
            return hotels
    
    # Check if destination contains any city names
    city_mappings = {
        'beijing': 'China',
        'shanghai': 'China', 
        'paris': 'Paris, France',
        'tokyo': 'Tokyo, Japan',
        'dubai': 'Dubai, UAE',
        'beirut': 'Beirut, Lebanon',
        'new york': 'New York, USA',
        'london': 'London, England',
        'sydney': 'Australia',
        'rome': 'Italy',
        'barcelona': 'Spain'
    }
    
    for city, country in city_mappings.items():
        if city in destination_lower:
            if country in hotels_database:
                return hotels_database[country]
    
    # Default fallback - create generic hotels with destination name
    destination_name = destination.split(',')[0]  # Get first part of destination
    return [
        {'id': 999, 'name': f'{destination_name} Grand Hotel', 'location': destination, 'rating': 4.5, 'price': 180, 'type': 'City Hotel', 'amenities': ['WiFi', 'Restaurant', 'Pool', 'Fitness Center']},
        {'id': 998, 'name': f'{destination_name} Budget Inn', 'location': destination, 'rating': 4.0, 'price': 85, 'type': 'Budget Hotel', 'amenities': ['WiFi', 'Continental Breakfast', 'Central Location']},
        {'id': 997, 'name': f'{destination_name} Luxury Resort', 'location': destination, 'rating': 4.7, 'price': 320, 'type': 'Resort', 'amenities': ['Spa', 'Fine Dining', 'Concierge', 'Pool']},
        {'id': 996, 'name': f'{destination_name} Business Hotel', 'location': destination, 'rating': 4.3, 'price': 140, 'type': 'Business', 'amenities': ['Business Center', 'Meeting Rooms', 'WiFi', 'Restaurant']}
    ]

def get_available_restaurants(city):
    """Get available restaurants for city"""
    return [
        {'id': 1, 'name': 'Tawlet', 'cuisine': 'Lebanese Traditional', 'rating': 4.7, 'location': f'{city} Downtown', 'price_range': '$$', 'deposit': 15},
        {'id': 2, 'name': 'Em Sherif', 'cuisine': 'Lebanese Fine Dining', 'rating': 4.9, 'location': f'{city} Center', 'price_range': '$$$$', 'deposit': 25},
        {'id': 3, 'name': 'Urbanista', 'cuisine': 'International', 'rating': 4.6, 'location': f'{city} Business District', 'price_range': '$$$', 'deposit': 20},
        {'id': 4, 'name': 'Babel Bay', 'cuisine': 'Mediterranean', 'rating': 4.5, 'location': f'{city} Marina', 'price_range': '$$$', 'deposit': 18}
    ]

def get_activities_for_destination(destination):
    """Get activities for destination"""
    activities_map = {
        "Beirut, Lebanon": [
            "Visit National Museum of Beirut",
            "Explore Pigeon Rocks (Raouche)",
            "Walk through Beirut Souks",
            "Tour Mohammad Al-Amin Mosque",
            "Stroll along Corniche Beirut",
            "Day trip to Jeita Grotto",
            "Visit Byblos Castle",
            "Explore Baalbek Temples"
        ],
        "Dubai, UAE": [
            "Visit Burj Khalifa",
            "Explore Dubai Mall",
            "Desert Safari Adventure",
            "Visit Dubai Marina",
            "Tour Gold and Spice Souks",
            "Palm Jumeirah Excursion"
        ]
    }
    return activities_map.get(destination, ["City Tour", "Cultural Experience", "Local Cuisine Tasting"])
    """Get available hotels for destination"""
    # This would query the actual database
    # For demo, returning mock data
    return [
        {'id': 1, 'name': 'Four Seasons Hotel', 'location': destination, 'rating': 4.8, 'price': 350, 'type': 'Luxury'},
        {'id': 2, 'name': 'Grand Beirut Hotel', 'location': destination, 'rating': 4.5, 'price': 220, 'type': 'Business'},
        {'id': 3, 'name': 'City Center Inn', 'location': destination, 'rating': 4.2, 'price': 120, 'type': 'Budget'},
        {'id': 4, 'name': 'Seaside Resort', 'location': destination, 'rating': 4.6, 'price': 280, 'type': 'Resort'}
    ]

def get_available_restaurants(city):
    """Get available restaurants for city"""
    return [
        {'id': 1, 'name': 'Tawlet', 'cuisine': 'Lebanese Traditional', 'rating': 4.7, 'location': f'{city} Downtown', 'price_range': '$$', 'deposit': 15},
        {'id': 2, 'name': 'Em Sherif', 'cuisine': 'Lebanese Fine Dining', 'rating': 4.9, 'location': f'{city} Center', 'price_range': '$$$$', 'deposit': 25},
        {'id': 3, 'name': 'Urbanista', 'cuisine': 'International', 'rating': 4.6, 'location': f'{city} Business District', 'price_range': '$$$', 'deposit': 20},
        {'id': 4, 'name': 'Babel Bay', 'cuisine': 'Mediterranean', 'rating': 4.5, 'location': f'{city} Marina', 'price_range': '$$$', 'deposit': 18}
    ]

def get_activities_for_destination(destination):
    """Get activities for destination"""
    activities_map = {
        "Beirut, Lebanon": [
            "Visit National Museum of Beirut",
            "Explore Pigeon Rocks (Raouche)",
            "Walk through Beirut Souks",
            "Tour Mohammad Al-Amin Mosque",
            "Stroll along Corniche Beirut",
            "Day trip to Jeita Grotto",
            "Visit Byblos Castle",
            "Explore Baalbek Temples"
        ],
        "Dubai, UAE": [
            "Visit Burj Khalifa",
            "Explore Dubai Mall",
            "Desert Safari Adventure",
            "Visit Dubai Marina",
            "Tour Gold and Spice Souks",
            "Palm Jumeirah Excursion"
        ]
    }
    return activities_map.get(destination, ["City Tour", "Cultural Experience", "Local Cuisine Tasting"])

def calculate_package_price(duration, travelers, budget):
    """Calculate package price based on parameters"""
    base_price_per_day = {
        "Budget ($500-1000)": 150,
        "Moderate ($1000-2500)": 350,
        "Luxury ($2500+)": 800
    }
    
    daily_rate = base_price_per_day.get(budget, 350)
    return daily_rate * duration * travelers

# Main application navigation
def main():
    """Main application with enhanced navigation"""
    
    # Initialize current page
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "main"
    
    # Enhanced sidebar navigation
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white; margin-bottom: 1rem;">
        <h2>🌍 AI Travel</h2>
        <p>Enhanced Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation menu
    pages = {
        "🏠 Home": "main",
        "🏨 Hotel Booking": "hotel_booking",
        "🍽️ Restaurant Booking": "restaurant_booking",
        "📦 Travel Packages": "package_creation",
        "📋 Booking History": "booking_history",
        "📊 Analytics": "analytics",
        "⚙️ Settings": "settings"
    }
    
    selected_page = st.sidebar.radio("🧭 **Navigation**", list(pages.keys()))
    st.session_state.current_page = pages[selected_page]
    
    # User info sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 👤 **User Profile**")
    st.sidebar.markdown("**Status:** 🟢 Online")
    st.sidebar.markdown("**Member:** ⭐ Premium")
    st.sidebar.markdown(f"**Bookings:** {len(st.session_state.booking_history)}")
    
    # Quick stats
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 **Quick Stats**")
    
    # Get dynamic counts
    destinations_count = len(get_all_destinations())
    
    st.sidebar.metric("Global Destinations", str(destinations_count), "🌍 Live Data")
    st.sidebar.metric("Hotels Available", "65", "↗️ 5")
    st.sidebar.metric("Restaurants", "20+", "↗️ 17 Added")
    st.sidebar.metric("Avg Savings", "$347", "↗️ 12%")
    
    # Support section
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 💬 **Support & Investment**")
    if st.sidebar.button("💰 Investor Relations", use_container_width=True):
        st.sidebar.success("📧 investors@aitravel.com")
        st.sidebar.info("📱 +1 (555) INVEST-1")
    if st.sidebar.button("📞 Live Chat", use_container_width=True):
        st.sidebar.success("💬 Chat initiated!")
    if st.sidebar.button("📧 General Support", use_container_width=True):
        st.sidebar.info("📧 support@aitravel.com")
    
    # Investment opportunity callout
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, #ff7675 0%, #e17055 100%); 
                padding: 1rem; border-radius: 10px; color: white; text-align: center;">
        <h4>🔥 Investment Opportunity</h4>
        <p><strong>Series A: $5M</strong></p>
        <p>45-65% IRR Potential</p>
        <p>Contact us today!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Page routing
    if st.session_state.current_page == "main":
        main_page()
    elif st.session_state.current_page == "hotel_booking":
        hotel_booking_page()
    elif st.session_state.current_page == "restaurant_booking":
        restaurant_booking_page()
    elif st.session_state.current_page == "package_creation":
        package_creation_page()
    elif st.session_state.current_page == "booking_history":
        booking_history_page()
    elif st.session_state.current_page == "analytics":
        analytics_dashboard()
    elif st.session_state.current_page == "settings":
        st.title("⚙️ Settings")
        st.info("🔧 Settings page coming soon!")

if __name__ == "__main__":
    main()
