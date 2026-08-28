from playwright.sync_api import Page, expect

class AccountsPage:

    def __init__(self, page: Page):
        self.page = page

    # Open Add Account dialog
        self.add_account_btn = page.get_by_role( "button",name="Add Account")
   
        self.account_name_input = page.get_by_test_id("account-form-name-input")

        self.balance_input = page.locator('input[name="account_balance_field"]')

    # Select an option
        self.account_type_dropdown = page.locator('span[data-slot="select-value"]').first

    # Terms checkbox
        self.terms_checkbox = page.locator("#account-form-accept-terms")

    def capture_screenshot(self, path):self.page.screenshot(path=path,full_page=True)

    def add_account(self,account_name: str,account_type: str,starting_balance: str):

    # Open dialog
        self.add_account_btn.click()

    # Wait for form
        self.account_name_input.wait_for(state="visible",timeout=10000)

    # Fill form
        self.account_name_input.fill(account_name)
        self.account_type_dropdown.click()
        self.page.get_by_role("option", name="Checking").click()
        self.balance_input.fill(starting_balance)

    # Accept terms
        self.page.get_by_text("I accept the terms and conditions").click()

    # Screenshot before submit
        self.page.screenshot(path="before_submit.png",full_page=True)

    # Click Add Account button inside dialog
        self.page.get_by_role("dialog").get_by_role("button",name="Add Account").click()

    def verify_account_exists(self,account_name: str):
        expect(self.page.get_by_text(account_name)).to_be_visible(timeout=10000)