"""
🧠 Conversation Memory System
Advanced memory management for personalized user experiences across sessions
"""

import json
import sqlite3
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass
class UserPreferences:
    """User preference data structure"""
    user_id: str
    travel_style: str = ""
    budget_preference: str = ""
    activity_preferences: List[str] = None
    dietary_restrictions: List[str] = None
    accommodation_preferences: Dict[str, Any] = None
    cultural_interests: List[str] = None
    travel_pace: str = ""  # fast, moderate, slow
    group_dynamics: str = ""  # solo, couple, family, friends
    past_destinations: List[str] = None
    preferred_seasons: List[str] = None
    language_preferences: List[str] = None
    accessibility_needs: List[str] = None
    created_at: str = ""
    updated_at: str = ""
    
    def __post_init__(self):
        if self.activity_preferences is None:
            self.activity_preferences = []
        if self.dietary_restrictions is None:
            self.dietary_restrictions = []
        if self.accommodation_preferences is None:
            self.accommodation_preferences = {}
        if self.cultural_interests is None:
            self.cultural_interests = []
        if self.past_destinations is None:
            self.past_destinations = []
        if self.preferred_seasons is None:
            self.preferred_seasons = []
        if self.language_preferences is None:
            self.language_preferences = []
        if self.accessibility_needs is None:
            self.accessibility_needs = []

@dataclass 
class ConversationContext:
    """Conversation context data structure"""
    session_id: str
    user_id: str
    conversation_history: List[Dict[str, Any]] = None
    current_query: str = ""
    extracted_preferences: Dict[str, Any] = None
    agent_insights: Dict[str, Any] = None
    package_feedback: List[Dict[str, Any]] = None
    session_start: str = ""
    last_interaction: str = ""
    
    def __post_init__(self):
        if self.conversation_history is None:
            self.conversation_history = []
        if self.extracted_preferences is None:
            self.extracted_preferences = {}
        if self.agent_insights is None:
            self.agent_insights = {}
        if self.package_feedback is None:
            self.package_feedback = []

class ConversationMemoryManager:
    """Advanced conversation memory management system"""
    
    def __init__(self, db_path: str = "user_memory.db"):
        self.db_path = Path(db_path)
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database for memory storage"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # User preferences table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_preferences (
                    user_id TEXT PRIMARY KEY,
                    travel_style TEXT,
                    budget_preference TEXT,
                    activity_preferences TEXT,
                    dietary_restrictions TEXT,
                    accommodation_preferences TEXT,
                    cultural_interests TEXT,
                    travel_pace TEXT,
                    group_dynamics TEXT,
                    past_destinations TEXT,
                    preferred_seasons TEXT,
                    language_preferences TEXT,
                    accessibility_needs TEXT,
                    created_at TEXT,
                    updated_at TEXT
                )
            """)
            
            # Conversation contexts table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS conversation_contexts (
                    session_id TEXT PRIMARY KEY,
                    user_id TEXT,
                    conversation_history TEXT,
                    current_query TEXT,
                    extracted_preferences TEXT,
                    agent_insights TEXT,
                    package_feedback TEXT,
                    session_start TEXT,
                    last_interaction TEXT,
                    FOREIGN KEY (user_id) REFERENCES user_preferences (user_id)
                )
            """)
            
            # User interaction patterns table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS interaction_patterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    interaction_type TEXT,
                    data TEXT,
                    timestamp TEXT,
                    FOREIGN KEY (user_id) REFERENCES user_preferences (user_id)
                )
            """)
            
            conn.commit()
    
    def generate_user_id(self, session_data: Dict[str, Any]) -> str:
        """Generate consistent user ID from session data"""
        # Create hash from IP, browser fingerprint, or login info
        identifier = f"{session_data.get('ip', 'anonymous')}_{session_data.get('browser', 'unknown')}"
        return hashlib.md5(identifier.encode()).hexdigest()[:16]
    
    def get_user_preferences(self, user_id: str) -> Optional[UserPreferences]:
        """Retrieve user preferences from memory"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user_preferences WHERE user_id = ?", (user_id,))
            row = cursor.fetchone()
            
            if row:
                return UserPreferences(
                    user_id=row[0],
                    travel_style=row[1],
                    budget_preference=row[2],
                    activity_preferences=json.loads(row[3]) if row[3] else [],
                    dietary_restrictions=json.loads(row[4]) if row[4] else [],
                    accommodation_preferences=json.loads(row[5]) if row[5] else {},
                    cultural_interests=json.loads(row[6]) if row[6] else [],
                    travel_pace=row[7],
                    group_dynamics=row[8],
                    past_destinations=json.loads(row[9]) if row[9] else [],
                    preferred_seasons=json.loads(row[10]) if row[10] else [],
                    language_preferences=json.loads(row[11]) if row[11] else [],
                    accessibility_needs=json.loads(row[12]) if row[12] else [],
                    created_at=row[13],
                    updated_at=row[14]
                )
        return None
    
    def save_user_preferences(self, preferences: UserPreferences):
        """Save or update user preferences"""
        preferences.updated_at = datetime.now().isoformat()
        if not preferences.created_at:
            preferences.created_at = preferences.updated_at
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO user_preferences VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                preferences.user_id,
                preferences.travel_style,
                preferences.budget_preference,
                json.dumps(preferences.activity_preferences),
                json.dumps(preferences.dietary_restrictions),
                json.dumps(preferences.accommodation_preferences),
                json.dumps(preferences.cultural_interests),
                preferences.travel_pace,
                preferences.group_dynamics,
                json.dumps(preferences.past_destinations),
                json.dumps(preferences.preferred_seasons),
                json.dumps(preferences.language_preferences),
                json.dumps(preferences.accessibility_needs),
                preferences.created_at,
                preferences.updated_at
            ))
            conn.commit()
    
    def get_conversation_context(self, session_id: str) -> Optional[ConversationContext]:
        """Retrieve conversation context"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM conversation_contexts WHERE session_id = ?", (session_id,))
            row = cursor.fetchone()
            
            if row:
                return ConversationContext(
                    session_id=row[0],
                    user_id=row[1],
                    conversation_history=json.loads(row[2]) if row[2] else [],
                    current_query=row[3],
                    extracted_preferences=json.loads(row[4]) if row[4] else {},
                    agent_insights=json.loads(row[5]) if row[5] else {},
                    package_feedback=json.loads(row[6]) if row[6] else [],
                    session_start=row[7],
                    last_interaction=row[8]
                )
        return None
    
    def save_conversation_context(self, context: ConversationContext):
        """Save conversation context"""
        context.last_interaction = datetime.now().isoformat()
        if not context.session_start:
            context.session_start = context.last_interaction
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO conversation_contexts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                context.session_id,
                context.user_id,
                json.dumps(context.conversation_history),
                context.current_query,
                json.dumps(context.extracted_preferences),
                json.dumps(context.agent_insights),
                json.dumps(context.package_feedback),
                context.session_start,
                context.last_interaction
            ))
            conn.commit()
    
    def add_interaction(self, user_id: str, interaction_type: str, data: Dict[str, Any]):
        """Record user interaction for pattern analysis"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO interaction_patterns (user_id, interaction_type, data, timestamp) 
                VALUES (?, ?, ?, ?)
            """, (
                user_id,
                interaction_type,
                json.dumps(data),
                datetime.now().isoformat()
            ))
            conn.commit()
    
    def get_interaction_patterns(self, user_id: str, days: int = 30) -> List[Dict[str, Any]]:
        """Get user interaction patterns for analysis"""
        cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT interaction_type, data, timestamp FROM interaction_patterns 
                WHERE user_id = ? AND timestamp > ? 
                ORDER BY timestamp DESC
            """, (user_id, cutoff_date))
            
            return [
                {
                    "type": row[0],
                    "data": json.loads(row[1]),
                    "timestamp": row[2]
                }
                for row in cursor.fetchall()
            ]
    
    def merge_preferences(self, existing: UserPreferences, new_data: Dict[str, Any]) -> UserPreferences:
        """Intelligently merge new preference data with existing"""
        # Update basic fields
        for field in ['travel_style', 'budget_preference', 'travel_pace', 'group_dynamics']:
            if new_data.get(field):
                setattr(existing, field, new_data[field])
        
        # Merge lists intelligently
        for list_field in ['activity_preferences', 'dietary_restrictions', 'cultural_interests', 
                          'past_destinations', 'preferred_seasons', 'language_preferences', 
                          'accessibility_needs']:
            if new_data.get(list_field):
                current_list = getattr(existing, list_field)
                new_items = new_data[list_field]
                # Add new items that aren't already present
                for item in new_items:
                    if item not in current_list:
                        current_list.append(item)
                setattr(existing, list_field, current_list)
        
        # Merge accommodation preferences
        if new_data.get('accommodation_preferences'):
            existing.accommodation_preferences.update(new_data['accommodation_preferences'])
        
        return existing
    
    def get_personalization_insights(self, user_id: str) -> Dict[str, Any]:
        """Generate personalization insights for agents"""
        preferences = self.get_user_preferences(user_id)
        patterns = self.get_interaction_patterns(user_id)
        
        if not preferences:
            return {}
        
        insights = {
            "personality_profile": {
                "travel_style": preferences.travel_style,
                "pace_preference": preferences.travel_pace,
                "group_dynamics": preferences.group_dynamics
            },
            "experience_preferences": {
                "activities": preferences.activity_preferences,
                "cultural_interests": preferences.cultural_interests,
                "budget_style": preferences.budget_preference
            },
            "practical_needs": {
                "dietary_restrictions": preferences.dietary_restrictions,
                "accessibility_needs": preferences.accessibility_needs,
                "accommodation_style": preferences.accommodation_preferences
            },
            "travel_history": {
                "past_destinations": preferences.past_destinations,
                "preferred_seasons": preferences.preferred_seasons
            },
            "behavioral_patterns": self._analyze_behavioral_patterns(patterns),
            "recommendation_adjustments": self._generate_recommendation_adjustments(preferences, patterns)
        }
        
        return insights
    
    def _analyze_behavioral_patterns(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze user behavioral patterns"""
        if not patterns:
            return {}
        
        # Analyze interaction frequency, preferences, and trends
        analysis = {
            "interaction_frequency": len(patterns),
            "preferred_interaction_time": self._find_preferred_times(patterns),
            "decision_making_style": self._analyze_decision_style(patterns),
            "engagement_level": self._calculate_engagement(patterns)
        }
        
        return analysis
    
    def _find_preferred_times(self, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Find when user prefers to interact"""
        times = [pattern["timestamp"] for pattern in patterns]
        # Analyze time patterns (simplified)
        return {"peak_hours": "evening", "preferred_days": "weekends"}
    
    def _analyze_decision_style(self, patterns: List[Dict[str, Any]]) -> str:
        """Analyze how user makes decisions"""
        # Simplified analysis
        if len(patterns) > 10:
            return "thorough_researcher"
        elif len(patterns) > 5:
            return "moderate_planner"
        else:
            return "quick_decider"
    
    def _calculate_engagement(self, patterns: List[Dict[str, Any]]) -> str:
        """Calculate user engagement level"""
        recent_interactions = len([p for p in patterns if (datetime.now() - datetime.fromisoformat(p["timestamp"])).days <= 7])
        
        if recent_interactions > 5:
            return "high"
        elif recent_interactions > 2:
            return "medium"
        else:
            return "low"
    
    def _generate_recommendation_adjustments(self, preferences: UserPreferences, patterns: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate recommendation adjustments based on user data"""
        adjustments = {
            "activity_weighting": {},
            "budget_sensitivity": 1.0,
            "cultural_depth": 1.0,
            "pace_adjustment": 1.0
        }
        
        # Adjust based on preferences and patterns
        if preferences.travel_style == "luxury":
            adjustments["budget_sensitivity"] = 0.5  # Less price sensitive
        elif preferences.travel_style == "budget":
            adjustments["budget_sensitivity"] = 2.0  # More price sensitive
        
        if "cultural" in preferences.activity_preferences:
            adjustments["cultural_depth"] = 1.5  # More cultural content
        
        return adjustments

# Global memory manager instance
memory_manager = ConversationMemoryManager()
