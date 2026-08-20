from playwright.sync_api import Page, expect


class AccountsPage:

    def __init__(self, page: Page):
        self.page = page

        # Open Add Account dialog
        self.add_account_btn = page.get_by_role(
            "button",
            name="Add Account"
        )

        # Form fields (using placeholders)
        self.account_name_input = page.get_by_placeholder(
            "Account Name"
        )

        self.balance_input = page.get_by_placeholder(
            "Starting Balance"
        )

        # Account type dropdown
        self.account_type_dropdown = page.locator("select")

        # Terms checkbox
        self.terms_checkbox = page.get_by_role("checkbox")

    def capture_screenshot(self, path):
        self.page.screenshot(
            path=path,
            full_page=True
        )

    def add_account(
        self,
        account_name: str,
        account_type: str,
        starting_balance: str
    ):
        # Open dialog
        self.add_account_btn.click()

        # Wait for form
        self.account_name_input.wait_for(
            state="visible",
            timeout=10000
        )

        # Fill form
        self.account_name_input.fill(account_name)

        self.account_type_dropdown.select_option(
            account_type
        )

        self.balance_input.fill(starting_balance)

        # Accept terms
        self.terms_checkbox.check()

        # Screenshot before submit
        self.page.screenshot(
            path="before_submit.png",
            full_page=True
        )

        # Click Add Account button inside dialog
        self.page.get_by_role(
            "dialog"
        ).get_by_role(
            "button",
            name="Add Account"
        ).click()

    def verify_account_exists(
        self,
        account_name: str
    ):
        expect(
            self.page.get_by_text(account_name)
        ).to_be_visible(timeout=10000)