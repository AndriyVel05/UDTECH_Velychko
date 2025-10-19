from pages.base_page import BasePage
from utils.locators import HomePageLocators
from utils.config import Config


class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.BASE_URL
    
    def open(self):
        self.open_url(self.url)
    
    def click_build_for_free_button(self):
        self.click(HomePageLocators.BUILD_FOR_FREE_BUTTON, timeout=Config.EXTENDED_TIMEOUT)
    
    def is_build_for_free_button_visible(self):
        return self.is_element_present(HomePageLocators.BUILD_FOR_FREE_BUTTON, 
                                       timeout=Config.EXTENDED_TIMEOUT)