@echo off
REM Quick test runner for Windows
REM Double-click this file to run tests

echo =====================================
echo  Shooters Global - Test Runner
echo =====================================
echo.

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Check if activation was successful
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    echo Please run: python -m venv .venv
    pause
    exit /b 1
)

echo.
echo Running tests...
echo.

REM Run pytest with verbose output
pytest tests/ -v -s

echo.
echo =====================================
echo  Test run completed!
echo =====================================
echo.

pause
