"""
🔬 Enhanced Psychology Analyst
Advanced NLP and machine learning for deep preference extraction and behavioral analysis
"""

import re
import json
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
import numpy as np
from datetime import datetime

try:
    # Try to import advanced NLP libraries
    import spacy
    from textblob import TextBlob
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.cluster import KMeans
    ADVANCED_NLP_AVAILABLE = True
except ImportError:
    print("Warning: Advanced NLP libraries not available. Install with: pip install spacy textblob scikit-learn")
    ADVANCED_NLP_AVAILABLE = False

@dataclass
class PsychologyProfile:
    """Comprehensive psychology profile"""
    personality_type: str
    travel_motivations: List[str]
    decision_making_style: str
    social_preferences: str
    risk_tolerance: str
    experience_seeking: str
    authenticity_preference: str
    luxury_orientation: str
    cultural_openness: str
    adventure_level: str
    pace_preference: str
    group_dynamics: str
    stress_management: str
    confidence_score: float

class EnhancedPsychologyAnalyst:
    """Advanced psychology analyst with NLP and ML capabilities"""
    
    def __init__(self):
        self.load_nlp_models()
        self.initialize_psychology_patterns()
    
    def load_nlp_models(self):
        """Load NLP models and resources"""
        if ADVANCED_NLP_AVAILABLE:
            try:
                # Load spaCy model for advanced NLP
                self.nlp = spacy.load("en_core_web_sm")
            except OSError:
                print("Warning: spaCy model not found. Install with: python -m spacy download en_core_web_sm")
                self.nlp = None
            
            # Initialize TF-IDF vectorizer for text analysis
            self.vectorizer = TfidfVectorizer(
                stop_words='english',
                max_features=1000,
                ngram_range=(1, 3)
            )
        else:
            self.nlp = None
            self.vectorizer = None
    
    def initialize_psychology_patterns(self):
        """Initialize psychology pattern recognition data"""
        self.personality_indicators = {
            "adventurous": [
                "adventure", "thrill", "extreme", "risk", "adrenaline", "exciting", 
                "challenging", "daring", "bold", "wild", "spontaneous"
            ],
            "cultural": [
                "culture", "history", "heritage", "tradition", "authentic", "local", 
                "museum", "art", "architecture", "historical", "immersive"
            ],
            "relaxed": [
                "relax", "peaceful", "calm", "quiet", "serene", "tranquil", 
                "spa", "wellness", "meditation", "slow", "leisurely"
            ],
            "luxury": [
                "luxury", "premium", "high-end", "exclusive", "elegant", "sophisticated", 
                "five-star", "upscale", "lavish", "indulgent", "pampering"
            ],
            "budget_conscious": [
                "budget", "affordable", "cheap", "economical", "value", "savings", 
                "reasonable", "cost-effective", "backpacking", "hostels"
            ],
            "social": [
                "friends", "social", "party", "nightlife", "meet people", "group", 
                "community", "networking", "sociable", "outgoing"
            ],
            "romantic": [
                "romantic", "honeymoon", "couple", "intimate", "private", "cozy", 
                "sunset", "candlelit", "secluded", "romantic dinner"
            ],
            "family": [
                "family", "kids", "children", "family-friendly", "safe", "educational", 
                "suitable for children", "playground", "family activities"
            ]
        }
        
        self.motivation_patterns = {
            "escape": ["escape", "get away", "break", "stress relief", "disconnect"],
            "discovery": ["discover", "explore", "new", "different", "unknown", "hidden"],
            "learning": ["learn", "education", "knowledge", "understand", "experience"],
            "connection": ["connect", "people", "culture", "local", "community"],
            "achievement": ["challenge", "accomplish", "goal", "bucket list", "dream"],
            "indulgence": ["treat myself", "deserve", "pamper", "luxury", "splurge"]
        }
        
        self.decision_style_patterns = {
            "planner": ["plan", "organize", "schedule", "itinerary", "detailed", "prepare"],
            "spontaneous": ["spontaneous", "flexible", "go with flow", "improvise", "wing it"],
            "researcher": ["research", "reviews", "compare", "best", "recommendations"],
            "delegator": ["arrange", "organize for me", "travel agent", "full service"]
        }
    
    def analyze_text_input(self, text: str) -> Dict[str, Any]:
        """Comprehensive text analysis using multiple NLP techniques"""
        analysis = {
            "sentiment": self._analyze_sentiment(text),
            "personality_indicators": self._extract_personality_indicators(text),
            "travel_motivations": self._extract_motivations(text),
            "decision_style": self._analyze_decision_style(text),
            "preferences": self._extract_preferences(text),
            "emotional_tone": self._analyze_emotional_tone(text),
            "complexity_level": self._analyze_text_complexity(text),
            "entities": self._extract_travel_entities(text)
        }
        
        return analysis
    
    def _analyze_sentiment(self, text: str) -> Dict[str, float]:
        """Analyze sentiment using TextBlob"""
        if ADVANCED_NLP_AVAILABLE:
            blob = TextBlob(text)
            return {
                "polarity": blob.sentiment.polarity,  # -1 to 1
                "subjectivity": blob.sentiment.subjectivity  # 0 to 1
            }
        else:
            # Simple fallback sentiment analysis
            positive_words = ["love", "amazing", "great", "wonderful", "excited", "fantastic"]
            negative_words = ["hate", "terrible", "awful", "bad", "disappointed", "worried"]
            
            text_lower = text.lower()
            positive_count = sum(1 for word in positive_words if word in text_lower)
            negative_count = sum(1 for word in negative_words if word in text_lower)
            
            # Simple polarity calculation
            total_words = len(text.split())
            polarity = (positive_count - negative_count) / max(total_words, 1)
            
            return {
                "polarity": max(-1, min(1, polarity)),  # Clamp between -1 and 1
                "subjectivity": min(1, (positive_count + negative_count) / max(total_words, 1))
            }
    
    def _extract_personality_indicators(self, text: str) -> Dict[str, float]:
        """Extract personality indicators from text"""
        text_lower = text.lower()
        scores = {}
        
        for personality_type, keywords in self.personality_indicators.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            # Normalize by text length and keyword count
            scores[personality_type] = score / max(len(keywords), 1)
        
        return scores
    
    def _extract_motivations(self, text: str) -> Dict[str, float]:
        """Extract travel motivations from text"""
        text_lower = text.lower()
        motivation_scores = {}
        
        for motivation, keywords in self.motivation_patterns.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            motivation_scores[motivation] = score / max(len(keywords), 1)
        
        return motivation_scores
    
    def _analyze_decision_style(self, text: str) -> Dict[str, float]:
        """Analyze decision-making style"""
        text_lower = text.lower()
        style_scores = {}
        
        for style, keywords in self.decision_style_patterns.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            style_scores[style] = score / max(len(keywords), 1)
        
        return style_scores
    
    def _extract_preferences(self, text: str) -> Dict[str, List[str]]:
        """Extract specific travel preferences"""
        preferences = {
            "activities": [],
            "destinations": [],
            "accommodation": [],
            "food": [],
            "transportation": []
        }
        
        # Use regex patterns to extract preferences
        activity_pattern = r'(?:want to|like to|enjoy|love)\s+([^.!?]+?)(?:\.|!|\?|,|$)'
        activities = re.findall(activity_pattern, text.lower())
        preferences["activities"] = [act.strip() for act in activities]
        
        # Extract destination mentions
        if self.nlp:
            doc = self.nlp(text)
            for ent in doc.ents:
                if ent.label_ in ["GPE", "LOC"]:  # Geopolitical entity or location
                    preferences["destinations"].append(ent.text)
        else:
            # Simple destination extraction
            common_destinations = ["paris", "london", "tokyo", "new york", "rome", "barcelona", 
                                 "dubai", "thailand", "italy", "france", "spain", "japan"]
            text_lower = text.lower()
            for dest in common_destinations:
                if dest in text_lower:
                    preferences["destinations"].append(dest.title())
        
        return preferences
    
    def _analyze_emotional_tone(self, text: str) -> Dict[str, float]:
        """Analyze emotional tone of the text"""
        emotional_indicators = {
            "excitement": ["excited", "amazing", "incredible", "fantastic", "awesome"],
            "anxiety": ["worried", "nervous", "anxious", "concerned", "scared"],
            "enthusiasm": ["love", "passion", "thrilled", "eager", "can't wait"],
            "uncertainty": ["maybe", "perhaps", "not sure", "uncertain", "might"]
        }
        
        text_lower = text.lower()
        emotions = {}
        
        for emotion, keywords in emotional_indicators.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            emotions[emotion] = score
        
        return emotions
    
    def _analyze_text_complexity(self, text: str) -> Dict[str, Any]:
        """Analyze text complexity to understand user sophistication"""
        words = text.split()
        sentences = text.split('.')
        
        return {
            "word_count": len(words),
            "sentence_count": len(sentences),
            "avg_word_length": np.mean([len(word) for word in words]) if words else 0,
            "complexity_score": len(set(words)) / len(words) if words else 0  # Lexical diversity
        }
    
    def _extract_travel_entities(self, text: str) -> Dict[str, List[str]]:
        """Extract travel-related entities using NLP"""
        entities = {
            "locations": [],
            "dates": [],
            "durations": [],
            "people": [],
            "organizations": []
        }
        
        if self.nlp:
            doc = self.nlp(text)
            for ent in doc.ents:
                if ent.label_ in ["GPE", "LOC"]:
                    entities["locations"].append(ent.text)
                elif ent.label_ == "DATE":
                    entities["dates"].append(ent.text)
                elif ent.label_ == "PERSON":
                    entities["people"].append(ent.text)
                elif ent.label_ == "ORG":
                    entities["organizations"].append(ent.text)
        
        # Extract duration patterns
        duration_pattern = r'(\d+)\s*(day|week|month)s?'
        durations = re.findall(duration_pattern, text.lower())
        entities["durations"] = [f"{num} {unit}s" for num, unit in durations]
        
        return entities
    
    def generate_psychology_profile(self, text_analysis: Dict[str, Any], 
                                  user_interactions: List[Dict[str, Any]] = None) -> PsychologyProfile:
        """Generate comprehensive psychology profile"""
        
        # Determine dominant personality type
        personality_scores = text_analysis["personality_indicators"]
        dominant_personality = max(personality_scores.items(), key=lambda x: x[1])[0] if personality_scores else "balanced"
        
        # Extract top motivations
        motivation_scores = text_analysis["travel_motivations"]
        top_motivations = [k for k, v in sorted(motivation_scores.items(), key=lambda x: x[1], reverse=True)[:3] if v > 0]
        
        # Determine decision-making style
        decision_scores = text_analysis["decision_style"]
        decision_style = max(decision_scores.items(), key=lambda x: x[1])[0] if decision_scores else "balanced"
        
        # Analyze social preferences
        social_score = personality_scores.get("social", 0)
        romantic_score = personality_scores.get("romantic", 0)
        family_score = personality_scores.get("family", 0)
        
        if family_score > max(social_score, romantic_score):
            social_preference = "family-oriented"
        elif romantic_score > social_score:
            social_preference = "intimate"
        elif social_score > 0.3:
            social_preference = "social"
        else:
            social_preference = "independent"
        
        # Determine risk tolerance
        adventure_score = personality_scores.get("adventurous", 0)
        relaxed_score = personality_scores.get("relaxed", 0)
        
        if adventure_score > relaxed_score:
            risk_tolerance = "high" if adventure_score > 0.5 else "moderate"
        else:
            risk_tolerance = "low"
        
        # Calculate confidence score based on text analysis quality
        confidence = self._calculate_confidence_score(text_analysis)
        
        return PsychologyProfile(
            personality_type=dominant_personality,
            travel_motivations=top_motivations,
            decision_making_style=decision_style,
            social_preferences=social_preference,
            risk_tolerance=risk_tolerance,
            experience_seeking="high" if adventure_score > 0.3 else "moderate",
            authenticity_preference="high" if personality_scores.get("cultural", 0) > 0.3 else "moderate",
            luxury_orientation="high" if personality_scores.get("luxury", 0) > 0.3 else "moderate",
            cultural_openness="high" if personality_scores.get("cultural", 0) > 0.2 else "moderate",
            adventure_level="high" if adventure_score > 0.4 else "moderate",
            pace_preference="slow" if relaxed_score > 0.3 else "moderate",
            group_dynamics=social_preference,
            stress_management="active" if adventure_score > relaxed_score else "passive",
            confidence_score=confidence
        )
    
    def _calculate_confidence_score(self, analysis: Dict[str, Any]) -> float:
        """Calculate confidence score for the analysis"""
        factors = [
            analysis["complexity_level"]["word_count"] > 20,  # Sufficient text
            sum(analysis["personality_indicators"].values()) > 0.5,  # Clear indicators
            analysis["sentiment"]["subjectivity"] > 0.3,  # Personal content
            len(analysis["entities"]["locations"]) > 0  # Specific locations mentioned
        ]
        
        return sum(factors) / len(factors)
    
    def provide_agent_guidance(self, profile: PsychologyProfile) -> Dict[str, Any]:
        """Provide guidance for other agents based on psychology profile"""
        guidance = {
            "itinerary_architect": {
                "pacing": "slow" if profile.pace_preference == "slow" else "moderate",
                "activity_balance": self._get_activity_balance(profile),
                "budget_allocation": self._get_budget_guidance(profile),
                "risk_level": profile.risk_tolerance
            },
            "experience_curator": {
                "authenticity_level": profile.authenticity_preference,
                "social_activities": profile.social_preferences != "independent",
                "cultural_depth": profile.cultural_openness,
                "adventure_inclusion": profile.adventure_level
            },
            "cultural_specialist": {
                "engagement_style": profile.cultural_openness,
                "learning_preference": "deep" if "learning" in profile.travel_motivations else "surface",
                "interaction_comfort": profile.social_preferences
            },
            "seasonal_specialist": {
                "flexibility": "high" if profile.decision_making_style == "spontaneous" else "low",
                "weather_sensitivity": "high" if profile.risk_tolerance == "low" else "moderate"
            }
        }
        
        return guidance
    
    def _get_activity_balance(self, profile: PsychologyProfile) -> Dict[str, float]:
        """Get activity balance recommendations"""
        balance = {
            "cultural": 0.3,
            "adventure": 0.2,
            "relaxation": 0.3,
            "social": 0.2
        }
        
        if profile.personality_type == "cultural":
            balance["cultural"] = 0.5
            balance["adventure"] = 0.1
        elif profile.personality_type == "adventurous":
            balance["adventure"] = 0.4
            balance["relaxation"] = 0.1
        elif profile.personality_type == "relaxed":
            balance["relaxation"] = 0.5
            balance["adventure"] = 0.1
        
        return balance
    
    def _get_budget_guidance(self, profile: PsychologyProfile) -> Dict[str, Any]:
        """Get budget allocation guidance"""
        if profile.luxury_orientation == "high":
            return {
                "accommodation_priority": "high",
                "experience_over_savings": True,
                "quality_focus": "premium"
            }
        elif profile.personality_type == "budget_conscious":
            return {
                "accommodation_priority": "low",
                "experience_over_savings": False,
                "quality_focus": "value"
            }
        else:
            return {
                "accommodation_priority": "medium",
                "experience_over_savings": True,
                "quality_focus": "balanced"
            }

# Global psychology analyst instance
psychology_analyst = EnhancedPsychologyAnalyst()
