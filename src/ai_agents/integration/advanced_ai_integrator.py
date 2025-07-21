"""
🔗 Advanced AI Integration Module
Integrates conversation memory, enhanced psychology analyst, and real-time validation
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import streamlit as st

# Import our enhanced modules
try:
    from ai_agents.memory.conversation_memory import memory_manager, UserPreferences, ConversationContext
    from ai_agents.psychology.enhanced_psychology_analyst import psychology_analyst, PsychologyProfile
    from ai_agents.validation.real_time_validator import real_time_validator
    MODULES_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Some AI modules not available: {e}")
    MODULES_AVAILABLE = False
    # Create dummy classes for graceful degradation
    class UserPreferences:
        pass
    class ConversationContext:
        pass
    class PsychologyProfile:
        personality_type = "balanced"
        confidence_score = 0.5
        travel_motivations = []
        decision_making_style = "balanced"
        social_preferences = "balanced"
        risk_tolerance = "moderate"
        experience_seeking = "moderate"
        authenticity_preference = "moderate"
        luxury_orientation = "moderate"
        cultural_openness = "moderate"
        adventure_level = "moderate"
        pace_preference = "moderate"
        group_dynamics = "balanced"
        stress_management = "balanced"

class AdvancedAIIntegrator:
    """Advanced AI integrator for enhanced travel platform"""
    
    def __init__(self):
        if MODULES_AVAILABLE:
            self.memory_system = memory_manager
            self.psychology_system = psychology_analyst
            self.validation_system = real_time_validator
        else:
            self.memory_system = None
            self.psychology_system = None
            self.validation_system = None
        self.initialize_integration()
    
    def initialize_integration(self):
        """Initialize integration between all systems"""
        # Initialize session state for integration
        if 'ai_integration_active' not in st.session_state:
            st.session_state.ai_integration_active = False
        if 'current_user_id' not in st.session_state:
            st.session_state.current_user_id = None
        if 'enhanced_mode' not in st.session_state:
            st.session_state.enhanced_mode = False
    
    def process_user_input_with_ai(self, user_input: str, user_id: str) -> Dict[str, Any]:
        """Process user input through all AI systems"""
        
        if not MODULES_AVAILABLE:
            # Fallback response when modules aren't available
            return {
                "user_preferences": None,
                "psychology_analysis": {"sentiment": {"polarity": 0.0, "subjectivity": 0.5}},
                "psychology_profile": PsychologyProfile(),
                "agent_guidance": {},
                "conversation_context": None,
                "enhanced_recommendations": {
                    "personalized_activities": ["Standard activities"],
                    "accommodation_suggestions": ["Standard accommodations"],
                    "dining_recommendations": ["Standard dining"],
                    "itinerary_adjustments": ["Standard itinerary"],
                    "budget_optimizations": ["Standard budget options"]
                }
            }
        
        # 1. Memory System: Store and retrieve context
        user_preferences = self.memory_system.get_user_preferences(user_id)
        conversation_context = self.memory_system.get_conversation_context(user_id)
        
        # Update conversation with new input
        self.memory_system.add_interaction(
            user_id=user_id,
            interaction_type="user_input",
            data={"content": user_input, "timestamp": datetime.now().isoformat()}
        )
        
        # 2. Psychology Analysis: Analyze input for psychological insights
        psychology_analysis = self.psychology_system.analyze_text_input(user_input)
        psychology_profile = self.psychology_system.generate_psychology_profile(
            psychology_analysis, 
            conversation_context.interaction_history if conversation_context else []
        )
        
        # 3. Update memory with psychology insights (method not implemented yet)
        # self.memory_system.update_behavioral_analysis(
        #     user_id=user_id,
        #     new_insights={
        #         "personality_type": psychology_profile.personality_type,
        #         "travel_motivations": psychology_profile.travel_motivations,
        #         "decision_style": psychology_profile.decision_making_style,
        #         "confidence_score": psychology_profile.confidence_score
        #     }
        # )
        
        # 4. Generate agent guidance
        agent_guidance = self.psychology_system.provide_agent_guidance(psychology_profile)
        
        return {
            "user_preferences": user_preferences,
            "psychology_analysis": psychology_analysis,
            "psychology_profile": psychology_profile,
            "agent_guidance": agent_guidance,
            "conversation_context": conversation_context,
            "enhanced_recommendations": self.generate_enhanced_recommendations(
                user_preferences, psychology_profile, agent_guidance
            )
        }
    
    def generate_enhanced_recommendations(self, 
                                        user_preferences: UserPreferences,
                                        psychology_profile: PsychologyProfile,
                                        agent_guidance: Dict[str, Any]) -> Dict[str, Any]:
        """Generate enhanced recommendations based on all AI insights"""
        
        recommendations = {
            "personalized_activities": [],
            "accommodation_suggestions": [],
            "dining_recommendations": [],
            "itinerary_adjustments": [],
            "budget_optimizations": []
        }
        
        # Activity recommendations based on psychology
        if psychology_profile.personality_type == "adventurous":
            recommendations["personalized_activities"].extend([
                "Extreme sports experiences",
                "Adventure tours",
                "Outdoor activities",
                "Thrill-seeking experiences"
            ])
        elif psychology_profile.personality_type == "cultural":
            recommendations["personalized_activities"].extend([
                "Museum visits",
                "Historical tours", 
                "Cultural workshops",
                "Local art experiences"
            ])
        elif psychology_profile.personality_type == "relaxed":
            recommendations["personalized_activities"].extend([
                "Spa treatments",
                "Beach time",
                "Scenic walks",
                "Wellness activities"
            ])
        
        # Accommodation based on preferences and psychology
        if user_preferences and user_preferences.accommodation_preferences:
            if psychology_profile.luxury_orientation == "high":
                recommendations["accommodation_suggestions"].append(
                    "Upgrade to luxury resorts with premium amenities"
                )
            elif psychology_profile.authenticity_preference == "high":
                recommendations["accommodation_suggestions"].append(
                    "Local boutique hotels or authentic guesthouses"
                )
        
        # Dining based on cultural openness and social preferences
        if psychology_profile.cultural_openness == "high":
            recommendations["dining_recommendations"].extend([
                "Local street food tours",
                "Traditional cooking classes",
                "Authentic local restaurants"
            ])
        
        if psychology_profile.social_preferences == "social":
            recommendations["dining_recommendations"].extend([
                "Group dining experiences",
                "Food and wine tours",
                "Social dining venues"
            ])
        
        # Itinerary adjustments based on pace and decision style
        if psychology_profile.pace_preference == "slow":
            recommendations["itinerary_adjustments"].append(
                "Reduce daily activities for a more relaxed pace"
            )
        
        if psychology_profile.decision_making_style == "spontaneous":
            recommendations["itinerary_adjustments"].append(
                "Leave flexible time slots for spontaneous discoveries"
            )
        
        return recommendations
    
    def create_enhanced_package_with_validation(self, 
                                              package_data: Dict[str, Any],
                                              user_id: str) -> Dict[str, Any]:
        """Create travel package with real-time validation enabled"""
        
        # Get user context and psychology profile
        ai_analysis = self.process_user_input_with_ai("", user_id)
        
        # Enhance package with AI insights
        enhanced_package = self.enhance_package_with_ai(
            package_data, 
            ai_analysis["user_preferences"],
            ai_analysis["psychology_profile"],
            ai_analysis["agent_guidance"]
        )
        
        # Enable real-time validation
        if st.session_state.enhanced_mode:
            st.header("🤖 AI-Enhanced Package Creation")
            
            # Show AI insights
            self.display_ai_insights(ai_analysis)
            
            # Create validation interface
            validated_package = self.validation_system.create_validation_interface(enhanced_package)
            
            # Update memory with validation feedback
            if st.session_state.validation_feedback:
                self.memory_system.add_interaction(
                    user_id=user_id,
                    interaction_type="validation_feedback",
                    content="User provided validation feedback",
                    metadata={
                        "feedback_count": len(st.session_state.validation_feedback),
                        "timestamp": datetime.now().isoformat()
                    }
                )
            
            return validated_package
        
        return enhanced_package
    
    def enhance_package_with_ai(self,
                               package_data: Dict[str, Any],
                               user_preferences: UserPreferences,
                               psychology_profile: PsychologyProfile,
                               agent_guidance: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance package data with AI insights"""
        
        enhanced_package = package_data.copy()
        
        # Add AI-driven metadata
        enhanced_package["ai_enhancements"] = {
            "personality_type": psychology_profile.personality_type,
            "confidence_score": psychology_profile.confidence_score,
            "personalization_level": "high" if psychology_profile.confidence_score > 0.7 else "medium",
            "enhancement_timestamp": datetime.now().isoformat()
        }
        
        # Enhance activities based on psychology
        if "itinerary" in enhanced_package and "activities" in enhanced_package["itinerary"]:
            enhanced_activities = []
            
            for activity in enhanced_package["itinerary"]["activities"]:
                enhanced_activity = activity.copy()
                
                # Add psychology-based tags
                enhanced_activity["psychology_match"] = self.calculate_activity_psychology_match(
                    activity, psychology_profile
                )
                
                # Add preference alignment score
                if user_preferences:
                    enhanced_activity["preference_score"] = self.calculate_preference_alignment(
                        activity, user_preferences
                    )
                
                enhanced_activities.append(enhanced_activity)
            
            enhanced_package["itinerary"]["activities"] = enhanced_activities
        
        # Enhance accommodation recommendations
        if "hotels" in enhanced_package:
            for hotel in enhanced_package["hotels"]:
                hotel["psychology_fit"] = self.calculate_accommodation_psychology_fit(
                    hotel, psychology_profile
                )
        
        # Add AI-generated insights
        enhanced_package["ai_insights"] = {
            "travel_style": self.determine_travel_style(psychology_profile),
            "recommended_pace": psychology_profile.pace_preference,
            "social_recommendations": self.get_social_recommendations(psychology_profile),
            "budget_guidance": agent_guidance.get("itinerary_architect", {}).get("budget_allocation", {})
        }
        
        return enhanced_package
    
    def display_ai_insights(self, ai_analysis: Dict[str, Any]):
        """Display AI insights in Streamlit interface"""
        
        st.subheader("🧠 AI Insights Dashboard")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Psychology Confidence", 
                f"{ai_analysis['psychology_profile'].confidence_score:.1%}"
            )
        
        with col2:
            st.metric(
                "Personality Type",
                ai_analysis['psychology_profile'].personality_type.title()
            )
        
        with col3:
            st.metric(
                "Risk Tolerance",
                ai_analysis['psychology_profile'].risk_tolerance.title()
            )
        
        # Expandable sections for detailed insights
        with st.expander("🎯 Travel Motivations"):
            motivations = ai_analysis['psychology_profile'].travel_motivations
            if motivations:
                for motivation in motivations:
                    st.write(f"• {motivation.title()}")
            else:
                st.write("No specific motivations identified yet.")
        
        with st.expander("🤝 Social Preferences"):
            social_pref = ai_analysis['psychology_profile'].social_preferences
            st.write(f"**Style:** {social_pref.title()}")
            st.write(f"**Group Dynamics:** {ai_analysis['psychology_profile'].group_dynamics}")
        
        with st.expander("💡 Enhanced Recommendations"):
            recommendations = ai_analysis['enhanced_recommendations']
            
            for category, items in recommendations.items():
                if items:
                    st.write(f"**{category.replace('_', ' ').title()}:**")
                    for item in items:
                        st.write(f"• {item}")
        
        with st.expander("🎛️ Agent Guidance"):
            guidance = ai_analysis['agent_guidance']
            
            for agent, settings in guidance.items():
                st.write(f"**{agent.replace('_', ' ').title()}:**")
                for setting, value in settings.items():
                    st.write(f"  • {setting.replace('_', ' ').title()}: {value}")
    
    def enable_enhanced_mode(self, user_id: str):
        """Enable enhanced AI mode"""
        st.session_state.enhanced_mode = True
        st.session_state.current_user_id = user_id
        st.session_state.ai_integration_active = True
        
        # Initialize user in memory system
        self.memory_system.initialize_user(user_id)
        
        # Show enhanced mode indicator
        st.success("🤖 Enhanced AI Mode Activated!")
        st.info("Now using conversation memory, psychology analysis, and real-time validation.")
    
    def disable_enhanced_mode(self):
        """Disable enhanced AI mode"""
        st.session_state.enhanced_mode = False
        st.session_state.ai_integration_active = False
        st.info("Enhanced AI Mode Deactivated")
    
    # Helper methods
    def calculate_activity_psychology_match(self, 
                                          activity: Dict[str, Any], 
                                          psychology_profile: PsychologyProfile) -> float:
        """Calculate how well an activity matches user psychology"""
        
        score = 0.0
        
        # Adventure matching
        if psychology_profile.adventure_level == "high":
            adventure_keywords = ["adventure", "extreme", "thrill", "challenging"]
            activity_text = f"{activity.get('name', '')} {activity.get('description', '')}".lower()
            
            for keyword in adventure_keywords:
                if keyword in activity_text:
                    score += 0.2
        
        # Cultural matching
        if psychology_profile.cultural_openness == "high":
            cultural_keywords = ["culture", "history", "museum", "traditional", "local"]
            activity_text = f"{activity.get('name', '')} {activity.get('description', '')}".lower()
            
            for keyword in cultural_keywords:
                if keyword in activity_text:
                    score += 0.2
        
        # Social matching
        if psychology_profile.social_preferences == "social":
            social_keywords = ["group", "tour", "social", "meet", "community"]
            activity_text = f"{activity.get('name', '')} {activity.get('description', '')}".lower()
            
            for keyword in social_keywords:
                if keyword in activity_text:
                    score += 0.2
        
        return min(1.0, score)  # Cap at 1.0
    
    def calculate_preference_alignment(self, 
                                     activity: Dict[str, Any], 
                                     user_preferences: UserPreferences) -> float:
        """Calculate preference alignment score"""
        
        if not user_preferences or not user_preferences.activity_preferences:
            return 0.5  # Neutral score if no preferences
        
        score = 0.0
        activity_text = f"{activity.get('name', '')} {activity.get('description', '')}".lower()
        
        for preference in user_preferences.activity_preferences:
            if preference.lower() in activity_text:
                score += 0.3
        
        return min(1.0, score)
    
    def calculate_accommodation_psychology_fit(self, 
                                             hotel: Dict[str, Any], 
                                             psychology_profile: PsychologyProfile) -> Dict[str, Any]:
        """Calculate accommodation psychology fit"""
        
        fit_analysis = {
            "luxury_match": 0.0,
            "authenticity_match": 0.0,
            "social_match": 0.0,
            "overall_fit": 0.0
        }
        
        # Luxury matching
        if psychology_profile.luxury_orientation == "high":
            if hotel.get('rating', 0) >= 4:
                fit_analysis["luxury_match"] = 0.8
            luxury_amenities = ["spa", "pool", "concierge", "suite"]
            hotel_amenities = hotel.get('amenities', [])
            
            for amenity in luxury_amenities:
                if any(amenity in str(hotel_amenity).lower() for hotel_amenity in hotel_amenities):
                    fit_analysis["luxury_match"] += 0.1
        
        # Authenticity matching
        if psychology_profile.authenticity_preference == "high":
            authentic_keywords = ["boutique", "local", "traditional", "heritage"]
            hotel_text = f"{hotel.get('name', '')} {hotel.get('description', '')}".lower()
            
            for keyword in authentic_keywords:
                if keyword in hotel_text:
                    fit_analysis["authenticity_match"] += 0.2
        
        # Calculate overall fit
        fit_analysis["overall_fit"] = (
            fit_analysis["luxury_match"] + 
            fit_analysis["authenticity_match"] + 
            fit_analysis["social_match"]
        ) / 3
        
        return fit_analysis
    
    def determine_travel_style(self, psychology_profile: PsychologyProfile) -> str:
        """Determine overall travel style based on psychology profile"""
        
        if psychology_profile.personality_type == "adventurous" and psychology_profile.risk_tolerance == "high":
            return "Adventure Seeker"
        elif psychology_profile.cultural_openness == "high" and psychology_profile.authenticity_preference == "high":
            return "Cultural Explorer"
        elif psychology_profile.luxury_orientation == "high" and psychology_profile.pace_preference == "slow":
            return "Luxury Traveler"
        elif psychology_profile.social_preferences == "social" and psychology_profile.experience_seeking == "high":
            return "Social Explorer"
        elif psychology_profile.personality_type == "family":
            return "Family Traveler"
        else:
            return "Balanced Explorer"
    
    def get_social_recommendations(self, psychology_profile: PsychologyProfile) -> List[str]:
        """Get social recommendations based on psychology"""
        
        recommendations = []
        
        if psychology_profile.social_preferences == "social":
            recommendations.extend([
                "Join group tours for meeting like-minded travelers",
                "Book social dining experiences",
                "Stay in accommodations with common areas"
            ])
        elif psychology_profile.social_preferences == "intimate":
            recommendations.extend([
                "Book private tours for personal experiences",
                "Choose romantic dining venues",
                "Select intimate, boutique accommodations"
            ])
        elif psychology_profile.social_preferences == "family":
            recommendations.extend([
                "Look for family-friendly group activities",
                "Choose restaurants with children's menus",
                "Select accommodations with family amenities"
            ])
        else:  # independent
            recommendations.extend([
                "Maintain flexibility for solo exploration",
                "Mix group and independent activities",
                "Choose accommodations that support both social and private time"
            ])
        
        return recommendations

# Global integrator instance
ai_integrator = AdvancedAIIntegrator()
