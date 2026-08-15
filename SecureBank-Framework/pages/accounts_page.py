from playwright.sync_api import Page


class AccountsPage:

    def __init__(self, page: Page):
        self.page = page

    def capture_screenshot(self):
        self.page.screenshot(
            path="screenshots/accounts_page.png",
            full_page=True
        )