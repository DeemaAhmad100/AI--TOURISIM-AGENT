"""
🌍 Enhanced AI Travel Platform - Streamlit UI
Beautiful and intuitive user interface for the travel platform
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
from enhanced_travel_platform import (
    SmartTravelAssistant, UserProfile, TravelPackage,
    PriceTracker, CalendarIntegration, GroupBookingManager
)

# Page configuration
st.set_page_config(
    page_title="AI Travel Platform",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
    padding: 2rem;
    border-radius: 10px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}

.package-card {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 10px;
    border-left: 4px solid #007bff;
    margin: 1rem 0;
}

.price-tag {
    background: #28a745;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-weight: bold;
}

.savings-tag {
    background: #fd7e14;
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 15px;
    font-size: 0.9rem;
}

.feature-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = None
if 'current_package' not in st.session_state:
    st.session_state.current_package = None
if 'booking_history' not in st.session_state:
    st.session_state.booking_history = []

# Initialize components
@st.cache_resource
def init_components():
    return {
        'assistant': SmartTravelAssistant(),
        'price_tracker': PriceTracker(),
        'calendar_integration': CalendarIntegration(),
        'group_booking': GroupBookingManager()
    }

components = init_components()

def main_page():
    """Main landing page"""
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🌍 ✈️ Enhanced AI Travel Platform 🏨 🍽️</h1>
        <h3>Your Personal AI Travel Assistant for Complete Travel Solutions</h3>
        <p>Flight + Hotel + Restaurant + Car Rental + Travel Guide - All in One Package!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features overview
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="text-align: center;">
            <div class="feature-icon">🤖</div>
            <h4>AI Personal Assistant</h4>
            <p>Smart recommendations based on your preferences</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <div class="feature-icon">📦</div>
            <h4>Complete Packages</h4>
            <p>Flight + Hotel + Car + Guide in one booking</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center;">
            <div class="feature-icon">💰</div>
            <h4>Price Tracking</h4>
            <p>Get notified when prices drop</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="text-align: center;">
            <div class="feature-icon">👥</div>
            <h4>Group Booking</h4>
            <p>Smart group discounts and coordination</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick stats
    st.markdown("### 📊 Platform Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Happy Travelers", "12,543", "↗️ 23%")
    
    with col2:
        st.metric("Destinations", "150+", "↗️ 8%")
    
    with col3:
        st.metric("Average Savings", "$347", "↗️ 15%")
    
    with col4:
        st.metric("Group Bookings", "2,891", "↗️ 31%")

def create_travel_package():
    """Travel package creation interface"""
    
    st.title("🗺️ Create Your Complete Travel Package")
    
    # User profile setup
    with st.expander("👤 User Profile & Preferences", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.slider("Age", 18, 80, 30)
            travel_style = st.selectbox("Travel Style", 
                ["budget", "moderate", "luxury", "adventure", "cultural", "family"])
            budget_range = st.selectbox("Budget Range", 
                ["budget", "moderate", "luxury"])
        
        with col2:
            interests = st.multiselect("Interests", 
                ["culture", "food", "nature", "adventure", "history", "art", "nightlife", "shopping"])
            dietary_restrictions = st.multiselect("Dietary Restrictions",
                ["vegetarian", "vegan", "halal", "kosher", "gluten-free", "none"])
            accessibility_needs = st.multiselect("Accessibility Needs",
                ["wheelchair_accessible", "hearing_impaired", "visually_impaired", "none"])
    
    # Trip details
    st.markdown("### 🎯 Trip Details")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        destination = st.text_input("🌍 Destination", placeholder="e.g., Beirut, Lebanon")
    
    with col2:
        start_date = st.date_input("📅 Start Date", datetime.now() + timedelta(days=30))
    
    with col3:
        end_date = st.date_input("📅 End Date", datetime.now() + timedelta(days=37))
    
    # Calculate duration
    if start_date and end_date:
        duration = (end_date - start_date).days
        st.info(f"Trip Duration: {duration} days")
    
    # Advanced options
    with st.expander("⚙️ Advanced Options"):
        col1, col2 = st.columns(2)
        
        with col1:
            preferred_airlines = st.multiselect("Preferred Airlines",
                ["Emirates", "Qatar Airways", "Turkish Airlines", "Lufthansa", "British Airways"])
            room_type = st.selectbox("Hotel Room Type",
                ["Standard", "Deluxe", "Suite", "Family Room"])
        
        with col2:
            car_rental = st.checkbox("Include Car Rental")
            group_booking = st.checkbox("Group Booking")
            if group_booking:
                group_size = st.number_input("Group Size", 2, 50, 4)
    
    # Create package button
    if st.button("🚀 Create My Travel Package", type="primary"):
        if destination and start_date and end_date:
            
            # Create user profile
            user_profile = UserProfile(
                user_id="user_001",
                age=age,
                interests=interests,
                travel_style=travel_style,
                accessibility_needs=accessibility_needs,
                budget_range=budget_range,
                preferred_airlines=preferred_airlines,
                dietary_restrictions=dietary_restrictions,
                language_preferences=["English"],
                previous_destinations=[]
            )
            
            # Show loading
            with st.spinner("🤖 AI is creating your personalized travel package..."):
                # Create package (mock implementation)
                package = create_mock_package(destination, duration, user_profile)
                st.session_state.current_package = package
            
            st.success("✅ Your travel package is ready!")
            st.rerun()
        else:
            st.error("Please fill in all required fields")
    
    # Display package if created
    if st.session_state.current_package:
        display_travel_package(st.session_state.current_package)

def display_travel_package(package):
    """Display the created travel package"""
    
    st.markdown("---")
    st.markdown("# 🎉 Your Personalized Travel Package")
    
    # Package summary
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="package-card">
            <h4>📍 {package['destination']}</h4>
            <p><strong>Duration:</strong> {package['duration']} days</p>
            <p><strong>Travel Dates:</strong> {package['dates']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="package-card">
            <h4>💰 Pricing</h4>
            <div class="price-tag">${package['total_price']:,.2f}</div>
            <br><br>
            <div class="savings-tag">Save ${package['savings']:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="package-card">
            <h4>⭐ Package Rating</h4>
            <p><strong>Overall:</strong> ⭐ {package['rating']}/5</p>
            <p><strong>Value:</strong> 💰 {package['value_rating']}/5</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Detailed breakdown
    tabs = st.tabs(["✈️ Flight", "🏨 Hotel", "🍽️ Restaurants", "🚗 Car Rental", "🎯 Activities", "📄 Guide"])
    
    with tabs[0]:  # Flight
        st.markdown("### ✈️ Flight Details")
        flight = package['flight']
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            **Airline:** {flight['airline']}  
            **Departure:** {flight['departure']}  
            **Arrival:** {flight['arrival']}  
            **Duration:** {flight['duration']}  
            """)
        
        with col2:
            st.markdown(f"""
            **Price:** ${flight['price']:,.2f}  
            **Rating:** ⭐ {flight['rating']}/5  
            **Stops:** {flight['stops']}  
            **Amenities:** {', '.join(flight['amenities'])}  
            """)
        
        st.markdown(f"[🔗 Book Flight]({flight['booking_url']})")
    
    with tabs[1]:  # Hotel
        st.markdown("### 🏨 Hotel Details")
        hotel = package['hotel']
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            **Name:** {hotel['name']}  
            **Location:** {hotel['location']}  
            **Price/night:** ${hotel['price_per_night']:,.2f}  
            **Rating:** ⭐ {hotel['rating']}/5  
            """)
        
        with col2:
            st.markdown("**Customer Reviews:**")
            for review in hotel['reviews'][:3]:
                st.markdown(f"💬 \"{review}\"")
        
        st.markdown(f"**Amenities:** {', '.join(hotel['amenities'])}")
        st.markdown(f"[🔗 Book Hotel]({hotel['booking_url']})")
    
    with tabs[2]:  # Restaurants
        st.markdown("### 🍽️ Recommended Restaurants")
        
        for restaurant in package['restaurants']:
            with st.expander(f"{restaurant['name']} ({restaurant['cuisine']})"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"""
                    **Cuisine:** {restaurant['cuisine']}  
                    **Rating:** ⭐ {restaurant['rating']}/5  
                    **Price Range:** {restaurant['price_range']}  
                    **Phone:** {restaurant['phone']}  
                    """)
                
                with col2:
                    st.markdown("**Specialties:**")
                    for specialty in restaurant['specialties']:
                        st.markdown(f"• {specialty}")
                
                if restaurant['booking_url']:
                    st.markdown(f"[🔗 Make Reservation]({restaurant['booking_url']})")
    
    with tabs[3]:  # Car Rental
        if package.get('car_rental'):
            st.markdown("### 🚗 Car Rental")
            car = package['car_rental']
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                **Company:** {car['company']}  
                **Model:** {car['model']}  
                **Price/day:** ${car['price_per_day']:,.2f}  
                **Pickup:** {car['pickup_location']}  
                """)
            
            with col2:
                st.markdown(f"""
                **Features:** {', '.join(car['features'])}  
                **Insurance:** {'✅ Included' if car['insurance'] else '❌ Not included'}  
                """)
            
            st.markdown(f"[🔗 Book Car]({car['booking_url']})")
        else:
            st.info("No car rental selected for this package")
    
    with tabs[4]:  # Activities
        st.markdown("### 🎯 Recommended Activities")
        
        for activity in package['activities']:
            st.markdown(f"• {activity}")
    
    with tabs[5]:  # Guide
        st.markdown("### 📄 Travel Guide")
        st.markdown("📖 A comprehensive PDF travel guide will be generated with:")
        
        guide_contents = [
            "🗺️ Detailed destination information",
            "🏛️ Historical and cultural insights",
            "🍜 Local cuisine recommendations",
            "💰 Budget tips and money-saving strategies",
            "🚌 Transportation guides",
            "📱 Essential apps and tools",
            "🆘 Emergency contacts and health information",
            "🎭 Cultural etiquette and customs",
            "📸 Instagram-worthy photo spots",
            "🎪 Seasonal events and festivals"
        ]
        
        for content in guide_contents:
            st.markdown(content)
    
    # Booking section
    st.markdown("---")
    st.markdown("## 💳 Complete Your Booking")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📦 Book Complete Package", type="primary"):
            show_booking_form(package)
    
    with col2:
        if st.button("📊 Track Prices"):
            st.success("✅ Price tracking enabled! You'll receive notifications when prices drop.")
    
    with col3:
        if st.button("👥 Create Group Booking"):
            show_group_booking_form(package)

def show_booking_form(package):
    """Show booking form"""
    
    st.markdown("### 💳 Booking Information")
    
    with st.form("booking_form"):
        st.markdown("**Personal Information**")
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name*")
            email = st.text_input("Email*")
            phone = st.text_input("Phone*")
        
        with col2:
            last_name = st.text_input("Last Name*")
            passport_number = st.text_input("Passport Number*")
            nationality = st.text_input("Nationality*")
        
        st.markdown("**Payment Information**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            card_number = st.text_input("Card Number*", type="password")
        
        with col2:
            expiry = st.text_input("MM/YY*")
        
        with col3:
            cvv = st.text_input("CVV*", type="password")
        
        cardholder_name = st.text_input("Cardholder Name*")
        
        # Terms and conditions
        terms_accepted = st.checkbox("I accept the terms and conditions*")
        
        submitted = st.form_submit_button("💳 Complete Booking")
        
        if submitted:
            if all([first_name, last_name, email, phone, passport_number, 
                   card_number, expiry, cvv, cardholder_name, terms_accepted]):
                
                # Process booking
                with st.spinner("Processing your booking..."):
                    booking_id = process_booking(package, {
                        'first_name': first_name,
                        'last_name': last_name,
                        'email': email,
                        'phone': phone,
                        'passport_number': passport_number
                    })
                
                st.success(f"✅ Booking confirmed! Booking ID: {booking_id}")
                st.balloons()
                
                # Show confirmation details
                st.markdown("### 📧 Confirmation Details")
                st.markdown(f"""
                **Booking ID:** {booking_id}  
                **Total Amount:** ${package['total_price']:,.2f}  
                **Email:** Confirmation sent to {email}  
                **Travel Guide:** PDF will be sent within 24 hours  
                """)
                
            else:
                st.error("Please fill in all required fields")

def show_group_booking_form(package):
    """Show group booking form"""
    
    st.markdown("### 👥 Group Booking")
    
    with st.form("group_booking_form"):
        group_name = st.text_input("Group Name*")
        leader_email = st.text_input("Group Leader Email*")
        expected_size = st.number_input("Expected Group Size", 2, 50, 5)
        
        st.markdown("**Group Discount Preview:**")
        
        if expected_size >= 10:
            discount = 15
        elif expected_size >= 5:
            discount = 10
        elif expected_size >= 3:
            discount = 5
        else:
            discount = 0
        
        if discount > 0:
            discounted_price = package['total_price'] * (1 - discount/100)
            st.success(f"🎉 {discount}% Group Discount! New price: ${discounted_price:,.2f} per person")
        else:
            st.info("Minimum 3 people required for group discount")
        
        submitted = st.form_submit_button("👥 Create Group Booking")
        
        if submitted and group_name and leader_email:
            group_id = f"GRP_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            st.success(f"✅ Group booking created! Group ID: {group_id}")
            st.markdown(f"📧 Invitation link will be sent to {leader_email}")

def price_tracking():
    """Price tracking interface"""
    
    st.title("📊 Price Tracking & Notifications")
    
    # Current tracked items
    st.markdown("### 📈 Your Tracked Items")
    
    # Mock data
    tracked_items = [
        {"destination": "Beirut, Lebanon", "type": "Flight", "current_price": 850, "lowest_price": 780, "trend": "↗️"},
        {"destination": "Dubai, UAE", "type": "Hotel", "current_price": 220, "lowest_price": 195, "trend": "↘️"},
        {"destination": "Paris, France", "type": "Package", "current_price": 1450, "lowest_price": 1280, "trend": "↗️"}
    ]
    
    df = pd.DataFrame(tracked_items)
    st.dataframe(df, use_container_width=True)
    
    # Price trend chart
    st.markdown("### 📈 Price Trends")
    
    # Generate mock price history
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq='D')
    price_data = {
        'Date': dates,
        'Beirut Flight': [850 + (i % 10 - 5) * 20 for i in range(len(dates))],
        'Dubai Hotel': [220 + (i % 8 - 4) * 15 for i in range(len(dates))],
        'Paris Package': [1450 + (i % 12 - 6) * 50 for i in range(len(dates))]
    }
    
    price_df = pd.DataFrame(price_data)
    
    fig = px.line(price_df, x='Date', y=['Beirut Flight', 'Dubai Hotel', 'Paris Package'],
                  title="Price Trends (Last 30 Days)")
    st.plotly_chart(fig, use_container_width=True)
    
    # Add new tracking
    st.markdown("### ➕ Add New Price Tracking")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        new_destination = st.text_input("Destination")
    
    with col2:
        tracking_type = st.selectbox("Type", ["Flight", "Hotel", "Package", "Car Rental"])
    
    with col3:
        email_notifications = st.checkbox("Email Notifications", value=True)
    
    if st.button("📊 Start Tracking"):
        if new_destination:
            st.success(f"✅ Now tracking {tracking_type} prices for {new_destination}")
        else:
            st.error("Please enter a destination")

def analytics_dashboard():
    """Travel analytics and insights"""
    
    st.title("📈 Travel Analytics & Insights")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Bookings", "1,234", "↗️ 12%")
    
    with col2:
        st.metric("Average Savings", "$347", "↗️ 8%")
    
    with col3:
        st.metric("Customer Satisfaction", "4.8/5", "↗️ 0.2")
    
    with col4:
        st.metric("Repeat Customers", "78%", "↗️ 5%")
    
    # Popular destinations
    st.markdown("### 🌍 Popular Destinations")
    
    destinations_data = {
        'Destination': ['Dubai', 'Paris', 'Tokyo', 'New York', 'London', 'Beirut', 'Istanbul', 'Barcelona'],
        'Bookings': [245, 198, 167, 134, 123, 98, 87, 76],
        'Avg Rating': [4.7, 4.8, 4.9, 4.6, 4.5, 4.8, 4.7, 4.6]
    }
    
    fig = px.bar(destinations_data, x='Destination', y='Bookings', 
                 title="Most Popular Destinations (This Month)")
    st.plotly_chart(fig, use_container_width=True)
    
    # Booking trends
    st.markdown("### 📅 Booking Trends")
    
    # Generate mock booking data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    bookings = [145, 167, 189, 223, 256, 278]
    
    fig = px.line(x=months, y=bookings, title="Monthly Booking Trends")
    fig.update_traces(mode='lines+markers')
    st.plotly_chart(fig, use_container_width=True)

def create_mock_package(destination, duration, user_profile):
    """Create a mock travel package for demonstration"""
    
    return {
        'destination': destination,
        'duration': duration,
        'dates': 'July 15-22, 2025',
        'total_price': 2450.00,
        'savings': 367.50,
        'rating': 4.8,
        'value_rating': 4.7,
        'flight': {
            'airline': 'Emirates',
            'departure': 'July 15, 2025 14:30',
            'arrival': 'July 15, 2025 23:45',
            'duration': '9h 15m',
            'price': 850.00,
            'rating': 4.7,
            'stops': 1,
            'amenities': ['Wi-Fi', 'Entertainment', 'Meals'],
            'booking_url': 'https://emirates.com/booking'
        },
        'hotel': {
            'name': 'Four Seasons Hotel Beirut',
            'location': 'Beirut Central District',
            'price_per_night': 280.00,
            'rating': 4.8,
            'reviews': [
                'Excellent service and beautiful sea views',
                'Perfect location in downtown Beirut',
                'Outstanding breakfast buffet'
            ],
            'amenities': ['Pool', 'Spa', 'Gym', 'Sea View', 'Concierge'],
            'booking_url': 'https://booking.com/fourseasons'
        },
        'restaurants': [
            {
                'name': 'Tawlet',
                'cuisine': 'Lebanese Traditional',
                'rating': 4.7,
                'price_range': '$$',
                'specialties': ['Meze', 'Kibbeh', 'Traditional Stews'],
                'phone': '+961-1-448129',
                'booking_url': 'https://tawlet.com/reservations'
            },
            {
                'name': 'Em Sherif',
                'cuisine': 'Lebanese Fine Dining',
                'rating': 4.9,
                'price_range': '$$$$',
                'specialties': ['Gourmet Meze', 'Lamb Ouzi', 'Traditional Sweets'],
                'phone': '+961-1-200043',
                'booking_url': 'https://emsherif.com/booking'
            }
        ],
        'car_rental': {
            'company': 'Budget',
            'model': 'Toyota Corolla',
            'price_per_day': 35.00,
            'features': ['GPS', 'AC', 'Automatic'],
            'pickup_location': 'Beirut Airport',
            'insurance': True,
            'booking_url': 'https://budget.com/beirut'
        },
        'activities': [
            'Visit the National Museum of Beirut',
            'Explore the ancient Roman Baths',
            'Walk through the historic Gemmayzeh district',
            'Take a Lebanese cooking class',
            'Day trip to Jeita Grotto',
            'Hiking in the Chouf Mountains'
        ]
    }

def process_booking(package, customer_info):
    """Process the booking and return booking ID"""
    
    # Generate booking ID
    booking_id = f"TB{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    # Save to session state (in real app, save to database)
    booking_record = {
        'booking_id': booking_id,
        'customer': customer_info,
        'package': package,
        'booking_date': datetime.now().isoformat(),
        'status': 'confirmed'
    }
    
    st.session_state.booking_history.append(booking_record)
    
    return booking_id

# Main app navigation
def main():
    """Main application"""
    
    # Sidebar navigation
    st.sidebar.title("🧭 Navigation")
    
    pages = {
        "🏠 Home": main_page,
        "🗺️ Create Package": create_travel_package,
        "📊 Price Tracking": price_tracking,
        "📈 Analytics": analytics_dashboard,
        "👤 Profile": lambda: st.write("Profile page coming soon!"),
        "👥 Group Booking": lambda: st.write("Group booking page coming soon!"),
        "🤖 AI Assistant": lambda: st.write("AI assistant chat coming soon!"),
        "📱 Mobile App": lambda: st.write("Mobile app features coming soon!")
    }
    
    selected_page = st.sidebar.radio("Select Page", list(pages.keys()))
    
    # User info in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 👤 User Info")
    st.sidebar.markdown("**Status:** 🟢 Online")
    st.sidebar.markdown("**Bookings:** 3")
    st.sidebar.markdown("**Savings:** $1,247")
    
    # Quick actions
    st.sidebar.markdown("---")
    st.sidebar.markdown("### ⚡ Quick Actions")
    if st.sidebar.button("📞 Support Chat"):
        st.sidebar.success("Chat initiated!")
    if st.sidebar.button("📧 Contact Us"):
        st.sidebar.info("Email: support@aitravel.com")
    
    # Run selected page
    pages[selected_page]()

if __name__ == "__main__":
    main()
