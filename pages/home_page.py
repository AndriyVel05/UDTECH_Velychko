"""
Home Page object for https://events.shooters.global/
Contains methods specific to the home page.
"""
from pages.base_page import BasePage
from utils.locators import HomePageLocators
from utils.config import Config


class HomePage(BasePage):
    """Page Object for the Home Page"""
    
    def __init__(self, driver):
        """
        Initialize HomePage.
        
        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
        self.url = Config.BASE_URL
    
    def open(self):
        """Open the home page"""
        self.open_url(self.url)
    
    def click_build_for_free(self):
        """
        Click on the 'Build for Free' button.
        This action should navigate to the login page.
        """
        self.click(HomePageLocators.BUILD_FOR_FREE_BUTTON, timeout=Config.EXTENDED_TIMEOUT)
    
    def is_build_for_free_button_visible(self):
        """
        Check if 'Build for Free' button is visible.
        
        Returns:
            bool: True if button is visible, False otherwise
        """
        return self.is_element_present(HomePageLocators.BUILD_FOR_FREE_BUTTON, 
                                       timeout=Config.EXTENDED_TIMEOUT)
