"""
🔍 Tavily Search API Integration
Tavily search API services
"""

from tavily import TavilyClient
import os
from typing import Dict, Any, Optional, List

class TavilyService:
    """Tavily API service wrapper"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.client = TavilyClient(api_key=api_key or os.getenv("TAVILY_API_KEY"))
    
    def search(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """Search for travel information"""
        response = self.client.search(
            query=query,
            max_results=max_results
        )
        return response.get("results", [])
    
    def context_search(self, query: str, max_results: int = 3) -> str:
        """Get contextual search results"""
        response = self.client.get_search_context(
            query=query,
            max_results=max_results
        )
        return response
