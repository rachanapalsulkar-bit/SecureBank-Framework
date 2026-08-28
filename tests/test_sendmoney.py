import os
from playwright.sync_api import Page
from pages.sendmoney_page import SendMoneyPage

def test_send_money_page_is_displayed(authenticated_page: Page):
    """Test 1: Simple validation that the landing page renders correctly."""
    sendmoney_page = SendMoneyPage(authenticated_page)
    sendmoney_page.open_send_money()
    
    os.makedirs("screenshots", exist_ok=True)
    authenticated_page.screenshot(path="screenshots/debug_send_money.png")


def test_screenshot_sendmoney_with_new_payee(authenticated_page: Page):
    """Test 2: Creates a new custom payee profile dynamically and processes transaction execution."""
    sendmoney_page = SendMoneyPage(authenticated_page)
    sendmoney_page.open_send_money()
    
    new_payee_data = {
        "name": "Rachana Palsulkar",
        "bank": "SBI Bank",
        "routing": "123456789",
        "account": "98765432134"
    }
    
    # Cleanized call tracking matching the simple name model format
    sendmoney_page.send_money_to_new_payee(
        from_account="Everyday Checking",
        payee_info=new_payee_data,
        amount="2000.00",
        note="Payment to new vendor profile"
    )
    
    os.makedirs("screenshots", exist_ok=True)
    authenticated_page.screenshot(path="screenshots/Money_Sent_Successfully.png")
