from selenium.webdriver.common.by import By


class HomePageLocators:
    BUILD_FOR_FREE_BUTTON = (By.XPATH, "//section[@id='are-you-ready']/preceding-sibling::section//button")


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@name='emailOrPhoneNumber']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@type='submit']")
    OK_BUTTON_AFTER_LOGIN = (By.XPATH, "//button[@tabindex='-1']")


class BuilderPageLocators:
    TOUCH_SCREEN_MODE_TEXT = (By.XPATH, "//*[contains(text(), 'Touch Screen Mode')]")
    DROPDOWN_MENU_TRIGGER = (By.XPATH, "//button[@id='radix-vue-dropdown-menu-trigger-v-2-0']")
    DROPDOWN_MENU = (By.CSS_SELECTOR, "button[id*='dropdown-menu-trigger']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Log Out']")
    LOGOUT_BUTTON_CONFIRM = (By.XPATH, "//p[text()='Log Out']")
