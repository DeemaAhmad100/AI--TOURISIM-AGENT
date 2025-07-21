#!/usr/bin/env python3
"""
🎯 Dynamic Activity Intelligence Database
Real-world activity data with contextual intelligence
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import json

@dataclass
class ActivityIntelligence:
    """Intelligent activity with contextual data"""
    name: str
    category: str
    subcategory: str
    duration_min: int
    duration_max: int
    cost_range: Dict[str, int]  # {min: 0, max: 50}
    time_sensitive: bool
    weather_dependent: bool
    crowd_patterns: Dict[str, str]
    energy_required: str  # low, medium, high
    cultural_significance: str
    authenticity_level: str  # tourist, mixed, local
    photo_worthiness: int  # 1-10
    learning_potential: int  # 1-10
    social_interaction: int  # 1-10
    prerequisites: List[str]
    best_combined_with: List[str]
    avoid_combining_with: List[str]
    seasonal_notes: Dict[str, str]
    insider_tips: List[str]
    common_mistakes: List[str]

class DynamicActivityDatabase:
    """Dynamic database of intelligent activities by destination"""
    
    def __init__(self):
        self.activities = self._load_activity_intelligence()
        
    def _load_activity_intelligence(self) -> Dict[str, List[ActivityIntelligence]]:
        """Load comprehensive activity database with real intelligence"""
        
        # This would ideally connect to a real database or API
        # For now, creating intelligent sample data
        
        return {
            "Tokyo": self._get_tokyo_activities(),
            "Paris": self._get_paris_activities(),
            "Istanbul": self._get_istanbul_activities(),
            "Bangkok": self._get_bangkok_activities(),
            "New York": self._get_newyork_activities(),
            # Add more destinations as needed
        }
    
    def _get_tokyo_activities(self) -> List[ActivityIntelligence]:
        """Tokyo-specific intelligent activities"""
        return [
            ActivityIntelligence(
                name="Tsukiji Outer Market Food Tour",
                category="culinary",
                subcategory="street_food",
                duration_min=120,
                duration_max=180,
                cost_range={"min": 15, "max": 35},
                time_sensitive=True,  # Best early morning
                weather_dependent=False,
                crowd_patterns={
                    "peak": "06:00-09:00",
                    "moderate": "09:00-11:00",
                    "low": "after 11:00"
                },
                energy_required="medium",
                cultural_significance="High - Heart of Tokyo's food culture",
                authenticity_level="mixed",
                photo_worthiness=9,
                learning_potential=9,
                social_interaction=7,
                prerequisites=["empty_stomach", "cash_only"],
                best_combined_with=["nearby_temple_visit", "ginza_walk"],
                avoid_combining_with=["heavy_breakfast", "afternoon_food_tour"],
                seasonal_notes={
                    "winter": "Warm foods especially comforting",
                    "summer": "Early morning visit essential for comfort"
                },
                insider_tips=[
                    "Arrive by 6 AM for freshest selection",
                    "Follow the lines - locals know best",
                    "Try uni (sea urchin) from Yamacho stall",
                    "Bring cash - most vendors don't accept cards"
                ],
                common_mistakes=[
                    "Going after 10 AM when best items are sold out",
                    "Not bringing enough cash",
                    "Filling up too early and missing other stalls"
                ]
            ),
            
            ActivityIntelligence(
                name="Traditional Sento (Public Bath) Experience",
                category="cultural",
                subcategory="wellness",
                duration_min=90,
                duration_max=150,
                cost_range={"min": 5, "max": 15},
                time_sensitive=False,
                weather_dependent=False,
                crowd_patterns={
                    "peak": "18:00-20:00",
                    "moderate": "15:00-18:00",
                    "low": "10:00-15:00"
                },
                energy_required="low",
                cultural_significance="Very High - Traditional Japanese wellness",
                authenticity_level="local",
                photo_worthiness=3,  # No photos allowed inside
                learning_potential=8,
                social_interaction=6,
                prerequisites=["basic_etiquette_knowledge", "towel_rental"],
                best_combined_with=["temple_visit", "traditional_meal"],
                avoid_combining_with=["heavy_physical_activity", "tight_schedule"],
                seasonal_notes={
                    "winter": "Perfect for warming up",
                    "summer": "Cool down after hot day exploring"
                },
                insider_tips=[
                    "Wash thoroughly before entering communal bath",
                    "Bring your own small towel",
                    "Observe and copy locals' behavior",
                    "Don't bring phone/camera into bathing area"
                ],
                common_mistakes=[
                    "Not washing before entering bath",
                    "Bringing soap into the bath",
                    "Taking photos inside",
                    "Being too loud or disruptive"
                ]
            ),
            
            ActivityIntelligence(
                name="Shibuya Sky Observation Deck",
                category="sightseeing",
                subcategory="city_views",
                duration_min=45,
                duration_max=90,
                cost_range={"min": 20, "max": 20},
                time_sensitive=True,  # Best at sunset
                weather_dependent=True,
                crowd_patterns={
                    "peak": "17:00-19:00 (sunset)",
                    "moderate": "14:00-17:00",
                    "low": "10:00-14:00"
                },
                energy_required="low",
                cultural_significance="Medium - Modern Tokyo perspective",
                authenticity_level="tourist",
                photo_worthiness=10,
                learning_potential=5,
                social_interaction=3,
                prerequisites=["advance_booking_recommended"],
                best_combined_with=["shibuya_crossing", "harajuku_exploration"],
                avoid_combining_with=["other_observation_decks_same_day"],
                seasonal_notes={
                    "winter": "Clear air often provides best views",
                    "spring": "Cherry blossom season adds beauty",
                    "summer": "Hazy conditions may limit visibility"
                },
                insider_tips=[
                    "Book sunset slots well in advance",
                    "Check weather forecast before booking",
                    "Visit Shibuya Crossing first to understand the view",
                    "Golden hour provides best photos"
                ],
                common_mistakes=[
                    "Not checking weather conditions",
                    "Booking during cloudy periods",
                    "Rushing the experience",
                    "Not exploring Shibuya area afterwards"
                ]
            )
        ]
    
    def _get_paris_activities(self) -> List[ActivityIntelligence]:
        """Paris-specific intelligent activities"""
        return [
            ActivityIntelligence(
                name="Marché des Enfants Rouges Market Experience",
                category="culinary",
                subcategory="local_market",
                duration_min=90,
                duration_max=150,
                cost_range={"min": 12, "max": 25},
                time_sensitive=True,
                weather_dependent=False,
                crowd_patterns={
                    "peak": "12:00-14:00",
                    "moderate": "10:00-12:00",
                    "low": "15:00-17:00"
                },
                energy_required="medium",
                cultural_significance="High - Oldest covered market in Paris",
                authenticity_level="local",
                photo_worthiness=8,
                learning_potential=7,
                social_interaction=8,
                prerequisites=["basic_french_phrases_helpful"],
                best_combined_with=["le_marais_walking_tour", "jewish_quarter_exploration"],
                avoid_combining_with=["other_food_markets_same_day"],
                seasonal_notes={
                    "winter": "Cozy covered atmosphere perfect for cold days",
                    "summer": "Fresh produce at peak quality"
                },
                insider_tips=[
                    "Try L'Estaminet for Moroccan cuisine",
                    "Visit Japanese vendor for authentic bento",
                    "Sample before buying at produce stalls",
                    "Lunch crowds indicate quality"
                ],
                common_mistakes=[
                    "Going on Monday when some stalls are closed",
                    "Not bringing reusable bags",
                    "Eating too much at first stall"
                ]
            ),
            
            ActivityIntelligence(
                name="Seine Walking Path Hidden Sections",
                category="exploration",
                subcategory="urban_discovery",
                duration_min=120,
                duration_max=240,
                cost_range={"min": 0, "max": 0},
                time_sensitive=False,
                weather_dependent=True,
                crowd_patterns={
                    "peak": "never_really_crowded",
                    "moderate": "weekends",
                    "low": "weekday_mornings"
                },
                energy_required="medium",
                cultural_significance="Medium - Modern Parisian urban planning",
                authenticity_level="local",
                photo_worthiness=7,
                learning_potential=6,
                social_interaction=4,
                prerequisites=["comfortable_walking_shoes"],
                best_combined_with=["riverside_picnic", "bridge_architecture_study"],
                avoid_combining_with=["rainy_weather", "tight_timeline"],
                seasonal_notes={
                    "spring": "Perfect weather and blooming trees",
                    "autumn": "Beautiful colors along the path",
                    "winter": "Peaceful but can be cold and wet"
                },
                insider_tips=[
                    "Start at Parc Rives de Seine",
                    "Download Paris walking app for route guidance",
                    "Bring snacks for impromptu picnic spots",
                    "Look for floating gardens and urban art"
                ],
                common_mistakes=[
                    "Not checking weather before starting",
                    "Wearing inappropriate shoes",
                    "Not bringing water for longer walks"
                ]
            )
        ]
    
    def get_activities_by_criteria(self, 
                                  destination: str,
                                  criteria: Dict[str, Any]) -> List[ActivityIntelligence]:
        """Get activities matching specific intelligent criteria"""
        
        if destination not in self.activities:
            return []
        
        activities = self.activities[destination]
        filtered = []
        
        for activity in activities:
            if self._matches_criteria(activity, criteria):
                filtered.append(activity)
        
        return filtered
    
    def _matches_criteria(self, activity: ActivityIntelligence, criteria: Dict) -> bool:
        """Check if activity matches intelligent criteria"""
        
        # Energy level matching
        if "energy_level" in criteria:
            if activity.energy_required != criteria["energy_level"]:
                return False
        
        # Budget matching
        if "budget_max" in criteria:
            if activity.cost_range["min"] > criteria["budget_max"]:
                return False
        
        # Weather dependency
        if "weather_dependent" in criteria:
            if activity.weather_dependent != criteria["weather_dependent"]:
                return False
        
        # Category matching
        if "categories" in criteria:
            if activity.category not in criteria["categories"]:
                return False
        
        # Authenticity level
        if "authenticity_min" in criteria:
            authenticity_scores = {"tourist": 1, "mixed": 2, "local": 3}
            if authenticity_scores[activity.authenticity_level] < criteria["authenticity_min"]:
                return False
        
        return True
    
    def get_complementary_activities(self, 
                                   base_activity: ActivityIntelligence,
                                   destination: str) -> List[ActivityIntelligence]:
        """Get activities that complement the base activity"""
        
        if destination not in self.activities:
            return []
        
        complementary = []
        
        for activity in self.activities[destination]:
            if activity.name in base_activity.best_combined_with:
                complementary.append(activity)
        
        return complementary
    
    def get_weather_alternatives(self, 
                               original_activities: List[ActivityIntelligence],
                               destination: str,
                               weather_condition: str) -> List[ActivityIntelligence]:
        """Get weather-appropriate alternatives"""
        
        if destination not in self.activities:
            return []
        
        alternatives = []
        
        weather_criteria = {
            "rainy": {"weather_dependent": False},
            "sunny": {"weather_dependent": True},
            "hot": {"energy_level": "low"},
            "cold": {"weather_dependent": False}
        }
        
        criteria = weather_criteria.get(weather_condition, {})
        
        for activity in self.activities[destination]:
            if self._matches_criteria(activity, criteria):
                # Avoid suggesting the same activities
                if activity not in original_activities:
                    alternatives.append(activity)
        
        return alternatives[:3]  # Top 3 alternatives
    
    # Simplified implementations for other destinations
    def _get_istanbul_activities(self) -> List[ActivityIntelligence]:
        return []  # Implement with Istanbul-specific activities
    
    def _get_bangkok_activities(self) -> List[ActivityIntelligence]:
        return []  # Implement with Bangkok-specific activities
    
    def _get_newyork_activities(self) -> List[ActivityIntelligence]:
        return []  # Implement with New York-specific activities
