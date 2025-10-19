import sys
import pytest

if __name__ == "__main__":
    exit_code = pytest.main([
        "tests/",
        "-v",
        "-s",
        "--tb=short"
    ])
    
sys.exit(exit_code)