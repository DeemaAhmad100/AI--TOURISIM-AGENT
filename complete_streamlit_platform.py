import streamlit as st
import asyncio
import json
import time
from datetime import datetime
from typing import Dict, List
import sys
from pathlib import Path

# Add current directory to path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

# Import both systems
from live_crewai_collaboration import LiveCrewAIOrchestrator, UserProfile
from final_booking_system import FinalBookingSystem

# Configure Streamlit page
st.set_page_config(
    page_title="🌍 Complete AI Travel Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .agent-message {
        padding: 10px;
        margin: 5px 0;
        border-radius: 10px;
        border-left: 4px solid #4CAF50;
        background-color: #f0f8ff;
    }
    .user-message {
        padding: 10px;
        margin: 5px 0;
        border-radius: 10px;
        border-left: 4px solid #2196F3;
        background-color: #e3f2fd;
    }
    .agent-communication {
        padding: 8px;
        margin: 3px 0;
        border-radius: 8px;
        font-size: 0.9em;
        background-color: #fff3e0;
        border: 1px solid #ff9800;
    }
    .profile-update {
        background-color: #e8f5e8;
        padding: 10px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .package-card {
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        background-color: #f9f9f9;
    }
    .hotel-info {
        background-color: #e3f2fd;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .restaurant-info {
        background-color: #f3e5f5;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .attraction-info {
        background-color: #e8f5e8;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .pricing-info {
        background-color: #fff3e0;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        border-left: 4px solid #ff9800;
    }
    .feature-list {
        background-color: #f0f8ff;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .main-header {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 30px;
    }
    .package-header {
        color: #1976d2;
        border-bottom: 2px solid #1976d2;
        padding-bottom: 10px;
    }
    .tab-header {
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

class CompleteTravelPlatform:
    """Complete Travel Platform with all features"""
    
    def __init__(self):
        if 'orchestrator' not in st.session_state:
            st.session_state.orchestrator = LiveCrewAIOrchestrator()
        if 'booking_system' not in st.session_state:
            st.session_state.booking_system = FinalBookingSystem()
        if 'conversation_history' not in st.session_state:
            st.session_state.conversation_history = []
        if 'agent_communications' not in st.session_state:
            st.session_state.agent_communications = []
        if 'current_profile' not in st.session_state:
            st.session_state.current_profile = UserProfile()
        if 'packages' not in st.session_state:
            st.session_state.packages = None
        if 'selected_package' not in st.session_state:
            st.session_state.selected_package = None
        if 'selected_mode' not in st.session_state:
            st.session_state.selected_mode = "Quick Packages"

    def display_agent_communication(self, comm: Dict):
        """Display agent-to-agent communication"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        sender = comm.get("sender", "Unknown")
        message = comm.get("message", "")
        
        # Color coding for different agents
        colors = {
            "Profile Analyzer": "#1f77b4",
            "Travel Researcher": "#ff7f0e", 
            "Local Culture Expert": "#e377c2",
            "Itinerary Planner": "#2ca02c",
            "Booking Coordinator": "#d62728",
            "User": "#9467bd",
            "System": "#8c564b"
        }
        
        color = colors.get(sender, "#7f7f7f")
        
        st.markdown(f"""
        <div class="agent-communication" style="border-left-color: {color};">
            <strong>[{timestamp}] 🤖 {sender}:</strong> {message}
        </div>
        """, unsafe_allow_html=True)
        
        if "data" in comm and comm["data"]:
            with st.expander(f"📊 Data shared by {sender}"):
                st.json(comm["data"])

    def display_package_card(self, package, index):
        """Display a single package in a card format"""
        hotel = package["hotel"]
        pricing = package["pricing"]
        
        with st.container():
            st.markdown(f'<div class="package-card">', unsafe_allow_html=True)
            
            # Package header
            st.markdown(f'<h3 class="package-header">📦 Package {index}: {package["name"]}</h3>', unsafe_allow_html=True)
            
            # Hotel information
            st.markdown(f'<div class="hotel-info">', unsafe_allow_html=True)
            st.markdown(f"**🏨 Hotel:** {hotel['name']}")
            st.markdown(f"**⭐ Rating:** {hotel['rating']}/5.0")
            st.markdown(f"**💰 Price per night:** ${hotel['price']}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Features
            st.markdown(f'<div class="feature-list">', unsafe_allow_html=True)
            st.markdown("**🎯 Features:**")
            for feature in package["features"]:
                st.markdown(f"• {feature}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Create columns for restaurants and attractions
            col1, col2 = st.columns(2)
            
            with col1:
                # Restaurant information
                st.markdown(f'<div class="restaurant-info">', unsafe_allow_html=True)
                st.markdown("**🍽️ Nearest Restaurants:**")
                for restaurant in package["restaurants"]:
                    st.markdown(f"• **{restaurant['name']}** ({restaurant['cuisine']})")
                    st.markdown(f"  📍 {restaurant['distance']}km away")
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                # Attraction information
                st.markdown(f'<div class="attraction-info">', unsafe_allow_html=True)
                st.markdown("**🎭 Best Attractions:**")
                for attraction in package["attractions"]:
                    price_str = f"${attraction['price']}" if attraction['price'] > 0 else "Free"
                    st.markdown(f"• **{attraction['name']}** - {price_str}")
                st.markdown('</div>', unsafe_allow_html=True)
            
            # Pricing information
            st.markdown(f'<div class="pricing-info">', unsafe_allow_html=True)
            st.markdown("**💰 Pricing:**")
            col_price1, col_price2, col_price3 = st.columns(3)
            
            with col_price1:
                st.metric("Total Cost", f"${pricing['total']:,}")
            with col_price2:
                st.metric("Savings", f"${pricing['savings']:,}")
            with col_price3:
                st.metric("Hotel Cost", f"${pricing['hotel']:,}")
            
            st.markdown("**📊 Breakdown:**")
            st.markdown(f"• Hotel: ${pricing['hotel']:,}")
            st.markdown(f"• Activities: ${pricing['activities']:,}")
            st.markdown(f"• Cultural: ${pricing['cultural']:,}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Book button
            if st.button(f"📋 Select Package {index}", key=f"select_{index}", use_container_width=True):
                st.session_state.selected_package = package
                st.success(f"✅ Selected {package['name']}!")
                st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)

    def display_booking_form(self):
        """Display booking form for selected package"""
        if st.session_state.selected_package:
            package = st.session_state.selected_package
            
            st.markdown("## 📋 Booking Form")
            st.markdown(f"**Selected Package:** {package['name']}")
            
            with st.form("booking_form"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("### 👤 Personal Information")
                    name = st.text_input("Full Name", placeholder="Enter your full name")
                    email = st.text_input("Email", placeholder="your.email@example.com")
                    phone = st.text_input("Phone Number", placeholder="+1234567890")
                    
                with col2:
                    st.markdown("### 🗓️ Travel Details")
                    check_in = st.date_input("Check-in Date")
                    check_out = st.date_input("Check-out Date")
                    guests = st.number_input("Number of Guests", min_value=1, max_value=10, value=2)
                
                st.markdown("### 💳 Payment Information")
                payment_method = st.selectbox("Payment Method", ["Credit Card", "PayPal", "Bank Transfer"])
                
                special_requests = st.text_area("Special Requests", placeholder="Any special requests or dietary requirements...")
                
                # Submit button
                submitted = st.form_submit_button("🚀 Book This Package", use_container_width=True)
                
                if submitted:
                    if name and email and phone:
                        # Simulate booking process
                        with st.spinner("Processing your booking..."):
                            time.sleep(2)
                        
                        st.success("🎉 Booking Confirmed!")
                        st.balloons()
                        
                        # Display booking confirmation
                        st.markdown("### 📧 Booking Confirmation")
                        booking_id = f"BK{datetime.now().strftime('%Y%m%d%H%M%S')}"
                        st.markdown(f"**Booking ID:** {booking_id}")
                        st.markdown(f"**Package:** {package['name']}")
                        st.markdown(f"**Hotel:** {package['hotel']['name']}")
                        st.markdown(f"**Total Cost:** ${package['pricing']['total']:,}")
                        st.markdown(f"**Savings:** ${package['pricing']['savings']:,}")
                        st.markdown("**Status:** ✅ Confirmed")
                    else:
                        st.error("Please fill in all required fields!")

    def quick_packages_mode(self):
        """Quick packages generation mode"""
        st.markdown('<div class="tab-header">🚀 Quick Intelligent Packages</div>', unsafe_allow_html=True)
        st.markdown("Generate 4 intelligent travel packages for Beirut with detailed information.")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            if st.button("🎯 Generate 4 Packages", use_container_width=True, type="primary"):
                with st.spinner("🧠 Generating intelligent packages..."):
                    time.sleep(2)
                    st.session_state.packages = st.session_state.booking_system.generate_4_packages()
                st.success("✅ Packages generated!")
                st.rerun()
        
        with col2:
            if st.session_state.packages:
                if st.button("💾 Export JSON", use_container_width=True):
                    json_data = json.dumps(st.session_state.packages, indent=2)
                    st.download_button(
                        label="📁 Download JSON",
                        data=json_data,
                        file_name=f"travel_packages_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                        mime="application/json"
                    )
        
        if st.session_state.packages is None:
            # Welcome screen
            st.markdown("### 🌟 Welcome to the Quick Packages Generator")
            st.markdown("Click **Generate 4 Packages** to create personalized travel packages for Beirut.")
            
            # Display sample features
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("#### 🏨 Hotel Names")
                st.markdown("• Detailed hotel information")
                st.markdown("• Ratings and prices")
                st.markdown("• Location details")
            
            with col2:
                st.markdown("#### 🍽️ Nearest Restaurants")
                st.markdown("• Restaurant names and cuisines")
                st.markdown("• Distance from hotels")
                st.markdown("• Curated recommendations")
            
            with col3:
                st.markdown("#### 🎭 Attractions with Prices")
                st.markdown("• Attraction names and types")
                st.markdown("• Exact pricing information")
                st.markdown("• Free and paid options")
        
        else:
            # Display packages
            st.markdown("### 🎁 Your Intelligent Travel Packages")
            
            # Create tabs for different views
            tab1, tab2 = st.tabs(["📦 Package Details", "📋 Booking"])
            
            with tab1:
                st.markdown("#### Choose from 4 carefully curated packages:")
                
                # Display each package
                for i, package in enumerate(st.session_state.packages, 1):
                    self.display_package_card(package, i)
                    st.markdown("---")
            
            with tab2:
                self.display_booking_form()

    def advanced_ai_mode(self):
        """Advanced AI agents mode"""
        st.markdown('<div class="tab-header">🤖 Advanced AI Agent Collaboration</div>', unsafe_allow_html=True)
        st.markdown("**🤖 Powered by 5 Specialized AI Agents with 20+ Advanced Tools & Capabilities**")
        
        orchestrator = st.session_state.orchestrator
        
        # Quick stats
        stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
        with stats_col1:
            st.metric("🤖 AI Agents", "5", "Specialized")
        with stats_col2:
            st.metric("🛠️ Total Tools", "20+", "Advanced")
        with stats_col3:
            st.metric("🌍 Destinations", "18+", "Global")
        with stats_col4:
            st.metric("📦 Package Types", "3", "Per Request")
        
        # Agent overview section
        with st.expander("🎯 Meet Your AI Agent Team", expanded=False):
            st.markdown("""
            ### 🔍 **Profile Analyzer Agent**
            **Purpose:** Intelligent natural language processing and user preference extraction
            **Tools & Capabilities:**
            - 🛠️ Multi-pattern budget extraction (handles $2000, 2000 USD, etc.)
            - 🛠️ Destination database matching with 18+ global cities
            - 🛠️ Travel style classification (cultural, adventure, luxury, relaxation)
            - 🛠️ Group dynamics analysis
            
            ### 📊 **Travel Researcher Agent**
            **Purpose:** Comprehensive destination research and feasibility analysis
            **Tools & Capabilities:**
            - 🛠️ Live destination database with cultural insights
            - 🛠️ Hotel filtering algorithms by price, rating, and style
            - 🛠️ Budget feasibility calculator
            - 🛠️ Seasonal travel optimization
            
            ### 🎭 **Local Culture Expert Agent**
            **Purpose:** Deep cultural intelligence and authentic local experiences
            **Tools & Capabilities:**
            - 🛠️ Cultural database for major destinations
            - 🛠️ Local customs and etiquette guide generator
            - 🛠️ Hidden gems discovery engine
            - 🛠️ Language and communication toolkit
            
            ### 📅 **Itinerary Planner Agent**
            **Purpose:** Dynamic itinerary creation with cultural integration
            **Tools & Capabilities:**
            - 🛠️ AI-powered schedule optimization
            - 🛠️ Cultural experience integration algorithm
            - 🛠️ Budget allocation across activities
            - 🛠️ Transportation route planning
            
            ### 💳 **Booking Coordinator Agent**
            **Purpose:** Complete booking orchestration and package generation
            **Tools & Capabilities:**
            - 🛠️ Multi-package generation engine
            - 🛠️ Dynamic pricing calculator
            - 🛠️ Booking simulation system
            - 🛠️ Upgrade and savings optimizer
            """)
        
        # Main content area
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.header("💬 Live Conversation")
            
            # Chat interface
            if st.button("🚀 Start Live Planning", type="primary", use_container_width=True):
                if not st.session_state.current_profile.destination:
                    st.error("Please enter a destination in the sidebar first!")
                else:
                    # Process through agents
                    with st.spinner("🤖 AI Agents are collaborating..."):
                        profile = st.session_state.current_profile
                        
                        # Simulate agent processing
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        # Step 1: Profile Analysis
                        status_text.text("🔍 Profile Analyzer working...")
                        progress_bar.progress(25)
                        
                        analysis = orchestrator.profile_analyzer.analyze_user_input(
                            f"Plan a {profile.duration}-day {profile.travel_style} trip to {profile.destination} with ${profile.budget} budget",
                            profile
                        )
                        time.sleep(1)
                        
                        # Step 2: Research
                        status_text.text("📊 Travel Researcher gathering data...")
                        progress_bar.progress(40)
                        
                        research_results = orchestrator.travel_researcher.research_destination(profile)
                        time.sleep(1)
                        
                        # Step 3: Cultural Analysis
                        status_text.text("🎭 Local Culture Expert analyzing cultural aspects...")
                        progress_bar.progress(60)
                        
                        cultural_insights = orchestrator.culture_expert.provide_cultural_insights(profile, research_results)
                        time.sleep(1)
                        
                        # Step 4: Itinerary Planning
                        status_text.text("📅 Itinerary Planner creating schedule with cultural integration...")
                        progress_bar.progress(80)
                        
                        itinerary = orchestrator.itinerary_planner.create_itinerary(profile, research_results, cultural_insights)
                        time.sleep(1)
                        
                        # Step 5: Booking Coordination
                        status_text.text("💳 Booking Coordinator checking prices...")
                        progress_bar.progress(100)
                        
                        booking_summary = orchestrator.booking_coordinator.coordinate_booking(
                            profile, itinerary, research_results.get("suitable_hotels", []), cultural_insights
                        )
                        
                        status_text.text("✅ Complete!")
                        
                        # Store results
                        st.session_state.last_itinerary = itinerary
                        st.session_state.last_booking = booking_summary
                        st.session_state.last_research = research_results
                        st.session_state.last_cultural_insights = cultural_insights
                    
                    st.success("🎉 Your personalized travel plan is ready!")
            
            # Display results if available
            if hasattr(st.session_state, 'last_itinerary'):
                st.header("🎯 Your AI-Generated Travel Plan")
                
                itinerary = st.session_state.last_itinerary
                booking = st.session_state.last_booking
                research = st.session_state.last_research
                
                # Overview
                col_a, col_b, col_c = st.columns(3)
                
                with col_a:
                    st.metric("Total Cost", f"${booking.get('total_cost', 0):.0f}", 
                             f"Budget: ${st.session_state.current_profile.budget}")
                
                with col_b:
                    st.metric("Duration", f"{itinerary.get('total_days', 0)} days")
                
                with col_c:
                    remaining = booking.get('budget_remaining', 0)
                    st.metric("Budget Status", 
                             "Under Budget" if remaining >= 0 else "Over Budget",
                             f"${abs(remaining):.0f}")
                
                # Hotel recommendation
                if booking.get('selected_hotel'):
                    hotel = booking['selected_hotel']
                    st.subheader("🏨 Recommended Hotel")
                    
                    hotel_col1, hotel_col2, hotel_col3 = st.columns(3)
                    with hotel_col1:
                        st.write(f"**{hotel['name']}**")
                        st.write(f"⭐ {hotel['rating']}/5.0")
                    with hotel_col2:
                        st.write(f"**${hotel['price']}/night**")
                        st.write(f"Style: {hotel['style'].title()}")
                    with hotel_col3:
                        total_hotel = hotel['price'] * st.session_state.current_profile.duration
                        st.write(f"**Total: ${total_hotel}**")
                        st.write(f"For {st.session_state.current_profile.duration} nights")
                
                # Travel Packages Display
                if booking.get('travel_packages'):
                    st.subheader("🎁 Generated Travel Packages")
                    
                    package_tabs = st.tabs([f"📦 {pkg['name']}" for pkg in booking['travel_packages']])
                    
                    for i, (tab, package) in enumerate(zip(package_tabs, booking['travel_packages'])):
                        with tab:
                            pkg_col1, pkg_col2 = st.columns([2, 1])
                            
                            with pkg_col1:
                                st.write(f"**🏨 Hotel:** {package['hotel']['name']}")
                                st.write(f"**⭐ Rating:** {package['hotel']['rating']}/5.0")
                                st.write(f"**🎯 Package Features:**")
                                for feature in package['features']:
                                    st.write(f"• {feature}")
                            
                            with pkg_col2:
                                st.metric("Total Cost", f"${package['total_cost']:.0f}")
                                if package['savings'] > 0:
                                    st.metric("Savings", f"${package['savings']:.0f}", "Under Budget")
                                else:
                                    st.metric("Over Budget", f"${abs(package['savings']):.0f}", "Needs Adjustment")
                                
                                st.write(f"**Cost Breakdown:**")
                                st.write(f"Hotel: ${package['hotel']['price'] * st.session_state.current_profile.duration:.0f}")
                                st.write(f"Activities: ${package['activities_cost']:.0f}")
                                st.write(f"Cultural: ${package['cultural_cost']:.0f}")
                
                # Daily itinerary
                st.subheader("📅 Daily Itinerary")
                
                for day_plan in itinerary.get('daily_plans', []):
                    with st.expander(f"Day {day_plan['day']}: {day_plan['theme']}"):
                        col_morning, col_afternoon, col_evening = st.columns(3)
                        
                        with col_morning:
                            st.write("🌅 **Morning**")
                            st.write(day_plan['morning'])
                        
                        with col_afternoon:
                            st.write("🌞 **Afternoon**") 
                            st.write(day_plan['afternoon'])
                        
                        with col_evening:
                            st.write("🌙 **Evening**")
                            st.write(day_plan['evening'])
                        
                        st.write(f"💰 Estimated daily cost: ${day_plan['estimated_cost']:.0f}")
                
                # Cultural insights section
                if hasattr(st.session_state, 'last_cultural_insights'):
                    cultural = st.session_state.last_cultural_insights
                    st.subheader("🎭 Cultural Insights & Local Expertise")
                    
                    if cultural.get('cultural_highlights'):
                        with st.expander("✨ Cultural Highlights"):
                            for highlight in cultural['cultural_highlights']:
                                st.write(f"• {highlight}")
                    
                    if cultural.get('local_customs'):
                        with st.expander("🤝 Local Customs & Etiquette"):
                            for custom in cultural['local_customs']:
                                st.write(f"• {custom}")
                    
                    if cultural.get('language_tips'):
                        with st.expander("🗣️ Language Tips"):
                            for tip in cultural['language_tips']:
                                st.write(f"• {tip}")
                    
                    if cultural.get('hidden_gems'):
                        with st.expander("💎 Hidden Gems"):
                            for gem in cultural['hidden_gems']:
                                st.write(f"• {gem}")
        
        with col2:
            st.header("🤖 Agent Communications")
            st.caption("Watch agents collaborate in real-time")
            
            # Display recent agent communications
            if orchestrator.comm_hub.messages:
                for comm in orchestrator.comm_hub.messages[-10:]:  # Show last 10 messages
                    self.display_agent_communication(comm)
            else:
                st.info("No agent communications yet. Start planning to see agents collaborate!")
            
            # Agent status
            st.subheader("👥 Agent Team Status")
            st.markdown("**5 Specialized AI Agents | 20+ Advanced Tools**")
            
            agents = [
                ("Profile Analyzer", "🔍", "4 Tools Active"),
                ("Travel Researcher", "📊", "4 Tools Active"),
                ("Local Culture Expert", "🎭", "4 Tools Active"),
                ("Itinerary Planner", "📅", "4 Tools Active"),
                ("Booking Coordinator", "💳", "4 Tools Active")
            ]
            
            for agent_name, emoji, tools in agents:
                with st.expander(f"{emoji} {agent_name} - {tools}"):
                    st.write("**Status:** ✅ Ready and Operational")
        
        # Natural language input
        st.header("💭 Tell me about your dream trip!")
        
        user_input = st.text_area("Describe your ideal vacation...", 
                                 placeholder="Example: I want a romantic 5-day trip to Paris with my partner. We love art and fine dining. Our budget is $3000.")
        
        if st.button("🚀 Process with AI Agents", use_container_width=True):
            if user_input.strip():
                # Process through orchestrator
                with st.spinner("🤖 Agents analyzing your request..."):
                    orchestrator.process_user_input(user_input)
                    
                    # Get results from each agent
                    profile = orchestrator.current_profile
                    
                    if profile.destination and profile.duration and profile.budget:
                        research_results = orchestrator.travel_researcher.research_destination(profile)
                        cultural_insights = orchestrator.culture_expert.provide_cultural_insights(profile, research_results)
                        itinerary = orchestrator.itinerary_planner.create_itinerary(profile, research_results, cultural_insights)
                        booking_summary = orchestrator.booking_coordinator.coordinate_booking(
                            profile, itinerary, research_results.get("suitable_hotels", []), cultural_insights
                        )
                        
                        # Store results in session state
                        st.session_state.last_itinerary = itinerary
                        st.session_state.last_booking = booking_summary
                        st.session_state.last_research = research_results
                        st.session_state.last_cultural_insights = cultural_insights
                        st.session_state.current_profile = profile
                
                st.success("✅ Request processed! Check your travel plan below.")
                st.rerun()
            else:
                st.error("Please enter your travel preferences!")

def main():
    """Main application function"""
    platform = CompleteTravelPlatform()
    
    # Header
    st.markdown('<h1 class="main-header">🌍 Complete AI Travel Platform</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2em; color: #666;">The Ultimate Travel Planning Experience with Quick Packages & Advanced AI Agents</p>', unsafe_allow_html=True)
    
    # Mode selector
    mode_col1, mode_col2 = st.columns(2)
    
    with mode_col1:
        if st.button("🚀 Quick Packages", use_container_width=True, 
                    type="primary" if st.session_state.selected_mode == "Quick Packages" else "secondary"):
            st.session_state.selected_mode = "Quick Packages"
            st.rerun()
    
    with mode_col2:
        if st.button("🤖 Advanced AI Agents", use_container_width=True,
                    type="primary" if st.session_state.selected_mode == "Advanced AI Agents" else "secondary"):
            st.session_state.selected_mode = "Advanced AI Agents"
            st.rerun()
    
    # Sidebar
    with st.sidebar:
        st.header("👤 Your Travel Profile")
        
        # Live profile building
        with st.form("profile_form"):
            name = st.text_input("Name", value=st.session_state.current_profile.name)
            destination = st.text_input("Destination", value=st.session_state.current_profile.destination, 
                                      placeholder="e.g., Tokyo, Paris, Bali")
            
            col1, col2 = st.columns(2)
            with col1:
                duration = st.number_input("Days", min_value=1, max_value=30, 
                                         value=st.session_state.current_profile.duration or 7)
            with col2:
                budget = st.number_input("Budget ($)", min_value=100, max_value=50000,
                                       value=int(st.session_state.current_profile.budget) or 2000, step=100)
            
            travel_style = st.selectbox("Travel Style", 
                                      ["cultural", "adventure", "relaxation", "luxury"],
                                      index=["cultural", "adventure", "relaxation", "luxury"].index(
                                          st.session_state.current_profile.travel_style) 
                                      if st.session_state.current_profile.travel_style else 0)
            
            group_size = st.number_input("Group Size", min_value=1, max_value=10,
                                       value=st.session_state.current_profile.group_size or 1)
            
            submitted = st.form_submit_button("Update Profile", type="primary")
            
            if submitted:
                # Update profile
                st.session_state.current_profile.name = name
                st.session_state.current_profile.destination = destination
                st.session_state.current_profile.duration = duration
                st.session_state.current_profile.budget = budget
                st.session_state.current_profile.travel_style = travel_style
                st.session_state.current_profile.group_size = group_size
                
                st.success("Profile updated! 🎉")
                st.rerun()
        
        # Current profile display
        st.subheader("📋 Current Profile")
        profile = st.session_state.current_profile
        if profile.name:
            st.write(f"**Name:** {profile.name}")
        if profile.destination:
            st.write(f"**Destination:** {profile.destination}")
        if profile.duration:
            st.write(f"**Duration:** {profile.duration} days")
        if profile.budget:
            st.write(f"**Budget:** ${profile.budget}")
        if profile.travel_style:
            st.write(f"**Style:** {profile.travel_style.title()}")
        
        # Package summary (for quick mode)
        if st.session_state.selected_mode == "Quick Packages" and st.session_state.packages:
            st.markdown("## 📊 Package Summary")
            for i, package in enumerate(st.session_state.packages, 1):
                st.markdown(f"**{i}. {package['name']}**")
                st.markdown(f"💰 ${package['pricing']['total']:,}")
                st.markdown(f"🏨 {package['hotel']['name']}")
                st.markdown("---")
    
    # Main content based on selected mode
    if st.session_state.selected_mode == "Quick Packages":
        platform.quick_packages_mode()
    else:
        platform.advanced_ai_mode()

if __name__ == "__main__":
    main()
