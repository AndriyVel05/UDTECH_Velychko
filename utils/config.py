import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent.parent
dotenv_path = PROJECT_ROOT / '.env'
load_dotenv(dotenv_path=dotenv_path)


class Config:
    BASE_URL = "https://events.shooters.global/"
    DEFAULT_TIMEOUT = 10
    EXTENDED_TIMEOUT = 30
    HEADLESS = False
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1080