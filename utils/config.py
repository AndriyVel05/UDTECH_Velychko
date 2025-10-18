"""
Configuration file for the project.
Stores URLs, timeouts, and other configuration settings.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Get the project root directory (parent of utils folder)
PROJECT_ROOT = Path(__file__).parent.parent

# Load environment variables from .env file in project root
dotenv_path = PROJECT_ROOT / '.env'
load_dotenv(dotenv_path=dotenv_path)


class Config:
    """Configuration class for storing project settings"""
    
    # URL Configuration
    BASE_URL = "https://events.shooters.global/"
    
    # Timeouts (in seconds)
    DEFAULT_TIMEOUT = 10
    EXTENDED_TIMEOUT = 30
    BUILDER_LOAD_TIMEOUT = 60
    
    # Browser Configuration
    BROWSER = "chrome"
    HEADLESS = False  # Set to True to run in headless mode
    
    # Credentials from .env file
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    
    # Window size
    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1080
