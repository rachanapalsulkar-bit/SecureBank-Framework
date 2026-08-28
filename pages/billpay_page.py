from playwright.sync_api import Page, expect

class BillPayPage:

    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.bill_pay_menu = page.get_by_text("Bill Pay", exact=True)

        # Page verification
        self.billpay_heading = page.get_by_role(
            "heading",
            name="Pay a Bill"
        )

        # Confirmation popup
        self.confirm_bill_payment_heading = page.get_by_role(
            "heading",
            name="Confirm Bill Payment"
        )

        # SUCCESS PAGE HEADING
        self.payment_scheduled_heading = page.get_by_role(
            "heading",
            name="Payment Scheduled"
        )

        self.confirm_payment_button = page.get_by_role(
            "button",
            name="Confirm Payment"
        )

        # Form fields
        self.select_from_account_dropdown = page.get_by_test_id("bill-pay-from-select")
        self.biller_search = page.get_by_test_id("biller-search-input")
        self.amount = page.get_by_test_id("bill-amount-input")
        self.payment_date = page.get_by_test_id("bill-payment-date-input")
        
        self.review_payment_button = page.get_by_role(
            "button",
            name="Review Payment"
        )

    def open_bill_pay(self):
        self.bill_pay_menu.click()
        expect(self.billpay_heading).to_be_visible()

    def verify_bill_pay_page(self):
        expect(self.billpay_heading).to_be_visible()

    def select_from_account(self, account_name):
        self.select_from_account_dropdown.click()
        option = self.page.get_by_role("option", name=account_name)
        expect(option).to_be_visible()
        option.click()

    def select_biller(self, biller_name):
        self.biller_search.click()
        self.biller_search.fill(biller_name)
        option = self.page.get_by_role("option", name=biller_name)
        expect(option).to_be_visible()
        option.click()

    def enter_amount(self, amount):
        self.amount.clear()
        self.amount.fill(str(amount))

    def enter_payment_date(self, payment_date):
        self.payment_date.fill(payment_date)

    def verify_confirmation_popup(self):
        expect(self.confirm_bill_payment_heading).to_be_visible()

    def click_review_payment(self):
        self.review_payment_button.click()

    def confirm_payment(self):
        expect(self.confirm_payment_button).to_be_visible()
        self.confirm_payment_button.click()

    def verify_payment_scheduled(self):
        expect(self.payment_scheduled_heading).to_be_visible()

    # This high-level wrapper method is now properly aligned with the class block
    def make_bill_payment(self, from_account, biller, amount, payment_date):
        self.select_from_account(from_account)
        self.select_biller(biller)
        self.enter_amount(amount)
        self.enter_payment_date(payment_date)
        
        # Clicks initial 'Review Payment' button
        self.click_review_payment()
        
        # Validates confirmation popup appears
        self.verify_confirmation_popup()
        
        # Clicks the final 'Confirm Payment' button
        self.confirm_payment()
        
        # Confirms the success state
        self.verify_payment_scheduled()
