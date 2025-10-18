"""
WebDriver factory for creating and configuring browser instances.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.config import Config


class DriverFactory:
    """Factory class for creating WebDriver instances"""
    
    @staticmethod
    def create_driver():
        """
        Create and configure Chrome WebDriver instance.
        Uses Selenium Manager (built-in) for automatic driver management.
        
        Returns:
            webdriver.Chrome: Configured Chrome WebDriver instance
        """
        chrome_options = Options()
        
        # Add Chrome options
        if Config.HEADLESS:
            chrome_options.add_argument("--headless=new")  # New headless mode
        
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument(f"--window-size={Config.WINDOW_WIDTH},{Config.WINDOW_HEIGHT}")
        
        # Disable logging
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Selenium 4.6+ has built-in Selenium Manager that handles driver download
        # No need for webdriver-manager anymore
        driver = webdriver.Chrome(options=chrome_options)
        
        # Maximize window
        driver.maximize_window()
        
        return driver
