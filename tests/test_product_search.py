import pytest
from playwright.sync_api import expect

from page_objects.home_page import HomePage
from page_objects.products_page import ProductsPage
from test_data.product_data import ProductSearchData, product_search_data_list

'''
Test Case 9: Search Product
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Products' button
5. Verify user is navigated to ALL PRODUCTS page successfully
6. Enter product name in search input and click search button
7. Verify 'SEARCHED PRODUCTS' is visible
8. Verify all the products related to search are visible
'''

@pytest.fixture
def products_page(validated_homepage: HomePage) -> ProductsPage:
    """
    Fixture that navigates to the products page and validates it.
    Returns a validated ProductsPage object that can be used in tests.
    """
    # Navigate to products page using proper page object navigation
    products_page = validated_homepage.goto_products()
    assert products_page.is_products_page_visible(), "Products page failed to load properly"
    return products_page

@pytest.mark.parametrize("search_data", product_search_data_list)
def test_search_product(products_page: ProductsPage, search_data: ProductSearchData):
    """Test searching for products with different search terms"""
    # Search for the product
    products_page.search_product(search_data.search_term)
    
    # Get search results count
    search_results_count = products_page.get_search_results_count()
    
    # Verify products are found (or not) as expected
    if search_data.expected_results:
        assert search_results_count > 0, f"No products found for search term: {search_data.search_term}"
    else:
        assert search_results_count == 0, f"Products found for non-existent search term: {search_data.search_term}" 