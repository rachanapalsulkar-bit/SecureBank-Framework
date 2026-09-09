from playwright.sync_api import Page


class SignupPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://automationexercise.com/login")

    def signup(self, name, email):
        self.page.locator('input[data-qa="signup-name"]').fill(name)
        self.page.locator('input[data-qa="signup-email"]').fill(email)
        self.page.locator('button[data-qa="signup-button"]').click()
