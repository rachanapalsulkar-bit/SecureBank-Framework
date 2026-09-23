from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Navigation
        self.login_menu_btn = page.locator(".shop-menu a[href='/login']")
        
        # New User Signup Elements
        self.signup_name_input = page.locator("input[data-qa='signup-name']")
        self.signup_email_input = page.locator("input[data-qa='signup-email']")
        self.signup_btn = page.locator("button[data-qa='signup-button']")

    def navigate(self):
        self.login_menu_btn.click()

    def register_new_user(self, name: str, email: str):
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_btn.click()