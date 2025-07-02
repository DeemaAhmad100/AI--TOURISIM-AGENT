#!/usr/bin/env python3
"""
🌍 AI Travel Platform - Main Application
Complete integrated travel booking and planning system
"""

import streamlit as st
import sys
import os
from pathlib import Path

# Add the current directory to the Python path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

from enhanced_travel_platform import (
    SmartTravelAssistant, UserProfile, TravelPackage,
    PriceTracker, CalendarIntegration, GroupBookingManager,
    FlightOption, HotelOption, RestaurantOption, CarRentalOption
)
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

def main():
    """Main application entry point"""
    
    # Page configuration
    st.set_page_config(
        page_title="🌍 AI Travel Platform",
        page_icon="✈️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for beautiful UI
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
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .price-tag {
        background: #28a745;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    
    .savings-tag {
        background: #dc3545;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.9em;
        margin-left: 1rem;
    }
    
    .feature-box {
        background: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #dee2e6;
        margin: 0.5rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #007bff 0%, #0056b3 100%);
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🌍 AI Travel Platform</h1>
        <p>Your Intelligent Travel Companion - Complete Booking & Planning Solution</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'travel_assistant' not in st.session_state:
        st.session_state.travel_assistant = SmartTravelAssistant()
    if 'price_tracker' not in st.session_state:
        st.session_state.price_tracker = PriceTracker()
    if 'calendar_integration' not in st.session_state:
        st.session_state.calendar_integration = CalendarIntegration()
    if 'group_booking' not in st.session_state:
        st.session_state.group_booking = GroupBookingManager()
    if 'user_profile' not in st.session_state:
        st.session_state.user_profile = None
    if 'current_package' not in st.session_state:
        st.session_state.current_package = None
    
    # Sidebar for navigation
    with st.sidebar:
        st.title("🚀 Navigation")
        page = st.selectbox("Choose a feature:", [
            "🏠 Home",
            "👤 User Profile",
            "✈️ Create Travel Package",
            "👥 Group Booking",
            "📊 Price Tracking",
            "📅 Calendar Integration",
            "📈 Analytics Dashboard",
            "🤖 AI Chat Assistant"
        ])
    
    # Main content based on selected page
    if page == "🏠 Home":
        show_home_page()
    elif page == "👤 User Profile":
        show_user_profile_page()
    elif page == "✈️ Create Travel Package":
        show_travel_package_page()
    elif page == "👥 Group Booking":
        show_group_booking_page()
    elif page == "📊 Price Tracking":
        show_price_tracking_page()
    elif page == "📅 Calendar Integration":
        show_calendar_page()
    elif page == "📈 Analytics Dashboard":
        show_analytics_page()
    elif page == "🤖 AI Chat Assistant":
        show_ai_chat_page()

def show_home_page():
    """Display the home page with platform overview"""
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-box">
            <h3>✈️ Smart Itinerary Planning</h3>
            <p>AI-powered personalized travel packages with flights, hotels, restaurants, and activities all in one.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-box">
            <h3>👥 Group Booking</h3>
            <p>Coordinate group travel with automatic discounts and shared planning features.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-box">
            <h3>📊 Price Tracking</h3>
            <p>Monitor price changes and get alerts when your dream trip becomes more affordable.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🌎 Destinations", "195+", "Global Coverage")
    with col2:
        st.metric("💰 Average Savings", "$450", "+15%")
    with col3:
        st.metric("⭐ Customer Rating", "4.8/5", "99% Satisfaction")
    with col4:
        st.metric("🚀 Bookings", "10,000+", "+25% this month")
    
    # Recent features
    st.subheader("🔥 What's New")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **🤖 AI-Powered Recommendations**
        Our enhanced AI now provides even more personalized suggestions based on your travel history and preferences.
        """)
    
    with col2:
        st.success("""
        **📱 Mobile Calendar Sync**
        Automatically sync your travel plans with Google Calendar, Outlook, and Apple Calendar.
        """)

def show_user_profile_page():
    """Display and edit user profile"""
    
    st.header("👤 User Profile")
    
    # Profile form
    with st.form("user_profile_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            user_id = st.text_input("User ID", value="user_001")
            age = st.number_input("Age", min_value=18, max_value=100, value=30)
            travel_style = st.selectbox("Travel Style", [
                "luxury", "budget", "adventure", "cultural", "family", "business"
            ])
            budget_range = st.selectbox("Budget Range", [
                "$0-500", "$500-1500", "$1500-3000", "$3000-5000", "$5000+"
            ])
        
        with col2:
            interests = st.multiselect("Interests", [
                "History", "Culture", "Food", "Adventure", "Nature", "Art", 
                "Museums", "Nightlife", "Shopping", "Photography", "Sports"
            ])
            
            dietary_restrictions = st.multiselect("Dietary Restrictions", [
                "Vegetarian", "Vegan", "Gluten-free", "Halal", "Kosher", "None"
            ])
            
            preferred_airlines = st.multiselect("Preferred Airlines", [
                "Emirates", "American Airlines", "Delta", "British Airways", 
                "Lufthansa", "Singapore Airlines", "Any"
            ])
            
            language_preferences = st.multiselect("Language Preferences", [
                "English", "Spanish", "French", "German", "Chinese", "Arabic", "Other"
            ])
        
        accessibility_needs = st.multiselect("Accessibility Needs", [
            "Wheelchair accessible", "Visual assistance", "Hearing assistance", "None"
        ])
        
        calendar_integration = st.checkbox("Enable calendar integration", value=True)
        
        if st.form_submit_button("💾 Save Profile"):
            st.session_state.user_profile = UserProfile(
                user_id=user_id,
                age=age,
                interests=interests,
                travel_style=travel_style,
                accessibility_needs=accessibility_needs,
                budget_range=budget_range,
                preferred_airlines=preferred_airlines,
                dietary_restrictions=dietary_restrictions,
                language_preferences=language_preferences,
                previous_destinations=[],
                calendar_integration=calendar_integration
            )
            st.success("✅ Profile saved successfully!")
    
    # Display current profile
    if st.session_state.user_profile:
        st.subheader("📋 Current Profile")
        
        profile_data = {
            "Field": ["User ID", "Age", "Travel Style", "Budget Range", "Interests", "Dietary Restrictions"],
            "Value": [
                st.session_state.user_profile.user_id,
                st.session_state.user_profile.age,
                st.session_state.user_profile.travel_style,
                st.session_state.user_profile.budget_range,
                ", ".join(st.session_state.user_profile.interests),
                ", ".join(st.session_state.user_profile.dietary_restrictions)
            ]
        }
        
        df = pd.DataFrame(profile_data)
        st.table(df)

def show_travel_package_page():
    """Create and display travel packages"""
    
    st.header("✈️ Create Your Perfect Travel Package")
    
    if not st.session_state.user_profile:
        st.warning("⚠️ Please create your user profile first to get personalized recommendations.")
        return
    
    # Travel package form
    with st.form("travel_package_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            destination = st.text_input("Destination", placeholder="e.g., Paris, France")
            start_date = st.date_input("Start Date", value=datetime.now() + timedelta(days=30))
        
        with col2:
            duration = st.number_input("Duration (days)", min_value=1, max_value=30, value=5)
            end_date = st.date_input("End Date", value=start_date + timedelta(days=duration))
        
        with col3:
            group_size = st.number_input("Group Size", min_value=1, max_value=10, value=1)
            package_type = st.selectbox("Package Type", [
                "Complete Package", "Flights Only", "Hotels Only", "Custom"
            ])
        
        special_requests = st.text_area("Special Requests", 
                                      placeholder="Any special requirements or preferences...")
        
        if st.form_submit_button("🔍 Generate Travel Package"):
            if destination:
                with st.spinner("🤖 Creating your personalized travel package..."):
                    try:
                        # Create travel package
                        travel_dates = (start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
                        
                        package = st.session_state.travel_assistant.create_personalized_itinerary(
                            destination=destination,
                            user_profile=st.session_state.user_profile,
                            travel_dates=travel_dates,
                            duration=duration
                        )
                        
                        st.session_state.current_package = package
                        st.success("✅ Travel package created successfully!")
                        
                    except Exception as e:
                        st.error(f"❌ Error creating package: {str(e)}")
            else:
                st.error("Please enter a destination")
    
    # Display current package
    if st.session_state.current_package:
        display_travel_package(st.session_state.current_package)

def display_travel_package(package: TravelPackage):
    """Display a travel package in a beautiful format"""
    
    st.markdown(f"""
    <div class="package-card">
        <h2>🌍 {package.destination} - {package.duration} Days</h2>
        <div class="price-tag">${package.total_price:.2f}</div>
        <div class="savings-tag">Save ${package.savings:.2f}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Package details in tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["✈️ Flight", "🏨 Hotel", "🍽️ Restaurants", "🚗 Car Rental", "🎯 Activities"])
    
    with tab1:
        st.subheader(f"✈️ {package.flight.airline}")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Departure:** {package.flight.departure_time}")
            st.write(f"**Duration:** {package.flight.duration}")
            st.write(f"**Stops:** {package.flight.stops}")
        with col2:
            st.write(f"**Arrival:** {package.flight.arrival_time}")
            st.write(f"**Price:** ${package.flight.price:.2f}")
            st.write(f"**Rating:** {'⭐' * int(package.flight.rating)}")
        
        st.write("**Amenities:** " + ", ".join(package.flight.amenities))
        
        if st.button("🎫 Book Flight"):
            st.success("Flight booking initiated! You would be redirected to the airline's booking page.")
    
    with tab2:
        st.subheader(f"🏨 {package.hotel.name}")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Location:** {package.hotel.location}")
            st.write(f"**Price per night:** ${package.hotel.price_per_night:.2f}")
            st.write(f"**Distance to center:** {package.hotel.distance_to_center:.1f} km")
        with col2:
            st.write(f"**Rating:** {'⭐' * int(package.hotel.rating)}")
            st.write(f"**Total hotel cost:** ${package.hotel.price_per_night * package.duration:.2f}")
        
        st.write("**Amenities:** " + ", ".join(package.hotel.amenities))
        
        if package.hotel.customer_reviews:
            st.write("**Recent Reviews:**")
            for review in package.hotel.customer_reviews[:3]:
                st.write(f"• {review}")
        
        if st.button("🏨 Book Hotel"):
            st.success("Hotel booking initiated! You would be redirected to the booking platform.")
    
    with tab3:
        st.subheader("🍽️ Restaurant Recommendations")
        for i, restaurant in enumerate(package.restaurants):
            with st.expander(f"{restaurant.name} - {restaurant.cuisine_type}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Location:** {restaurant.location}")
                    st.write(f"**Price Range:** {restaurant.price_range}")
                    st.write(f"**Phone:** {restaurant.phone}")
                with col2:
                    st.write(f"**Rating:** {'⭐' * int(restaurant.rating)}")
                    st.write("**Specialties:** " + ", ".join(restaurant.specialties))
                
                if restaurant.customer_reviews:
                    st.write("**Reviews:** " + restaurant.customer_reviews[0])
                
                if st.button(f"📞 Reserve at {restaurant.name}", key=f"restaurant_{i}"):
                    st.success(f"Reservation request sent to {restaurant.name}!")
    
    with tab4:
        if package.car_rental:
            st.subheader(f"🚗 {package.car_rental.company} - {package.car_rental.car_model}")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Price per day:** ${package.car_rental.price_per_day:.2f}")
                st.write(f"**Pickup location:** {package.car_rental.pickup_location}")
                st.write(f"**Insurance included:** {'Yes' if package.car_rental.insurance_included else 'No'}")
            with col2:
                st.write(f"**Total rental cost:** ${package.car_rental.price_per_day * package.duration:.2f}")
                st.write("**Features:** " + ", ".join(package.car_rental.features))
            
            if st.button("🚗 Book Car Rental"):
                st.success("Car rental booking initiated!")
        else:
            st.info("No car rental included in this package. You can add one separately.")
    
    with tab5:
        st.subheader("🎯 Recommended Activities")
        for activity in package.activities:
            st.write(f"• {activity}")
        
        st.write(f"**Travel Guide PDF:** {package.travel_guide_pdf}")
        
        if st.button("📱 Add to Calendar"):
            calendar_events = st.session_state.calendar_integration.add_travel_to_calendar(
                st.session_state.user_profile.user_id,
                package,
                "2024-01-01"  # This should be the actual start date
            )
            st.success(f"✅ Added {len(calendar_events)} events to your calendar!")
    
    # Action buttons
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("💾 Save Package"):
            st.success("Package saved to your favorites!")
    
    with col2:
        if st.button("📊 Track Prices"):
            # Add to price tracking
            st.session_state.price_tracker.track_price(
                "package", f"{package.destination}_{package.duration}",
                package.total_price, "user@example.com"
            )
            st.success("Price tracking enabled!")
    
    with col3:
        if st.button("👥 Share with Group"):
            st.info("Group sharing feature coming soon!")
    
    with col4:
        if st.button("🔄 Modify Package"):
            st.info("Package modification feature available in the form above!")

def show_group_booking_page():
    """Group booking management"""
    
    st.header("👥 Group Booking Management")
    
    # Create new group
    st.subheader("➕ Create New Group Booking")
    
    with st.form("create_group_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            group_destination = st.text_input("Destination")
            start_date = st.date_input("Start Date")
        
        with col2:
            end_date = st.date_input("End Date")
            max_participants = st.number_input("Max Participants", min_value=2, max_value=20, value=5)
        
        if st.form_submit_button("🚀 Create Group"):
            if group_destination:
                group_id = st.session_state.group_booking.create_group_booking(
                    st.session_state.user_profile.user_id if st.session_state.user_profile else "user_001",
                    group_destination,
                    (start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")),
                    max_participants
                )
                st.success(f"✅ Group created! Group ID: {group_id}")
    
    # Join existing group
    st.subheader("🤝 Join Existing Group")
    
    group_id_to_join = st.text_input("Group ID")
    if st.button("Join Group"):
        if group_id_to_join:
            success = st.session_state.group_booking.join_group_booking(
                group_id_to_join,
                st.session_state.user_profile.user_id if st.session_state.user_profile else "user_001"
            )
            if success:
                st.success("✅ Successfully joined the group!")
            else:
                st.error("❌ Could not join group. Check the ID or group capacity.")
    
    # Display existing groups
    st.subheader("📋 Your Groups")
    
    if st.session_state.group_booking.group_bookings:
        for group_id, group_data in st.session_state.group_booking.group_bookings.items():
            with st.expander(f"🏖️ {group_data['destination']} - {group_id}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Destination:** {group_data['destination']}")
                    st.write(f"**Dates:** {group_data['travel_dates'][0]} to {group_data['travel_dates'][1]}")
                    st.write(f"**Status:** {group_data['status']}")
                
                with col2:
                    st.write(f"**Participants:** {len(group_data['participants'])}/{group_data['max_participants']}")
                    st.write(f"**Leader:** {group_data['leader_id']}")
                    st.write(f"**Created:** {group_data['created_at'][:10]}")
                
                # Show participants
                st.write("**Participants:**")
                for participant in group_data['participants']:
                    st.write(f"• {participant}")
                
                # Group discount calculation
                if st.session_state.current_package:
                    group_package = st.session_state.group_booking.calculate_group_discounts(
                        group_id, st.session_state.current_package
                    )
                    
                    discount_amount = st.session_state.current_package.total_price - group_package.total_price
                    if discount_amount > 0:
                        st.success(f"💰 Group discount: ${discount_amount:.2f} per person!")
    else:
        st.info("No groups created yet. Create one above!")

def show_price_tracking_page():
    """Price tracking dashboard"""
    
    st.header("📊 Price Tracking Dashboard")
    
    # Add new item to track
    st.subheader("➕ Add Price Tracking")
    
    with st.form("price_tracking_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            item_type = st.selectbox("Item Type", ["flight", "hotel", "package", "car_rental"])
            item_id = st.text_input("Item ID", placeholder="e.g., flight_LAX_CDG")
        
        with col2:
            current_price = st.number_input("Current Price", min_value=0.0, value=500.0)
            target_price = st.number_input("Target Price (Alert)", min_value=0.0, value=450.0)
        
        with col3:
            user_email = st.text_input("Email for Alerts", value="user@example.com")
        
        if st.form_submit_button("🔔 Start Tracking"):
            st.session_state.price_tracker.track_price(
                item_type, item_id, current_price, user_email, target_price
            )
            st.success(f"✅ Now tracking {item_type} {item_id}")
    
    # Display tracked items
    st.subheader("📋 Currently Tracking")
    
    if st.session_state.price_tracker.tracked_items:
        for item_key, item_data in st.session_state.price_tracker.tracked_items.items():
            with st.expander(f"📊 {item_data['type']} - {item_data['id']}"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Current Price", f"${item_data['current_price']:.2f}")
                    if item_data['target_price']:
                        st.metric("Target Price", f"${item_data['target_price']:.2f}")
                
                with col2:
                    st.write(f"**Email:** {item_data['user_email']}")
                    st.write(f"**Alerts Sent:** {item_data['alerts_sent']}")
                
                with col3:
                    if st.button(f"🔍 Check Now", key=f"check_{item_key}"):
                        st.session_state.price_tracker.check_price_changes()
                        st.success("Price check completed!")
                
                # Price history chart
                if len(item_data['price_history']) > 1:
                    df = pd.DataFrame(item_data['price_history'])
                    df['date'] = pd.to_datetime(df['date'])
                    
                    fig = px.line(df, x='date', y='price', 
                                title=f"Price History - {item_data['id']}")
                    st.plotly_chart(fig, use_container_width=True)
        
        # Bulk actions
        if st.button("🔄 Check All Prices"):
            st.session_state.price_tracker.check_price_changes()
            st.success("All prices checked!")
    else:
        st.info("No items being tracked yet. Add one above!")

def show_calendar_page():
    """Calendar integration page"""
    
    st.header("📅 Calendar Integration")
    
    if not st.session_state.user_profile:
        st.warning("⚠️ Please create your user profile first.")
        return
    
    # Display user's travel calendar
    events = st.session_state.calendar_integration.get_user_calendar(
        st.session_state.user_profile.user_id
    )
    
    if events:
        st.subheader("📋 Your Travel Calendar")
        
        # Create calendar view
        calendar_data = []
        for event in events:
            calendar_data.append({
                "Event": event["title"],
                "Start": event["start"][:10],
                "End": event["end"][:10],
                "Type": event["type"],
                "Details": event["details"]
            })
        
        df = pd.DataFrame(calendar_data)
        st.dataframe(df, use_container_width=True)
        
        # Calendar visualization
        st.subheader("📊 Calendar Overview")
        
        # Count events by type
        event_counts = df['Type'].value_counts()
        fig = px.pie(values=event_counts.values, names=event_counts.index, 
                    title="Events by Type")
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.info("📅 No travel events in your calendar yet. Create a travel package to add events!")
    
    # Availability checker
    st.subheader("🔍 Check Availability")
    
    with st.form("availability_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            check_start = st.date_input("Start Date")
        
        with col2:
            check_end = st.date_input("End Date")
        
        if st.form_submit_button("Check Availability"):
            is_available = st.session_state.calendar_integration.check_availability(
                st.session_state.user_profile.user_id,
                check_start.strftime("%Y-%m-%d"),
                check_end.strftime("%Y-%m-%d")
            )
            
            if is_available:
                st.success("✅ You're available for these dates!")
            else:
                st.warning("⚠️ You have conflicts during these dates.")

def show_analytics_page():
    """Analytics dashboard"""
    
    st.header("📈 Travel Analytics Dashboard")
    
    # Sample analytics data
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Bookings", "47", "+5 this month")
    
    with col2:
        st.metric("Total Savings", "$2,340", "+$420 this month")
    
    with col3:
        st.metric("Favorite Destination", "Paris", "3 visits")
    
    with col4:
        st.metric("Average Trip Cost", "$1,250", "-$150 vs last year")
    
    # Charts
    st.subheader("📊 Travel Trends")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Sample spending data
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        spending = [800, 1200, 900, 1500, 1100, 1300]
        
        fig = px.bar(x=months, y=spending, title="Monthly Travel Spending")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Sample destination data
        destinations = ['Paris', 'Tokyo', 'New York', 'London', 'Rome']
        visits = [3, 2, 4, 2, 1]
        
        fig = px.pie(values=visits, names=destinations, 
                    title="Most Visited Destinations")
        st.plotly_chart(fig, use_container_width=True)
    
    # Travel history table
    st.subheader("🗓️ Recent Travel History")
    
    travel_history = pd.DataFrame({
        'Destination': ['Paris, France', 'Tokyo, Japan', 'New York, USA', 'London, UK'],
        'Dates': ['2024-01-15 to 2024-01-22', '2023-11-10 to 2023-11-17', 
                 '2023-09-05 to 2023-09-12', '2023-06-20 to 2023-06-27'],
        'Cost': ['$1,450', '$2,100', '$1,200', '$1,600'],
        'Rating': ['⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐']
    })
    
    st.dataframe(travel_history, use_container_width=True)

def show_ai_chat_page():
    """AI chat assistant page"""
    
    st.header("🤖 AI Travel Chat Assistant")
    
    # Chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm your AI Travel Assistant. How can I help you plan your next adventure? 🌍✈️"}
        ]
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about travel..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_ai_response(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

def generate_ai_response(prompt: str) -> str:
    """Generate AI response for chat"""
    
    # This is a simplified response system
    # In a real implementation, you'd use the OpenAI API or your LLM
    
    prompt_lower = prompt.lower()
    
    if "destination" in prompt_lower or "where" in prompt_lower:
        return """🌍 I can help you find the perfect destination! Here are some popular options:

**For Culture & History:** Paris, Rome, Athens, Kyoto
**For Adventure:** New Zealand, Costa Rica, Nepal, Iceland  
**For Beaches:** Maldives, Bali, Caribbean Islands, Hawaii
**For Food:** Tokyo, Bangkok, Istanbul, Barcelona

What type of experience are you looking for? I can create a personalized itinerary for you!"""
    
    elif "budget" in prompt_lower or "cost" in prompt_lower:
        return """💰 Great question! Here are some budget-friendly tips:

**Budget Travel (Under $1000):**
- Southeast Asia: Thailand, Vietnam, Cambodia
- Eastern Europe: Prague, Budapest, Krakow
- Central America: Guatemala, Nicaragua

**Mid-range ($1000-3000):**
- Mediterranean: Greece, Portugal, Spain
- South America: Peru, Argentina, Chile

**Luxury ($3000+):**
- Japan, Switzerland, Norway, Maldives

Would you like me to create a package within your specific budget range?"""
    
    elif "group" in prompt_lower:
        return """👥 Group travel is amazing! Here's what I can help with:

✅ **Group Booking Management**
✅ **Automatic Group Discounts** (up to 15% off)
✅ **Shared Itinerary Planning**
✅ **Split Payment Options**
✅ **Group Activity Coordination**

How many people are in your group? I can create a custom group package with special discounts!"""
    
    elif "flight" in prompt_lower or "hotel" in prompt_lower:
        return """✈️🏨 I can help you find the best deals!

**Flight Tips:**
- Book 2-3 months in advance for best prices
- Tuesday/Wednesday departures are usually cheaper
- Consider nearby airports for better deals

**Hotel Tips:**
- Compare prices across multiple platforms
- Check for package deals with flights
- Look for hotels with free breakfast/WiFi

Would you like me to search for specific flights or hotels for your destination?"""
    
    else:
        return """🤖 I'm here to help with all your travel needs! I can assist with:

🎯 **Personalized Itinerary Planning**
✈️ **Flight & Hotel Bookings** 
🍽️ **Restaurant Recommendations**
👥 **Group Travel Coordination**
📊 **Price Tracking & Alerts**
📅 **Calendar Integration**
💰 **Budget Planning**

What specific aspect of travel planning can I help you with today?"""

if __name__ == "__main__":
    main()
