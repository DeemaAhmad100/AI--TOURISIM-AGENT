import sys
import os

print("=== System Information ===")
print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Current directory: {os.getcwd()}")
print(f"Script location: {os.path.dirname(os.path.abspath(__file__))}")

print("\n=== Testing Imports ===")
try:
    import streamlit as st
    print("✓ Streamlit imported successfully")
    print(f"Streamlit version: {st.__version__}")
except ImportError as e:
    print(f"✗ Streamlit import failed: {e}")

try:
    import pandas as pd
    print("✓ Pandas imported successfully")
except ImportError as e:
    print(f"✗ Pandas import failed: {e}")

try:
    import sqlite3
    print("✓ SQLite3 imported successfully")
except ImportError as e:
    print(f"✗ SQLite3 import failed: {e}")

print("\n=== File Check ===")
main_app = "enhanced_streamlit_app.py"
if os.path.exists(main_app):
    print(f"✓ {main_app} found")
    print(f"File size: {os.path.getsize(main_app)} bytes")
else:
    print(f"✗ {main_app} not found")

print("\n=== Testing App Import ===")
try:
    # Test if the app can be imported
    sys.path.insert(0, os.getcwd())
    import enhanced_streamlit_app
    print("✓ enhanced_streamlit_app imported successfully")
except Exception as e:
    print(f"✗ enhanced_streamlit_app import failed: {e}")

print("\nTest completed. Check results above.")
input("Press Enter to exit...")
