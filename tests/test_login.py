import os
from datetime import datetime
from pages.login_page import LoginPage
from pages.accounts_page import AccountsPage
from config.config import Config
import allure
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

@allure.title("Login and Create Account")
@allure.description("Verify user can login and create an account")

def test_login_and_capture_accounts(page):

    with allure.step("Login to application"):
     login_page = LoginPage(page)
     accounts_page = AccountsPage(page)
     screenshot_dir = r"D:\Screenshot"

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

# Login
    
    login_page.open(Config.BASE_URL)
    login_page.login(Config.USERNAME, Config.PASSWORD)

# Wait for Dashboard
    page.wait_for_url("**/bank/dashboard", timeout=15000)

# Notification Screenshot
    page.get_by_text("Notifications", exact=False).click()
    page.wait_for_timeout(1000)
    page.screenshot(
    path=os.path.join(
        screenshot_dir,
        f"Notification_{current_time}.png"
    ),
    full_page=True
)

# Close notification panel
    page.keyboard.press("Escape")
    page.wait_for_timeout(1000)

# Navigate to Accounts
    with allure.step("Navigate to Accounts"):
     page.get_by_text("Accounts", exact=False).click()
     page.wait_for_url("**/bank/accounts", timeout=15000)

# Accounts Page Screenshot
    page.screenshot(
    path=os.path.join(
        screenshot_dir,
        f"Accounts_Page_{current_time}.png"
    ),
    full_page=True
)

# Create Account
    with allure.step("Create Salary Account"):
       accounts_page.add_account(
    account_name="Salary Account",
    account_type="Checking",
    starting_balance="500"
)
# Verify Account
    with allure.step("Verify account creation"):
     accounts_page.verify_account_exists("Salary Account")

# Final Accounts Screenshot
    accounts_page.capture_screenshot(
    os.path.join(
        screenshot_dir,
        f"Accounts_After_Create_{current_time}.png"
    )
)

print("All screenshots saved successfully!")