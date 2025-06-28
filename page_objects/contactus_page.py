import time
from playwright.sync_api import Page

from test_data.contactus_data import ContactUs


class ContactusPage:
    CONTACTUS_SUCCESS_TEXT ='Success! Your details have been submitted successfully.'
    CONTACT_PAGE_HEADER_TEXT = 'Contact Us'
    def __init__(self, page: Page):
        self.page = page
        self.locators = self.Locators(page)

    class Locators:
        def __init__(self, page : Page):
            self.page = page
            self.continue_to_homepage_button = self.page.locator('#form-section a')
            self.success_alert_text = self.page.locator('div.status.alert-success').filter(has_text='Success!')
            self.confirm_loaded_text = self.page.locator('h2').filter(has_text=ContactusPage.CONTACT_PAGE_HEADER_TEXT)
            self.name_intput_field = self. page.locator('[data-qa="name"]')
            self.email_intput_field = self.page.locator('[data-qa="email"]')
            self.subject_input_field = self.page.locator('[data-qa="subject"]')
            self.message_input_field = self.page.locator('[data-qa="message"]')
            self.upload_file_field = self.page.locator('input[name="upload_file"]')
            self.submit_button = self.page.locator('[data-qa="submit-button"]')


    def fill_up_form(self, data: ContactUs):
        self.locators.name_intput_field.fill(data.name)
        self.locators.email_intput_field.fill(data.email)
        self.locators.subject_input_field.fill(data.subject)
        self.locators.message_input_field.fill(data.message_body)
        self.upload_file(data.file_path)


    def upload_file(self, file_path: str):
        self.locators.upload_file_field.set_input_files(file_path)


    def submit_feedback(self, data: ContactUs):
        self.fill_up_form(data)

        # with self.page.expect_event("dialog", timeout=3000) as dialog_info:
        #     self.locators.submit_button.click()  # This must happen *immediately*
        # dialog_info.value.accept()

        self.page.on("dialog", lambda dialog: dialog.accept())
        time.sleep(.5)
        self.locators.submit_button.click()


    def is_submitted(self):
        self.locators.success_alert_text.wait_for(state="visible", timeout=5000)
        return self.locators.success_alert_text.is_visible()


    def is_loaded(self):
        return self.locators.confirm_loaded_text.is_visible()

    def goback_to_homepage(self):
        from page_objects.home_page import HomePage
        self.locators.continue_to_homepage_button.click()
        return HomePage(self.page)

