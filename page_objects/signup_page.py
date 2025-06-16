from playwright.sync_api import Page


class SignupPage:
    def __init__(self, page):
        self.page = page
        self.locators = self.Locators(page)

    class Locators:
        def __init__(self, page: Page):
            self.page = page
            self.title_radio_box = self.page.get_by_role("radio", name="Mr.")
            self.name_input_field = self.page.locator('[data-qa="name"]')
            self.email_input_field = self.page.locator('[data-qa="email"]')
            self.password_input_field = self.page.locator('[date-qa="password"]')
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

