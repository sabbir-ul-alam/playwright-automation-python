from playwright.sync_api import Page, expect

from page_objects.cart_page import CartPage
from test_data.product_data import ProductData


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = self.Locators(page)

    class Locators:
        def __init__(self, page: Page):
            self.page = page
            self.all_products_text = page.get_by_text("ALL PRODUCTS")
            self.search_input = page.get_by_placeholder("Search Product")
            self.search_button = page.locator("#submit_search")
            self.product_items = page.locator(".features_items .product-image-wrapper")
            self.view_cart_modal= page.locator('.modal-body').get_by_text('View Cart')
            self


        def product_locators(self, product_id):
            return[
                self.page.locator('.features_items').locator(f'.productinfo > a[data-product-id="{product_id}"]'),
                self.page.locator(f'.overlay-content > a[data-product-id="{product_id}"]')
            ]

        # def item_price_locator(self, product_id):
        #     return self.page.locator(f'#product-{product_id} .cart_price')

    def is_products_page_visible(self) -> bool:
        """Check if products page is loaded"""
        return self.locators.all_products_text.is_visible()
        
    def search_product(self, product_name: str):
        """Search for a product"""
        self.locators.search_input.fill(product_name)
        self.locators.search_button.click()
        # self.locators.product_items.scroll_into_view_if_needed()
        
    def get_search_results_count(self) -> int:
        """Get the number of products found in search results"""
        return self.locators.product_items.count()

    def add_product_to_cart(self, product: ProductData):
        product_element, overlay_element = self.locators.product_locators(product_id=product.product_id)
        product_element.scroll_into_view_if_needed()
        product_element.hover()
        assert overlay_element.is_visible()
        # overlay_element.scroll_into_view_if_needed()
        overlay_element.click()

    def goto_cart_from_modal(self):
        self.locators.view_cart_modal.click()
        return CartPage(self.page)

    # def get_item_price(self, product: ProductData):
    #     return int(self.locators.item_price_locator(product_id=product.product_id).text_content())