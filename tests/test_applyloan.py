from playwright.sync_api import Page, expect
from pages.applyloan_page import ApplyloanPage


def test_apply_loan(authenticated_page: Page):

    applyloan_page = ApplyloanPage(
        authenticated_page
    )

    # Navigate
    applyloan_page.open_applyloan()

    # Open loan form
    applyloan_page.click_apply_loan()

    # Fill form
    applyloan_page.fill_loan_application(
        loan_type="Personal Loan",
        amount="10000",
        term="24 Months",
        purpose="Home renovation"
    )

    # Review application
    applyloan_page.review_application()

    # Submit application
    applyloan_page.submit_application()

    # Validation
    expect(
        authenticated_page.get_by_text(
            "Application Submitted"
        )
    ).to_be_visible()