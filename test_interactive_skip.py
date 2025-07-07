#!/usr/bin/env python3
"""
Test script for interactive setup with skip options
"""
import subprocess
import sys
import os

def test_interactive_setup_skip_all():
    """Test interactive setup by skipping all features"""
    print("Testing interactive setup with skip all features...")
    
    # Prepare inputs: 
    # 3 - Skip email setup
    # n - Skip payment setup
    # n - Skip Google services
    # n - Skip travel APIs
    # n - Skip dependency installation
    inputs = "3\nn\nn\nn\nn\n"
    
    try:
        # Change to the correct directory
        os.chdir(r"c:\Users\AYMAN\AI TRAVEL AGENT (TOURISIM)")
        
        # Run the interactive setup with inputs
        process = subprocess.Popen(
            [sys.executable, "interactive_setup.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        
        stdout, stderr = process.communicate(input=inputs, timeout=30)
        
        print("STDOUT:")
        print(stdout)
        
        if stderr:
            print("\nSTDERR:")
            print(stderr)
            
        print(f"\nReturn code: {process.returncode}")
        
        if process.returncode == 0:
            print("✅ Interactive setup completed successfully!")
        else:
            print("❌ Interactive setup failed!")
            
    except subprocess.TimeoutExpired:
        print("❌ Setup timed out!")
        process.kill()
    except Exception as e:
        print(f"❌ Error running setup: {e}")

def test_interactive_setup_partial():
    """Test interactive setup with partial configuration"""
    print("\nTesting interactive setup with partial configuration...")
    
    # Prepare inputs:
    # 3 - Skip email setup
    # y - Setup payment
    # test_pk - Test publishable key
    # test_sk - Test secret key
    # n - Skip Google services
    # n - Skip travel APIs
    # n - Skip dependency installation
    inputs = "3\ny\ntest_pk\ntest_sk\nn\nn\nn\n"
    
    try:
        # Change to the correct directory
        os.chdir(r"c:\Users\AYMAN\AI TRAVEL AGENT (TOURISIM)")
        
        # Run the interactive setup with inputs
        process = subprocess.Popen(
            [sys.executable, "interactive_setup.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'
        )
        
        stdout, stderr = process.communicate(input=inputs, timeout=30)
        
        print("STDOUT:")
        print(stdout)
        
        if stderr:
            print("\nSTDERR:")
            print(stderr)
            
        print(f"\nReturn code: {process.returncode}")
        
        if process.returncode == 0:
            print("✅ Interactive setup completed successfully!")
        else:
            print("❌ Interactive setup failed!")
            
    except subprocess.TimeoutExpired:
        print("❌ Setup timed out!")
        process.kill()
    except Exception as e:
        print(f"❌ Error running setup: {e}")

if __name__ == "__main__":
    print("AI Travel Platform - Interactive Setup Test")
    print("=" * 50)
    
    test_interactive_setup_skip_all()
    test_interactive_setup_partial()
    
    print("\n" + "=" * 50)
    print("Test completed!")
