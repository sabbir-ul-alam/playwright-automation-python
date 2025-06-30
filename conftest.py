import pytest
import json
from page_objects.home_page import HomePage
from playwright.sync_api import  sync_playwright, Page

def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="stg", help="Environment to run"
    )
    parser.addoption(
        "--e2e-browser", action="store", default=None, help="Browser to run tests on (chromium, firefox, webkit)"
    )

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    with open(f"config/{env}.json") as f:
        return json.load(f)

def pytest_generate_tests(metafunc):
    if "test_browser" in metafunc.fixturenames:
        browser_option = metafunc.config.getoption("e2e_browser")
        browsers = ["chromium", "firefox", "webkit"]
        if browser_option in browsers:
            metafunc.parametrize("test_browser", [browser_option], indirect=True)
        else:
            metafunc.parametrize("test_browser", browsers, indirect=True)

@pytest.fixture(scope="function")
def test_browser(request):
    browser_name = request.param
    headless = not getattr(request.config.option, "headed", False)
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=headless)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture
def validated_homepage(page: Page):
    """
    Fixture that visits and validates the homepage.
    Returns a validated HomePage object that can be used in tests.
    """
    homepage = HomePage(page)
    homepage.visit()
    assert homepage.is_loaded(), "Homepage failed to load properly"
    return homepage



