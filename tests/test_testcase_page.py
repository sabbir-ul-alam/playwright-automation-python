from playwright.sync_api import Page, expect

from page_objects.testcase_page import PageTestCase


def test_verify_test_case_page(validated_homepage):
    page = validated_homepage.page
    with page.context.expect_page() as new_page_info:
        validated_homepage.goto_testcase_page_in_new_tab()
    testcase_page = PageTestCase(new_page_info.value)
    # new_tab = new_page_info.value
    assert new_page_info is not None, "Failed to open new tab"
    assert "https://automationexercise.com/test_cases" == testcase_page.url
    expect(testcase_page.test_case_title).to_be_visible()

