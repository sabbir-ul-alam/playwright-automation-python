from playwright.sync_api import Playwright, Page
import pytest
from playwright.sync_api import expect
from page_objects.home_page import HomePage
from utils.css_assert import assert_css_property


def test_case_1_register_user(page: Page):
    homepage = HomePage(page)
    homepage.visit()
    assert homepage.is_loaded()
    assert_css_property(homepage.locators.home_link,'color', 'rgb(255, 165, 0)')
    login_page = homepage.goto_login_or_signup()
    signup_page = login_page.signup('Sabbir','ssualsabbir@gmail.com')


    # # page.get_by_role("radio", name="Mr.").check()
    # # page.get_by_role("textbox", name="Name *", exact=True).click()
    # # page.get_by_role("textbox", name="Password *").click()
    # page.get_by_role("textbox", name="Password *").fill("123456789")
    # page.locator("#days").select_option("29")
    # page.locator("#months").select_option("10")
    # page.locator("#years").select_option("1996")
    # page.get_by_role("checkbox", name="Sign up for our newsletter!").check()
    # page.get_by_role("checkbox", name="Receive special offers from").check()
    # # page.get_by_role("textbox", name="First name *").click()
    # page.get_by_role("textbox", name="First name *").fill("sabbir ul alam")
    # # page.get_by_role("textbox", name="First name *").press("Tab")
    # page.get_by_role("textbox", name="Last name *").fill("sabbir")
    # page.get_by_role("paragraph").filter(has_text="Company").first.click()
    # # page.get_by_role("textbox", name="Company", exact=True).fill("tigerit")
    # # page.get_by_role("textbox", name="Address * (Street address, P.").click()
    # page.get_by_role("textbox", name="Address * (Street address, P.").fill("matikata")
    # page.get_by_label("Country *").select_option("United States")
    # # page.get_by_role("textbox", name="State *").click()
    # page.get_by_role("textbox", name="State *").fill("chicago")
    # # page.get_by_text("Title Mr. Mrs. Name * Email").click()
    # # page.get_by_role("textbox", name="City * Zipcode *").click()
    # page.get_by_role("textbox", name="City * Zipcode *").fill("illonois")
    # # page.locator("#zipcode").click()
    # page.locator("#zipcode").fill("34430")
    # # page.get_by_role("textbox", name="Mobile Number *").click()
    # page.get_by_role("textbox", name="Mobile Number *").fill("01558258590")
    # page.get_by_role("button", name="Create Account").click()
    # page.pause()
    # page.get_by_text("Account Created!").click()
    expect(page.get_by_text("Account Created!")).to_be_visible()
    page.get_by_role("link", name="Continue").click()
    expect(page.get_by_text("Logged in as sabbir")).to_be_visible()
    # page.get_by_text("Logged in as sabbir").click()
    page.get_by_role("link", name="Delete Account").click()
    expect(page.get_by_text("Account Deleted!")).to_be_visible()
    page.get_by_role("link", name="Continue").click()



