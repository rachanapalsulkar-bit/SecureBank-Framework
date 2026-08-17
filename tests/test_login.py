import os
from pages.login_page import LoginPage
from pages.accounts_page import AccountsPage
from config.config import Config

def test_login_and_capture_accounts(page):
    login_page = LoginPage(page)
    accounts_page = AccountsPage(page)

    screenshot_dir = "D:\\Screenshot"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    # 1. Open Login Page and Authenticate
    login_page.open(Config.BASE_URL)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    # 2. CAPTURE DASHBOARD
    page.wait_for_url("**/bank/dashboard", wait_until="commit", timeout=15000)
    page.get_by_text("Welcome back,", exact=False).wait_for(state="visible", timeout=5000)
    page.screenshot(path=os.path.join(screenshot_dir, "Dashboard.png"), full_page=True)

    # 3. CAPTURE NOTIFICATIONS
    # The layout lists this item as "Notifications" followed by a counter badge '2'
    # We use a partial text match instead of an exact match to avoid counter issues
    page.get_by_text("Notifications", exact=False).click()
    
    # FIX: We remove wait_for_url() here because the URL does not change.
    # Instead, we pause briefly for the panel/view to update visually.
    page.wait_for_timeout(1000) 
    page.screenshot(path=os.path.join(screenshot_dir, "Notification.png"), full_page=True)

    # 4. CAPTURE ACCOUNTS
    page.get_by_text("Accounts", exact=True).click()
    page.wait_for_url("**/bank/accounts", wait_until="commit", timeout=15000)
    page.get_by_text("My Accounts", exact=True).wait_for(state="visible", timeout=5000)
    page.screenshot(path=os.path.join(screenshot_dir, "Accounts.png"), full_page=True)

    print("All 3 screenshots successfully saved!")
