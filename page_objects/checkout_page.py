from playwright.sync_api import Page

from page_objects.payment_page import PaymentPage


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = self.Locator(self.page)

    class Locator:
        def __init__(self, page: Page):
            self.page = page
            self.place_order_button = self.page.get_by_text('Place Order')

    def place_order(self):
        self.locators.place_order_button.click()
        return PaymentPage(self.page)