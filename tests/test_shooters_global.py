"""
Test suite for Shooters Global Events website.
Tests the complete user flow: login, builder load, and logout.
"""
import pytest
import time
from utils.driver_factory import DriverFactory
from utils.config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.builder_page import BuilderPage


class TestShootersGlobal:
    """Test class for Shooters Global automation tests"""
    
    @pytest.fixture(scope="function")
    def driver(self):
        """
        Fixture to create and cleanup WebDriver instance for each test.
        
        Yields:
            WebDriver: Chrome WebDriver instance
        """
        driver = DriverFactory.create_driver()
        yield driver
        driver.quit()
    
    def test_login_builder_logout_flow(self, driver):
        """
        Test complete flow: open site, login, verify logged in, and logout.
        
        Test Steps:
        1. Open https://events.shooters.global/
        2. Click on 'Build for Free' button
        3. Login using credentials from .env file
        4. Verify user is logged in (check for avatar)
        5. Logout from the application
        
        Args:
            driver: WebDriver fixture
        """
        # Step 1: Open the home page
        home_page = HomePage(driver)
        home_page.open()
        print("✓ Opened home page")
        
        # Verify home page loaded
        assert home_page.is_build_for_free_button_visible(), \
            "Build for Free button is not visible on the home page"
        
        # Step 2: Click 'Build for Free' button
        home_page.click_build_for_free()
        print("✓ Clicked 'Build for Free' button")
        
        # Step 3: Login with credentials
        login_page = LoginPage(driver)
        
        # Verify we're on the login page
        assert login_page.is_login_form_visible(), \
            "Login form is not visible after clicking 'Build for Free'"
        
        # Perform login
        login_page.login(Config.EMAIL, Config.PASSWORD)
        print(f"✓ Logged in with email: {Config.EMAIL}")
        
        # Step 4: Verify user is logged in by checking avatar
        builder_page = BuilderPage(driver)
        
        # Check if user avatar is visible (indicates successful login)
        is_logged_in = builder_page.is_user_logged_in()
        assert is_logged_in, \
            "User avatar not found - login may have failed"
        print("✓ User is logged in (avatar found)")
        
        # Step 5: Logout
        builder_page.logout()
        print("✓ Logged out successfully")
        
        # Optional: verify logout by checking if we're redirected
        time.sleep(2)
        current_url = driver.current_url
        print(f"✓ Current URL after logout: {current_url}")
    
    def test_login_with_valid_credentials(self, driver):
        """
        Test login functionality with valid credentials.
        
        Args:
            driver: WebDriver fixture
        """
        home_page = HomePage(driver)
        home_page.open()
        home_page.click_build_for_free()
        
        login_page = LoginPage(driver)
        assert login_page.is_login_form_visible(), "Login form not visible"
        
        login_page.login(Config.EMAIL, Config.PASSWORD)
        
        # Verify successful login by checking if builder starts loading
        builder_page = BuilderPage(driver)
        time.sleep(3)  # Give some time for redirect
        
        # If builder canvas appears, login was successful
        builder_loaded = builder_page.is_builder_loaded()
        assert builder_loaded, "Login failed - builder did not load"
        print("✓ Login test passed - canvas found")
        
        # Try to click Next button if present
        builder_page.click_next_button()
