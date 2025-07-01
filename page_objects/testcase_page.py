from playwright.sync_api import Page


class PageTestCase:

    def __init__(self, page: Page):
        self.page = page

    @property
    def test_case_title(self):
        return self.page.locator('.title',has_text='Test Cases')

    @property
    def url(self):
        return self.page.url