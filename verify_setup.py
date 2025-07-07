#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Enhanced Features Verification Script
Run this script to verify all enhanced features are properly configured
'''

import os
import sys
from pathlib import Path

def verify_setup():
    print("Verifying Enhanced Features Setup...")
    
    # Check environment variables
    required_vars = [
        'OPENAI_API_KEY',
        'SUPABASE_URL', 
        'SUPABASE_KEY'
    ]
    
    optional_vars = [
        'SENDGRID_API_KEY',
        'STRIPE_SECRET_KEY',
        'GOOGLE_MAPS_API_KEY',
        'AMADEUS_CLIENT_ID'
    ]
    
    print("\nRequired Environment Variables:")
    for var in required_vars:
        if os.getenv(var):
            print(f"✓ {var}")
        else:
            print(f"✗ {var} - MISSING")
    
    print("\nOptional Environment Variables:")
    for var in optional_vars:
        if os.getenv(var):
            print(f"✓ {var}")
        else:
            print(f"○ {var} - Not configured")
    
    # Check directory structure
    print("\nDirectory Structure:")
    directories = [
        "src/utils",
        "src/integrations",
        "src/ui", 
        "tests",
        "config"
    ]
    
    for directory in directories:
        if Path(directory).exists():
            print(f"✓ {directory}")
        else:
            print(f"✗ {directory} - Missing")
    
    print("\nSetup verification complete!")

if __name__ == "__main__":
    verify_setup()
