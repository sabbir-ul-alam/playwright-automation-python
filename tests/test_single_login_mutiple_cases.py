from page_objects.home_page import HomePage
from test_data.product_data import product_data_list

product_data = product_data_list[0]


def test_add_product_to_cart_from_product_page(validated_homepage: HomePage):
    product_page = validated_homepage.goto_product_page()
    product_page.search_product(product_name=product_data.product_name)
    product_page.add_product_to_cart(product_data)
    cart_page = product_page.goto_cart_from_modal()
    assert not cart_page.is_cart_empty(), "Cart is empty, failed to add product"

def test_verify_cart_item(validated_homepage: HomePage):
    product_page = validated_homepage.goto_product_page()
    product_page.search_product(product_name=product_data.product_name)
    product_page.add_product_to_cart(product_data)
    cart_page = product_page.goto_cart_from_modal()
    assert not cart_page.is_cart_empty(), "Cart is empty, failed to add product"

    assert cart_page.get_item_price(product_data) == product_data.price, "Cart item price doesnt match"







