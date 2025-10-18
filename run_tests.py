"""
Quick test runner script.
Run this file to execute all tests: python run_tests.py
"""
import sys
import pytest

if __name__ == "__main__":
    # Run pytest with verbose output and show print statements
    exit_code = pytest.main([
        "tests/",
        "-v",           # Verbose output
        "-s",           # Show print statements
        "--tb=short"    # Short traceback format
    ])
    
    sys.exit(exit_code)
