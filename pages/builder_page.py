from pages.base_page import BasePage
from utils.locators import BuilderPageLocators
from utils.config import Config


class BuilderPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_user_logged_in(self):
        try:
            print(f"Current URL: {self.get_current_url()}")
            print("Checking if user is logged in (looking for 'Touch Screen Mode' text)...")
            
            if self.is_element_present(BuilderPageLocators.TOUCH_SCREEN_MODE_TEXT, timeout=Config.EXTENDED_TIMEOUT):
                print("✓ 'Touch Screen Mode' text found - user is logged in to builder!")
                return True
            
            print("✗ 'Touch Screen Mode' text not found - user might not be logged in")
            return False
            
        except Exception as e:
            print(f"✗ Error checking login status: {e}")
            return False
    
    def click_dropdown_menu(self):
        try:
            print("Clicking dropdown menu...")
            self.click(BuilderPageLocators.DROPDOWN_MENU_TRIGGER, timeout=Config.EXTENDED_TIMEOUT)
            print("✓ Dropdown menu clicked")
            import time
            time.sleep(1)
        except Exception as e:
            print(f"Normal click failed, trying JavaScript: {e}")
            try:
                self.click_with_js(BuilderPageLocators.DROPDOWN_MENU_TRIGGER)
                print("✓ Dropdown menu clicked with JavaScript")
                import time
                time.sleep(1)
            except Exception as e2:
                print(f"✗ Failed to click dropdown menu: {e2}")
                try:
                    print("Trying alternative dropdown locator...")
                    self.click_with_js(BuilderPageLocators.DROPDOWN_MENU)
                    print("✓ Dropdown menu clicked (alternative)")
                    import time
                    time.sleep(1)
                except:
                    raise Exception("Could not click dropdown menu with any method")
    
    def click_logout(self):
        try:
            print("Clicking logout button...")
            
            if self.is_element_present(BuilderPageLocators.LOGOUT_BUTTON, timeout=10):
                self.click_with_js(BuilderPageLocators.LOGOUT_BUTTON)
                print("✓ Logout button clicked (button)")
                return
            
            if self.is_element_present(BuilderPageLocators.LOGOUT_BUTTON_CONFIRM, timeout=5):
                self.click_with_js(BuilderPageLocators.LOGOUT_BUTTON_CONFIRM)
                print("✓ Logout button clicked (p element)")
                return
            
            print("✗ Logout button not found")
            
        except Exception as e:
            print(f"✗ Error clicking logout: {e}")
            raise
    
    def logout(self):
        self.click_dropdown_menu()
        self.click_logout()
        import time
        time.sleep(2)
