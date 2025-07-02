import pytest
from pathlib import Path
from playwright.sync_api import Playwright, Page
from page_objects.home_page import HomePage
from test_data.login_data import login_data_list
from test_data.product_data import product_data_list

product_data = product_data_list[0]
login_data = login_data_list[0]

@pytest.fixture(scope="class", autouse=True)
def login_and_save_state(playwright: Playwright):
    state_file = Path("state/state.json")
    # if not state_file.exists():
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    homepage = HomePage(page)
    homepage.visit()
    assert homepage.is_loaded(), "Homepage failed to load properly"

    login_page = homepage.goto_login_or_signup()
    login_page.login(login_data)

    context.storage_state(path=str(state_file))
    browser.close()

@pytest.fixture(scope="function")
def browser_context_args():
    return {"storage_state": "state/state.json"}

class TestSingleLogin:

    def test_add_product_to_cart_from_product_page(self, page: Page):
        homepage = HomePage(page)
        homepage.visit()
        product_page = homepage.goto_product_page()
        product_page.search_product(product_name=product_data.product_name)
        product_page.add_product_to_cart(product_data)
        cart_page = product_page.goto_cart_from_modal()
        assert not cart_page.is_cart_empty(), "Cart is empty, failed to add product"

    def test_verify_cart_item(self, page: Page):
        homepage = HomePage(page)
        homepage.visit()
        cart_page = homepage.goto_cart_page()
        assert not cart_page.is_cart_empty(), "Cart is empty, failed to add product"
        assert cart_page.get_item_price(product_data) == product_data.price, "Cart item price doesn't match"
