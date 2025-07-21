"""
Enhanced Flight Routes Database System
Creates comprehensive flight routes connecting airlines to destinations
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client
import json
from datetime import datetime, timedelta
import random

def get_comprehensive_routes_data():
    """Generate comprehensive flight routes data"""
    
    # Major airport hubs and their connections
    route_data = [
        # MIDDLE EAST HUB ROUTES
        {
            "origin_airport": "DOH",
            "origin_city": "Doha",
            "origin_country": "Qatar",
            "destination_airport": "DXB",
            "destination_city": "Dubai", 
            "destination_country": "United Arab Emirates",
            "airline_iata": "QR",
            "flight_duration_minutes": 75,
            "base_price_usd": 180,
            "weekly_frequency": 35,
            "aircraft_types": "A350,A380,B777",
            "route_type": "regional"
        },
        {
            "origin_airport": "DOH",
            "origin_city": "Doha",
            "origin_country": "Qatar",
            "destination_airport": "LHR",
            "destination_city": "London",
            "destination_country": "United Kingdom", 
            "airline_iata": "QR",
            "flight_duration_minutes": 420,
            "base_price_usd": 650,
            "weekly_frequency": 21,
            "aircraft_types": "A350,A380",
            "route_type": "international"
        },
        {
            "origin_airport": "DOH",
            "origin_city": "Doha", 
            "origin_country": "Qatar",
            "destination_airport": "JFK",
            "destination_city": "New York",
            "destination_country": "United States",
            "airline_iata": "QR",
            "flight_duration_minutes": 780,
            "base_price_usd": 1200,
            "weekly_frequency": 14,
            "aircraft_types": "A350,B777",
            "route_type": "international"
        },
        {
            "origin_airport": "DXB",
            "origin_city": "Dubai",
            "origin_country": "United Arab Emirates",
            "destination_airport": "LHR",
            "destination_city": "London",
            "destination_country": "United Kingdom",
            "airline_iata": "EK",
            "flight_duration_minutes": 460,
            "base_price_usd": 750,
            "weekly_frequency": 42,
            "aircraft_types": "A380,B777",
            "route_type": "international"
        },
        {
            "origin_airport": "DXB",
            "origin_city": "Dubai",
            "origin_country": "United Arab Emirates", 
            "destination_airport": "JFK",
            "destination_city": "New York",
            "destination_country": "United States",
            "airline_iata": "EK",
            "flight_duration_minutes": 800,
            "base_price_usd": 1350,
            "weekly_frequency": 14,
            "aircraft_types": "A380,B777",
            "route_type": "international"
        },
        {
            "origin_airport": "DXB",
            "origin_city": "Dubai",
            "origin_country": "United Arab Emirates",
            "destination_airport": "SIN",
            "destination_city": "Singapore", 
            "destination_country": "Singapore",
            "airline_iata": "EK",
            "flight_duration_minutes": 460,
            "base_price_usd": 580,
            "weekly_frequency": 21,
            "aircraft_types": "A380,B777",
            "route_type": "international"
        },
        
        # EUROPEAN ROUTES
        {
            "origin_airport": "FRA",
            "origin_city": "Frankfurt",
            "origin_country": "Germany",
            "destination_airport": "JFK",
            "destination_city": "New York",
            "destination_country": "United States",
            "airline_iata": "LH",
            "flight_duration_minutes": 510,
            "base_price_usd": 850,
            "weekly_frequency": 21,
            "aircraft_types": "A350,B747",
            "route_type": "international"
        },
        {
            "origin_airport": "LHR",
            "origin_city": "London",
            "origin_country": "United Kingdom",
            "destination_airport": "JFK",
            "destination_city": "New York", 
            "destination_country": "United States",
            "airline_iata": "BA",
            "flight_duration_minutes": 480,
            "base_price_usd": 900,
            "weekly_frequency": 35,
            "aircraft_types": "B777,A350",
            "route_type": "international"
        },
        {
            "origin_airport": "CDG",
            "origin_city": "Paris",
            "origin_country": "France",
            "destination_airport": "JFK",
            "destination_city": "New York",
            "destination_country": "United States", 
            "airline_iata": "AF",
            "flight_duration_minutes": 500,
            "base_price_usd": 820,
            "weekly_frequency": 21,
            "aircraft_types": "A350,B777",
            "route_type": "international"
        },
        
        # ASIAN ROUTES
        {
            "origin_airport": "SIN",
            "origin_city": "Singapore",
            "origin_country": "Singapore",
            "destination_airport": "JFK", 
            "destination_city": "New York",
            "destination_country": "United States",
            "airline_iata": "SQ",
            "flight_duration_minutes": 1080,
            "base_price_usd": 1500,
            "weekly_frequency": 7,
            "aircraft_types": "A350ULR",
            "route_type": "international"
        },
        {
            "origin_airport": "NRT",
            "origin_city": "Tokyo",
            "origin_country": "Japan",
            "destination_airport": "JFK",
            "destination_city": "New York",
            "destination_country": "United States",
            "airline_iata": "JL",
            "flight_duration_minutes": 780,
            "base_price_usd": 1100,
            "weekly_frequency": 14,
            "aircraft_types": "B777,B787",
            "route_type": "international"
        },
        {
            "origin_airport": "HKG",
            "origin_city": "Hong Kong",
            "origin_country": "Hong Kong",
            "destination_airport": "JFK",
            "destination_city": "New York", 
            "destination_country": "United States",
            "airline_iata": "CX",
            "flight_duration_minutes": 900,
            "base_price_usd": 1250,
            "weekly_frequency": 14,
            "aircraft_types": "A350,B777",
            "route_type": "international"
        },
        
        # US DOMESTIC ROUTES
        {
            "origin_airport": "JFK",
            "origin_city": "New York",
            "origin_country": "United States",
            "destination_airport": "LAX",
            "destination_city": "Los Angeles",
            "destination_country": "United States",
            "airline_iata": "AA",
            "flight_duration_minutes": 360,
            "base_price_usd": 350,
            "weekly_frequency": 35,
            "aircraft_types": "A321,B737",
            "route_type": "domestic"
        },
        {
            "origin_airport": "JFK",
            "origin_city": "New York", 
            "origin_country": "United States",
            "destination_airport": "MIA",
            "destination_city": "Miami",
            "destination_country": "United States",
            "airline_iata": "DL",
            "flight_duration_minutes": 180,
            "base_price_usd": 280,
            "weekly_frequency": 42,
            "aircraft_types": "A320,B737",
            "route_type": "domestic"
        },
        
        # BUDGET CARRIER ROUTES
        {
            "origin_airport": "DUB",
            "origin_city": "Dublin",
            "origin_country": "Ireland",
            "destination_airport": "STN",
            "destination_city": "London",
            "destination_country": "United Kingdom",
            "airline_iata": "FR",
            "flight_duration_minutes": 90,
            "base_price_usd": 45,
            "weekly_frequency": 28,
            "aircraft_types": "B737",
            "route_type": "regional"
        },
        {
            "origin_airport": "BUD",
            "origin_city": "Budapest",
            "origin_country": "Hungary", 
            "destination_airport": "LGW",
            "destination_city": "London",
            "destination_country": "United Kingdom",
            "airline_iata": "W6",
            "flight_duration_minutes": 150,
            "base_price_usd": 85,
            "weekly_frequency": 21,
            "aircraft_types": "A320,A321",
            "route_type": "international"
        },
        
        # AFRICAN ROUTES
        {
            "origin_airport": "ADD",
            "origin_city": "Addis Ababa",
            "origin_country": "Ethiopia",
            "destination_airport": "JFK",
            "destination_city": "New York",
            "destination_country": "United States",
            "airline_iata": "ET",
            "flight_duration_minutes": 900,
            "base_price_usd": 950,
            "weekly_frequency": 7,
            "aircraft_types": "B787,A350",
            "route_type": "international"
        },
        
        # OCEANIA ROUTES
        {
            "origin_airport": "SYD",
            "origin_city": "Sydney",
            "origin_country": "Australia",
            "destination_airport": "LAX",
            "destination_city": "Los Angeles",
            "destination_country": "United States", 
            "airline_iata": "QF",
            "flight_duration_minutes": 840,
            "base_price_usd": 1300,
            "weekly_frequency": 14,
            "aircraft_types": "A380,B787",
            "route_type": "international"
        },
        
        # LATIN AMERICAN ROUTES
        {
            "origin_airport": "BOG",
            "origin_city": "Bogotá",
            "origin_country": "Colombia",
            "destination_airport": "MIA",
            "destination_city": "Miami",
            "destination_country": "United States",
            "airline_iata": "AV",
            "flight_duration_minutes": 300,
            "base_price_usd": 420,
            "weekly_frequency": 21,
            "aircraft_types": "A320,B787",
            "route_type": "international"
        }
    ]
    
    return route_data

def create_routes_table(supabase: Client):
    """Create flight routes table in Supabase"""
    
    create_table_sql = '''
        CREATE TABLE IF NOT EXISTS flight_routes (
            id SERIAL PRIMARY KEY,
            origin_airport VARCHAR(3) NOT NULL,
            origin_city VARCHAR(100) NOT NULL,
            origin_country VARCHAR(100) NOT NULL,
            destination_airport VARCHAR(3) NOT NULL,
            destination_city VARCHAR(100) NOT NULL,
            destination_country VARCHAR(100) NOT NULL,
            airline_iata VARCHAR(3) NOT NULL,
            flight_duration_minutes INTEGER NOT NULL,
            base_price_usd DECIMAL(10,2) NOT NULL,
            weekly_frequency INTEGER NOT NULL,
            aircraft_types TEXT NOT NULL,
            route_type VARCHAR(20) NOT NULL,
            active BOOLEAN DEFAULT true,
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW(),
            
            FOREIGN KEY (airline_iata) REFERENCES airlines(iata_code)
        );
        
        CREATE INDEX IF NOT EXISTS idx_flight_routes_origin ON flight_routes(origin_airport);
        CREATE INDEX IF NOT EXISTS idx_flight_routes_destination ON flight_routes(destination_airport);
        CREATE INDEX IF NOT EXISTS idx_flight_routes_airline ON flight_routes(airline_iata);
        CREATE INDEX IF NOT EXISTS idx_flight_routes_route_type ON flight_routes(route_type);
    '''
    
    print("Flight Routes Table Creation SQL:")
    print(create_table_sql)
    print("\nRun this in your Supabase SQL editor to create the table structure.")

def populate_routes(supabase: Client, routes_data: list):
    """Populate flight routes table with comprehensive route data"""
    try:
        print(f"Upserting {len(routes_data)} flight routes into database...")
        
        # Use upsert to handle any duplicates
        result = supabase.table("flight_routes").upsert(routes_data).execute()
        
        if result.data:
            print(f"Successfully processed {len(result.data)} flight routes")
            return True
        else:
            print("No data returned from upsert operation")
            return False
            
    except Exception as e:
        print(f"Error populating routes: {e}")
        return False

def verify_routes(supabase: Client):
    """Verify routes data in database"""
    try:
        # Get total count
        result = supabase.table('flight_routes').select('*', count='exact').execute()
        print(f"Total routes in database: {result.count}")
        
        # Get routes by type
        route_types = ['domestic', 'regional', 'international']
        for route_type in route_types:
            count = supabase.table('flight_routes').select('*', count='exact').eq('route_type', route_type).execute()
            print(f"{route_type.title()} routes: {count.count}")
        
        # Sample routes
        sample = supabase.table('flight_routes').select('origin_city, destination_city, airline_iata, base_price_usd').limit(5).execute()
        print("\nSample routes:")
        for route in sample.data:
            print(f"  • {route['origin_city']} → {route['destination_city']} ({route['airline_iata']}) - ${route['base_price_usd']}")
            
    except Exception as e:
        print(f"Error verifying routes: {e}")

def main():
    """Main function to create and populate flight routes"""
    load_dotenv()
    
    url = os.getenv('SUPABASE_URL')
    key = os.getenv('SUPABASE_KEY')
    
    if not url or not key:
        print("Missing Supabase credentials in .env file")
        return
    
    try:
        supabase: Client = create_client(url, key)
        print("Flight Routes Database Populator")
        print("=" * 50)
        print("Connected to Supabase")
        
        # Create table structure
        print("\nCreating flight routes table...")
        create_routes_table(supabase)
        
        # Get route data
        print("\nPreparing route data...")
        routes_data = get_comprehensive_routes_data()
        print(f"Prepared {len(routes_data)} routes for insertion")
        
        # Populate routes
        print("\nPopulating route data...")
        if populate_routes(supabase, routes_data):
            print("\nVerifying route data...")
            verify_routes(supabase)
            
            print("\n" + "=" * 50)
            print("Flight routes database population completed!")
            print("\nNext Steps:")
            print("1. Run the CREATE TABLE SQL in your Supabase SQL editor")
            print("2. Update your flight search to use these routes")
            print("3. Implement dynamic pricing based on demand")
            
        else:
            print("Failed to populate routes database")
            
    except Exception as e:
        print(f"Database connection error: {e}")

if __name__ == "__main__":
    main()
