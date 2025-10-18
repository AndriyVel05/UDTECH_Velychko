# Quick test runner for Windows PowerShell
# Run this file: .\run_tests.ps1

Write-Host "=====================================" -ForegroundColor Cyan
Write-Host " Shooters Global - Test Runner" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow

try {
    & .\.venv\Scripts\Activate.ps1
    Write-Host "✓ Virtual environment activated" -ForegroundColor Green
} catch {
    Write-Host "✗ ERROR: Failed to activate virtual environment" -ForegroundColor Red
    Write-Host "Please run: python -m venv .venv" -ForegroundColor Yellow
    Read-Host -Prompt "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "Running tests..." -ForegroundColor Yellow
Write-Host ""

# Run pytest with verbose output
pytest tests/ -v -s

Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host " Test run completed!" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

Read-Host -Prompt "Press Enter to exit"
