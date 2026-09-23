import pytest
from playwright.sync_api import sync_playwright
from pages.products_page import ProductsPage

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=300
        )
        # Bypasses corporate VPN/SSL inspection blocks
        browser_context = browser.new_context(ignore_https_errors=True)
        page = browser_context.new_page()
        
        # Automatically launch homepage on every test start
        page.goto("https://automationexercise.com/")
        
        yield page
        browser.close()

@pytest.fixture
def products_page(page):
    return ProductsPage(page)

@pytest.fixture(autouse=True)
def block_ads(page):
    page.route(
        "**/*",
        lambda route: (
            route.abort()
            if any(
                ad_domain in route.request.url
                for ad_domain in [
                    "googlesyndication.com",
                    "doubleclick.net",
                    "googleads.g.doubleclick.net",
                    "adservice.google.com",
                ]
            )
            else route.continue_()
        ),
    )
    yield