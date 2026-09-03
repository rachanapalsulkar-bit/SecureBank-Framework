import os
from playwright.sync_api import Page, expect
from pages.applyloan_page import ApplyloanPage

def test_apply_loan(authenticated_page: Page):

    applyloan_page = ApplyloanPage(authenticated_page)

    # Navigate to Apply Loan page
    applyloan_page.open_applyloan()

    # Open Apply Loan form
    applyloan_page.click_apply_loan()

    # Fill loan application
    applyloan_page.fill_loan_application(
        loan_type="Personal",
        amount="1000",
        term="36",
        interest="5.0",
        disbursement="Everyday Checking — $4,250.00",
        purpose="Home renovation"
    )

    # Review application
    applyloan_page.review_application()

    # Submit application
    applyloan_page.submit_application()

    # Verify success message
    expect(
        authenticated_page.get_by_text(
            "Application Submitted",
            exact=True
        )
    ).to_be_visible(timeout=10000)

    # Take screenshot
    os.makedirs("screenshots", exist_ok=True)
    authenticated_page.screenshot(
        path="screenshots/successful_applyloan.png"
    )