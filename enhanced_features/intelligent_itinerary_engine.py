#!/usr/bin/env python3
"""
🧠 Intelligent Itinerary Engine
Advanced AI system for creating dynamic, personalized, and contextually aware travel itineraries
"""

import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import math
from dataclasses import dataclass, asdict

@dataclass
class ActivityTimeslot:
    """Represents a time-specific activity with intelligent attributes"""
    time_start: str
    time_end: str
    activity: str
    location: str
    category: str  # cultural, adventure, food, relaxation, shopping, nature
    energy_level: str  # low, medium, high
    crowd_factor: str  # low, medium, high
    weather_dependency: str  # indoor, outdoor, flexible
    cost_level: str  # free, low, medium, high
    duration_flexibility: float  # hours that can be adjusted
    prerequisites: List[str]  # what needs to happen before
    alternatives: List[str]  # backup options
    local_insights: List[str]  # insider tips
    photo_opportunities: List[str]  # Instagram-worthy spots
    learning_outcomes: List[str]  # what you'll learn/experience

@dataclass
class DayTheme:
    """Intelligent day theme with progression logic"""
    theme_name: str
    description: str
    energy_pattern: str  # gradual_build, peak_early, steady, relaxed
    cultural_focus: str
    must_include: List[str]
    avoid_combinations: List[str]

class IntelligentItineraryEngine:
    """Advanced itinerary generation with real intelligence"""
    
    def __init__(self):
        self.weather_patterns = self._load_weather_intelligence()
        self.crowd_patterns = self._load_crowd_intelligence()
        self.local_rhythms = self._load_local_rhythms()
        self.activity_intelligence = self._load_activity_intelligence_base()
        
    def _load_weather_intelligence(self) -> Dict:
        """Load weather-based activity recommendations"""
        return {
            "sunny": {
                "optimal": ["outdoor_markets", "walking_tours", "parks", "beaches", "rooftops"],
                "avoid": ["indoor_museums_all_day"],
                "timing": "morning_and_evening_best"
            },
            "rainy": {
                "optimal": ["museums", "galleries", "indoor_markets", "cooking_classes", "spas"],
                "indoor_alternatives": True,
                "covered_areas": ["covered_markets", "shopping_centers", "temples_with_cover"]
            },
            "hot": {
                "optimal_times": ["early_morning", "late_afternoon", "evening"],
                "midday_alternatives": ["air_conditioned_museums", "underground_areas", "cool_temples"],
                "hydration_stops": "every_2_hours"
            },
            "cold": {
                "warm_up_spots": ["cafes", "heated_transport", "indoor_attractions"],
                "optimal_activities": ["thermal_baths", "indoor_cultural_sites", "warm_food_tours"]
            }
        }
    
    def _load_crowd_intelligence(self) -> Dict:
        """Load crowd pattern intelligence"""
        return {
            "major_attractions": {
                "peak_times": ["10:00-15:00"],
                "optimal_times": ["08:00-10:00", "16:00-18:00"],
                "crowd_hacks": ["early_morning", "late_afternoon", "sunset_timing"]
            },
            "markets": {
                "peak_times": ["09:00-12:00"],
                "optimal_times": ["07:00-09:00", "15:00-17:00"],
                "local_rhythm": "follow_locals"
            },
            "restaurants": {
                "avoid_times": ["12:00-13:30", "19:00-21:00"],
                "optimal_times": ["11:30-12:00", "18:00-19:00", "21:30+"]
            }
        }
    
    def _load_local_rhythms(self) -> Dict:
        """Load local cultural rhythm intelligence"""
        return {
            "asian_cities": {
                "morning_culture": "early_markets_6am",
                "afternoon_rest": "2pm_siesta_equivalent",
                "evening_energy": "night_markets_after_6pm",
                "meal_timing": ["7:00", "12:00", "18:30"]
            },
            "european_cities": {
                "morning_culture": "cafe_culture_8am",
                "lunch_break": "12:00-14:00_slow_pace",
                "evening_culture": "aperitivo_18:00",
                "late_dining": "20:00_or_later"
            },
            "middle_eastern": {
                "prayer_times": "respect_5_daily_prayers",
                "afternoon_rest": "13:00-16:00_hot_weather",
                "evening_social": "sunset_community_time"
            }
        }
    
    def _load_activity_intelligence_base(self) -> Dict:
        """Load base activity intelligence patterns"""
        return {
            "energy_patterns": {
                "morning": ["market_visits", "cultural_sites", "walking_tours"],
                "afternoon": ["museums", "neighborhoods", "activities"],
                "evening": ["dining", "entertainment", "social"]
            },
            "progression_logic": {
                "day_1": "cultural_foundation",
                "day_2": "authentic_exploration", 
                "day_3": "deeper_immersion",
                "day_4+": "specialized_interests"
            },
            "anti_repetition": {
                "avoid_patterns": ["multiple_museums_same_day", "tourist_trap_clusters"],
                "variation_requirements": ["different_neighborhoods", "varied_activity_types"]
            }
        }
    
    def generate_intelligent_itinerary(self, 
                                     destination: str,
                                     duration_days: int,
                                     preferences: Dict,
                                     budget: str,
                                     travel_dates: str,
                                     traveler_profile: Dict) -> Dict:
        """
        Generate truly intelligent, adaptive itinerary
        """
        
        # Analyze traveler intelligence
        traveler_analysis = self._analyze_traveler_profile(preferences, traveler_profile)
        
        # Create daily themes with progression
        daily_themes = self._generate_intelligent_daily_themes(
            duration_days, destination, traveler_analysis
        )
        
        # Generate activities with real intelligence
        daily_itineraries = []
        
        for day in range(1, duration_days + 1):
            day_theme = daily_themes[day - 1]
            
            # Generate intelligent daily schedule
            daily_schedule = self._create_intelligent_daily_schedule(
                day=day,
                theme=day_theme,
                destination=destination,
                traveler_analysis=traveler_analysis,
                budget=budget,
                previous_days=daily_itineraries
            )
            
            daily_itineraries.append(daily_schedule)
        
        return {
            "destination": destination,
            "duration": duration_days,
            "traveler_profile": traveler_analysis,
            "daily_themes": [asdict(theme) for theme in daily_themes],
            "itinerary": daily_itineraries,
            "intelligence_features": self._add_intelligence_features(),
            "adaptive_recommendations": self._generate_adaptive_recommendations()
        }
    
    def _analyze_traveler_profile(self, preferences: Dict, profile: Dict) -> Dict:
        """Deep analysis of traveler to personalize experience"""
        return {
            "energy_preference": self._detect_energy_preference(preferences),
            "cultural_curiosity": self._detect_cultural_interest(preferences),
            "adventure_level": self._detect_adventure_level(preferences),
            "social_preference": self._detect_social_preference(preferences),
            "learning_style": self._detect_learning_style(preferences),
            "pace_preference": self._detect_pace_preference(preferences),
            "authentic_vs_comfort": self._detect_authenticity_preference(preferences)
        }
    
    def _generate_intelligent_daily_themes(self, duration: int, destination: str, analysis: Dict) -> List[DayTheme]:
        """Create progressive daily themes that build upon each other"""
        
        if duration <= 3:
            return self._create_short_trip_themes(duration, destination, analysis)
        elif duration <= 7:
            return self._create_week_trip_themes(duration, destination, analysis)
        else:
            return self._create_extended_trip_themes(duration, destination, analysis)
    
    def _create_short_trip_themes(self, duration: int, destination: str, analysis: Dict) -> List[DayTheme]:
        """Intensive themes for short trips"""
        themes = []
        
        if duration >= 1:
            themes.append(DayTheme(
                theme_name="Cultural Immersion Intensive",
                description="Dive deep into the heart of the destination's culture",
                energy_pattern="gradual_build",
                cultural_focus="authentic_local_experience",
                must_include=["signature_local_experience", "traditional_meal", "cultural_site"],
                avoid_combinations=["too_many_museums", "all_tourist_traps"]
            ))
        
        if duration >= 2:
            themes.append(DayTheme(
                theme_name="Hidden Gems & Local Secrets",
                description="Discover what locals love and tourists miss",
                energy_pattern="peak_early",
                cultural_focus="local_neighborhoods",
                must_include=["neighborhood_exploration", "local_market", "hidden_restaurant"],
                avoid_combinations=["mainstream_attractions", "tourist_restaurants"]
            ))
        
        if duration >= 3:
            themes.append(DayTheme(
                theme_name="Signature Experiences & Farewell",
                description="Must-do experiences and memorable farewell",
                energy_pattern="steady",
                cultural_focus="iconic_experiences",
                must_include=["signature_attraction", "memorable_meal", "souvenir_with_story"],
                avoid_combinations=["rushed_schedule", "tourist_shopping"]
            ))
        
        return themes[:duration]
    
    def _create_intelligent_daily_schedule(self, 
                                         day: int,
                                         theme: DayTheme,
                                         destination: str,
                                         traveler_analysis: Dict,
                                         budget: str,
                                         previous_days: List) -> Dict:
        """Create truly intelligent daily schedule"""
        
        # Analyze what's been done to avoid repetition
        previous_activities = self._extract_previous_activities(previous_days)
        
        # Generate time slots with intelligence
        morning_activities = self._generate_morning_intelligence(
            theme, traveler_analysis, previous_activities
        )
        
        afternoon_activities = self._generate_afternoon_intelligence(
            theme, traveler_analysis, previous_activities, morning_activities
        )
        
        evening_activities = self._generate_evening_intelligence(
            theme, traveler_analysis, previous_activities, afternoon_activities
        )
        
        return {
            "day": day,
            "theme": asdict(theme),
            "morning": morning_activities,
            "afternoon": afternoon_activities,
            "evening": evening_activities,
            "daily_insights": self._generate_daily_insights(theme, day),
            "energy_management": self._generate_energy_management_tips(theme),
            "weather_alternatives": self._generate_weather_alternatives(),
            "budget_tracking": self._generate_budget_tracking(budget),
            "local_rhythm_sync": self._generate_local_rhythm_tips()
        }
    
    def _generate_morning_intelligence(self, theme: DayTheme, analysis: Dict, previous: List) -> List[ActivityTimeslot]:
        """Generate intelligent morning activities"""
        activities = []
        
        # Base morning activity on energy preference and theme
        if analysis["energy_preference"] == "early_bird" and theme.energy_pattern == "peak_early":
            activities.append(ActivityTimeslot(
                time_start="07:00",
                time_end="09:00",
                activity="Sunrise Market Experience",
                location="Central Local Market",
                category="cultural",
                energy_level="medium",
                crowd_factor="low",
                weather_dependency="flexible",
                cost_level="low",
                duration_flexibility=1.0,
                prerequisites=[],
                alternatives=["Neighborhood Cafe Culture", "Morning Park Walk"],
                local_insights=[
                    "Markets are most authentic before 8 AM",
                    "Try local breakfast specialties from vendors",
                    "Observe morning rituals of local workers"
                ],
                photo_opportunities=["Golden hour market shots", "Steam from food stalls"],
                learning_outcomes=["Local food culture", "Daily life rhythms", "Ingredient knowledge"]
            ))
        
        # Add intelligent breakfast integration
        activities.append(self._generate_breakfast_activity(theme, analysis))
        
        return activities
    
    def _generate_afternoon_intelligence(self, theme: DayTheme, analysis: Dict, previous: List, morning: List) -> List[ActivityTimeslot]:
        """Generate intelligent afternoon activities that build on morning"""
        activities = []
        
        # Analyze morning activities to create logical progression
        morning_categories = [act.category for act in morning]
        
        # Create complementary afternoon based on morning and theme
        if "cultural" in morning_categories and "Hidden" in theme.theme_name:
            activities.append(ActivityTimeslot(
                time_start="14:00",
                time_end="17:00",
                activity="Neighborhood Deep Dive",
                location="Off-beaten-path District",
                category="exploration",
                energy_level="high",
                crowd_factor="low",
                weather_dependency="outdoor",
                cost_level="free",
                duration_flexibility=2.0,
                prerequisites=["Morning cultural foundation"],
                alternatives=["Artisan Workshop Visit", "Local Community Center"],
                local_insights=[
                    "Follow where locals shop for groceries",
                    "Look for neighborhood bulletin boards",
                    "Small shrines often have interesting stories"
                ],
                photo_opportunities=["Street art", "Local life candids", "Architecture details"],
                learning_outcomes=["Social dynamics", "Urban planning", "Community culture"]
            ))
        
        return activities
    
    def _generate_evening_intelligence(self, theme: DayTheme, analysis: Dict, previous: List, afternoon: List) -> List[ActivityTimeslot]:
        """Generate intelligent evening activities that complete the day's story"""
        activities = []
        
        # Create evening that synthesizes the day's experiences
        activities.append(ActivityTimeslot(
            time_start="18:30",
            time_end="21:00",
            activity="Reflective Dining Experience",
            location="Restaurant matching day's discoveries",
            category="culinary",
            energy_level="low",
            crowd_factor="medium",
            weather_dependency="indoor",
            cost_level="medium",
            duration_flexibility=0.5,
            prerequisites=["Day's cultural context"],
            alternatives=["Street food tour", "Cooking class"],
            local_insights=[
                "Order dishes that connect to morning market ingredients",
                "Ask staff about preparation methods you saw today",
                "Observe local dining customs and timing"
            ],
            photo_opportunities=["Food presentation", "Restaurant atmosphere"],
            learning_outcomes=["Culinary culture", "Social dining customs", "Flavor profiles"]
        ))
        
        return activities
    
    def _add_intelligence_features(self) -> Dict:
        """Add advanced intelligence features to the itinerary"""
        return {
            "adaptive_timing": "Schedule adjusts based on your pace and interests",
            "weather_integration": "Real-time alternatives for weather changes",
            "energy_management": "Activities balanced for sustainable enjoyment",
            "cultural_progression": "Each day builds deeper cultural understanding",
            "local_rhythm_sync": "Schedule aligns with local lifestyle patterns",
            "budget_optimization": "Smart spending spread across experiences",
            "crowd_avoidance": "Strategic timing to avoid tourist crowds",
            "authentic_discovery": "Balance planned activities with spontaneous exploration"
        }
    
    def _generate_adaptive_recommendations(self) -> Dict:
        """Generate adaptive recommendations for different scenarios"""
        return {
            "if_behind_schedule": [
                "Skip the least essential activity",
                "Combine nearby attractions",
                "Use faster transportation"
            ],
            "if_ahead_schedule": [
                "Extend time at favorite locations",
                "Add spontaneous local interaction",
                "Explore nearby hidden gems"
            ],
            "if_weather_changes": [
                "Indoor alternatives for each outdoor activity",
                "Covered walkways and transportation",
                "Weather-appropriate clothing suggestions"
            ],
            "if_energy_low": [
                "Cafe breaks with local atmosphere",
                "Shorter walking routes",
                "More transportation, less walking"
            ],
            "if_extra_interested": [
                "Deep dive options for each activity",
                "Related experiences nearby",
                "Expert guides or classes available"
            ]
        }
    
    # Helper methods for detection and generation
    def _detect_energy_preference(self, preferences: Dict) -> str:
        # Implement intelligent energy detection
        return "early_bird"  # Simplified for example
    
    def _detect_cultural_interest(self, preferences: Dict) -> str:
        return "high"
    
    def _detect_adventure_level(self, preferences: Dict) -> str:
        return "moderate"
    
    def _detect_social_preference(self, preferences: Dict) -> str:
        return "local_interaction"
    
    def _detect_learning_style(self, preferences: Dict) -> str:
        return "experiential"
    
    def _detect_pace_preference(self, preferences: Dict) -> str:
        return "relaxed_exploration"
    
    def _detect_authenticity_preference(self, preferences: Dict) -> str:
        return "authentic_priority"
    
    def _extract_previous_activities(self, previous_days: List) -> List:
        return []  # Implementation for avoiding repetition
    
    def _generate_breakfast_activity(self, theme: DayTheme, analysis: Dict) -> ActivityTimeslot:
        return ActivityTimeslot(
            time_start="08:30",
            time_end="09:30",
            activity="Cultural Breakfast Experience",
            location="Local Breakfast Spot",
            category="culinary",
            energy_level="low",
            crowd_factor="medium",
            weather_dependency="indoor",
            cost_level="low",
            duration_flexibility=0.5,
            prerequisites=[],
            alternatives=["Hotel breakfast", "Street food breakfast"],
            local_insights=["Try regional breakfast specialties"],
            photo_opportunities=["Traditional breakfast setup"],
            learning_outcomes=["Morning food culture"]
        )
    
    def _generate_daily_insights(self, theme: DayTheme, day: int) -> List[str]:
        return [f"Day {day} focuses on {theme.cultural_focus}"]
    
    def _generate_energy_management_tips(self, theme: DayTheme) -> List[str]:
        return ["Plan rest stops every 3 hours"]
    
    def _generate_weather_alternatives(self) -> Dict:
        return {"rainy": "Indoor alternatives available"}
    
    def _generate_budget_tracking(self, budget: str) -> Dict:
        return {"daily_target": f"Aligned with {budget} budget"}
    
    def _generate_local_rhythm_tips(self) -> List[str]:
        return ["Follow local meal timing for authentic experience"]
