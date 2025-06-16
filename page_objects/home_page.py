from playwright.sync_api import Page

from page_objects.login_page import LoginPage


class HomePage:

    homeUrl : str =  'http://automationexercise.com'


    def __init__(self, page: Page):
        self.page = page
        self.locators = self.Locators(page)



    class Locators:
        def __init__(self,page: Page):
            self.home_link = page.get_by_role('link',name='Home')
            # page.get_by_role("link", name="Signup / Login")
            self.login_link = page.locator('a[href="/login"]')

    def visit(self):
        self.page.goto(self.homeUrl)

    def is_loaded(self):
        return self.locators.home_link.is_visible()

    def goto_login_or_signup(self):
        self.locators.login_link.click()
        return LoginPage(self.page)










