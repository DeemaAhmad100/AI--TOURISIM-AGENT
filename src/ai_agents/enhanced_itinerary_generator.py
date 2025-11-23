"""
Enhanced Daily Itinerary Generation System
Leverages Supabase activities table for hyper-personalized itineraries
"""

import random
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import json

class EnhancedItineraryGenerator:
    """
    Hyper-personalized daily itinerary generator that leverages:
    - Supabase activities table
    - User profile analysis
    - Contextual day progression
    - Activity diversity optimization
    """
    
    def __init__(self, supabase_client=None):
        """Initialize with Supabase client for database access"""
        self.supabase = supabase_client
        self.activity_cache = {}
        
    def generate_intelligent_daily_itinerary(self, destination: str, duration: int, 
                                           profile: Dict, user_prompt: str, 
                                           package_style: str) -> List[Dict]:
        """
        Generate highly detailed, context-aware daily itinerary
        
        Args:
            destination: Target destination
            duration: Trip duration in days
            profile: User profile with preferences
            user_prompt: User's dream trip description
            package_style: Travel style (cultural, adventure, luxury, etc.)
            
        Returns:
            List of detailed daily plans
        """
        
        # Get destination-specific activities from database
        destination_activities = self._fetch_destination_activities(destination)
        
        # Analyze user preferences and interests
        user_interests = self._analyze_user_interests(profile, user_prompt)
        
        # Create day-by-day progression strategy
        itinerary_strategy = self._create_itinerary_strategy(duration, user_interests, package_style)
        
        # Generate each day with context awareness
        daily_itinerary = []
        used_activities = set()  # Track to avoid repetition
        
        for day in range(1, duration + 1):
            day_plan = self._generate_contextual_day_plan(
                day=day,
                total_duration=duration,
                destination=destination,
                activities_pool=destination_activities,
                user_interests=user_interests,
                strategy=itinerary_strategy[day-1],
                used_activities=used_activities,
                profile=profile,
                package_style=package_style
            )
            
            # Update used activities to ensure variety
            self._update_used_activities(day_plan, used_activities)
            daily_itinerary.append(day_plan)
            
        return daily_itinerary
    
    def _fetch_destination_activities(self, destination: str) -> List[Dict]:
        """Fetch activities from Supabase activities table"""
        if not self.supabase:
            return self._get_fallback_activities(destination)
            
        try:
            # Query activities table for destination
            result = self.supabase.table("activities").select("""
                id, name, description, category, duration_hours, price_range,
                difficulty_level, best_time_of_day, season_availability,
                age_suitability, group_size_max, booking_required,
                location_details, cultural_significance, insider_tips,
                photo_opportunities, accessibility_features
            """).eq("destination", destination).execute()
            
            if result.data:
                return result.data
            else:
                # Fallback to hardcoded data if no DB data
                return self._get_fallback_activities(destination)
                
        except Exception as e:
            print(f"Database query failed: {e}")
            return self._get_fallback_activities(destination)
    
    def _get_fallback_activities(self, destination: str) -> List[Dict]:
        """Fallback activities when database is unavailable"""
        fallback_activities = {
            "Paris, France": [
                {
                    "name": "Louvre Museum Private Tour",
                    "category": "cultural",
                    "duration_hours": 3,
                    "best_time_of_day": "morning",
                    "cultural_significance": "World's largest art museum",
                    "insider_tips": "Book skip-the-line tickets in advance",
                    "price_range": "€25-45"
                },
                {
                    "name": "Seine River Photography Walk",
                    "category": "photography",
                    "duration_hours": 2,
                    "best_time_of_day": "evening",
                    "cultural_significance": "Historic riverbank views",
                    "insider_tips": "Golden hour lighting is spectacular",
                    "price_range": "Free"
                },
                {
                    "name": "Montmartre Artist Quarter Exploration",
                    "category": "cultural",
                    "duration_hours": 4,
                    "best_time_of_day": "afternoon",
                    "cultural_significance": "Historic artist community",
                    "insider_tips": "Visit local artist studios",
                    "price_range": "€15-30"
                },
                {
                    "name": "French Cooking Class Experience",
                    "category": "culinary",
                    "duration_hours": 4,
                    "best_time_of_day": "afternoon",
                    "cultural_significance": "Traditional French cuisine",
                    "insider_tips": "Learn market shopping first",
                    "price_range": "€85-120"
                }
            ],
            "Dubai, UAE": [
                {
                    "name": "Desert Conservation Reserve Safari",
                    "category": "adventure",
                    "duration_hours": 6,
                    "best_time_of_day": "morning",
                    "cultural_significance": "Traditional Emirati desert life",
                    "insider_tips": "Early morning for wildlife viewing",
                    "price_range": "$95-150"
                },
                {
                    "name": "Traditional Souk Cultural Walk",
                    "category": "cultural",
                    "duration_hours": 3,
                    "best_time_of_day": "evening",
                    "cultural_significance": "Historic trading traditions",
                    "insider_tips": "Practice negotiation skills",
                    "price_range": "$25-40"
                }
            ]
        }
        
        return fallback_activities.get(destination, [])
    
    def _analyze_user_interests(self, profile: Dict, user_prompt: str) -> Dict:
        """Analyze user interests from profile and prompt"""
        interests = profile.get('interests', [])
        
        # Extract interests from user prompt
        prompt_interests = []
        interest_keywords = {
            'cultural': ['culture', 'museum', 'history', 'heritage', 'traditional'],
            'culinary': ['food', 'cuisine', 'cooking', 'restaurant', 'local dishes'],
            'photography': ['photo', 'camera', 'instagram', 'scenic', 'views'],
            'adventure': ['adventure', 'outdoor', 'hiking', 'sports', 'active'],
            'luxury': ['luxury', 'premium', 'exclusive', 'high-end', 'spa'],
            'nightlife': ['nightlife', 'bars', 'clubs', 'entertainment', 'evening'],
            'shopping': ['shopping', 'markets', 'souvenirs', 'boutiques', 'local crafts'],
            'nature': ['nature', 'parks', 'gardens', 'wildlife', 'natural']
        }
        
        user_prompt_lower = user_prompt.lower()
        for category, keywords in interest_keywords.items():
            if any(keyword in user_prompt_lower for keyword in keywords):
                prompt_interests.append(category)
        
        # Combine profile interests with prompt-derived interests
        all_interests = list(set(interests + prompt_interests))
        
        return {
            'primary_interests': all_interests[:3],  # Top 3 interests
            'secondary_interests': all_interests[3:6],  # Secondary interests
            'travel_style': profile.get('travel_style', 'cultural explorer'),
            'pace_preference': profile.get('pace_preference', 'moderate'),
            'budget_preference': profile.get('budget_preference', 'moderate')
        }
    
    def _create_itinerary_strategy(self, duration: int, user_interests: Dict, 
                                 package_style: str) -> List[Dict]:
        """Create day-by-day strategy ensuring variety and progression"""
        strategies = []
        
        # Day 1: Always arrival and orientation
        strategies.append({
            'theme': 'Arrival & Cultural Orientation',
            'energy_level': 'low',
            'focus': 'orientation',
            'activity_types': ['cultural', 'local_orientation'],
            'avoid_intensive': True
        })
        
        # Middle days: Mix based on interests and duration
        for day in range(2, duration):
            if day == 2:
                # Second day: Dive into primary interest
                primary_interest = user_interests['primary_interests'][0] if user_interests['primary_interests'] else 'cultural'
                strategies.append({
                    'theme': f'{primary_interest.title()} Deep Dive',
                    'energy_level': 'high',
                    'focus': primary_interest,
                    'activity_types': [primary_interest, 'cultural'],
                    'avoid_intensive': False
                })
            elif day % 3 == 0:
                # Every third day: Relaxed local experiences
                strategies.append({
                    'theme': 'Local Life & Hidden Gems',
                    'energy_level': 'moderate',
                    'focus': 'local_experiences',
                    'activity_types': ['local_experiences', 'culinary'],
                    'avoid_intensive': False
                })
            else:
                # Rotate through interests
                interest_idx = (day - 2) % len(user_interests['primary_interests']) if user_interests['primary_interests'] else 0
                interest = user_interests['primary_interests'][interest_idx] if user_interests['primary_interests'] else 'cultural'
                strategies.append({
                    'theme': f'{interest.title()} Adventures',
                    'energy_level': 'high',
                    'focus': interest,
                    'activity_types': [interest, 'adventure'],
                    'avoid_intensive': False
                })
        
        # Last day: Farewell and shopping/souvenirs
        if duration > 1:
            strategies.append({
                'theme': 'Farewell & Final Discoveries',
                'energy_level': 'moderate',
                'focus': 'shopping',
                'activity_types': ['shopping', 'cultural', 'souvenirs'],
                'avoid_intensive': True
            })
        
        return strategies
    
    def _generate_contextual_day_plan(self, day: int, total_duration: int, 
                                    destination: str, activities_pool: List[Dict],
                                    user_interests: Dict, strategy: Dict,
                                    used_activities: set, profile: Dict,
                                    package_style: str) -> Dict:
        """Generate a single day's detailed plan with context awareness"""
        
        # Filter activities based on day strategy
        relevant_activities = self._filter_activities_for_strategy(
            activities_pool, strategy, used_activities
        )
        
        # Generate time-slot specific activities
        morning_activity = self._select_activity_for_time(
            relevant_activities, 'morning', strategy, used_activities
        )
        
        afternoon_activity = self._select_activity_for_time(
            relevant_activities, 'afternoon', strategy, used_activities
        )
        
        evening_activity = self._select_activity_for_time(
            relevant_activities, 'evening', strategy, used_activities
        )
        
        # Generate contextual meals
        meals = self._generate_contextual_meals(
            day, destination, morning_activity, afternoon_activity, profile
        )
        
        # Calculate transportation and logistics
        transportation = self._calculate_transportation(
            morning_activity, afternoon_activity, evening_activity, destination
        )
        
        # Estimate realistic costs
        estimated_cost = self._calculate_realistic_daily_cost(
            morning_activity, afternoon_activity, evening_activity, meals, transportation, profile
        )
        
        return {
            'day': day,
            'theme': strategy['theme'],
            'morning': {
                'activity': morning_activity['name'] if morning_activity else 'Flexible morning exploration',
                'details': morning_activity.get('description', 'Self-guided exploration'),
                'duration': morning_activity.get('duration_hours', 2),
                'insider_tip': morning_activity.get('insider_tips', 'Take your time to absorb the atmosphere'),
                'cultural_context': morning_activity.get('cultural_significance', 'Local cultural immersion'),
                'estimated_cost': morning_activity.get('price_range', '$20-40'),
                'location_details': morning_activity.get('location_details', f'{destination} city center')
            },
            'afternoon': {
                'activity': afternoon_activity['name'] if afternoon_activity else 'Afternoon discovery time',
                'details': afternoon_activity.get('description', 'Personal exploration'),
                'duration': afternoon_activity.get('duration_hours', 3),
                'insider_tip': afternoon_activity.get('insider_tips', 'Connect with locals for authentic experiences'),
                'cultural_context': afternoon_activity.get('cultural_significance', 'Cultural understanding'),
                'estimated_cost': afternoon_activity.get('price_range', '$30-60'),
                'location_details': afternoon_activity.get('location_details', f'{destination} main district')
            },
            'evening': {
                'activity': evening_activity['name'] if evening_activity else 'Evening cultural immersion',
                'details': evening_activity.get('description', 'Local evening experiences'),
                'duration': evening_activity.get('duration_hours', 2),
                'insider_tip': evening_activity.get('insider_tips', 'Evening is perfect for local interactions'),
                'cultural_context': evening_activity.get('cultural_significance', 'Evening cultural practices'),
                'estimated_cost': evening_activity.get('price_range', '$25-50'),
                'location_details': evening_activity.get('location_details', f'{destination} evening district')
            },
            'meals': meals,
            'transportation': transportation,
            'estimated_cost': estimated_cost,
            'travel_tips': self._generate_daily_travel_tips(day, total_duration, destination, strategy),
            'packing_suggestions': self._generate_packing_suggestions(morning_activity, afternoon_activity, evening_activity),
            'photography_opportunities': self._identify_photography_opportunities(morning_activity, afternoon_activity, evening_activity),
            'cultural_etiquette': self._get_cultural_etiquette_tips(destination, strategy['focus'])
        }
    
    def _filter_activities_for_strategy(self, activities: List[Dict], 
                                      strategy: Dict, used_activities: set) -> List[Dict]:
        """Filter activities based on day strategy and usage"""
        relevant_activities = []
        
        for activity in activities:
            # Skip if already used
            if activity.get('name') in used_activities:
                continue
                
            # Check if activity matches strategy focus
            activity_category = activity.get('category', '').lower()
            if activity_category in strategy.get('activity_types', []):
                relevant_activities.append(activity)
            elif strategy.get('focus') in activity_category:
                relevant_activities.append(activity)
                
        return relevant_activities
    
    def _select_activity_for_time(self, activities: List[Dict], time_slot: str,
                                strategy: Dict, used_activities: set) -> Optional[Dict]:
        """Select best activity for specific time slot"""
        suitable_activities = []
        
        for activity in activities:
            best_time = activity.get('best_time_of_day', '').lower()
            if best_time == time_slot or best_time == 'any':
                suitable_activities.append(activity)
        
        # If no time-specific activities, select from general pool
        if not suitable_activities and activities:
            suitable_activities = activities[:3]  # Take first 3 as options
            
        # Select based on strategy energy level and focus
        if suitable_activities:
            # Prioritize based on strategy focus
            for activity in suitable_activities:
                if strategy['focus'] in activity.get('category', '').lower():
                    return activity
            # Return first suitable if no perfect match
            return suitable_activities[0]
            
        return None
    
    def _generate_contextual_meals(self, day: int, destination: str, 
                                 morning_activity: Dict, afternoon_activity: Dict,
                                 profile: Dict) -> Dict:
        """Generate contextual meal recommendations"""
        dietary_restrictions = profile.get('dietary_restrictions', [])
        
        # Context-aware meal selection
        breakfast_context = "hotel" if day == 1 else "local café"
        lunch_context = "near activity location" if afternoon_activity else "city center"
        dinner_context = "traditional restaurant" if day <= 2 else "local recommendation"
        
        return {
            'breakfast': f'{breakfast_context.title()} breakfast - local specialties with {dietary_restrictions[0] if dietary_restrictions else "standard"} options',
            'lunch': f'{lunch_context.title()} lunch featuring regional cuisine',
            'dinner': f'{dinner_context.title()} dinner with authentic {destination.split(",")[0]} flavors',
            'dietary_accommodations': dietary_restrictions,
            'local_specialties': self._get_local_food_specialties(destination)
        }
    
    def _calculate_transportation(self, morning: Dict, afternoon: Dict, 
                                evening: Dict, destination: str) -> Dict:
        """Calculate realistic transportation between activities"""
        base_transport = "Walking + Metro" if "Paris" in destination else "Taxi + Local Transport"
        
        return {
            'primary_method': base_transport,
            'estimated_time_between_activities': '15-30 minutes',
            'daily_transport_cost': '$15-25',
            'transport_tips': f'Use local transport apps for {destination}',
            'walking_distance': 'Moderate walking required between some activities'
        }
    
    def _calculate_realistic_daily_cost(self, morning: Dict, afternoon: Dict,
                                      evening: Dict, meals: Dict, 
                                      transportation: Dict, profile: Dict) -> int:
        """Calculate realistic daily cost based on activities and budget"""
        base_cost = 120  # Base daily cost
        
        # Activity costs
        activity_cost = 0
        for activity in [morning, afternoon, evening]:
            if activity:
                price_range = activity.get('price_range', '$20-40')
                # Extract average cost from price range
                if '$' in price_range:
                    prices = [int(x) for x in price_range.replace('$', '').replace('€', '').split('-')]
                    activity_cost += sum(prices) / len(prices) if prices else 30
        
        # Enhanced budget adjustment for 6-tier system
        budget_multiplier = {
            'ultra_budget': 0.5,    # 50% of base cost - hostels, street food
            'budget': 0.7,          # 70% of base cost - budget hotels, local food
            'moderate': 1.0,        # 100% base cost - mid-range everything
            'premium': 1.4,         # 140% of base cost - 4-star hotels, fine dining
            'luxury': 1.8,          # 180% of base cost - 5-star resorts, exclusive
            'ultra_luxury': 2.5     # 250% of base cost - private jets, presidential suites
        }.get(profile.get('budget_preference', 'moderate'), 1.0)
        
        total_cost = (base_cost + activity_cost) * budget_multiplier
        return int(total_cost)
    
    def _generate_daily_travel_tips(self, day: int, total_duration: int,
                                  destination: str, strategy: Dict) -> List[str]:
        """Generate contextual daily travel tips"""
        tips = []
        
        if day == 1:
            tips.extend([
                "Start with orientation walk to get your bearings",
                "Keep important documents accessible",
                "Stay hydrated and don't over-schedule first day"
            ])
        elif day == total_duration:
            tips.extend([
                "Confirm departure logistics the night before",
                "Allow extra time for last-minute shopping",
                "Take final photos at favorite locations"
            ])
        else:
            tips.extend([
                f"Focus on {strategy['focus']} experiences today",
                "Engage with locals for authentic insights", 
                "Document your experiences in a travel journal"
            ])
            
        return tips
    
    def _generate_packing_suggestions(self, morning: Dict, afternoon: Dict, 
                                    evening: Dict) -> List[str]:
        """Generate activity-specific packing suggestions"""
        suggestions = ["Comfortable walking shoes", "Weather-appropriate clothing"]
        
        activities = [morning, afternoon, evening]
        for activity in activities:
            if activity:
                category = activity.get('category', '').lower()
                if 'outdoor' in category or 'adventure' in category:
                    suggestions.append("Sunscreen and hat")
                elif 'cultural' in category:
                    suggestions.append("Respectful attire for cultural sites")
                elif 'culinary' in category:
                    suggestions.append("Appetite and openness to try new foods")
                    
        return list(set(suggestions))  # Remove duplicates
    
    def _identify_photography_opportunities(self, morning: Dict, afternoon: Dict,
                                          evening: Dict) -> List[str]:
        """Identify best photography opportunities for the day"""
        opportunities = []
        
        activities = [
            (morning, "Morning golden light"),
            (afternoon, "Afternoon clarity"), 
            (evening, "Evening atmosphere")
        ]
        
        for activity, time_note in activities:
            if activity:
                if activity.get('photo_opportunities'):
                    opportunities.append(f"{activity['name']}: {time_note}")
                elif 'cultural' in activity.get('category', '').lower():
                    opportunities.append(f"Architectural details at {activity['name']}")
                    
        return opportunities
    
    def _get_cultural_etiquette_tips(self, destination: str, focus: str) -> List[str]:
        """Get cultural etiquette tips for destination and focus"""
        etiquette_db = {
            "Paris, France": [
                "Greet with 'Bonjour' when entering shops",
                "Dress elegantly, especially for dinner",
                "Keep voices low in public spaces"
            ],
            "Dubai, UAE": [
                "Dress modestly, especially at cultural sites",
                "Use right hand for greetings and eating",
                "Respect prayer times and local customs"
            ]
        }
        
        base_tips = etiquette_db.get(destination, ["Respect local customs", "Be culturally sensitive"])
        
        # Add focus-specific tips
        if focus == 'culinary':
            base_tips.append("Ask about ingredients for dietary restrictions")
        elif focus == 'cultural':
            base_tips.append("Ask permission before photographing people")
            
        return base_tips
    
    def _get_local_food_specialties(self, destination: str) -> List[str]:
        """Get local food specialties for destination"""
        specialties = {
            "Paris, France": ["Croissants", "Coq au vin", "French cheese", "Macarons"],
            "Dubai, UAE": ["Shawarma", "Hummus", "Dates", "Arabic coffee"],
            "Beirut, Lebanon": ["Hummus", "Tabbouleh", "Kibbeh", "Baklava"]
        }
        
        return specialties.get(destination, ["Local specialties", "Regional dishes"])
    
    def _update_used_activities(self, day_plan: Dict, used_activities: set):
        """Update set of used activities to avoid repetition"""
        time_slots = ['morning', 'afternoon', 'evening']
        for slot in time_slots:
            activity_info = day_plan.get(slot, {})
            if isinstance(activity_info, dict) and 'activity' in activity_info:
                used_activities.add(activity_info['activity'])