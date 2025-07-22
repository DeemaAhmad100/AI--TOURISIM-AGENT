@echo off
echo ========================================
echo   AI Travel Agent Platform Launcher
echo ========================================
echo.

cd /d "%~dp0"

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python not found in PATH
    echo Please install Python or add it to your PATH
    pause
    exit /b 1
)
echo Python found successfully!
echo.

echo Starting AI Travel Agent Platform...
echo This will open your browser automatically
echo Press Ctrl+C to stop the application
echo.

python direct_runner.py

pause
