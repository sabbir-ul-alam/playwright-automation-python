from playwright.sync_api import  Page

from page_objects.confirmation_page import ConfirmationPage
from test_data.payment_data import PaymentData


class PaymentPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = self.Locator(self.page)

    class Locator:
        def __init__(self, page: Page):
            self.page = page
            self.name_input_field = self.page.locator('[data-qa="name-on-card"]')
            self.card_number_input_field = self.page.locator('[data-qa="card-number"]')
            self.cvc_input_field = self.page.locator('[data-qa="cvc"]')
            self.expire_month_input_field = self.page.locator('[data-qa="expiry-month"]')
            self.expire_year_input_field = self.page.locator('[data-qa="expiry-year"]')
            self.payment_submit_button = self.page.locator('[data-qa="pay-button"]')


    def make_payment(self, payment_data: PaymentData):
        self.locators.name_input_field.fill(payment_data.name_on_card)
        self.locators.card_number_input_field.fill(payment_data.card_number)
        self.locators.cvc_input_field.fill(payment_data.cvc)
        self.locators.expire_month_input_field.fill(payment_data.expire_month)
        self.locators.expire_year_input_field.fill(payment_data.expire_year)
        self.locators.payment_submit_button.click()
        return ConfirmationPage(self.page)