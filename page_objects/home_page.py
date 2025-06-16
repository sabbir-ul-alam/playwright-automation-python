import re

from playwright.sync_api import Page

from page_objects.confirmation_page import ConfirmationPage
from page_objects.login_page import LoginPage
from utils.css_helper import get_css_property


class HomePage:

    homeUrl : str =  'http://automationexercise.com'
    LOGGED_IN_AS_TEXT : str = "Logged in as"

    def __init__(self, page: Page):
        self.page = page
        self.locators = self.Locators(page)

    class Locators:
        def __init__(self,page: Page):
            self.home_link = page.get_by_role('link',name='Home')
            # page.get_by_role("link", name="Signup / Login")
            self.login_link = page.locator('a[href="/login"]')
            self.logged_in_as = page.get_by_text(re.compile("Logged in as \w+",re.IGNORECASE))
            self.delete_account_link = page.locator('a[href="/delete_account"]')

    def visit(self):
        self.page.goto(self.homeUrl)

    def is_loaded(self):
        home_link = self.locators.home_link
        if not home_link.is_visible():
            return False
        if get_css_property(self.locators.home_link, 'color')!='rgb(255, 165, 0)':
            return False
        return  True

    def goto_login_or_signup(self):
        self.locators.login_link.click()
        return LoginPage(self.page)

    def is_user_logged_in(self, user_name:str):
        element = self.locators.logged_in_as
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










