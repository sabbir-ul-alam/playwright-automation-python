import pytest
from typing import Dict, Any
from utils.api_helper import APIHelper

@pytest.fixture(scope="session")
def api_helper() -> APIHelper:
    """Fixture to provide APIHelper instance."""
    return APIHelper()

@pytest.mark.api
class TestProductAPI:
    """Test suite for Product-related API endpoints."""
    
    def test_get_all_products_list(self, api_helper: APIHelper):
        """
        Test Case for API 1: Get All Products List
        
        API URL: https://automationexercise.com/api/productsList
        Request Method: GET
        Expected Response Code: 200
        Expected Response: All products list
        """
        response = api_helper.get(api_helper.endpoints["products_list"])
        response_data = api_helper.validate_response(response)
        
        # Verify response structure
        assert "products" in response_data, "Response does not contain 'products' key"
        assert isinstance(response_data["products"], list), "Products is not a list"
        assert len(response_data["products"]) > 0, "Products list is empty"
        
        # Verify product schema
        first_product = response_data["products"][0]
        required_keys = {"id", "name", "price", "brand", "category"}
        assert all(key in first_product for key in required_keys), \
            f"Product missing required keys. Expected {required_keys}"
    
    def test_post_to_all_products_list(self, api_helper: APIHelper):
        """
        Test Case for API 2: POST To All Products List
        
        API URL: https://automationexercise.com/api/productsList
        Request Method: POST
        Response Code: 200 (with responseCode 405)
        Response Message: This request method is not supported.
        """
        response = api_helper.post(api_helper.endpoints["products_list"])
        response_data = api_helper.validate_response(
            response,
            expected_response_code=405
        )
        
        assert response_data["message"] == "This request method is not supported.", \
            "Unexpected error message" 