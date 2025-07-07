#!/usr/bin/env python3
"""
🗺️ Alternative Maps & Places API Setup
Configure multiple mapping services for your AI Travel Platform
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class AlternativeMapsSetup:
    def __init__(self):
        self.env_file = Path('.env')
        self.maps_providers = {
            'google': 'Google Maps (Best but requires billing)',
            'openstreetmap': 'OpenStreetMap (Free, no API key needed)',
            'mapbox': 'Mapbox (50K free requests/month)',
            'here': 'Here Maps (250K free requests/month)'
        }
    
    def show_intro(self):
        """Show introduction and options"""
        print("🗺️ MAPS & PLACES API SETUP")
        print("=" * 50)
        print()
        print("Since Google APIs can be challenging to set up, let's explore options:")
        print()
        
        for i, (provider, description) in enumerate(self.maps_providers.items(), 1):
            print(f"{i}. {provider.title()}: {description}")
        
        print()
        print("📍 What each provider offers:")
        print("• Maps: Interactive maps for your travel platform")
        print("• Places: Search for hotels, restaurants, attractions")
        print("• Geocoding: Convert addresses to coordinates")
        print("• Directions: Route planning and navigation")
        print()
    
    def setup_google_maps(self):
        """Setup Google Maps (with guidance)"""
        print("🌍 GOOGLE MAPS SETUP")
        print("=" * 30)
        print()
        print("⚠️ Google Maps requires billing to be enabled")
        print("But you get $300 free credits for new accounts!")
        print()
        print("📋 Required steps:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create new project: 'AI Travel Platform'")
        print("3. Enable these APIs:")
        print("   • Google Maps JavaScript API")
        print("   • Google Places API")
        print("   • Google Calendar API")
        print("   • Geocoding API")
        print("4. Create API credentials")
        print("5. Enable billing (required)")
        print()
        
        choice = input("Do you have a Google API key ready? (y/n): ").strip().lower()
        
        if choice == 'y':
            api_key = input("Enter your Google Maps API key: ").strip()
            if api_key:
                self._add_env_var('GOOGLE_MAPS_API_KEY', api_key)
                self._add_env_var('GOOGLE_PLACES_API_KEY', api_key)
                self._add_env_var('GOOGLE_CALENDAR_API_KEY', api_key)
                print("✅ Google Maps configured successfully!")
                return True
            else:
                print("❌ Invalid API key")
                return False
        else:
            print("📚 Please follow the detailed guide in GOOGLE_APIS_SETUP_GUIDE.md")
            print("Or choose an alternative provider below.")
            return False
    
    def setup_openstreetmap(self):
        """Setup OpenStreetMap (Free)"""
        print("🗺️ OPENSTREETMAP SETUP")
        print("=" * 30)
        print()
        print("✅ OpenStreetMap is completely FREE!")
        print("• No API key required")
        print("• No billing needed")
        print("• No usage limits")
        print()
        print("📋 Features available:")
        print("• Interactive maps with Leaflet.js")
        print("• Place search with Nominatim API")
        print("• Geocoding and reverse geocoding")
        print("• Route planning with OSRM")
        print()
        
        choice = input("Enable OpenStreetMap? (y/n): ").strip().lower()
        
        if choice == 'y':
            self._add_env_var('USE_OPENSTREETMAP', 'true')
            self._add_env_var('NOMINATIM_API_URL', 'https://nominatim.openstreetmap.org')
            self._add_env_var('OSRM_API_URL', 'https://router.project-osrm.org')
            print("✅ OpenStreetMap configured successfully!")
            return True
        
        return False
    
    def setup_mapbox(self):
        """Setup Mapbox (Free tier available)"""
        print("📍 MAPBOX SETUP")
        print("=" * 30)
        print()
        print("💡 Mapbox offers 50,000 free requests per month")
        print("• No billing required for free tier")
        print("• Beautiful, customizable maps")
        print("• Excellent mobile support")
        print()
        print("📋 Setup steps:")
        print("1. Go to https://www.mapbox.com/")
        print("2. Create free account")
        print("3. Get your access token from dashboard")
        print("4. No credit card required for free tier")
        print()
        
        choice = input("Do you have a Mapbox access token? (y/n): ").strip().lower()
        
        if choice == 'y':
            token = input("Enter your Mapbox access token: ").strip()
            if token:
                self._add_env_var('MAPBOX_ACCESS_TOKEN', token)
                self._add_env_var('USE_MAPBOX', 'true')
                print("✅ Mapbox configured successfully!")
                return True
            else:
                print("❌ Invalid token")
                return False
        else:
            print("📚 Visit https://www.mapbox.com/ to get your free token")
            return False
    
    def setup_here_maps(self):
        """Setup Here Maps (Free tier available)"""
        print("📍 HERE MAPS SETUP")
        print("=" * 30)
        print()
        print("💡 Here Maps offers 250,000 free requests per month")
        print("• No billing required for free tier")
        print("• Excellent for geocoding and places")
        print("• Good for route optimization")
        print()
        print("📋 Setup steps:")
        print("1. Go to https://developer.here.com/")
        print("2. Create free account")
        print("3. Create project and get API key")
        print("4. No credit card required for free tier")
        print()
        
        choice = input("Do you have a Here Maps API key? (y/n): ").strip().lower()
        
        if choice == 'y':
            api_key = input("Enter your Here Maps API key: ").strip()
            if api_key:
                self._add_env_var('HERE_MAPS_API_KEY', api_key)
                self._add_env_var('USE_HERE_MAPS', 'true')
                print("✅ Here Maps configured successfully!")
                return True
            else:
                print("❌ Invalid API key")
                return False
        else:
            print("📚 Visit https://developer.here.com/ to get your free API key")
            return False
    
    def create_maps_config(self):
        """Create maps configuration file"""
        config = {
            "maps_providers": {
                "google": {
                    "enabled": bool(os.getenv('GOOGLE_MAPS_API_KEY')),
                    "api_key": os.getenv('GOOGLE_MAPS_API_KEY', ''),
                    "features": ["maps", "places", "geocoding", "directions"]
                },
                "openstreetmap": {
                    "enabled": os.getenv('USE_OPENSTREETMAP', 'false').lower() == 'true',
                    "api_url": os.getenv('NOMINATIM_API_URL', 'https://nominatim.openstreetmap.org'),
                    "features": ["maps", "places", "geocoding"]
                },
                "mapbox": {
                    "enabled": os.getenv('USE_MAPBOX', 'false').lower() == 'true',
                    "access_token": os.getenv('MAPBOX_ACCESS_TOKEN', ''),
                    "features": ["maps", "places", "geocoding", "directions"]
                },
                "here": {
                    "enabled": os.getenv('USE_HERE_MAPS', 'false').lower() == 'true',
                    "api_key": os.getenv('HERE_MAPS_API_KEY', ''),
                    "features": ["maps", "places", "geocoding", "directions"]
                }
            }
        }
        
        import json
        config_dir = Path('config')
        config_dir.mkdir(exist_ok=True)
        
        with open(config_dir / 'maps_config.json', 'w') as f:
            json.dump(config, f, indent=2)
        
        print("✅ Maps configuration saved to config/maps_config.json")
    
    def _add_env_var(self, key: str, value: str):
        """Add environment variable to .env file"""
        if not self.env_file.exists():
            self.env_file.touch()
        
        # Read existing content
        with open(self.env_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Check if key already exists
        key_exists = False
        for i, line in enumerate(lines):
            if line.startswith(f'{key}='):
                lines[i] = f'{key}={value}\n'
                key_exists = True
                break
        
        # Add new key if it doesn't exist
        if not key_exists:
            lines.append(f'{key}={value}\n')
        
        # Write back to file
        with open(self.env_file, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    
    def run_setup(self):
        """Run the complete setup process"""
        self.show_intro()
        
        setup_functions = [
            ("Google Maps", self.setup_google_maps),
            ("OpenStreetMap", self.setup_openstreetmap),
            ("Mapbox", self.setup_mapbox),
            ("Here Maps", self.setup_here_maps)
        ]
        
        configured_providers = []
        
        for provider_name, setup_func in setup_functions:
            print(f"\n🔧 Setting up {provider_name}...")
            if setup_func():
                configured_providers.append(provider_name)
            
            # Ask if user wants to continue with other providers
            if len(configured_providers) > 0:
                continue_setup = input(f"\nSet up another provider? (y/n): ").strip().lower()
                if continue_setup != 'y':
                    break
        
        # Create configuration file
        self.create_maps_config()
        
        # Show summary
        print("\n🎉 SETUP COMPLETE!")
        print("=" * 30)
        
        if configured_providers:
            print(f"✅ Configured providers: {', '.join(configured_providers)}")
            print("\n📋 Your platform now supports:")
            print("• Interactive maps")
            print("• Place search and recommendations")
            print("• Address geocoding")
            print("• Route planning")
            print("\n🚀 Next steps:")
            print("• Run: python verify_setup.py")
            print("• Test: python working_user_demo.py")
        else:
            print("ℹ️ No providers configured.")
            print("Your platform will work with basic features.")
            print("You can run this setup again anytime.")
        
        print("\n💡 Tip: OpenStreetMap is the easiest to start with - it's completely free!")

def main():
    setup = AlternativeMapsSetup()
    setup.run_setup()

if __name__ == "__main__":
    main()
