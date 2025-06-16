from playwright.sync_api import Page

class ConfirmationPage:

    CONFIRMATION_TEXT : str = 'Account Created!'
    DELETE_ACCOUNT_CONFIRMATION_TEXT: str = 'Account Deleted!'


    def __init__(self,page: Page):
        self.page = page
        self.locators = self.Locators(page)


    class Locators:
        def __init__(self,page):
            self.page = page
            self.confirm_account_created = self.page.locator('[data-qa="account-created"]')
            self.confirm_account_delete = page.locator('[data-qa="account-deleted"]')
            self.continue_to_homepage_button = self.page.locator('[data-qa="continue-button"]')



    def is_account_created(self):
        return self.locators.confirm_account_created.text_content() == self.CONFIRMATION_TEXT

    def is_account_deleted(self):
        return self.locators.confirm_account_delete.text_content() == self.DELETE_ACCOUNT_CONFIRMATION_TEXT

    def goback_to_homepage(self):
        from page_objects.home_page import HomePage
        self.locators.continue_to_homepage_button.click()
        return HomePage(self.page)
