import pytest
from pages.signup_page import SignupPage
from pages.locators.signup_locator import SignupLocator

@pytest.fixture
def login(page):
    login_page = SignupPage(page)

    login_page.navigate()
    login_page.login(
        "rachana.palsulkar@acldigital.com",
        "Password123"
    )

    return page

