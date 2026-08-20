import os
from datetime import datetime
from pages.login_page import LoginPage
from pages.accounts_page import AccountsPage
from config.config import Config
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def test_login_and_capture_accounts(page):

    login_page = LoginPage(page)
    accounts_page = AccountsPage(page)
    screenshot_dir = r"D:\Screenshot"

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # Login
    login_page.open(Config.BASE_URL)
    login_page.login(Config.USERNAME,Config.PASSWORD)

    # Dashboard Screenshot
    page.wait_for_url("**/bank/dashboard",timeout=15000)

    page.screenshot(path=os.path.join(screenshot_dir,f"Dashboard_{current_time}.png"),full_page=True)

    # Notification Screenshot
    page.get_by_text("Notifications",exact=False).click()
    page.wait_for_timeout(1000)
    page.screenshot(path=os.path.join(screenshot_dir,f"Notification_{current_time}.png"),full_page=True)

    # Close notification panel
    page.keyboard.press("Escape")
    page.wait_for_timeout(1000)

    # Navigate to Accounts
    page.get_by_text("Accounts",exact=False).click()
    page.wait_for_url("**/bank/accounts",timeout=15000)

    # Create Account
    accounts_page.add_account(account_name="Salary Account",account_type="Checking",starting_balance="5000")

    # Verify Account
    accounts_page.verify_account_exists("Salary Account")

    # Accounts Screenshot
    accounts_page.capture_screenshot(os.path.join(screenshot_dir,f"Accounts_{current_time}.png"))
    print("All screenshots saved successfully!")