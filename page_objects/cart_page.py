from playwright.sync_api import  Page

from page_objects.checkout_page import CheckoutPage
from page_objects.login_page import LoginPage


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.locators = self.Locators(self.page)

    class Locators:
        def __init__(self, page: Page):
            self.page = page
            self.checkout = self.page.get_by_text('Proceed To Checkout')
            self.login_link_modal = self.page.get_by_text('Register / Login',exact=True)

    def checkout(self, logged_in: bool):
        self.locators.checkout.click()
        if logged_in:
            return CheckoutPage(self.page)
        else:
            return None

    def goto_login_from_modal(self):
        self.locators.login_link_modal.click()
        return LoginPage(self.page)