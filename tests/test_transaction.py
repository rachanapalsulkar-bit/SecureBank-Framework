import os
from playwright.sync_api import Page, expect
from pages.transactions_page import TransactionPage


def test_transaction_page_is_displayed(authenticated_page: Page):
    transaction_page = TransactionPage(authenticated_page)

    transaction_page.open_transactions()
    transaction_page.search_transaction("Amazon")
    transaction_page.select_account("Everyday Checking")

    expect(
        authenticated_page.get_by_text("Amazon.com")
    ).to_be_visible()

    os.makedirs("screenshots", exist_ok=True)
    authenticated_page.screenshot(
        path="screenshots/transaction_search.png"
    )

    with authenticated_page.expect_download() as download_info:
        transaction_page.download_csv()

    download = download_info.value

    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)

    file_path = os.path.join(
        download_dir,
        download.suggested_filename
    )

    print("Saving file to:", file_path)

    download.save_as(file_path)

    assert os.path.isfile(file_path)