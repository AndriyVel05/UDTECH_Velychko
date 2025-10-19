from pages.base_page import BasePage
from utils.locators import BuilderPageLocators
from utils.config import Config


class BuilderPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_user_logged_in(self):
        try:
            print(f"✓ Current URL: {self.get_current_url()}")
            print("✓ Checking if user is logged in (looking for 'Touch Screen Mode' text)...")
            
            if self.is_element_present(BuilderPageLocators.TOUCH_SCREEN_MODE_TEXT, timeout=Config.EXTENDED_TIMEOUT):
                print("✓ 'Touch Screen Mode' text found - user is logged in to builder!")
                return True
            
            print("✗ 'Touch Screen Mode' text not found - user might not be logged in")
            return False
            
        except Exception as e:
            print(f"✗ Error checking login status: {e}")
            return False
    
    def logout(self):
        print("✓ Clicking dropdown menu...")
        self.click(BuilderPageLocators.DROPDOWN_MENU_TRIGGER, timeout=Config.EXTENDED_TIMEOUT)
        print("✓ Dropdown menu clicked")
        
        print("✓ Clicking logout button...")
        if self.is_element_present(BuilderPageLocators.LOGOUT_BUTTON, timeout=Config.DEFAULT_TIMEOUT):
            self.click(BuilderPageLocators.LOGOUT_BUTTON, timeout=Config.EXTENDED_TIMEOUT)
            print("✓ Logout button clicked")
        elif self.is_element_present(BuilderPageLocators.LOGOUT_BUTTON_CONFIRM, timeout=Config.DEFAULT_TIMEOUT):
            self.click(BuilderPageLocators.LOGOUT_BUTTON_CONFIRM, timeout=Config.EXTENDED_TIMEOUT)
            print("✓ Logout button clicked (alternative locator)")