import pytest
from utils.driver_factory import DriverFactory
from utils.config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.builder_page import BuilderPage


class TestShootersGlobal:
    
    @pytest.fixture(scope="function")
    def driver(self):
        driver = DriverFactory.create_driver()
        yield driver
        driver.quit()
    
    def test_login_builder_logout_flow(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        print("✓ Opened home page")
        
        assert home_page.is_build_for_free_button_visible(), \
            "❌ Build for Free button is not visible on the home page"
        
        home_page.click_build_for_free_button()
        print("✓ Clicked 'Build for Free' button")
        
        login_page = LoginPage(driver)
        
        assert login_page.is_login_form_visible(), \
            "❌ Login form is not visible after clicking 'Build for Free'"
        
        login_page.login(Config.EMAIL, Config.PASSWORD)
        print(f"✓ Logged in with email: {Config.EMAIL}")
        
        builder_page = BuilderPage(driver)
        
        is_logged_in = builder_page.is_user_logged_in()
        assert is_logged_in, \
            "❌ User avatar not found - login may have failed"
        print("✓ User is logged in (avatar found)")
        
        builder_page.logout()
        print("✓ Logged out successfully")
        
        current_url = driver.current_url
        print(f"✓ Current URL after logout: {current_url}")