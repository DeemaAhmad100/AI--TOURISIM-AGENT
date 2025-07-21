"""
🗄️ Supabase API Integration
Supabase database client and services
"""

from supabase import create_client, Client
import os
from typing import Dict, Any, Optional, List

class SupabaseService:
    """Supabase API service wrapper"""
    
    def __init__(self, url: Optional[str] = None, key: Optional[str] = None):
        self.url = url or os.getenv("SUPABASE_URL")
        self.key = key or os.getenv("SUPABASE_KEY")
        self.client: Client = create_client(self.url, self.key)
    
    def insert(self, table: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Insert data into table"""
        response = self.client.table(table).insert(data).execute()
        return response.data
    
    def select(self, table: str, columns: str = "*", filter_dict: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Select data from table"""
        query = self.client.table(table).select(columns)
        if filter_dict:
            for key, value in filter_dict.items():
                query = query.eq(key, value)
        response = query.execute()
        return response.data
    
    def update(self, table: str, data: Dict[str, Any], filter_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Update data in table"""
        query = self.client.table(table).update(data)
        for key, value in filter_dict.items():
            query = query.eq(key, value)
        response = query.execute()
        return response.data
    
    def delete(self, table: str, filter_dict: Dict[str, Any]) -> Dict[str, Any]:
        """Delete data from table"""
        query = self.client.table(table).delete()
        for key, value in filter_dict.items():
            query = query.eq(key, value)
        response = query.execute()
        return response.data
