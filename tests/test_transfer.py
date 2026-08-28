from playwright.sync_api import Page, expect
from pages.transfer_page import TransferPage


def test_transfer_page_is_displayed(
    authenticated_page: Page
):
    transfer_page = TransferPage(
        authenticated_page
    )

    transfer_page.open()

    transfer_page.verify_transfer_page()

    transfer_page.make_transfer(
        from_account="Everyday Checking",
        to_account="High-Yield Savings",
        amount=500,
    )

    expect(
        authenticated_page.get_by_role(
            "heading",
            name="Confirm Transfer"
        )
    ).to_be_visible()
