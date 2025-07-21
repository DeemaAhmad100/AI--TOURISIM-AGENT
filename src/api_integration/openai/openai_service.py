"""
🤖 OpenAI API Integration
OpenAI API client and services
"""

from openai import OpenAI
import os
from typing import Dict, Any, Optional

class OpenAIService:
    """OpenAI API service wrapper"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
    
    def chat_completion(self, messages: list, model: str = "gpt-3.5-turbo") -> Dict[str, Any]:
        """Create chat completion"""
        response = self.client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
    
    def embedding(self, text: str, model: str = "text-embedding-ada-002") -> list:
        """Create text embedding"""
        response = self.client.embeddings.create(
            model=model,
            input=text
        )
        return response.data[0].embedding
