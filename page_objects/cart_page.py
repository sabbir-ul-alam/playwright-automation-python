from playwright.sync_api import  Page

from page_objects.checkout_page import CheckoutPage
from page_objects.login_page import LoginPage
from test_data.product_data import ProductData


class CartPage:

    CART_EMPTY_TEXT = 'Cart is empty!'

    def __init__(self, page: Page):
        self.page = page
        self.locators = self.Locators(self.page)

    class Locators:
        def __init__(self, page: Page):
            self.page = page
            self.checkout = self.page.get_by_text('Proceed To Checkout')
            self.login_link_modal = self.page.get_by_text('Register / Login',exact=True)
            self.cart_is_empty_text = self.page.get_by_text('Cart is empty!')

        def item_price_locator(self, product_id):
            return self.page.locator(f'#product-{product_id} .cart_price')

    def checkout(self, logged_in: bool):
        self.locators.checkout.click()
        if logged_in:
            return CheckoutPage(self.page)
        else:
            return None

    def is_cart_empty(self):
        return self.locators.cart_is_empty_text.is_visible()

    def goto_login_from_modal(self):
        self.locators.login_link_modal.click()
        return LoginPage(self.page)

    def get_item_price(self, product: ProductData):
        return int(self.locators.item_price_locator(product_id=product.product_id).text_content().split()[1])