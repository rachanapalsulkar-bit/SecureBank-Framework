from playwright.sync_api import Page, expect


class TransferPage:
    def __init__(self, page: Page):
        self.page = page

        self.transfer_heading = page.get_by_role(
            "heading",
            name="Transfer Money"
        )

        self.from_account = page.locator(
            "#transfer-from-trigger"
        )

        self.to_account = page.locator(
            "#transfer-to-trigger"
        )

        self.amount = page.get_by_label("Amount")

        self.today_radio = page.get_by_label("Today")

        self.review_transfer_button = page.get_by_role(
            "button",
            name="Review Transfer"
        )

    def open(self):
        self.page.goto(
            "https://qaplayground.com/bank/transfer",
            wait_until="domcontentloaded"
        )

    def verify_transfer_page(self):
        expect(self.transfer_heading).to_be_visible()

    def select_from_account(self, account_name):
        self.from_account.click()

        self.page.get_by_role(
            "option",
            name=account_name
        ).click()

    def select_to_account(self, account_name):
        self.to_account.click()

        self.page.get_by_role(
            "option",
            name=account_name
        ).click()

    def enter_amount(self, amount):
        self.amount.fill(str(amount))

    def select_today(self):
        self.today_radio.check()

    def click_review_transfer(self):
        self.review_transfer_button.click()

    def make_transfer(
        self,
        from_account,
        to_account,
        amount,
    ):
        self.select_from_account(from_account)
        self.select_to_account(to_account)
        self.enter_amount(amount)
        self.select_today()
        self.click_review_transfer()