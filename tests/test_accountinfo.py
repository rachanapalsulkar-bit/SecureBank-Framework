from playwright.sync_api import expect

from pages.accountinfo_page import AccountInfoPage
from pages.signup_page import SignupPage
from utils.data_generator import DataGenerator


def test_account_information(account_page):
    expect(account_page.page.locator("text=ENTER ACCOUNT INFORMATION")).to_be_visible(timeout=10000)

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
        state="NY",
        city="New York",
        zipcode="10001",
        mobile="9999999999",
    )

    account_page.click_create_account()

    expect(account_page.page.locator("text=ACCOUNT CREATED!")).to_be_visible(timeout=10000)
    account_page.page.screenshot(path="screenshots/account_created.png")
