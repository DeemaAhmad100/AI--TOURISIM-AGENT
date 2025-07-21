"""
⚡ Real-time Validation & Modification System
Advanced Streamlit interface for live user feedback and package modification
"""

import streamlit as st
import json
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, asdict
from datetime import datetime
import uuid

@dataclass
class ValidationFeedback:
    """Structure for user validation feedback"""
    element_id: str
    element_type: str  # 'activity', 'restaurant', 'hotel', 'timing', 'budget'
    feedback_type: str  # 'approve', 'reject', 'modify', 'replace'
    user_comment: str
    suggested_changes: Dict[str, Any]
    priority: int  # 1-5, how important this change is to the user
    timestamp: datetime

@dataclass 
class PackageElement:
    """Structure for package elements that can be validated"""
    id: str
    type: str
    title: str
    description: str
    details: Dict[str, Any]
    user_approved: Optional[bool] = None
    modification_history: List[ValidationFeedback] = None
    
    def __post_init__(self):
        if self.modification_history is None:
            self.modification_history = []

class RealTimeValidator:
    """Real-time validation and modification system"""
    
    def __init__(self):
        self.initialize_session_state()
        self.setup_validation_interface()
    
    def initialize_session_state(self):
        """Initialize Streamlit session state for validation"""
        if 'validation_active' not in st.session_state:
            st.session_state.validation_active = False
        if 'current_package' not in st.session_state:
            st.session_state.current_package = {}
        if 'validation_feedback' not in st.session_state:
            st.session_state.validation_feedback = []
        if 'modification_queue' not in st.session_state:
            st.session_state.modification_queue = []
        if 'real_time_mode' not in st.session_state:
            st.session_state.real_time_mode = False
    
    def setup_validation_interface(self):
        """Setup the validation interface components"""
        self.validation_components = {
            "activity_validator": self.validate_activities_section,
            "restaurant_validator": self.validate_restaurants_section,
            "hotel_validator": self.validate_hotels_section,
            "timing_validator": self.validate_timing_section,
            "budget_validator": self.validate_budget_section
        }
    
    def enable_real_time_mode(self):
        """Enable real-time validation mode"""
        st.session_state.real_time_mode = True
        st.session_state.validation_active = True
        
        # Create validation sidebar
        with st.sidebar:
            st.header("🔍 Real-Time Validation")
            st.write("**Mode:** Live Feedback Active")
            
            # Show validation statistics
            total_elements = len(st.session_state.current_package.get('elements', []))
            approved_count = sum(1 for elem in st.session_state.current_package.get('elements', []) 
                               if elem.get('user_approved') == True)
            
            st.metric("Package Elements", total_elements)
            st.metric("User Approved", approved_count)
            st.metric("Completion Rate", f"{(approved_count/max(total_elements,1))*100:.1f}%")
            
            if st.button("💾 Save Current State"):
                self.save_validation_state()
                st.success("State saved!")
            
            if st.button("🔄 Reset Validation"):
                self.reset_validation()
                st.rerun()
    
    def create_validation_interface(self, package_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create interactive validation interface for a travel package"""
        st.header("🎯 Package Validation & Modification")
        
        # Store package data in session state
        st.session_state.current_package = package_data
        
        # Enable real-time mode toggle
        real_time = st.toggle("Enable Real-Time Validation", value=st.session_state.real_time_mode)
        
        if real_time and not st.session_state.real_time_mode:
            self.enable_real_time_mode()
        elif not real_time:
            st.session_state.real_time_mode = False
        
        # Create tabs for different validation aspects
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🏃 Activities", "🍽️ Restaurants", "🏨 Hotels", "⏰ Timing", "💰 Budget"
        ])
        
        validated_package = package_data.copy()
        
        with tab1:
            validated_package = self.validate_activities_section(validated_package)
        
        with tab2:
            validated_package = self.validate_restaurants_section(validated_package)
        
        with tab3:
            validated_package = self.validate_hotels_section(validated_package)
        
        with tab4:
            validated_package = self.validate_timing_section(validated_package)
        
        with tab5:
            validated_package = self.validate_budget_section(validated_package)
        
        # Show overall validation status
        self.show_validation_summary()
        
        return validated_package
    
    def validate_activities_section(self, package_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate activities with real-time modification"""
        st.subheader("🏃 Activities Validation")
        
        activities = package_data.get('itinerary', {}).get('activities', [])
        modified_activities = []
        
        for i, activity in enumerate(activities):
            with st.expander(f"📍 {activity.get('name', f'Activity {i+1}')}"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.write(f"**Description:** {activity.get('description', 'N/A')}")
                    st.write(f"**Duration:** {activity.get('duration', 'N/A')}")
                    st.write(f"**Location:** {activity.get('location', 'N/A')}")
                    if activity.get('price'):
                        st.write(f"**Price:** ${activity['price']}")
                
                with col2:
                    # Validation buttons
                    approval_key = f"activity_approval_{i}"
                    
                    if st.button("✅ Approve", key=f"approve_act_{i}"):
                        activity['user_approved'] = True
                        if st.session_state.real_time_mode:
                            st.success("Activity approved!")
                            st.rerun()
                    
                    if st.button("❌ Reject", key=f"reject_act_{i}"):
                        activity['user_approved'] = False
                        if st.session_state.real_time_mode:
                            st.error("Activity rejected!")
                    
                    if st.button("✏️ Modify", key=f"modify_act_{i}"):
                        self.show_activity_modification_interface(activity, i)
                
                # Show modification interface if requested
                if activity.get('show_modification'):
                    self.render_activity_modification(activity, i)
                
                modified_activities.append(activity)
        
        # Update package data
        if 'itinerary' not in package_data:
            package_data['itinerary'] = {}
        package_data['itinerary']['activities'] = modified_activities
        
        return package_data
    
    def show_activity_modification_interface(self, activity: Dict[str, Any], index: int):
        """Show modification interface for an activity"""
        activity['show_modification'] = True
        
        # Force rerun to show modification interface
        if st.session_state.real_time_mode:
            st.rerun()
    
    def render_activity_modification(self, activity: Dict[str, Any], index: int):
        """Render modification form for activity"""
        st.write("### ✏️ Modify This Activity")
        
        # Modification form
        new_name = st.text_input("Activity Name", value=activity.get('name', ''), key=f"mod_name_{index}")
        new_description = st.text_area("Description", value=activity.get('description', ''), key=f"mod_desc_{index}")
        new_duration = st.text_input("Duration", value=activity.get('duration', ''), key=f"mod_dur_{index}")
        new_location = st.text_input("Location", value=activity.get('location', ''), key=f"mod_loc_{index}")
        
        # Alternative suggestions
        st.write("**Or choose an alternative:**")
        alternatives = self.generate_activity_alternatives(activity)
        
        for alt_idx, alternative in enumerate(alternatives):
            if st.button(f"🔄 Replace with: {alternative['name']}", key=f"alt_{index}_{alt_idx}"):
                # Replace activity with alternative
                activity.update(alternative)
                activity['user_approved'] = True
                activity['show_modification'] = False
                if st.session_state.real_time_mode:
                    st.success(f"Replaced with {alternative['name']}!")
                    st.rerun()
        
        # Save modifications
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Save Changes", key=f"save_mod_{index}"):
                activity.update({
                    'name': new_name,
                    'description': new_description,
                    'duration': new_duration,
                    'location': new_location,
                    'user_approved': True,
                    'show_modification': False
                })
                
                # Record modification
                feedback = ValidationFeedback(
                    element_id=str(uuid.uuid4()),
                    element_type='activity',
                    feedback_type='modify',
                    user_comment=f"Modified activity: {new_name}",
                    suggested_changes={
                        'name': new_name,
                        'description': new_description,
                        'duration': new_duration,
                        'location': new_location
                    },
                    priority=3,
                    timestamp=datetime.now()
                )
                st.session_state.validation_feedback.append(asdict(feedback))
                
                if st.session_state.real_time_mode:
                    st.success("Changes saved!")
                    st.rerun()
        
        with col2:
            if st.button("❌ Cancel", key=f"cancel_mod_{index}"):
                activity['show_modification'] = False
                if st.session_state.real_time_mode:
                    st.rerun()
    
    def generate_activity_alternatives(self, activity: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate alternative activities based on the current one"""
        # This would integrate with your existing activity search/recommendation system
        base_alternatives = [
            {
                "name": "Cultural Museum Tour",
                "description": "Explore local history and culture through guided museum visits",
                "duration": "3 hours",
                "location": "City Center",
                "price": 25
            },
            {
                "name": "Local Food Walking Tour",
                "description": "Taste authentic local cuisine while exploring neighborhoods",
                "duration": "4 hours", 
                "location": "Historic District",
                "price": 45
            },
            {
                "name": "Scenic Photography Tour",
                "description": "Capture beautiful moments with professional photography guidance",
                "duration": "2.5 hours",
                "location": "Scenic Viewpoints",
                "price": 35
            }
        ]
        
        return base_alternatives[:2]  # Return top 2 alternatives
    
    def validate_restaurants_section(self, package_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate restaurants with real-time modification"""
        st.subheader("🍽️ Restaurant Validation")
        
        restaurants = package_data.get('restaurants', [])
        
        for i, restaurant in enumerate(restaurants):
            with st.expander(f"🍴 {restaurant.get('name', f'Restaurant {i+1}')}"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.write(f"**Cuisine:** {restaurant.get('cuisine', 'N/A')}")
                    st.write(f"**Price Range:** {restaurant.get('price_range', 'N/A')}")
                    st.write(f"**Rating:** {restaurant.get('rating', 'N/A')}")
                    if restaurant.get('special_features'):
                        st.write(f"**Features:** {', '.join(restaurant['special_features'])}")
                
                with col2:
                    if st.button("✅ Approve", key=f"approve_rest_{i}"):
                        restaurant['user_approved'] = True
                        if st.session_state.real_time_mode:
                            st.success("Restaurant approved!")
                    
                    if st.button("❌ Replace", key=f"replace_rest_{i}"):
                        self.show_restaurant_alternatives(restaurant, i)
                    
                    if st.button("💬 Comment", key=f"comment_rest_{i}"):
                        self.show_comment_interface(restaurant, i, 'restaurant')
        
        return package_data
    
    def validate_hotels_section(self, package_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate hotels with real-time modification"""
        st.subheader("🏨 Hotel Validation")
        
        hotels = package_data.get('hotels', [])
        
        for i, hotel in enumerate(hotels):
            with st.expander(f"🏨 {hotel.get('name', f'Hotel {i+1}')}"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.write(f"**Location:** {hotel.get('location', 'N/A')}")
                    st.write(f"**Rating:** {hotel.get('rating', 'N/A')} stars")
                    st.write(f"**Price per night:** ${hotel.get('price_per_night', 'N/A')}")
                    if hotel.get('amenities'):
                        st.write(f"**Amenities:** {', '.join(hotel['amenities'])}")
                
                with col2:
                    if st.button("✅ Approve", key=f"approve_hotel_{i}"):
                        hotel['user_approved'] = True
                        if st.session_state.real_time_mode:
                            st.success("Hotel approved!")
                    
                    if st.button("🔄 Alternative", key=f"alt_hotel_{i}"):
                        self.show_hotel_alternatives(hotel, i)
        
        return package_data
    
    def validate_timing_section(self, package_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate timing and schedule"""
        st.subheader("⏰ Timing & Schedule Validation")
        
        # Overall schedule validation
        st.write("### 📅 Overall Schedule")
        
        schedule = package_data.get('schedule', {})
        
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Duration:** {schedule.get('total_duration', 'N/A')}")
            st.write(f"**Start Date:** {schedule.get('start_date', 'N/A')}")
            st.write(f"**End Date:** {schedule.get('end_date', 'N/A')}")
        
        with col2:
            if st.button("✏️ Modify Dates"):
                self.show_date_modification_interface()
            
            if st.button("⚡ Optimize Schedule"):
                self.optimize_schedule(package_data)
        
        # Daily schedule validation
        daily_schedules = package_data.get('daily_schedules', [])
        
        for i, day in enumerate(daily_schedules):
            with st.expander(f"📅 Day {i+1} Schedule"):
                st.write(f"**Activities:** {len(day.get('activities', []))}")
                
                # Show pace indicator
                pace = self.calculate_day_pace(day)
                pace_color = {"relaxed": "🟢", "moderate": "🟡", "busy": "🔴"}.get(pace, "⚪")
                st.write(f"**Pace:** {pace_color} {pace.title()}")
                
                if st.button(f"⚡ Adjust Day {i+1} Pace", key=f"adjust_pace_{i}"):
                    self.show_pace_adjustment(day, i)
        
        return package_data
    
    def validate_budget_section(self, package_data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate budget with real-time modification"""
        st.subheader("💰 Budget Validation")
        
        budget = package_data.get('budget', {})
        
        # Budget overview
        col1, col2, col3 = st.columns(3)
        
        with col1:
            total_budget = budget.get('total', 0)
            st.metric("Total Budget", f"${total_budget:,.2f}")
        
        with col2:
            estimated_cost = self.calculate_estimated_cost(package_data)
            st.metric("Estimated Cost", f"${estimated_cost:,.2f}")
        
        with col3:
            difference = total_budget - estimated_cost
            st.metric("Difference", f"${difference:,.2f}", 
                     delta=f"{'Within budget' if difference >= 0 else 'Over budget'}")
        
        # Budget breakdown validation
        st.write("### 💸 Budget Breakdown")
        
        breakdown = budget.get('breakdown', {})
        
        for category, amount in breakdown.items():
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.write(f"**{category.title()}:** ${amount:,.2f}")
            
            with col2:
                if st.button("✏️", key=f"edit_budget_{category}"):
                    new_amount = st.number_input(
                        f"New amount for {category}",
                        value=float(amount),
                        min_value=0.0,
                        key=f"new_amount_{category}"
                    )
                    
                    if st.button("💾 Save", key=f"save_budget_{category}"):
                        breakdown[category] = new_amount
                        if st.session_state.real_time_mode:
                            st.success(f"Updated {category} budget!")
                            st.rerun()
            
            with col3:
                priority = st.selectbox(
                    "Priority",
                    ["Low", "Medium", "High"],
                    key=f"priority_{category}"
                )
        
        # Budget optimization suggestions
        if difference < 0:  # Over budget
            st.warning("⚠️ **Over Budget!** Here are some suggestions:")
            suggestions = self.generate_budget_suggestions(package_data, abs(difference))
            
            for suggestion in suggestions:
                if st.button(f"💡 {suggestion['title']}", key=f"suggestion_{suggestion['id']}"):
                    self.apply_budget_suggestion(package_data, suggestion)
                    if st.session_state.real_time_mode:
                        st.success("Suggestion applied!")
                        st.rerun()
        
        return package_data
    
    def show_validation_summary(self):
        """Show overall validation summary"""
        st.header("📊 Validation Summary")
        
        total_feedback = len(st.session_state.validation_feedback)
        
        if total_feedback > 0:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                approved = sum(1 for f in st.session_state.validation_feedback 
                             if f.get('feedback_type') == 'approve')
                st.metric("Approved Items", approved)
            
            with col2:
                modified = sum(1 for f in st.session_state.validation_feedback 
                             if f.get('feedback_type') == 'modify')
                st.metric("Modified Items", modified)
            
            with col3:
                rejected = sum(1 for f in st.session_state.validation_feedback 
                             if f.get('feedback_type') == 'reject')
                st.metric("Rejected Items", rejected)
            
            # Show recent feedback
            st.write("### 📝 Recent Feedback")
            recent_feedback = st.session_state.validation_feedback[-5:]
            
            for feedback in reversed(recent_feedback):
                with st.expander(f"{feedback.get('feedback_type', '').title()} - {feedback.get('element_type', '').title()}"):
                    st.write(f"**Comment:** {feedback.get('user_comment', 'N/A')}")
                    st.write(f"**Time:** {feedback.get('timestamp', 'N/A')}")
                    st.write(f"**Priority:** {feedback.get('priority', 'N/A')}/5")
        else:
            st.info("No validation feedback yet. Start validating package elements above!")
        
        # Export validation report
        if st.button("📄 Export Validation Report"):
            report = self.generate_validation_report()
            st.download_button(
                label="Download Report",
                data=json.dumps(report, indent=2, default=str),
                file_name=f"validation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
    
    # Helper methods
    def calculate_day_pace(self, day: Dict[str, Any]) -> str:
        """Calculate the pace of a day based on activities"""
        activities = day.get('activities', [])
        
        if len(activities) <= 2:
            return "relaxed"
        elif len(activities) <= 4:
            return "moderate"
        else:
            return "busy"
    
    def calculate_estimated_cost(self, package_data: Dict[str, Any]) -> float:
        """Calculate estimated cost from package data"""
        total = 0
        
        # Add activity costs
        for activity in package_data.get('itinerary', {}).get('activities', []):
            total += activity.get('price', 0)
        
        # Add hotel costs
        for hotel in package_data.get('hotels', []):
            nights = package_data.get('schedule', {}).get('nights', 1)
            total += hotel.get('price_per_night', 0) * nights
        
        # Add restaurant costs (estimated)
        restaurants = len(package_data.get('restaurants', []))
        total += restaurants * 50  # Rough estimate per meal
        
        return total
    
    def generate_budget_suggestions(self, package_data: Dict[str, Any], overage: float) -> List[Dict[str, Any]]:
        """Generate budget optimization suggestions"""
        suggestions = [
            {
                "id": "reduce_hotel_tier",
                "title": f"Switch to mid-range hotels (Save ~${overage * 0.3:.0f})",
                "description": "Reduce accommodation costs while maintaining comfort",
                "savings": overage * 0.3
            },
            {
                "id": "optimize_activities",
                "title": f"Replace expensive activities (Save ~${overage * 0.4:.0f})",
                "description": "Find similar but more affordable experiences",
                "savings": overage * 0.4
            },
            {
                "id": "extend_duration",
                "title": f"Extend trip by 1 day (Spread costs)",
                "description": "Reduce daily spending by extending the trip",
                "savings": overage * 0.2
            }
        ]
        
        return suggestions
    
    def save_validation_state(self):
        """Save current validation state"""
        state_data = {
            "current_package": st.session_state.current_package,
            "validation_feedback": st.session_state.validation_feedback,
            "timestamp": datetime.now().isoformat()
        }
        
        # In a real application, this would save to a database
        # For now, we'll store in session state
        st.session_state.saved_validation_states = getattr(st.session_state, 'saved_validation_states', [])
        st.session_state.saved_validation_states.append(state_data)
    
    def reset_validation(self):
        """Reset validation state"""
        st.session_state.validation_feedback = []
        st.session_state.modification_queue = []
        st.session_state.current_package = {}
        st.session_state.validation_active = False
    
    def generate_validation_report(self) -> Dict[str, Any]:
        """Generate comprehensive validation report"""
        return {
            "report_id": str(uuid.uuid4()),
            "generated_at": datetime.now().isoformat(),
            "package_summary": {
                "total_elements": len(st.session_state.current_package.get('elements', [])),
                "validated_elements": len(st.session_state.validation_feedback)
            },
            "validation_feedback": st.session_state.validation_feedback,
            "statistics": {
                "approval_rate": len([f for f in st.session_state.validation_feedback 
                                    if f.get('feedback_type') == 'approve']) / max(len(st.session_state.validation_feedback), 1),
                "modification_rate": len([f for f in st.session_state.validation_feedback 
                                        if f.get('feedback_type') == 'modify']) / max(len(st.session_state.validation_feedback), 1)
            }
        }

# Global validator instance
real_time_validator = RealTimeValidator()
