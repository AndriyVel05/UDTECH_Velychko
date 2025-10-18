from pages.base_page import BasePage
from utils.locators import LoginPageLocators
from utils.config import Config


class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_email(self, email):
        self.enter_text(LoginPageLocators.EMAIL_FIELD, email, timeout=Config.EXTENDED_TIMEOUT)
    
    def enter_password(self, password):
        self.enter_text(LoginPageLocators.PASSWORD_FIELD, password)
    
    def click_sign_in(self):
        self.click(LoginPageLocators.SIGN_IN_BUTTON)
    
    def click_ok_after_login(self):
        try:
            if self.is_element_present(LoginPageLocators.OK_BUTTON_AFTER_LOGIN, timeout=Config.EXTENDED_TIMEOUT):
                self.click(LoginPageLocators.OK_BUTTON_AFTER_LOGIN, timeout=Config.DEFAULT_TIMEOUT)
                return True
        except Exception as e:
            print(f"OK button not found or not clickable: {e}")
            pass
        return False
    
    def login(self, email, password):
        try:
            self.enter_email(email)
            self.enter_password(password)
            self.click_sign_in()
            
            import time
            time.sleep(2)
            
            ok_clicked = self.click_ok_after_login()
            if ok_clicked:
                print("✓ OK button clicked after login")
                time.sleep(3)
            else:
                print("✓ OK button not present, proceeding...")
                time.sleep(2)
            
            return True
        except Exception as e:
            print(f"✗ Login error: {e}")
            return False
    
    def is_login_form_visible(self):
        return self.is_element_present(LoginPageLocators.EMAIL_FIELD, 
                                       timeout=Config.DEFAULT_TIMEOUT)
