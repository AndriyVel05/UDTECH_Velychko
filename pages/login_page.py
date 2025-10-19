from pages.base_page import BasePage
from utils.locators import LoginPageLocators
from utils.config import Config
from utils.locators import BuilderPageLocators

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def login(self, email, password):
        try:
            self.enter_text(LoginPageLocators.EMAIL_FIELD, email, timeout=Config.EXTENDED_TIMEOUT)
            self.enter_text(LoginPageLocators.PASSWORD_FIELD, password)
            self.click(LoginPageLocators.SIGN_IN_BUTTON)
            self.wait_for_page_load()
            
            try:
                if self.is_element_present(LoginPageLocators.OK_BUTTON_AFTER_LOGIN, timeout=Config.EXTENDED_TIMEOUT):
                    self.click(LoginPageLocators.OK_BUTTON_AFTER_LOGIN, timeout=Config.DEFAULT_TIMEOUT)
                    print("✓ OK button clicked after login")
                    self.is_element_present(BuilderPageLocators.TOUCH_SCREEN_MODE_TEXT, timeout=Config.EXTENDED_TIMEOUT)
                else:
                    print("✓ OK button not present, proceeding...")
            except Exception as e:
                print(f"OK button not found or not clickable: {e}")
            
            return True
        except Exception as e:
            print(f"✗ Login error: {e}")
            return False
    
    def is_login_form_visible(self):
        return self.is_element_present(LoginPageLocators.EMAIL_FIELD, 
                                       timeout=Config.DEFAULT_TIMEOUT)