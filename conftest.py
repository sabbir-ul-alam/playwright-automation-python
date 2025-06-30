import pytest
import json
from page_objects.home_page import HomePage
from playwright.sync_api import Page


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="stg", help="Environment to run"
    )


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    with open(f"config/{env}.json") as f:
        return json.load(f)


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



