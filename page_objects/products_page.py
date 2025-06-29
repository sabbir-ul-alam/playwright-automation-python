from playwright.sync_api import Page, expect

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
            
    def is_products_page_visible(self) -> bool:
        """Check if products page is loaded"""
        return self.locators.all_products_text.is_visible()
        
    def search_product(self, product_name: str):
        """Search for a product"""
        self.locators.search_input.fill(product_name)
        self.locators.search_button.click()
        
    def get_search_results_count(self) -> int:
        """Get the number of products found in search results"""
        return self.locators.product_items.count() 