from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.config import Config


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = Config.DEFAULT_TIMEOUT
    
    def open_url(self, url):
        self.driver.get(url)
    
    def find_element(self, locator, timeout=None):
        wait_time = timeout if timeout else self.timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator)
        )
    
    def find_clickable_element(self, locator, timeout=None):
        wait_time = timeout if timeout else self.timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(locator)
        )
    
    def click(self, locator, timeout=None):
        element = self.find_clickable_element(locator, timeout)
        element.click()
    
    def enter_text(self, locator, text, timeout=None):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def is_element_present(self, locator, timeout=None):
        wait_time = timeout if timeout else self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        return self.driver.current_url