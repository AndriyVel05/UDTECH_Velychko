from utils.driver_factory import DriverFactory
from utils.config import Config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time

print("=" * 60)
print("DIAGNOSTIC SCRIPT - Builder Loading Debug")
print("=" * 60)

driver = DriverFactory.create_driver()

try:
    print("\n[1] Opening home page...")
    home = HomePage(driver)
    home.open()
    time.sleep(2)
    print(f"    URL: {driver.current_url}")
    
    print("\n[2] Clicking 'Build for Free'...")
    home.click_build_for_free()
    time.sleep(3)
    print(f"    URL: {driver.current_url}")
    
    print("\n[3] Logging in...")
    login = LoginPage(driver)
    login.login(Config.EMAIL, Config.PASSWORD)
    time.sleep(5)
    print(f"    URL after login: {driver.current_url}")
    
    print("\n[4] Looking for canvas elements...")
    
    canvases = driver.find_elements(By.TAG_NAME, "canvas")
    print(f"    Found {len(canvases)} canvas element(s)")
    
    for i, canvas in enumerate(canvases):
        print(f"\n    Canvas #{i+1}:")
        print(f"      ID: {canvas.get_attribute('id')}")
        print(f"      Class: {canvas.get_attribute('class')}")
        print(f"      Width: {canvas.get_attribute('width')}")
        print(f"      Height: {canvas.get_attribute('height')}")
        print(f"      Displayed: {canvas.is_displayed()}")
    
    print("\n[5] Looking for unity-app-canvas specifically...")
    try:
        unity_canvas = driver.find_element(By.ID, "unity-app-canvas")
        print(f"    ✓ Found unity-app-canvas!")
        print(f"      Displayed: {unity_canvas.is_displayed()}")
        print(f"      Enabled: {unity_canvas.is_enabled()}")
    except Exception as e:
        print(f"    ✗ unity-app-canvas not found: {e}")
    
    print("\n[6] Looking for Next button...")
    try:
        next_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Next') or contains(text(), 'next') or contains(@class, 'next')]")
        print(f"    Found {len(next_buttons)} potential Next button(s)")
        for i, btn in enumerate(next_buttons):
            print(f"      Button #{i+1}: text='{btn.text}', visible={btn.is_displayed()}")
    except Exception as e:
        print(f"    Error finding Next buttons: {e}")
    
    print("\n[7] Page source snippet (first 2000 chars):")
    print("-" * 60)
    print(driver.page_source[:2000])
    print("-" * 60)
    
    print("\n[8] Taking screenshot...")
    screenshot_path = "diagnostic_after_login.png"
    driver.save_screenshot(screenshot_path)
    print(f"    Screenshot saved: {screenshot_path}")
    
    print("\n" + "=" * 60)
    print("Browser will stay open for manual inspection.")
    print("Check the browser window and the screenshot.")
    print("=" * 60)
    input("\nPress Enter to close browser and exit...")

except Exception as e:
    print(f"\n✗ ERROR: {e}")
    import traceback
    traceback.print_exc()
    
    try:
        driver.save_screenshot("diagnostic_error.png")
        print("Screenshot saved: diagnostic_error.png")
    except:
        pass
    
    input("\nPress Enter to close browser...")

finally:
    driver.quit()
    print("\nBrowser closed.")
