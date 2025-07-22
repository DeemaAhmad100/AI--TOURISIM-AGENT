@echo off
echo ========================================
echo    AI Travel Platform Launcher
echo ========================================
echo.

echo [1/4] Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)

echo [2/4] Testing Streamlit installation...
python -c "import streamlit; print('Streamlit OK')" 2>nul
if %errorlevel% neq 0 (
    echo Installing/Updating Streamlit...
    pip install streamlit --quiet --no-warn-script-location
)

echo [3/4] Checking main app file...
if not exist "enhanced_streamlit_app.py" (
    echo ERROR: enhanced_streamlit_app.py not found!
    pause
    exit /b 1
)

echo [4/4] Starting Streamlit app...
echo.
echo App will be available at: http://localhost:8501
echo Press Ctrl+C to stop the app
echo.

start "" "http://localhost:8501"
python -m streamlit run enhanced_streamlit_app.py --server.port 8501

pause
