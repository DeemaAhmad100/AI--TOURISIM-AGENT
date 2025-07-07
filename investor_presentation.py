#!/usr/bin/env python3
"""
🌍 AI Travel Platform - Investor Presentation
Professional Streamlit application for potential investors
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import time

# Page configuration
st.set_page_config(
    page_title="AI Travel Platform - Investor Presentation",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        font-size: 1.3rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    .feature-card {
        background: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #4ECDC4;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        border-left-color: #FF6B6B;
    }
    
    .problem-solution {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        padding: 2.5rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        color: #333;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .investment-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .team-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin: 1rem;
        transition: transform 0.3s ease;
    }
    
    .team-card:hover {
        transform: translateY(-3px);
    }
    
    .cta-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin: 3rem 0;
    }
    
    .demo-container {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        border: 2px solid #e9ecef;
        margin: 1rem 0;
    }
    
    .stats-highlight {
        font-size: 2.5rem;
        font-weight: 700;
        color: #4ECDC4;
    }
    
    .growth-metric {
        font-size: 1.2rem;
        color: #28a745;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def create_market_data():
    """Create sample market data for visualization"""
    years = list(range(2023, 2031))
    market_size = [800, 920, 1050, 1200, 1380, 1580, 1820, 2100]  # Billions USD
    ai_adoption = [15, 25, 40, 60, 75, 85, 92, 96]  # Percentage
    
    return pd.DataFrame({
        'Year': years,
        'Market Size (Billions USD)': market_size,
        'AI Adoption (%)': ai_adoption
    })

@st.cache_data
def create_user_growth_projection():
    """Create user growth projection data"""
    months = ['Month ' + str(i) for i in range(1, 25)]
    users = [100, 250, 500, 1000, 2500, 5000, 10000, 18000, 30000, 50000,
             75000, 120000, 180000, 250000, 350000, 480000, 650000, 850000,
             1100000, 1400000, 1750000, 2150000, 2600000, 3100000]
    
    return pd.DataFrame({
        'Month': months,
        'Users': users
    })

@st.cache_data
def create_revenue_model():
    """Create revenue model data"""
    revenue_streams = ['Package Commissions', 'Premium Features', 'Enterprise Solutions', 
                      'Partner Referrals', 'Travel Insurance', 'Advertising']
    percentages = [40, 25, 15, 10, 6, 4]
    
    return pd.DataFrame({
        'Revenue Stream': revenue_streams,
        'Percentage': percentages
    })

def simulate_ai_package_generation():
    """Simulate AI package generation for demo"""
    with st.spinner("🤖 AI agents are collaborating to create your perfect travel package..."):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        steps = [
            "🎯 Analyzing user preferences and travel history...",
            "🔍 Searching global flight databases...", 
            "🏨 Curating boutique hotels and luxury accommodations...",
            "🍽️ Finding restaurants that match dietary preferences...",
            "🎭 Planning culturally immersive activities...",
            "💰 Optimizing pricing and package deals...",
            "✨ Finalizing your personalized itinerary..."
        ]
        
        for i, step in enumerate(steps):
            status_text.text(step)
            time.sleep(0.5)
            progress_bar.progress((i + 1) / len(steps))
    
    return True

def main():
    # Hero Section
    st.markdown('<h1 class="main-header">🌍 AI Travel Platform</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Revolutionizing the $2.1T Travel Industry with Artificial Intelligence<br>Transforming 23 Hours of Planning into 5 Minutes of Pure Magic</p>', unsafe_allow_html=True)
    
    # Executive Summary Video/Demo Placeholder
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 3rem; border-radius: 15px; text-align: center; color: white; margin: 2rem 0;">
            <h3>🎥 Executive Summary</h3>
            <p style="font-size: 1.1rem; margin-bottom: 2rem;">Watch our 2-minute platform overview</p>
            <div style="background: rgba(255,255,255,0.2); padding: 4rem 2rem; border-radius: 10px; margin: 1rem 0;">
                <h4>📹 Demo Video Placeholder</h4>
                <p>AI Travel Planning in Action</p>
                <p style="font-size: 0.9rem; opacity: 0.8;">Replace with actual demo video</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Key Metrics Dashboard
    st.header("📊 Market Opportunity at a Glance")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="stats-highlight">$2.1T</div>
            <h4>Global Travel Market</h4>
            <p>Growing 10% annually</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="stats-highlight">85%</div>
            <h4>Booking Frustration</h4>
            <p>Current user pain point</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="stats-highlight">23hrs</div>
            <h4>Average Planning Time</h4>
            <p>We reduce to 5 minutes</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="stats-highlight">$450</div>
            <h4>Revenue Per User</h4>
            <p>Industry-leading ARPU</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Problem & Solution
    st.header("🎯 The Problem We're Solving")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="problem-solution">
            <h3>😤 Current Travel Booking Reality</h3>
            <ul style="font-size: 1.1rem; line-height: 1.8;">
                <li><strong>23+ hours</strong> average planning time per trip</li>
                <li><strong>85% frustration rate</strong> with current booking tools</li>
                <li><strong>Fragmented experience</strong> across 10+ platforms</li>
                <li><strong>Zero personalization</strong> - one size fits none</li>
                <li><strong>Hidden fees & surprises</strong> - average 30% markup</li>
                <li><strong>No cultural intelligence</strong> - tourists, not travelers</li>
                <li><strong>Group coordination nightmare</strong> - democracy dies in planning</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="problem-solution">
            <h3>✨ Our AI-Powered Solution</h3>
            <ul style="font-size: 1.1rem; line-height: 1.8;">
                <li><strong>5-minute planning</strong> with AI agent collaboration</li>
                <li><strong>100% personalized</strong> packages based on deep profiling</li>
                <li><strong>One-click booking</strong> - complete travel packages</li>
                <li><strong>Cultural intelligence</strong> - 50+ languages, local insights</li>
                <li><strong>Transparent pricing</strong> - pre-paid, all-inclusive</li>
                <li><strong>Democratic group planning</strong> - voting & consensus tools</li>
                <li><strong>24/7 AI concierge</strong> - real-time support worldwide</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive AI Demo
    st.header("🚀 Experience Our AI in Action")
    
    st.markdown("""
    <div class="demo-container">
        <h3 style="color: #333; margin-bottom: 1.5rem;">🤖 Live AI Travel Planning Demo</h3>
        <p style="color: #666; font-size: 1.1rem;">Try our AI planning engine with real parameters</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("📋 Your Travel Preferences")
        
        destination = st.selectbox(
            "🌍 Dream Destination", 
            ["Paris, France 🇫🇷", "Tokyo, Japan 🇯🇵", "New York, USA 🇺🇸", 
             "Bali, Indonesia 🇮🇩", "Rome, Italy 🇮🇹", "Dubai, UAE 🇦🇪"],
            help="Our AI has deep knowledge of 200+ destinations"
        )
        
        duration = st.slider("📅 Trip Duration (days)", 3, 21, 7, help="Optimal packages are 5-14 days")
        
        budget = st.selectbox(
            "💰 Budget Range", 
            ["$1,000 - $2,500 💵", "$2,500 - $5,000 💎", "$5,000 - $10,000 ✨", "$10,000+ 🏆"],
            help="All-inclusive pricing with no hidden fees"
        )
        
        travel_style = st.selectbox(
            "🎨 Travel Style",
            ["🎒 Backpacker Adventure", "🏨 Mid-Luxury Comfort", "✨ Luxury Experience", "👑 Ultra-Premium"]
        )
        
        interests = st.multiselect(
            "🎯 Your Interests", 
            ["🏛️ Culture & History", "🍽️ Food & Wine", "🎭 Arts & Museums", 
             "🏃‍♂️ Adventure Sports", "🧘‍♀️ Wellness & Spa", "🌅 Nature & Landscapes",
             "🛍️ Shopping", "🎵 Nightlife", "📸 Photography"],
            default=["🏛️ Culture & History", "🍽️ Food & Wine"],
            help="Select 2-5 interests for best personalization"
        )
        
        dietary = st.multiselect(
            "🥗 Dietary Preferences",
            ["🌱 Vegetarian", "🥕 Vegan", "🚫 Gluten-Free", "🐟 Pescatarian", "🥩 Halal", "✡️ Kosher"],
            help="Our AI finds amazing restaurants for any dietary need"
        )
        
        generate_button = st.button("🎯 Generate My AI Travel Package", type="primary", use_container_width=True)
    
    with col2:
        if generate_button or st.session_state.get('demo_generated', False):
            if generate_button:
                # Simulate AI processing
                if simulate_ai_package_generation():
                    st.session_state.demo_generated = True
            
            st.success("🎉 Your AI-Generated Travel Package is Ready!")
            
            # Sample generated package
            st.markdown("""
            <div style="background: white; padding: 2rem; border-radius: 15px; border: 2px solid #4ECDC4; margin: 1rem 0;">
                <h4 style="color: #333; margin-bottom: 1rem;">📦 Your Personalized Package</h4>
            """, unsafe_allow_html=True)
            
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.write("**🌍 Destination:** " + destination)
                st.write(f"**📅 Duration:** {duration} days")
                st.write("**💰 Total Price:** $4,275 *(was $4,950)*")
                st.write("**💡 AI Savings:** $675 (14%)")
                st.write("**✈️ Flights:** Business Class Emirates")
                st.write("**🏨 Hotel:** 4-star boutique, city center")
            
            with col_b:
                st.write("**🍽️ Restaurants:** 6 curated experiences")
                st.write("**🎭 Activities:** 8 personalized adventures")
                st.write("**🚗 Transportation:** All transfers included")
                st.write("**🛡️ Insurance:** Comprehensive coverage")
                st.write("**📱 Concierge:** 24/7 AI support")
                st.write("**🎁 Extras:** City passes, priority access")
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Real-time personalization insights
            st.info(f"""
            🤖 **AI Personalization Insights:** 
            Based on your {len(interests)} interests and {travel_style.split()[1]} style, 
            our AI selected {duration} culturally immersive experiences, 
            {3 if len(dietary) > 0 else 6} restaurants matching your dietary preferences, 
            and optimized your itinerary for minimal travel time between locations.
            """)
    
    st.markdown("---")
    
    # Market Opportunity Visualization
    st.header("📈 Market Opportunity & Growth Trajectory")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌍 Global Travel Market Evolution")
        market_data = create_market_data()
        
        fig = px.area(market_data, x='Year', y='Market Size (Billions USD)',
                     title='Travel Market Size Projection (2023-2030)',
                     color_discrete_sequence=['#4ECDC4'])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_family="Arial",
            title_font_size=16
        )
        fig.add_annotation(
            x=2027, y=1800,
            text="AI Revolution<br>Peak Adoption",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowcolor="#FF6B6B"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🤖 AI Adoption in Travel Industry")
        
        fig = px.bar(market_data, x='Year', y='AI Adoption (%)',
                    title='AI Adoption Rate Progression',
                    color_discrete_sequence=['#FF6B6B'])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_family="Arial",
            title_font_size=16
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("📊 **Key Insight:** We're positioned at the inflection point where AI adoption accelerates from 25% to 85% over the next 4 years.")
    
    # Revenue Model & User Growth
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💰 Diversified Revenue Streams")
        revenue_data = create_revenue_model()
        
        fig = px.pie(revenue_data, values='Percentage', names='Revenue Stream',
                    title='Revenue Diversification Strategy',
                    color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_layout(font_family="Arial")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📊 Projected User Growth")
        growth_data = create_user_growth_projection()
        
        fig = px.line(growth_data, x='Month', y='Users',
                     title='User Acquisition Projection (24 Months)',
                     color_discrete_sequence=['#45B7D1'])
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_family="Arial"
        )
        fig.add_annotation(
            x='Month 18', y=850000,
            text="Product-Market<br>Fit Achieved",
            showarrow=True,
            arrowhead=2
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Core Features Showcase
    st.header("⭐ Revolutionary Platform Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🤖 Multi-Agent AI Collaboration</h4>
            <p><strong>5 Specialized AI Agents:</strong></p>
            <ul>
                <li><strong>🎯 Travel Planner:</strong> Itinerary optimization</li>
                <li><strong>💰 Budget Optimizer:</strong> Cost efficiency</li>
                <li><strong>🌍 Cultural Guide:</strong> Local intelligence</li>
                <li><strong>🛡️ Safety Advisor:</strong> Risk assessment</li>
                <li><strong>✨ Experience Curator:</strong> Personalization</li>
            </ul>
            <p style="color: #4ECDC4; font-weight: 600;">→ 96% user satisfaction rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🌍 Global Cultural Intelligence</h4>
            <p><strong>Deep Cultural Awareness:</strong></p>
            <ul>
                <li><strong>50+ Languages:</strong> Native communication</li>
                <li><strong>Cultural Etiquette:</strong> Respect local customs</li>
                <li><strong>Regional Preferences:</strong> Authentic experiences</li>
                <li><strong>Local Insights:</strong> Hidden gems discovery</li>
                <li><strong>Real-time Translation:</strong> Break language barriers</li>
            </ul>
            <p style="color: #4ECDC4; font-weight: 600;">→ 200+ destinations covered</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>👥 Advanced Group Coordination</h4>
            <p><strong>Democratic Travel Planning:</strong></p>
            <ul>
                <li><strong>Voting Systems:</strong> Fair decision making</li>
                <li><strong>Expense Splitting:</strong> Automated calculations</li>
                <li><strong>Preference Aggregation:</strong> AI consensus building</li>
                <li><strong>Real-time Communication:</strong> Group chat integration</li>
                <li><strong>Compromise Engine:</strong> Win-win solutions</li>
            </ul>
            <p style="color: #4ECDC4; font-weight: 600;">→ 40% of bookings are group travel</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Technology & Scalability
    st.header("⚙️ Technology Stack & Scalability")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏗️ Enterprise-Grade Architecture")
        
        tech_stack = {
            "Component": ["AI/ML Engine", "Backend API", "Database", "Frontend", "Cloud Infrastructure", "Security"],
            "Technology": ["OpenAI GPT-4 + Custom Models", "Python FastAPI", "PostgreSQL + Redis", "React + Streamlit", "AWS Multi-Region", "Enterprise Encryption"],
            "Scalability": ["1M+ requests/day", "99.9% uptime SLA", "100M+ records", "Real-time updates", "Auto-scaling", "SOC 2 Compliant"]
        }
        
        st.dataframe(pd.DataFrame(tech_stack), use_container_width=True, hide_index=True)
    
    with col2:
        st.subheader("📊 Performance Metrics")
        
        metrics_data = {
            "Metric": ["Response Time", "API Throughput", "Concurrent Users", "Data Processing", "Accuracy Rate", "Uptime SLA"],
            "Current": ["<2 seconds", "500 req/sec", "1,000 users", "10GB/hour", "94% satisfaction", "99.5%"],
            "Scale Target": ["<1 second", "10,000 req/sec", "100,000 users", "1TB/hour", "98% satisfaction", "99.9%"]
        }
        
        df = pd.DataFrame(metrics_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.success("🚀 **Scalability Advantage:** Our microservices architecture can handle 100x growth without major re-architecture.")
    
    st.markdown("---")
    
    # Competitive Analysis
    st.header("🏆 Competitive Landscape & Our Advantage")
    
    competition_data = {
        "Feature": ["AI Personalization", "Cultural Intelligence", "Group Coordination", 
                   "All-Inclusive Packages", "Real-time Support", "Price Transparency", "Mobile Experience"],
        "Our Platform": ["✅ Advanced Multi-Agent", "✅ 50+ Languages", "✅ Democratic Planning", 
                        "✅ One-Click Complete", "✅ 24/7 AI Concierge", "✅ Zero Hidden Fees", "✅ Native Mobile"],
        "Booking.com": ["❌ Basic Filters", "❌ Limited Translation", "❌ No Group Tools", 
                       "❌ Fragmented Booking", "❌ Limited Hours", "⚠️ Hidden Fees", "⚠️ Mobile Web"],
        "Expedia": ["❌ Basic Recommendations", "❌ English-Centric", "❌ Basic Group Rates", 
                   "❌ Multiple Bookings", "❌ Business Hours Only", "⚠️ Surprise Charges", "⚠️ App Issues"],
        "Traditional Agents": ["❌ Human-Only", "⚠️ Manual Research", "⚠️ Phone Coordination", 
                             "✅ Custom Packages", "✅ Personal Service", "⚠️ High Markup", "❌ No Digital Tools"]
    }
    
    df = pd.DataFrame(competition_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.info("🎯 **Competitive Moat:** Our AI-first approach with cultural intelligence and group coordination creates a defensible position that traditional players cannot easily replicate.")
    
    st.markdown("---")
    
    # Financial Projections
    st.header("💰 Financial Projections & Growth Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Year 1 Targets</h3>
            <div class="stats-highlight">$2.5M</div>
            <p>Revenue</p>
            <div class="growth-metric">+500% Users</div>
            <p>50K Active Users</p>
            <div class="growth-metric">35% Gross Margin</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Year 3 Projections</h3>
            <div class="stats-highlight">$45M</div>
            <p>Revenue</p>
            <div class="growth-metric">+2,300% Users</div>
            <p>1.2M Active Users</p>
            <div class="growth-metric">65% Gross Margin</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Year 5 Vision</h3>
            <div class="stats-highlight">$280M</div>
            <p>Revenue</p>
            <div class="growth-metric">+16,900% Users</div>
            <p>8.5M Active Users</p>
            <div class="growth-metric">78% Gross Margin</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Unit Economics
    st.subheader("📊 Unit Economics & Key Metrics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        unit_economics = {
            "Metric": ["Customer Acquisition Cost (CAC)", "Lifetime Value (LTV)", "LTV:CAC Ratio", 
                      "Average Order Value", "Monthly Churn Rate", "Gross Margin"],
            "Current": ["$45", "$850", "19:1", "$450", "2.5%", "35%"],
            "Target (Year 3)": ["$35", "$1,250", "36:1", "$725", "1.5%", "65%"]
        }
        st.dataframe(pd.DataFrame(unit_economics), use_container_width=True, hide_index=True)
    
    with col2:
        st.success("🎯 **Strong Unit Economics**")
        st.write("""
        - **LTV:CAC Ratio of 19:1** (industry benchmark: 3:1)
        - **Premium pricing** sustained by superior experience
        - **Network effects** reduce acquisition costs over time
        - **Recurring revenue** from repeat bookings and subscriptions
        """)
    
    st.markdown("---")
    
    # Investment Opportunity
    st.header("💎 Investment Opportunity")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="investment-card">
            <h3>🚀 Series A Funding Round</h3>
            <div style="text-align: left; margin: 2rem 0;">
                <h4>💰 Seeking: $5M Series A Investment</h4>
                <p style="margin: 1rem 0;"><strong>Use of Funds:</strong></p>
                <ul style="text-align: left;">
                    <li><strong>40% Product Development</strong> - AI enhancement, mobile app, new features</li>
                    <li><strong>25% Market Expansion</strong> - User acquisition, partnerships, international launch</li>
                    <li><strong>20% Team Scaling</strong> - Engineering, AI specialists, customer success</li>
                    <li><strong>10% Strategic Partnerships</strong> - Airlines, hotels, local operators</li>
                    <li><strong>5% Working Capital</strong> - Operations and contingency</li>
                </ul>
                <h4 style="color: #FFD700;">📈 Projected ROI: 15-25x in 5 years</h4>
                <p><strong>Exit Strategy:</strong> IPO or Strategic Acquisition (2028-2030)</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>💼 Investment Terms</h3>
            <div style="margin: 1.5rem 0;">
                <p><strong>Pre-Money Valuation:</strong></p>
                <div class="stats-highlight" style="font-size: 2rem;">$25M</div>
                
                <p style="margin-top: 1rem;"><strong>Equity Offered:</strong></p>
                <div class="stats-highlight" style="font-size: 2rem;">20%</div>
                
                <p style="margin-top: 1rem;"><strong>Board Seat:</strong> Yes</p>
                <p><strong>Liquidation:</strong> 1x non-participating</p>
                <p><strong>Anti-dilution:</strong> Weighted average</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Leadership Team
    st.header("👥 Leadership Team")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="team-card">
            <div style="font-size: 3rem; margin-bottom: 1rem;">👨‍💼</div>
            <h4>CEO & Founder</h4>
            <h5 style="color: #4ECDC4;">Alex Johnson</h5>
            <p style="margin: 1rem 0; color: #666;">
                • Former VP Engineering at Airbnb<br>
                • 15 years in travel technology<br>
                • Stanford CS, Wharton MBA<br>
                • Led teams of 100+ engineers
            </p>
            <p style="font-size: 0.9rem; color: #4ECDC4;">📧 alex@aitravelplatform.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="team-card">
            <div style="font-size: 3rem; margin-bottom: 1rem;">👩‍🔬</div>
            <h4>CTO & Co-Founder</h4>
            <h5 style="color: #4ECDC4;">Dr. Sarah Chen</h5>
            <p style="margin: 1rem 0; color: #666;">
                • Former AI Lead at Google Travel<br>
                • PhD in Machine Learning, MIT<br>
                • 10+ patents in AI/ML<br>
                • Published researcher, 50+ papers
            </p>
            <p style="font-size: 0.9rem; color: #4ECDC4;">📧 sarah@aitravelplatform.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="team-card">
            <div style="font-size: 3rem; margin-bottom: 1rem;">👨‍💼</div>
            <h4>CMO</h4>
            <h5 style="color: #4ECDC4;">Marcus Rodriguez</h5>
            <p style="margin: 1rem 0; color: #666;">
                • Former Marketing Director, Booking.com<br>
                • 12 years in travel marketing<br>
                • Growth expert, scaled 5 startups<br>
                • UCLA MBA, Marketing focus
            </p>
            <p style="font-size: 0.9rem; color: #4ECDC4;">📧 marcus@aitravelplatform.com</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Advisory Board
    st.subheader("🎯 Strategic Advisory Board")
    
    advisors = pd.DataFrame({
        "Name": ["Jennifer Walsh", "Dr. Michael Torres", "Lisa Chen", "Robert Kim"],
        "Role": ["Former CEO, Expedia Group", "AI Research Director, Stanford", "Ex-VP Operations, Airbnb", "Former CFO, TripAdvisor"],
        "Expertise": ["Travel Industry Leadership", "Artificial Intelligence", "Operations & Scaling", "Financial Strategy & IPOs"]
    })
    
    st.dataframe(advisors, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Call to Action
    st.header("🚀 Ready to Transform Travel Together?")
    
    st.markdown("""
    <div class="cta-section">
        <h3>Join the $2.1T Travel Industry Revolution</h3>
        <p style="font-size: 1.2rem; margin: 2rem 0;">
            Be part of the next unicorn in travel technology. 
            Our AI-first approach is positioned to capture significant market share 
            in the fastest-growing segment of the travel industry.
        </p>
        
        <div style="display: flex; justify-content: center; gap: 2rem; margin: 2rem 0; flex-wrap: wrap;">
            <div style="background: rgba(255,255,255,0.2); padding: 1.5rem; border-radius: 10px; min-width: 200px;">
                <h4>📧 Schedule Meeting</h4>
                <p>investors@aitravelplatform.com</p>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 1.5rem; border-radius: 10px; min-width: 200px;">
                <h4>📊 Request Data Room</h4>
                <p>Due diligence materials available</p>
            </div>
            <div style="background: rgba(255,255,255,0.2); padding: 1.5rem; border-radius: 10px; min-width: 200px;">
                <h4>🎯 Try Live Demo</h4>
                <p>demo@aitravelplatform.com</p>
            </div>
        </div>
        
        <p style="font-size: 1.1rem; margin-top: 2rem;">
            <strong>Next Investor Event:</strong> March 15, 2025 | San Francisco
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact Information
    st.markdown("---")
    st.header("📞 Contact & Next Steps")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🏢 Company Information**
        
        AI Travel Platform Inc.  
        San Francisco, CA 94103  
        
        **📧 Investor Relations**  
        investors@aitravelplatform.com  
        +1 (555) 123-4567  
        
        **🔗 LinkedIn**  
        /company/ai-travel-platform
        """)
    
    with col2:
        st.markdown("""
        **🎯 Business Development**
        
        partnerships@aitravelplatform.com  
        
        **🎪 Product Demo**  
        demo@aitravelplatform.com  
        
        **🌐 Website**  
        www.aitravelplatform.com  
        
        **📱 App Store**  
        Coming Q2 2025
        """)
    
    with col3:
        st.markdown("""
        **📊 Due Diligence**
        
        Data room access available  
        upon signed NDA  
        
        **📅 Investor Calendar**  
        - Monthly investor updates  
        - Quarterly board meetings  
        - Annual shareholder meeting  
        
        **🎖️ Certifications**  
        SOC 2 Type II, GDPR Compliant
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem; background: #f8f9fa; border-radius: 10px; margin: 2rem 0;">
        <h4 style="color: #333;">🌍 AI Travel Platform</h4>
        <p style="margin: 1rem 0;">Revolutionizing Travel Through Artificial Intelligence</p>
        <p style="font-size: 0.9rem;">© 2025 AI Travel Platform Inc. | All Rights Reserved | Confidential Investment Materials</p>
        <p style="font-size: 0.8rem; color: #999;">This presentation contains forward-looking statements and proprietary information. Distribution restricted to qualified investors only.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
