from pages.login_page import BasePage

class AccountInfoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def enter_account_information(self, password: str, day: str, month: str, year: str):
        self.page.locator("#id_gender1").click()
        self.page.locator("#password").fill(password)
        self.page.locator("select#days").select_option(day)
        self.page.locator("select#months").select_option(month)
        self.page.locator("select#years").select_option(year)

    def enter_address_information(
        self, first_name, last_name, company, address, country, state, city, zipcode, mobile
    ):
        self.page.locator("#first_name").fill(first_name)
        self.page.locator("#last_name").fill(last_name)
        self.page.locator("#company").fill(company)
        self.page.locator("#address1").fill(address)
        self.page.locator("select#country").select_option(country)
        self.page.locator("#state").fill(state)
        self.page.locator("#city").fill(city)
        self.page.locator("#zipcode").fill(zipcode)
        self.page.locator("#mobile_number").fill(mobile)

    def click_create_account(self):
        self.page.locator("button[data-qa='create-account']").click()