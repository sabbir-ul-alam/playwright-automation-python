import re

from playwright.sync_api import Page

from page_objects.cart_page import CartPage
from page_objects.confirmation_page import ConfirmationPage
from page_objects.contactus_page import ContactusPage
from page_objects.login_page import LoginPage
from page_objects.products_page import ProductsPage
from test_data.product_data import ProductData
from utils.css_helper import get_css_property


class HomePage:

    homeUrl : str =  'https://automationexercise.com'
    LOGGED_IN_AS_TEXT : str = "Logged in as"

    def __init__(self, page: Page):
        self.page = page
        self.locators = self.Locators(page)

    class Locators:
        def __init__(self, page: Page):
            self.page = page
            self.home_link = page.get_by_role("link", name=" Home")
            self.login_signup_link = page.get_by_role("link", name=" Signup / Login")
            self.logged_in_as_text = page.get_by_text(HomePage.LOGGED_IN_AS_TEXT)
            self.logout_link = page.get_by_role("link", name=" Logout")
            self.contact_us_link = page.get_by_role("link", name=" Contact us")
            self.products_link = page.get_by_role("link", name=" Products")
            self.cart_link = page.locator('.navbar-nav > li >a[href="/view_cart"]')
            self.delete_account_link = page.locator('a[href="/delete_account"]')
            self.view_cart_modal= page.locator('.modal-body').get_by_text('View Cart')


        def product_locators(self, product_id):
            return[
                self.page.locator('.features_items').locator(f'.productinfo > a[data-product-id="{product_id}"]'),
                self.page.locator(f'.overlay-content > a[data-product-id="{product_id}"]')
            ]





    def visit(self):
        self.page.goto(self.homeUrl)

    def is_loaded(self):
        home_link = self.locators.home_link
        if not home_link.is_visible():
            return False
        if get_css_property(self.locators.home_link, 'color')!='rgb(255, 165, 0)':
            return False
        return  True

    def goto_login_or_signup(self) -> LoginPage:
        self.locators.login_signup_link.click()
        return LoginPage(self.page)

    def goto_products(self) -> ProductsPage:
        """Navigate to products page and return ProductsPage instance"""
        self.locators.products_link.click()
        return ProductsPage(self.page)

    def goto_contact_us(self) -> ContactusPage:
        self.locators.contact_us_link.click()
        return ContactusPage(self.page)

    def is_user_logged_in(self, user_name:str):
        element = self.locators.logged_in_as_text
        if not element.is_visible():
            return  False
        if element.text_content().strip() != f"{self.LOGGED_IN_AS_TEXT} {user_name}":
            print(f"{element.text_content()}")
            print(f"{self.LOGGED_IN_AS_TEXT} {user_name}")
            return  False
        return True

    def delete_account(self):
        self.locators.delete_account_link.click()
        return ConfirmationPage(self.page)

    def logout(self):
        self.locators.logout_link.click()
        return LoginPage(self.page)

    def add_feature_product_to_cart(self, product: ProductData):
        product_element, overlay_element = self.locators.product_locators(product_id=product.product_id)
        product_element.hover()
        assert overlay_element.is_visible()
        overlay_element.scroll_into_view_if_needed()
        overlay_element.click()

    def goto_cart_from_modal(self):
        self.locators.view_cart_modal.click()
        return CartPage(self.page)

    def goto_cart(self):
        self.locators.cart_link.click()
        return CartPage(self.page)








