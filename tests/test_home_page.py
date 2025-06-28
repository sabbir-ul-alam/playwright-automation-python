import time

from click import pause
from playwright.sync_api import Page

from page_objects.home_page import HomePage


def test_verify_scrollup_functionality_using_arrow_icon(validated_homepage: HomePage):
    locator = validated_homepage.page.locator('h2').get_by_text('Subscription')
    locator.scroll_into_view_if_needed()
    assert locator.is_visible()

    validated_homepage.page.locator('#scrollUp').click()
    text = validated_homepage.page.get_by_text('Full-Fledged practice website for Automation Engineers').first
    text.scroll_into_view_if_needed()
    bounding_box = text.bounding_box()
    assert bounding_box is not None, "Element not found on the page"
    assert text.is_visible()

