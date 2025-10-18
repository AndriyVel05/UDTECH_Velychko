"""
Login Page object.
Contains methods for user authentication.
"""
from pages.base_page import BasePage
from utils.locators import LoginPageLocators
from utils.config import Config


class LoginPage(BasePage):
    """Page Object for the Login Page"""
    
    def __init__(self, driver):
        """
        Initialize LoginPage.
        
        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
    
    def enter_email(self, email):
        """
        Enter email into the email field.
        
        Args:
            email (str): Email address to enter
        """
        self.enter_text(LoginPageLocators.EMAIL_FIELD, email, timeout=Config.EXTENDED_TIMEOUT)
    
    def enter_password(self, password):
        """
        Enter password into the password field.
        
        Args:
            password (str): Password to enter
        """
        self.enter_text(LoginPageLocators.PASSWORD_FIELD, password)
    
    def click_sign_in(self):
        """Click the Sign In button"""
        self.click(LoginPageLocators.SIGN_IN_BUTTON)
    
    def click_ok_after_login(self):
        """
        Click the OK button that appears after successful login.
        This button may appear as a confirmation dialog.
        Waits for button to be clickable before attempting to click.
        
        Returns:
            bool: True if OK button was found and clicked, False otherwise
        """
        try:
            # Wait for OK button to appear and be clickable
            if self.is_element_present(LoginPageLocators.OK_BUTTON_AFTER_LOGIN, timeout=Config.EXTENDED_TIMEOUT):
                self.click(LoginPageLocators.OK_BUTTON_AFTER_LOGIN, timeout=Config.DEFAULT_TIMEOUT)
                return True
        except Exception as e:
            # OK button might not always appear, so we handle it gracefully
            print(f"OK button not found or not clickable: {e}")
            pass
        return False
    
    def login(self, email, password):
        """
        Complete login process with improved OK button handling.
        
        Args:
            email (str): Email address
            password (str): Password
            
        Returns:
            bool: True if login completed (with or without OK button), False on error
        """
        try:
            self.enter_email(email)
            self.enter_password(password)
            self.click_sign_in()
            
            # Wait a bit after sign in for the page to respond
            import time
            time.sleep(2)
            
            # Wait and click OK button if it appears
            ok_clicked = self.click_ok_after_login()
            if ok_clicked:
                print("✓ OK button clicked after login")
                # Wait for the dialog to close and page to redirect
                time.sleep(3)
            else:
                print("✓ OK button not present, proceeding...")
                # Even if no OK button, wait for potential redirect
                time.sleep(2)
            
            return True
        except Exception as e:
            print(f"✗ Login error: {e}")
            return False
    
    def is_login_form_visible(self):
        """
        Check if login form is visible.
        
        Returns:
            bool: True if login form is visible, False otherwise
        """
        return self.is_element_present(LoginPageLocators.EMAIL_FIELD, 
                                       timeout=Config.DEFAULT_TIMEOUT)
