import pytest
from playwright.sync_api import Playwright, Page


def test_create_account(page: Page):
    page.goto("http://localhost:3000/signin")
    page.get_by_role("textbox", name="Username").fill("Heath93")
    page.get_by_role("textbox", name="Password").fill("s3cret")
    page.get_by_role("checkbox", name="Remember me").check()
    page.locator("[data-test=\"signin-submit\"]").click()
    page.locator("[data-test=\"sidenav-user-settings\"]").click()
    page.locator("[data-test=\"sidenav-bankaccounts\"]").click()
    page.locator("[data-test=\"bankaccount-new\"]").click()
    page.get_by_role("textbox", name="Bank Name").click()
    page.get_by_role("textbox", name="Bank Name").fill("test1")
    page.get_by_role("textbox", name="Routing Number").fill("123456789")
    # page.get_by_role("textbox", name="Routing Number").press("Tab")
    page.get_by_role("textbox", name="Account Number").fill("abcdefghij")
    # page.locator("[data-test=\"bankaccount-submit\"]").click()
    page.locator("[data-test=\"sidenav-signout\"]").click()


def test_create_account_copy(page: Page, config):
    page.goto("http://localhost:3000/user/settings")
    page.get_by_role("textbox", name="Username").fill("Heath93")
    page.get_by_role("textbox", name="Password").fill("s3cret")
    page.get_by_role("checkbox", name="Remember me").check()
    page.pause()
    page.locator("[data-test=\"signin-submit\"]").click()
    page.locator("[data-test=\"sidenav-user-settings\"]").click()
    page.locator("[data-test=\"sidenav-bankaccounts\"]").click()
    page.locator("[data-test=\"bankaccount-new\"]").click()
    page.get_by_role("textbox", name="Bank Name").click()
    page.get_by_role("textbox", name="Bank Name").fill("test1")
    page.get_by_role("textbox", name="Routing Number").fill("123456789")
    # page.get_by_role("textbox", name="Routing Number").press("Tab")
    page.get_by_role("textbox", name="Account Number").fill("abcdefghij")
    # page.locator("[data-test=\"bankaccount-submit\"]").click()
    page.locator("[data-test=\"sidenav-signout\"]").click()
