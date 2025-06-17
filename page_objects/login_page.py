from gc import set_debug

from playwright.sync_api import Page

from page_objects.confirmation_page import ConfirmationPage
from page_objects.signup_page import SignupPage
from test_data.login_data import LoginData


class LoginPage:

    LOGIN_ERROR_TEXT : str = 'Your email or password is incorrect!'

    def __init__(self, page: Page):
        self.page = page
        # self.locator = self.Locators(page)

        # class Locators:
        #     def __init__(self,page):
        #         self.page = page
        #         self.username_input_field = self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Name")
        #         self.email_input_field = self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")

    @property
    def signup_username_input_field(self):
        return self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Name")

    @property
    def signup_email_input_field(self):
        return self.page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")

    @property
    def signup_button(self):
        return self.page.get_by_role("button", name="Signup")

    @property
    def login_user_email_input_field(self):
        return self.page.locator('.login-form').get_by_placeholder('Email Address')

    @property
    def login_user_password_input_field(self):
        return self.page.locator('.login-form').get_by_placeholder('Password')

    @property
    def login_button(self):
        return self.page.get_by_role('button', name='Login')

    @property
    def login_error_message(self):
        return  self.page.get_by_text(self.LOGIN_ERROR_TEXT)

    def signup(self, name, email):
        self.signup_username_input_field.fill(name)
        self.signup_email_input_field.fill(email)
        self.signup_button.click()
        return SignupPage(self.page)

    def login(self, data: LoginData):
        self.login_user_email_input_field.fill(data.email)
        self.login_user_password_input_field.fill(data.password)
        self.login_button.click()
        if data.valid:
            from page_objects.home_page import HomePage
            return HomePage(self.page)
        else:
            return None


    def is_loaded(self):
        login_text = self.page.get_by_text('Login to your account')
        if not login_text.is_visible():
            return False
        return True

    def invalid_login(self):
        return self.login_error_message.is_visible()






