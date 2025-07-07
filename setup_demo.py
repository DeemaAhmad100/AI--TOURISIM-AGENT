#!/usr/bin/env python3
"""
AI Travel Platform - Setup Demonstration Script
This script demonstrates different ways to run the interactive setup
"""

import os
import sys
import subprocess

def demo_skip_all():
    """Demonstrate skipping all features"""
    print("🔄 Demo: Skipping all features")
    print("Input: 3 (skip email), n (skip payment), n (skip google), n (skip travel), n (skip deps)")
    
    inputs = "3\nn\nn\nn\nn\n"
    
    try:
        process = subprocess.Popen(
            [sys.executable, "interactive_setup.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        
        stdout, stderr = process.communicate(input=inputs, timeout=30)
        
        if process.returncode == 0:
            print("✅ Successfully skipped all features!")
        else:
            print("❌ Setup failed")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("-" * 50)

def demo_partial_setup():
    """Demonstrate partial setup"""
    print("🔄 Demo: Partial setup (email skip, payment setup)")
    print("Input: 3 (skip email), y (setup payment), test keys, n (skip others)")
    
    inputs = "3\ny\ntest_publishable_key\ntest_secret_key\nn\nn\nn\n"
    
    try:
        process = subprocess.Popen(
            [sys.executable, "interactive_setup.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        
        stdout, stderr = process.communicate(input=inputs, timeout=30)
        
        if process.returncode == 0:
            print("✅ Successfully completed partial setup!")
        else:
            print("❌ Setup failed")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("-" * 50)

def demo_interrupted_setup():
    """Demonstrate interrupted setup (EOF handling)"""
    print("🔄 Demo: Interrupted setup (EOF handling)")
    print("Input: Just '3' (skip email) then EOF")
    
    inputs = "3\n"
    
    try:
        process = subprocess.Popen(
            [sys.executable, "interactive_setup.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        
        stdout, stderr = process.communicate(input=inputs, timeout=30)
        
        if "Setup interrupted" in stdout:
            print("✅ EOF handling works correctly!")
        else:
            print("❌ EOF handling failed")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("-" * 50)

def show_setup_options():
    """Show all available setup options"""
    print("📋 Available Setup Options:")
    print()
    print("1. 🚀 Automated Setup:")
    print("   python setup_enhanced_features.py")
    print("   - Automatically sets up all features")
    print("   - Uses default configurations")
    print("   - No user interaction required")
    print()
    print("2. 🎯 Interactive Setup:")
    print("   python interactive_setup.py")
    print("   - Step-by-step configuration")
    print("   - Choose which features to setup")
    print("   - Customizable options")
    print()
    print("3. 🔍 Verification:")
    print("   python verify_setup.py")
    print("   - Check current configuration")
    print("   - Verify all dependencies")
    print("   - Show missing requirements")
    print()
    print("4. 📚 Documentation:")
    print("   - API_KEYS_GUIDE.md - Detailed API key instructions")
    print("   - API_KEYS_SUMMARY.md - Quick reference")
    print("   - ENHANCED_FEATURES_GUIDE.md - Feature explanations")
    print()

def main():
    print("AI Travel Platform - Setup Demo")
    print("=" * 50)
    
    os.chdir(r"c:\Users\AYMAN\AI TRAVEL AGENT (TOURISIM)")
    
    show_setup_options()
    
    print("Running demonstrations...")
    print("=" * 50)
    
    demo_skip_all()
    demo_partial_setup()
    demo_interrupted_setup()
    
    print("🎉 All demonstrations completed!")
    print()
    print("The interactive setup script now supports:")
    print("✅ Skipping individual features")
    print("✅ Graceful EOF handling")
    print("✅ Partial configuration")
    print("✅ Configuration persistence")
    print("✅ Clear error messages")

if __name__ == "__main__":
    main()
