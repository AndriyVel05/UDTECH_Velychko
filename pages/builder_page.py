"""
Builder Page object.
Contains methods for interacting with the builder interface.
"""
from pages.base_page import BasePage
from utils.locators import BuilderPageLocators
from utils.config import Config


class BuilderPage(BasePage):
    """Page Object for the Builder Page"""
    
    def __init__(self, driver):
        """
        Initialize BuilderPage.
        
        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
    
    def is_user_logged_in(self):
        """
        Check if user is logged in by verifying "Touch Screen Mode" text presence.
        
        Returns:
            bool: True if "Touch Screen Mode" text found (logged in to builder), False otherwise
        """
        try:
            print(f"Current URL: {self.get_current_url()}")
            print("Checking if user is logged in (looking for 'Touch Screen Mode' text)...")
            
            # Check for "Touch Screen Mode" text
            if self.is_element_present(BuilderPageLocators.TOUCH_SCREEN_MODE_TEXT, timeout=Config.EXTENDED_TIMEOUT):
                print("✓ 'Touch Screen Mode' text found - user is logged in to builder!")
                return True
            
            print("✗ 'Touch Screen Mode' text not found - user might not be logged in")
            return False
            
        except Exception as e:
            print(f"✗ Error checking login status: {e}")
            return False
    
    def click_dropdown_menu(self):
        """
        Click the dropdown menu trigger button (user avatar/account menu).
        This opens the user menu with logout option.
        Uses JavaScript click as fallback.
        """
        try:
            print("Clicking dropdown menu...")
            self.click(BuilderPageLocators.DROPDOWN_MENU_TRIGGER, timeout=Config.EXTENDED_TIMEOUT)
            print("✓ Dropdown menu clicked")
            import time
            time.sleep(1)  # Wait for menu to open
        except Exception as e:
            print(f"Normal click failed, trying JavaScript: {e}")
            try:
                self.click_with_js(BuilderPageLocators.DROPDOWN_MENU_TRIGGER)
                print("✓ Dropdown menu clicked with JavaScript")
                import time
                time.sleep(1)
            except Exception as e2:
                print(f"✗ Failed to click dropdown menu: {e2}")
                # Try alternative locator
                try:
                    print("Trying alternative dropdown locator...")
                    self.click_with_js(BuilderPageLocators.DROPDOWN_MENU_ALT)
                    print("✓ Dropdown menu clicked (alternative)")
                    import time
                    time.sleep(1)
                except:
                    raise Exception("Could not click dropdown menu with any method")
    
    def click_logout(self):
        """
        Click the Logout button from the dropdown menu.
        Tries both //button[text()='Log Out'] and //p[text()='Log Out']
        Uses JavaScript click as fallback.
        """
        try:
            print("Clicking logout button...")
            
            # Try primary logout button (button element)
            if self.is_element_present(BuilderPageLocators.LOGOUT_BUTTON, timeout=10):
                self.click_with_js(BuilderPageLocators.LOGOUT_BUTTON)
                print("✓ Logout button clicked (button)")
                return
            
            # Try alternative logout button (p element)
            if self.is_element_present(BuilderPageLocators.LOGOUT_BUTTON_ALT, timeout=5):
                self.click_with_js(BuilderPageLocators.LOGOUT_BUTTON_ALT)
                print("✓ Logout button clicked (p element)")
                return
            
            print("✗ Logout button not found")
            
        except Exception as e:
            print(f"✗ Error clicking logout: {e}")
            raise
    
    def logout(self):
        """
        Perform complete logout process.
        Opens dropdown menu and clicks logout button.
        """
        self.click_dropdown_menu()
        self.click_logout()
        import time
        time.sleep(2)  # Wait for logout to complete
