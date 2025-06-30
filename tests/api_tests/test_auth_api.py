import pytest
from utils.api_helper import APIHelper
from test_data.login_data import login_data_list

@pytest.mark.auth
class TestAuthAPI:
    """
    Test suite for Authentication-related API endpoints.
    Uses explicit login data and validates both message and responseCode.
    """

    @pytest.mark.parametrize("login_data", login_data_list)
    def test_verify_login_various_cases(self, api_helper: APIHelper, login_data):
        """
        Test API: Verify Login with various scenarios using explicit login data.
        API URL: https://automationexercise.com/api/verifyLogin
        Request Method: POST
        """
        response = api_helper.post(api_helper.endpoints["verify_login"], data=login_data.payload)
        response_data = api_helper.validate_response(
            response,
            expected_status=login_data.expected_code,
            expected_response_code=login_data.expected_response_code
        )
        assert response_data["message"] == login_data.expected_message, \
            f"Expected message '{login_data.expected_message}' but got '{response_data.get('message')}'"
        # login_data.email, login_data.password, login_data.valid, login_data.user_name remain available for other usages 