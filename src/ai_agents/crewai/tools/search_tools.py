"""
🔍 Search Tools for CrewAI Agents
Specialized search tools for different types of travel information
"""

import sys
import os
from pathlib import Path

# Add the project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

try:
    from crewai import tool
except ImportError:
    def tool(name=None, description=None):
        def decorator(func):
            func._tool_name = name or func.__name__
            func._tool_description = description or func.__doc__
            return func
        return decorator

from langchain_community.tools.tavily_search import TavilySearchResults
import os
import json
from dotenv import load_dotenv

load_dotenv()

# Initialize search tool
try:
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if tavily_api_key:
        search_tool = TavilySearchResults(api_key=tavily_api_key, max_results=5)
    else:
        search_tool = None
        print("⚠️ Tavily API key not found. Search functionality limited.")
except Exception as e:
    search_tool = None
    print(f"⚠️ Search tool initialization failed: {e}")

@tool
def tavily_search_tool(query: str) -> str:
    """
    General web search using Tavily API
    
    Args:
        query (str): Search query
        
    Returns:
        str: Search results
    """
    if not search_tool:
        return f"Search unavailable. Please manually research: {query}"
    
    try:
        results = search_tool.run(query)
        return f"Search results for '{query}':\n{results}"
    except Exception as e:
        return f"Search error for '{query}': {str(e)}"

@tool
def google_search_tool(query: str) -> str:
    """
    Google search integration (placeholder - requires Google API setup)
    
    Args:
        query (str): Search query
        
    Returns:
        str: Search results
    """
    # For now, use Tavily as fallback
    return tavily_search_tool(query)

@tool
def local_search_tool(location: str, business_type: str) -> str:
    """
    Local business search tool
    
    Args:
        location (str): Location to search in
        business_type (str): Type of business
        
    Returns:
        str: Local business results
    """
    query = f"{business_type} in {location} local businesses"
    return tavily_search_tool(query)

@tool
def review_search_tool(business_name: str, location: str) -> str:
    """
    Search for reviews of specific businesses
    
    Args:
        business_name (str): Name of business
        location (str): Location of business
        
    Returns:
        str: Review information
    """
    query = f"{business_name} {location} reviews ratings customer feedback"
    return tavily_search_tool(query)

@tool
def real_time_search_tool(query: str) -> str:
    """
    Real-time information search
    
    Args:
        query (str): Search query for current information
        
    Returns:
        str: Real-time search results
    """
    query_with_time = f"{query} current latest today 2024"
    return tavily_search_tool(query_with_time)

@tool
def price_search_tool(item: str, location: str = "") -> str:
    """
    Search for pricing information
    
    Args:
        item (str): Item to search pricing for
        location (str): Location context (optional)
        
    Returns:
        str: Pricing information
    """
    query = f"{item} price cost {location} current pricing"
    return tavily_search_tool(query)

# Export all search tools
def get_search_tools():
    """Get all available search tools"""
    return [
        tavily_search_tool,
        google_search_tool,
        local_search_tool,
        review_search_tool,
        real_time_search_tool,
        price_search_tool
    ]