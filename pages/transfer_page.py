from playwright.sync_api import Page, expect


class TransferPage:

    def __init__(self, page: Page):
        self.page = page

        self.from_account_dropdown = page.get_by_test_id("transfer-from-select")
        self.to_account_dropdown = page.get_by_test_id("transfer-to-select")

        self.amount_input = page.get_by_test_id("transfer-amount-input)

        self.transfer_btn = page.get_by_role("button",name="Transfer Money")

    def transfer_money(self,from_account: str,to_account: str, amount: str):

        # From Account
        self.from_account_dropdown.click()
        self.page.get_by_text(from_account,exact=True).click()

        # To Account
        self.to_account_dropdown.click()
        self.page.get_by_text(to_account,exact=True).click()

        # Amount
        self.amount_input.fill(amount)

        # Transfer
        self.transfer_btn.click()

    def verify_transfer_success(self):

        expect(self.page.get_by_text("Transfer successful")).to_be_visible(timeout=10000)