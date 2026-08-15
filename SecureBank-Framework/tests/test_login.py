import os
import re
from pages.login_page import LoginPage
from pages.accounts_page import AccountsPage
from config.config import Config

def test_login_and_capture_accounts(page):
    login_page = LoginPage(page)
    accounts_page = AccountsPage(page)

    # 1. Open Login Page and Authenticate
    login_page.open(Config.BASE_URL)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    # 2. Wait for Dashboard (Using lowercase pattern to match the actual URL string)
    # Using wait_until="commit" handles the SPA routing transition perfectly without timing out
    page.wait_for_url("**/bank/dashboard", wait_until="commit", timeout=15000)
    assert "dashboard" in page.url.lower()

    # 3. Handle navigating to Accounts via your Page Object or directly
    # Replace this direct click with an accounts_page method if you have one defined!
    page.get_by_text("Accounts", exact=True).click()

    # 4. Wait for Accounts URL transition
    page.wait_for_url("**/bank/accounts", wait_until="commit", timeout=15000)
    
    # 5. Verify the target element on the view is ready
    page.get_by_text("Notifications", exact=True).wait_for(state="visible", timeout=5000)

    # 6. Ensure target folder exists and save the screenshot correctly
    screenshot_dir = "D:\\Screenshot"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
        
    # Execute the actual Playwright method call
    page.screenshot(path=os.path.join(screenshot_dir, "My Accounts Details.png"), full_page=True)
    print("Screenshot successfully captured!")
