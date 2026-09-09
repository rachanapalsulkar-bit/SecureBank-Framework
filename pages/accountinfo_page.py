from playwright.sync_api import Page

class AccountInfoPage:

    def __init__(self, page: Page):
        self.page = page
        
    def enter_account_information(
        self,
        password,
        day,
        month,
        year
    ):

        # Mrs
        self.page.locator("#id_gender2").check()

        self.page.locator(
            'input[data-qa="password"]'
        ).fill(password)

        self.page.locator(
            'select[data-qa="days"]'
        ).select_option(day)

        self.page.locator(
            'select[data-qa="months"]'
        ).select_option(month)

        self.page.locator(
            'select[data-qa="years"]'
        ).select_option(year)

    def enter_address_information(
        self,
        first_name,
        last_name,
        company,
        address,
        country,
        state,
        city,
        zipcode,
        mobile
    ):

        self.page.locator(
            'input[data-qa="first_name"]'
        ).fill(first_name)

        self.page.locator(
            'input[data-qa="last_name"]'
        ).fill(last_name)

        self.page.locator(
            'input[data-qa="company"]'
        ).fill(company)

        self.page.locator(
            'input[data-qa="address"]'
        ).fill(address)

        self.page.locator(
            'select[data-qa="country"]'
        ).select_option(label=country)

        self.page.locator(
            'input[data-qa="state"]'
        ).fill(state)

        self.page.locator(
            'input[data-qa="city"]'
        ).fill(city)

        self.page.locator(
            'input[data-qa="zipcode"]'
        ).fill(zipcode)

        self.page.locator(
            'input[data-qa="mobile_number"]'
        ).fill(mobile)

    def click_create_account(self):
        self.page.locator('button[data-qa="create-account"]').click()