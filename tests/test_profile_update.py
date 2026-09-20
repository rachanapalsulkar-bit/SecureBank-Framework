import re
from playwright.sync_api import Page, expect

BASE_URL = "https://qaplayground.com/bank/login"


def login(page: Page):
    """Helper function to log in with standard credentials"""
    page.goto(BASE_URL)
    page.get_by_test_id("login-username-input").fill("standard_user")
    page.get_by_test_id("login-password-input").fill("bank_sauce")
    page.get_by_test_id("login-submit-btn").click()
    page.wait_for_load_state("networkidle")


def test_verify_successful_profile_update(page: Page) -> None:
    """Test Case: Verify users can modify personal details and see confirmation"""
    login(page)
    
    # 1. Navigate to profile page via sidebar
    page.get_by_test_id("sidebar-link-profile").click()
    page.wait_for_load_state("networkidle")
    
    # 2. Click the "Edit" button in the Personal Information card
    page.get_by_role("button", name="Edit").click()
    
    # 3. Target input fields reliably (e.g., updating the phone input field safely)
    # Using locator based on type and filtering or grabbing input elements inside the card
    phone_input = page.locator("input").filter(has_not=page.locator("[type='hidden']")).locator("nth=3")
    phone_input.click()
    phone_input.fill("(415) 555-9999")
    
    # 4. Click the Save / Submit button 
    page.get_by_role("button", name=re.compile("Save|Update|Submit", re.IGNORECASE)).click()
    
    # 5. Verify success or updated text reflection
    page.wait_for_load_state("networkidle")
    expect(page.locator("text=(415) 555-9999")).to_be_visible()
    
    # 6. Capture final state snapshot
    page.screenshot(path="profile_update_snapshot.png", full_page=True)