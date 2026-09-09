import pytest
from playwright.sync_api import sync_playwright
from pages.signup_page import SignupPage
from pages.accountinfo_page import AccountInfoPage


@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )
        page = browser.new_page()
        yield page
        #browser.close()

@pytest.fixture
def account_page(page):
    signup = SignupPage(page)
    signup.navigate()
    signup.register_new_user("Rachana", "rachana.palsulkar@acldigital.com")
    return AccountInfoPage(page)

import uuid

@pytest.fixture
def unique_email():
    return f"rachana_{uuid.uuid4().hex[:8]}@acldigital.com"

@pytest.fixture
def account_page(page, unique_email):

    signup = SignupPage(page)

    signup.navigate()

    signup.signup(
        "Rachana",
        unique_email
    )

    return AccountInfoPage(page)