"""
Base Page class that contains common methods for all page objects.
Implements the Page Object Model pattern.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.config import Config


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, driver):
        """
        Initialize the BasePage with WebDriver instance.
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.timeout = Config.DEFAULT_TIMEOUT
    
    def open_url(self, url):
        """
        Open the specified URL.
        
        Args:
            url (str): URL to open
        """
        self.driver.get(url)
    
    def find_element(self, locator, timeout=None):
        """
        Find a single element with explicit wait.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "locator_value")
            timeout (int, optional): Custom timeout in seconds
            
        Returns:
            WebElement: Found element
        """
        wait_time = timeout if timeout else self.timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator)
        )
    
    def find_clickable_element(self, locator, timeout=None):
        """
        Find a clickable element with explicit wait.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "locator_value")
            timeout (int, optional): Custom timeout in seconds
            
        Returns:
            WebElement: Clickable element
        """
        wait_time = timeout if timeout else self.timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(locator)
        )
    
    def click(self, locator, timeout=None):
        """
        Click on an element.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "locator_value")
            timeout (int, optional): Custom timeout in seconds
        """
        element = self.find_clickable_element(locator, timeout)
        element.click()
    
    def enter_text(self, locator, text, timeout=None):
        """
        Enter text into an input field.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "locator_value")
            text (str): Text to enter
            timeout (int, optional): Custom timeout in seconds
        """
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def wait_for_element_visible(self, locator, timeout=None):
        """
        Wait for element to be visible.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "locator_value")
            timeout (int, optional): Custom timeout in seconds
            
        Returns:
            bool: True if element is visible, False otherwise
        """
        wait_time = timeout if timeout else self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def is_element_present(self, locator, timeout=None):
        """
        Check if element is present on the page.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "locator_value")
            timeout (int, optional): Custom timeout in seconds
            
        Returns:
            bool: True if element is present, False otherwise
        """
        wait_time = timeout if timeout else self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def wait_for_element_to_disappear(self, locator, timeout=None):
        """
        Wait for element to disappear from the page.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "locator_value")
            timeout (int, optional): Custom timeout in seconds
            
        Returns:
            bool: True if element disappeared, False if still present
        """
        wait_time = timeout if timeout else self.timeout
        try:
            WebDriverWait(self.driver, wait_time).until_not(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
    
    def get_current_url(self):
        """
        Get the current URL.
        
        Returns:
            str: Current URL
        """
        return self.driver.current_url
    
    def execute_script(self, script, *args):
        """
        Execute JavaScript code.
        
        Args:
            script (str): JavaScript code to execute
            *args: Arguments to pass to the script
            
        Returns:
            Any: Result of script execution
        """
        return self.driver.execute_script(script, *args)
    
    def click_with_js(self, locator, timeout=None):
        """
        Click element using JavaScript (useful when normal click doesn't work).
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "locator_value")
            timeout (int, optional): Custom timeout in seconds
        """
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].click();", element)
    
    def scroll_to_element(self, locator, timeout=None):
        """
        Scroll to element using JavaScript.
        
        Args:
            locator (tuple): Locator tuple (By.TYPE, "locator_value")
            timeout (int, optional): Custom timeout in seconds
        """
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
