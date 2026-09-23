from playwright.sync_api import expect, Page
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.accountinfo_page import AccountInfoPage
from utils.data_generator import DataGenerator

def test_register_user(page: Page):
    login_page = LoginPage(page)
    unique_email = DataGenerator.generate_email()

    login_page.navigate()
    login_page.register_new_user("Rachana", unique_email)

    expect(page.locator("text=Enter Account Information")).to_be_visible(timeout=10000)
    
    account_page = AccountInfoPage(page)
    account_page.enter_account_information(
        password="Password123!",
        day="1",
        month="1",
        year="2000",
    )
    account_page.enter_address_information(
        first_name="Rachana",
        last_name="Palsulkar",
        company="ACL Digital",
        address="123 Main Street",
        country="United States",
        state="New York",
        city="New York",
        zipcode="10001",
        mobile="9999999999",
    )

    page.screenshot(path="screenshots/before_create_account.png")
    account_page.click_create_account()

    expect(page.locator("text=Account Created!")).to_be_visible(timeout=10000)
    page.screenshot(path="screenshots/account_created.png")
    print("Account created successfully")