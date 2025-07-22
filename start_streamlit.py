import subprocess
import sys

print("Starting Streamlit app...")
try:
    result = subprocess.run([
        sys.executable, "-m", "streamlit", "run", 
        "enhanced_streamlit_app.py", 
        "--server.port", "8501"
    ], capture_output=True, text=True, timeout=10)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    print("Return code:", result.returncode)
except subprocess.TimeoutExpired:
    print("Command timed out - Streamlit is likely starting in background")
except Exception as e:
    print(f"Error: {e}")
