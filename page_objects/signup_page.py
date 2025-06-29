from playwright.sync_api import Page

from page_objects.confirmation_page import ConfirmationPage
from test_data.registration_data import UserRegisterData


class SignupPage:

    def __init__(self, page):
        self.page = page
        self.locators = self.Locators(page)

    class Locators:
        def __init__(self, page: Page):
            self.page = page
            # self.title_radio_box = self.page.get_by_role("radio", name="Mr.")
            self.name_input_field = self.page.locator('[data-qa="name"]')
            self.email_input_field = self.page.locator('[data-qa="email"]')
            self.password_input_field = self.page.locator('[data-qa="password"]')
            self.select_days = self.page.locator('[data-qa="days"]')
            self.select_months = self.page.locator('[data-qa="months"]')
            self.select_years = self.page.locator('[data-qa="years"]')
            self.newsletter_check_box = self.page.locator('#newsletter')
            self.offer_check_box = self.page.locator('#optin')
            self.first_name_input_field = self.page.locator('[data-qa="first_name"]')
            self.last_name_input_field = self.page.locator('[data-qa="last_name"]')
            self.company_input_field = self.page.locator('[data-qa="company"]')
            self.address_1_input_field = self.page.locator('[data-qa="address"]')
            self.address_2_input_field = self.page.locator('[data-qa="address2"]')
            self.country_input_field = self.page.locator('[data-qa="country"]')
            self.state_input_field = self.page.locator('[data-qa="state"]')
            self.city_input_field = self.page.locator('[data-qa="city"]')
            self.zipcode_input_field = self.page.locator('[data-qa="zipcode"]')
            self.mobile_input_field = self.page.locator('[data-qa="mobile_number"]')
            self.create_account_button = self.page.locator('[data-qa="create-account"]')

        def title_radio_box(self, label: str):
            return self.page.get_by_role("radio", name=label)


    def fill_form(self,data: UserRegisterData):
        self.locators.title_radio_box(data.title).check()
        self.locators.password_input_field.fill(data.password)
        self.locators.select_days.select_option(data.day)
        self.locators.select_months.select_option(data.month)
        self.locators.select_years.select_option(data.year)
        self.locators.newsletter_check_box.check()
        self.locators.offer_check_box.check()
        self.locators.first_name_input_field.fill(data.first_name)
        self.locators.last_name_input_field.fill(data.last_name)
        self.locators.company_input_field.fill(data.company)
        self.locators.address_1_input_field.fill(data.address)
        self.locators.country_input_field.select_option(data.country)
        self.locators.state_input_field.fill(data.state)
        self.locators.city_input_field.fill(data.city)
        self.locators.zipcode_input_field.fill(data.zipcode)
        self.locators.mobile_input_field.fill(data.mobile)

    def create_account(self, data: UserRegisterData):
        self.fill_form(data)
        self.locators.create_account_button.click()
        return ConfirmationPage(self.page)



