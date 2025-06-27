"""
🎯 INTENT DETECTION SYSTEM FOR AI TRAVEL AGENT
Using Sentence Transformers for semantic understanding
"""

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, List, Tuple
import json

class TravelIntentDetector:
    def __init__(self):
        """Initialize the intent detection system"""
        self.model = None
        self.intent_categories = {}
        self.intent_embeddings = {}
        self.threshold = 0.6  # Similarity threshold for intent matching
        
    def load_model(self):
        """Load the sentence transformer model"""
        print("🔄 Loading sentence transformer model...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        print("✅ Model loaded successfully!")
        
    def define_intent_categories(self):
        """Define travel-specific intent categories with example phrases"""
        self.intent_categories = {
            "destination_search": [
                "find destinations",
                "show me places to visit",
                "where should I go",
                "recommend destinations",
                "best places to travel",
                "suggest travel locations",
                "where can I travel",
                "tourist destinations",
                "vacation spots",
                "travel recommendations"
            ],
            "budget_planning": [
                "what's the cost",
                "budget travel",
                "cheap destinations",
                "affordable places",
                "travel costs",
                "how much does it cost",
                "budget-friendly",
                "inexpensive travel",
                "cost of living",
                "travel expenses"
            ],
            "activity_recommendations": [
                "things to do",
                "attractions",
                "museums",
                "restaurants",
                "activities",
                "sightseeing",
                "entertainment",
                "local attractions",
                "tourist activities",
                "places to visit"
            ],
            "trip_planning": [
                "plan my trip",
                "create itinerary",
                "travel schedule",
                "trip planning",
                "organize my travel",
                "plan vacation",
                "travel arrangements",
                "trip organizer",
                "vacation planning",
                "travel planning"
            ],
            "weather_information": [
                "what's the weather",
                "best time to visit",
                "weather forecast",
                "climate information",
                "seasonal weather",
                "when to travel",
                "weather conditions",
                "temperature",
                "rainy season",
                "sunny weather"
            ],
            "transportation": [
                "how to get there",
                "flights",
                "transportation",
                "travel methods",
                "getting around",
                "public transport",
                "car rental",
                "train tickets",
                "bus routes",
                "airport transfers"
            ],
            "accommodation": [
                "hotels",
                "where to stay",
                "accommodation",
                "lodging",
                "booking hotels",
                "places to stay",
                "resorts",
                "hostels",
                "vacation rentals",
                "bed and breakfast"
            ],
            "cultural_information": [
                "local customs",
                "culture",
                "traditions",
                "language",
                "local etiquette",
                "cultural tips",
                "customs and traditions",
                "local practices",
                "cultural events",
                "festivals"
            ]
        }
        
    def create_intent_embeddings(self):
        """Create embeddings for all intent categories"""
        print("🔄 Creating intent embeddings...")
        
        for intent, phrases in self.intent_categories.items():
            # Create embeddings for all example phrases
            embeddings = self.model.encode(phrases)
            # Store the mean embedding for this intent
            self.intent_embeddings[intent] = np.mean(embeddings, axis=0)
            
        print(f"✅ Created embeddings for {len(self.intent_categories)} intent categories")
        
    def detect_intent(self, user_input: str) -> Tuple[str, float]:
        """
        Detect the intent of user input
        
        Args:
            user_input: The user's query
            
        Returns:
            Tuple of (intent_name, confidence_score)
        """
        if not self.model:
            raise ValueError("Model not loaded. Call load_model() first.")
            
        # Create embedding for user input
        user_embedding = self.model.encode([user_input])
        
        # Calculate similarities with all intent embeddings
        similarities = {}
        for intent, intent_embedding in self.intent_embeddings.items():
            similarity = cosine_similarity(user_embedding, [intent_embedding])[0][0]
            similarities[intent] = similarity
            
        # Find the best match
        best_intent = max(similarities, key=similarities.get)
        best_score = similarities[best_intent]
        
        # Check if similarity meets threshold
        if best_score < self.threshold:
            return "unknown", best_score
            
        return best_intent, best_score
        
    def get_intent_suggestions(self, user_input: str, top_k: int = 3) -> List[Tuple[str, float]]:
        """
        Get top K intent suggestions for user input
        
        Args:
            user_input: The user's query
            top_k: Number of top suggestions to return
            
        Returns:
            List of (intent_name, confidence_score) tuples
        """
        if not self.model:
            raise ValueError("Model not loaded. Call load_model() first.")
            
        # Create embedding for user input
        user_embedding = self.model.encode([user_input])
        
        # Calculate similarities with all intent embeddings
        similarities = []
        for intent, intent_embedding in self.intent_embeddings.items():
            similarity = cosine_similarity(user_embedding, [intent_embedding])[0][0]
            similarities.append((intent, similarity))
            
        # Sort by similarity and return top K
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:top_k]
        
    def setup(self):
        """Complete setup of the intent detection system"""
        print("🚀 Setting up Travel Intent Detection System...")
        self.load_model()
        self.define_intent_categories()
        self.create_intent_embeddings()
        print("✅ Intent detection system ready!")
        
    def test_intent_detection(self):
        """Test the intent detection with sample queries"""
        test_queries = [
            "I want to find romantic destinations in Europe",
            "What are some budget-friendly places to visit?",
            "Show me museums in Paris",
            "Can you help me plan a 7-day trip to Japan?",
            "What's the weather like in Bali in December?",
            "How can I get from the airport to downtown?",
            "Where should I stay in New York?",
            "Tell me about local customs in Thailand"
        ]
        
        print("\n🧪 TESTING INTENT DETECTION:")
        print("=" * 50)
        
        for query in test_queries:
            intent, confidence = self.detect_intent(query)
            print(f"Query: '{query}'")
            print(f"Intent: {intent} (confidence: {confidence:.3f})")
            print("-" * 30)

def main():
    """Demonstration of the intent detection system"""
    detector = TravelIntentDetector()
    detector.setup()
    detector.test_intent_detection()

if __name__ == "__main__":
    main()
