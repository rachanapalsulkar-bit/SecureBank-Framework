import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def browser_context_args(browser_context_args):
    """Automatically injects config arguments into the Playwright browser context."""
    return {
        **browser_context_args,
        "ignore_https_errors": True  # <-- THIS BYPASSES THE SSL CERTIFICATE ERROR
    }


@pytest.fixture(scope="function")
def authenticated_page(page: Page) -> Page:
    page.goto(
        "https://qaplayground.com/bank/login",
        wait_until="domcontentloaded"
    )

    page.get_by_label(
        "Username",
        exact=True
    ).fill("standard_user")

    page.get_by_label(
        "Password",
        exact=True
    ).fill("bank_sauce")

    page.get_by_role(
        "button",
        name="Sign in to SecureBank"
    ).click()

    page.wait_for_load_state("networkidle")

    expect(
        page.get_by_text(
            "standard_user",
            exact=True
        )
    ).to_be_visible(timeout=15000)
  
    return page

