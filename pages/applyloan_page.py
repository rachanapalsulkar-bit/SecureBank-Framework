from playwright.sync_api import Page, expect

class ApplyloanPage:

    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.applyloan_menu = page.get_by_test_id("sidebar-link-apply-loan")
        self.applyloan_heading = page.get_by_text("Apply for a Loan") # Fixed to look for text/heading

        # Buttons
        self.apply_loan_button = page.get_by_test_id("open-apply-loan-btn")
        self.review_application_button = page.get_by_test_id("review-loan-btn")
        self.confirm_submit_button = page.get_by_test_id("confirm-loan-btn")

        # Form Fields
        self.loan_type_dropdown = page.locator("[data-testid='loan-type-select']")
        self.loan_amount = page.get_by_test_id("loan-amount-input")
        self.term_length_dropdown = page.locator("[data-testid='loan-term-select']")
        self.interest_rate = page.get_by_test_id("loan_interest_rate_input")
        self.disbursement_dropdown = page.get_by_text("Select account") 
        self.purpose = page.get_by_placeholder("What will this loan be used for?")

    def open_applyloan(self):
        self.applyloan_menu.click()
        expect(self.applyloan_heading).to_be_visible()

    def click_apply_loan(self):
        self.apply_loan_button.click()

    def fill_loan_application(self, loan_type: str, amount: str, term: str, interest: str, disbursement: str, purpose: str):
        # 1. Click dropdown and scope text selection to 'loan-type-options'
        self.loan_type_dropdown.click()
        self.page.get_by_test_id("loan-type-options").get_by_text(loan_type, exact=True).click()
        
        # 2. Assert value updated
        expect(self.loan_type_dropdown.locator("[data-slot='select-value']")).to_have_text(loan_type)
     
        self.term_length_dropdown.click()
        self.loan_amount.fill(amount)
        self.page.get_by_test_id("loan-term-options").click()
        
        # 4. Assert term value updated
        # To check the actual input value ("5.0"):
        expect(self.page.get_by_role("spinbutton", name="Interest Rate (%)")).to_have_value("5.0")

        # Disbursement Account Selection
        self.page.get_by_text("Select account").click()
        self.page.get_by_role("option").filter(has_text=disbursement).click()

       #Loan Purpose
        self.page.get_by_placeholder("What will this loan be used for?").fill("Home renovation")

    def review_application(self):
     self.review_application_button.click()
     expect(self.page.get_by_text("Review Application")).to_be_visible()

    def submit_application(self):
     self.confirm_submit_button.click()
     expect(self.page.get_by_text("Reference Number")).to_be_visible()
     #self.page.screenshot(path="screenshots/final_loan_submission.png",full_page=True)