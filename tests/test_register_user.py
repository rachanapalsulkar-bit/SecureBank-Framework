from playwright.sync_api import expect
from pages.accountinfo_page import AccountInfoPage
from pages.signup_page import SignupPage
from utils.data_generator import DataGenerator


def test_register_user(page):
    signup_page = SignupPage(page)
    unique_email = DataGenerator.generate_email()


    signup_page.navigate()
    signup_page.signup("Rachana", unique_email)


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
