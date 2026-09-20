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


def test_verify_personal_information(page: Page) -> None:
    """Test Case: Verify personal information fields load accurately and capture snapshot"""
    login(page)
    
    # Navigate to profile via test ID
    page.get_by_test_id("sidebar-link-profile").click()
    
    # Wait for profile card or section to load explicitly
    expect(page.locator("text=Personal Information")).to_be_visible()
    
    # Use precise profile data selectors to avoid matching multiple elements
    expect(page.get_by_test_id("profile-first-name")).to_have_text("Alex")
    expect(page.get_by_test_id("profile-last-name")).to_have_text("Morgan")
    expect(page.get_by_test_id("profile-email")).to_have_text("alex.morgan@example.com")
    
    # Take a screenshot snapshot at the end of the test
    page.screenshot(path="profile_snapshot.png", full_page=True)