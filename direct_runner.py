#!/usr/bin/env python3
"""
Direct Streamlit App Runner
Bypasses streamlit command by importing and running directly
"""

import sys
import os
import webbrowser
import time
from threading import Timer

def start_app():
    """Start the Streamlit app directly"""
    try:
        # Add current directory to path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        
        print("Starting AI Travel Agent Platform...")
        print("Please wait while the application loads...")
        
        # Import streamlit
        import streamlit as st
        from streamlit import cli as stcli
        
        # Set up Streamlit configuration
        os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'
        
        # App file path
        app_file = os.path.join(current_dir, 'enhanced_streamlit_app.py')
        
        if not os.path.exists(app_file):
            print(f"Error: App file not found at {app_file}")
            input("Press Enter to exit...")
            return
        
        # Open browser after delay
        def open_browser():
            time.sleep(3)
            webbrowser.open('http://localhost:8501')
            print("Browser should open automatically at http://localhost:8501")
        
        Timer(1, open_browser).start()
        
        # Run streamlit
        sys.argv = ['streamlit', 'run', app_file, '--server.port', '8501', '--server.headless', 'true']
        stcli.main()
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("Please ensure Streamlit is installed: pip install streamlit")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"Error starting app: {e}")
        print("Trying alternative method...")
        
        # Alternative: direct execution
        try:
            import subprocess
            subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'enhanced_streamlit_app.py'])
        except Exception as e2:
            print(f"Alternative method failed: {e2}")
            input("Press Enter to exit...")

if __name__ == "__main__":
    start_app()
