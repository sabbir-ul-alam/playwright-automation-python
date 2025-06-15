from playwright.sync_api import Playwright, Page
import pytest
from playwright.sync_api import expect


def test_case_1_register_user(page: Page):
    page.goto('http://automationexercise.com')
    expect(page.locator("body")).to_be_visible()

