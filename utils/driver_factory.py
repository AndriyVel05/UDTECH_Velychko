from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config import Config


class DriverFactory:
    
    @staticmethod
    def create_driver():
        chrome_options = Options()
        
        if Config.HEADLESS:
            chrome_options.add_argument("--headless=new")
        
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument(f"--window-size={Config.WINDOW_WIDTH},{Config.WINDOW_HEIGHT}")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        
        return driver
