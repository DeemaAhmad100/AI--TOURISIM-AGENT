#!/usr/bin/env python3
"""
Manual Streamlit launcher for the AI Travel Platform
"""

import sys
import os
import webbrowser
import threading
import time

def launch_browser():
    """Launch browser after a delay"""
    time.sleep(3)  # Wait 3 seconds for server to start
    webbrowser.open("http://localhost:8501")

def start_streamlit():
    """Start Streamlit manually"""
    try:
        # Add current directory to Python path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, current_dir)
        
        # Import streamlit
        import streamlit.web.cli as stcli
        
        print("🚀 Starting AI Travel Platform...")
        print("📱 App will be available at: http://localhost:8501")
        print("⏹️  Press Ctrl+C to stop the app")
        print("")
        
        # Start browser in background
        browser_thread = threading.Thread(target=launch_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        # Start Streamlit
        sys.argv = [
            "streamlit", 
            "run", 
            "enhanced_streamlit_app.py",
            "--server.port", "8501",
            "--server.headless", "false"
        ]
        
        stcli.main()
        
    except ImportError as e:
        print(f"❌ Error: Streamlit not properly installed - {e}")
        print("💡 Try running: pip install streamlit")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"❌ Error starting app: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    start_streamlit()
