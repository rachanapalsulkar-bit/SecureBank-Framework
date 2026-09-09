from pages.signup_page import SignupPage
from utils.data_generator import DataGenerator


def test_signup(page):
    signup_page = SignupPage(page)
    signup_page.navigate()

    email = DataGenerator.generate_email()
    signup_page.signup("Rachana", email)
