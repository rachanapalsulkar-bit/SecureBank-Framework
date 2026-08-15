from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # Pierce the shadow DOM by targeting the input fields safely
        self.username = page.locator("input[type='text'], input#username")
        self.password = page.locator("input[type='password'], input#password")
        self.sign_in = page.locator("button[type='submit'], button:has-text('Sign In')")

    def open(self, url: str):
        """Navigates to the QA Playground site and forces synchronization loops."""
        self.page.goto(url, wait_until="networkidle")

    def login(self, username: str, password: str):
        """Logs into the bank application workspace."""
        # Wait until the input element completes loading and renders visually
        self.username.wait_for(state="visible", timeout=15000)
        
        self.username.fill(username)
        self.password.fill(password)
        self.sign_in.click()
