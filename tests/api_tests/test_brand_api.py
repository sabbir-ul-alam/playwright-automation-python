import pytest
from typing import Dict, Any
from utils.api_helper import APIHelper

@pytest.fixture(scope="session")
def api_helper() -> APIHelper:
    """Fixture to provide APIHelper instance."""
    return APIHelper()

@pytest.mark.api
class TestBrandAPI:
    """Test suite for Brand-related API endpoints."""
    
    def test_get_all_brands_list(self, api_helper: APIHelper):
        """
        Test Case for API 3: Get All Brands List
        
        API URL: https://automationexercise.com/api/brandsList
        Request Method: GET
        Response Code: 200
        Response: All brands list
        """
        response = api_helper.get(api_helper.endpoints["brands_list"])
        response_data = api_helper.validate_response(response)
        
        # Verify response structure
        assert "brands" in response_data, "Response does not contain 'brands' key"
        assert isinstance(response_data["brands"], list), "Brands is not a list"
        assert len(response_data["brands"]) > 0, "Brands list is empty"
        
        # Verify brand schema
        first_brand = response_data["brands"][0]
        required_keys = {"id", "brand"}
        assert all(key in first_brand for key in required_keys), \
            f"Brand missing required keys. Expected {required_keys}" 