import pytest
from typing import Dict, Generator
from utils.api_helper import APIHelper

@pytest.fixture(scope="session")
def api_helper() -> Generator[APIHelper, None, None]:
    """Fixture to provide APIHelper instance for the entire test session."""
    helper = APIHelper()
    yield helper

@pytest.fixture(scope="session")
def test_user_data() -> Dict[str, str]:
    """Fixture to provide test user data."""
    return {
        "email": "ssualsabbir@gmail.com",
        "password": "123456789"
    }

@pytest.fixture(autouse=True)
def log_test_info(request) -> Generator[None, None, None]:
    """Automatically log test information before and after each test."""
    test_name = request.node.name
    print(f"\nStarting test: {test_name}")
    yield
    print(f"\nFinished test: {test_name}")

def pytest_collection_modifyitems(items):
    """Add markers to tests based on their location/name."""
    for item in items:
        if "api_tests" in str(item.fspath):
            item.add_marker(pytest.mark.api)
            
        if "test_product" in str(item.fspath):
            item.add_marker(pytest.mark.product)
        elif "test_brand" in str(item.fspath):
            item.add_marker(pytest.mark.brand)
        elif "test_auth" in str(item.fspath):
            item.add_marker(pytest.mark.auth) 