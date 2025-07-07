#!/usr/bin/env python3
"""
🚀 AI Travel Platform - Investor Presentation Launcher
Run this to start the professional investor presentation
"""

import subprocess
import sys
import os
import webbrowser
import time

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['streamlit', 'pandas', 'plotly']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   • {package}")
        print()
        print("💡 Install missing packages with:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False
    
    return True

def run_presentation():
    """Launch the investor presentation"""
    print("🌍 AI Travel Platform - Investor Presentation")
    print("=" * 60)
    print()
    print("🎯 Launching professional investor presentation...")
    print("📊 Interactive charts, live demos, and financial projections")
    print("💼 Designed to impress potential investors")
    print()
    
    if not check_dependencies():
        print("❌ Cannot start presentation due to missing dependencies.")
        return
    
    print("🚀 Starting Streamlit application...")
    print("🌐 Opening in your default browser...")
    print()
    print("💡 Tips:")
    print("   • Use the interactive AI demo to showcase our technology")
    print("   • Navigate through all sections for full investor experience")
    print("   • Press Ctrl+C in this terminal to stop the presentation")
    print()
    
    try:
        # Start Streamlit with optimized settings for presentation
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "investor_presentation.py",
            "--server.port", "8501",
            "--server.headless", "true",
            "--browser.gatherUsageStats", "false",
            "--theme.base", "light",
            "--theme.primaryColor", "#4ECDC4",
            "--theme.backgroundColor", "#FFFFFF",
            "--theme.secondaryBackgroundColor", "#F8F9FA"
        ])
    except KeyboardInterrupt:
        print("\n\n👋 Presentation ended successfully!")
        print("🎯 Ready to meet with investors? Contact: investors@aitravelplatform.com")
    except FileNotFoundError:
        print("❌ Streamlit not found. Install with: pip install streamlit")
    except Exception as e:
        print(f"❌ Error starting presentation: {e}")
        print("💡 Try running directly: streamlit run investor_presentation.py")

if __name__ == "__main__":
    run_presentation()
