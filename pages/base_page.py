from playwright.sync_api import Page


class BasePage:  # <-- Ensure this class name matches exactly

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)