#!/usr/bin/env python3
"""
Final Comprehensive Project Cleanup
Removes all unnecessary files, duplicate directories, and streamlines the project
"""

import os
import shutil
from pathlib import Path

def cleanup_project():
    """Remove all unnecessary files and directories"""
    
    base_path = Path(r"c:\Users\AYMAN\AI TRAVEL AGENT (TOURISIM)")
    
    # Files to remove - all test, debug, utility, and temporary files
    files_to_remove = [
        # Test and debug files
        "add_beirut_hotels.py",
        "add_hotels_simple.py", 
        "add_more_hotels.py",
        "check_database_structure.py",
        "check_table_permissions.py",
        "complete_payment_test.py",
        "deprecated_agent_removal_summary.py",
        "discover_all_tables.py",
        "fix_import_paths.py",
        "fix_supabase_connection.py",
        "inspect_hotels.py",
        "markdown_cleanup.py",
        "project_cleanup.py",
        "quick_db_check.py",
        "quick_fix_tool.py",
        "simple_db_check.py",
        "simple_hotel_adder.py",
        "simple_payment_test.py",
        "test_enhanced_flights.py",
        "test_stripe_integration.py",
        "validate_supabase_key.py",
        "verify_airlines.py",
        "workspace_cleanup.py",
        
        # Duplicate database files
        "database_hotel_populator.py",
        "populate_existing_hotels.py",
        "populate_hotels_database.py",
        "populate_airlines_table.py",
        "setup_routes_table.py",
        "setup_validation.py",
        "comprehensive_database_populator.py",
        
        # Duplicate platform files
        "enhanced_multi_destination_app.py",
        "enhanced_personalized_platform.py", 
        "database_enhanced_platform.py",
        "multi_destination_booking.py",
        "streamlined_booking_system.py",
        "intelligent_booking_system.py",
        "enhanced_booking_api.py",
        
        # Duplicate flight files
        "create_flight_routes.py",
        "create_flight_routes_clean.py",
        "flight_routes_sql.py",
        "enhanced_flight_service.py",
        
        # Duplicate hotel files
        "enhanced_hotel_database.py",
        "hotels_database_sql.py",
        "hotels_database_summary.py",
        
        # Duplicate configuration files
        "live_booking_config.env",
        ".env.template",
        "live_booking_requirements.txt",
        
        # Analysis and summary files
        "complete_database_analysis.py",
        "final_hotels_database_analysis.py",
        "hotels_expansion_phase2.py",
        "large_scale_hotels_expansion.py",
        
        # SQL files (data already in database)
        "create_airlines_table.sql",
        "hotels_table_creation.sql",
        
        # Package files
        "package_integration.py",
    ]
    
    # Directories to remove - empty or duplicate directories
    dirs_to_remove = [
        "agents",      # Contains only __init__.py
        "booking",     # Contains only __init__.py  
        "apps",        # Duplicate of app
        "booking_system", # Duplicate functionality
        "crewai",      # Not used
        "deployment",  # Not needed for development
        "docs",        # Not used
        "scripts",     # Scripts are in root
        "tests",       # Test files removed
        ".github",     # Not needed
    ]
    
    removed_files = []
    removed_dirs = []
    total_size_saved = 0
    
    print("🧹 Starting Final Comprehensive Cleanup...")
    print("=" * 50)
    
    # Remove files
    for file_name in files_to_remove:
        file_path = base_path / file_name
        if file_path.exists():
            try:
                file_size = file_path.stat().st_size
                file_path.unlink()
                removed_files.append(file_name)
                total_size_saved += file_size
                print(f"✅ Removed file: {file_name}")
            except Exception as e:
                print(f"❌ Error removing {file_name}: {e}")
    
    # Remove directories
    for dir_name in dirs_to_remove:
        dir_path = base_path / dir_name
        if dir_path.exists() and dir_path.is_dir():
            try:
                shutil.rmtree(dir_path)
                removed_dirs.append(dir_name)
                print(f"✅ Removed directory: {dir_name}")
            except Exception as e:
                print(f"❌ Error removing directory {dir_name}: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 CLEANUP COMPLETE!")
    print("=" * 50)
    print(f"📁 Files Removed: {len(removed_files)}")
    print(f"📂 Directories Removed: {len(removed_dirs)}")
    print(f"💾 Total Space Saved: {total_size_saved / 1024:.1f} KB")
    
    # Show essential files remaining
    print("\n🔑 ESSENTIAL FILES REMAINING:")
    essential_files = [
        "complete_streamlit_platform.py",  # Main application
        "database_enhanced_booking_system.py",  # Core booking system
        "final_booking_system.py",  # Production booking system  
        "live_booking_system.py",  # Live booking functionality
        "enhanced_streamlit_app.py",  # Enhanced UI
        ".env",  # Environment variables
        ".env.example",  # Template for new users
        "requirements.txt",  # Dependencies
        "pyproject.toml",  # Project configuration
        "README.md",  # Project documentation
    ]
    
    for file_name in essential_files:
        file_path = base_path / file_name
        if file_path.exists():
            print(f"  ✅ {file_name}")
        else:
            print(f"  ❌ MISSING: {file_name}")
    
    print("\n🚀 PROJECT IS NOW STREAMLINED AND READY!")
    
    return removed_files, removed_dirs, total_size_saved

if __name__ == "__main__":
    cleanup_project()
