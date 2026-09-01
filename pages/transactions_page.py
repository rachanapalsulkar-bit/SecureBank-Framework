from playwright.sync_api import Page, expect


class TransactionPage:

    def __init__(self, page: Page):
        self.page = page

        # Navigation & Landing Verification
        self.transaction_menu = page.get_by_test_id(
            "sidebar-link-transactions"
        )
        self.transaction_heading = page.get_by_test_id(
            "transactions-page-title"
        )

        # Search & Filters
        self.search_input = page.get_by_test_id(
            "all-txn-search-input"
        )

        self.account_dropdown = page.get_by_test_id(
            "all-txn-account-select"
        )

        # Action Buttons
        self.all_button = page.get_by_test_id("all-btn")
        self.download_csv_button = page.get_by_test_id("download-all-transactions-btn")

    def open_transactions(self):
        self.transaction_menu.click()
        expect(self.transaction_heading).to_be_visible()

    
    def search_transaction(self, Amazon: str):
        self.search_input.fill(Amazon)

    def select_account(self, account_name: str):
            self.account_dropdown.click()
            self.page.get_by_role(
                "option",
                name=account_name
            ).click()

    #def click_all_filter(self):
        #self.all_button.click()

    def download_csv(self):
        print(f"Inside download_csv : {self}")
        self.download_csv_button.click()

        #return 