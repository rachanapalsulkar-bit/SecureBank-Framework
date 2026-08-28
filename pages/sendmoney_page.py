from playwright.sync_api import Page, expect

class SendMoneyPage:

    def __init__(self, page: Page):
        self.page = page

        # Navigation & Landing Verification
        self.send_money_menu = page.get_by_role("link", name="Send Money", exact=True)
        self.sendmoney_heading = page.get_by_role("heading", name="Send Money")
        
        # Confirmation & Success States
        self.confirm_send_heading = page.get_by_role("heading", name="Confirm Send Money")
        self.success_heading = page.get_by_role("heading", name="Money Sent Successfully")

        # Action Buttons
        self.add_payee_trigger = page.get_by_test_id("add-payee-btn")
        self.review_transfer_button = page.get_by_test_id("review-send-btn")
        self.confirm_transfer_button = page.get_by_test_id("confirm-send-btn")

        # Form fields 
        self.select_from_account_dropdown = page.locator("button:has-text('Select account')")
        self.amount_input = page.get_by_test_id("send-amount-input")
        self.note_input = page.get_by_test_id("send-note-input")

        # "Add New Payee" Modal Form Fields
        self.add_new_payee_modal_heading = page.get_by_role("heading", name="Add New Payee")
        self.payee_name_input = page.get_by_test_id("add-payee-name-input")
        self.bank_name_input = page.get_by_test_id("add-payee-bank-input")
        self.routing_number_input = page.get_by_test_id("add-payee-routing-input")
        self.account_number_input = page.get_by_test_id("add-payee-account-input")
        self.submit_new_payee_button = page.get_by_test_id("save-add-payee-btn")


    def open_send_money(self):
        self.send_money_menu.click()
        expect(self.sendmoney_heading).to_be_visible()

    def select_from_account(self, account_name):
        # Using a forced check to ensure execution pierces any overlay layout variations
        self.select_from_account_dropdown.click(force=True)
        
        option = self.page.get_by_role("option", name=account_name)
        expect(option).to_be_visible()
        option.click()

    def add_new_payee_details(self, name, bank, routing, account):
        self.add_payee_trigger.click()
        expect(self.add_new_payee_modal_heading).to_be_visible()
        
        self.payee_name_input.fill(name)
        self.bank_name_input.fill(bank)
        self.routing_number_input.fill(str(routing))
        self.account_number_input.fill(str(account))
        
        self.submit_new_payee_button.click()
        expect(self.add_new_payee_modal_heading).to_be_hidden()

    def send_money_to_new_payee(self, from_account, payee_info: dict, amount, note=""):
        self.select_from_account(from_account)
        self.add_new_payee_details(
            name=payee_info["name"],
            bank=payee_info["bank"],
            routing=payee_info["routing"],
            account=payee_info["account"]
        )
        
        self.amount_input.fill(str(amount))
        if note:
            self.note_input.fill(note)
            
        self.review_transfer_button.click()
        expect(self.confirm_send_heading).to_be_visible()
        
        self.confirm_transfer_button.click()
        expect(self.success_heading).to_be_visible()
