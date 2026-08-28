import os
import conftest
from playwright.sync_api import Page, expect
from conftest import authenticated_page
from pages.billpay_page import BillPayPage
from datetime import datetime
import os

# This is the short test that is currently passing in your screenshot:
def test_bill_pay_page_is_displayed(authenticated_page: Page):
    billpay_page = BillPayPage(authenticated_page)
    billpay_page.open_bill_pay()
    authenticated_page.screenshot(path="screenshots/debug_bill_pay.png")

# This is the test you NEED to run to finish the flow and save the final receipt:
def test_screenshot_payment_schedule(authenticated_page: Page):
    billpay_page = BillPayPage(authenticated_page)
    billpay_page.open_bill_pay()
    
    # Fills form, clicks review, clicks confirm, validates success page
    billpay_page.make_bill_payment(
        from_account="Everyday Checking",
        biller="City Electric Co.",
        amount="20.00",
        payment_date="2026-08-27"
    )
    
    # Saves the completed confirmation screen
    os.makedirs("screenshots", exist_ok=True)
    authenticated_page.screenshot(path="screenshots/payment_scheduled.png")
