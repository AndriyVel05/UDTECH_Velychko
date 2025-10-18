"""
Locators for all pages in the application.
Stores all XPath and CSS selectors used in the tests.
"""
from selenium.webdriver.common.by import By


class HomePageLocators:
    """Locators for the Home Page"""
    BUILD_FOR_FREE_BUTTON = (By.XPATH, "//section[@id='are-you-ready']/preceding-sibling::section//button")


class LoginPageLocators:
    """Locators for the Login Page"""
    EMAIL_FIELD = (By.XPATH, "//input[@name='emailOrPhoneNumber']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@type='submit']")
    OK_BUTTON_AFTER_LOGIN = (By.XPATH, "//button[@tabindex='-1']")


class BuilderPageLocators:
    """Locators for the Builder Page"""
    # Text "Touch Screen Mode" (indicates successful login to builder)
    TOUCH_SCREEN_MODE_TEXT = (By.XPATH, "//*[contains(text(), 'Touch Screen Mode')]")
    
    # Dropdown menu and logout
    DROPDOWN_MENU_TRIGGER = (By.XPATH, "//button[@id='radix-vue-dropdown-menu-trigger-v-2-0']")
    DROPDOWN_MENU_ALT = (By.CSS_SELECTOR, "button[id*='dropdown-menu-trigger']")
    
    # Logout button in dropdown
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Log Out']")
    LOGOUT_BUTTON_ALT = (By.XPATH, "//p[text()='Log Out']")
