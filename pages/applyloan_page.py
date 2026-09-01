from playwright.sync_api import Page, expect

class ApplyloanPage:

    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.applyloan_menu = page.get_by_role(
    "link",
    name="Loans"
)

        self.applyloan_heading = page.get_by_text(
            "Apply for a Loan"
        )

        # Buttons
        self.apply_loan_button = page.get_by_test_id(
            "open-apply-loan-btn"
        )

        self.review_application_button = page.get_by_test_id(
            "review-loan-btn"
        )

        self.confirm_submit_button = page.get_by_test_id(
            "confirm-loan-btn"
        )

        # Form Fields
        self.loan_type_dropdown = page.locator(
            "[data-testid='loan-type-select']"
        )

        self.loan_amount = page.get_by_test_id(
            "loan-amount-input"
        )

        self.term_length_dropdown = page.locator(
            "[data-testid='loan-term-select']"
        )

        self.interest_rate = page.get_by_test_id(
            "loan_interest_rate_input"
        )

        self.purpose = page.get_by_test_id(
            "loan_purpose_field"
        )

    def open_applyloan(self):
        self.applyloan_menu.click()
        expect(self.applyloan_heading).to_be_visible()

    def click_apply_loan(self):
        self.apply_loan_button.click()

    def fill_loan_application(
        self,
        loan_type: str,
        amount: str,
        term: str,
        purpose: str
    ):
        self.loan_type_dropdown.click()
        self.page.get_by_text(
            loan_type,
            exact=True
        ).click()

        self.loan_amount.fill(amount)

        self.term_length_dropdown.click()
        self.page.get_by_text(
            term,
            exact=True
        ).click()

        self.purpose.fill(purpose)

    def review_application(self):
        self.review_application_button.click()

    def submit_application(self):
        self.confirm_submit_button.click()