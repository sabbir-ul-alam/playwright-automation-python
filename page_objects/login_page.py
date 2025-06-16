from playwright.sync_api import Page

from page_objects.signup_page import SignupPage


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # self.locator = self.Locators(page)

        # class Locators:
        #     def __init__(self,page):
        #         self.page = page
        #         self.username_input_field = self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Name")
        #         self.email_input_field = self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")

    @property
    def username_input_field(self):
        return self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Name")

    @property
    def email_input_field(self):
        return self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")

    @property
    def signup_button(self):
        return self.page.get_by_role("button", name="Signup")

    def signup(self, name, email):
        self.username_input_field.fill(name)
        self.email_input_field.fill(email)
        self.signup_button.click()
        return SignupPage(self.page)






