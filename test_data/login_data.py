from dataclasses import dataclass
from typing import Dict

@dataclass
class LoginData:
    email: str
    password: str
    valid: bool
    user_name: str
    # Extra fields for API tests
    payload: Dict[str, str]
    expected_code: int
    expected_message: str
    expected_response_code: int


login_data_list = [
    # Valid login
    LoginData(
        email="sualsabbir@gmail.com",
        password="123456789",
        valid=True,
        user_name="Sabbir",
        payload={"email": "sualsabbir@gmail.com", "password": "123456789"},
        expected_code=200,
        expected_message="User Sabbir logged in successfully.",
        expected_response_code=200
    ),
    # Missing email
    LoginData(
        email="",
        password="123456789",
        valid=False,
        user_name="Sabbir",
        payload={"password": "123456789"},
        expected_code=400,
        expected_message="Bad request, email or password parameter is missing in POST request.",
        expected_response_code=400
    ),
    # Missing password
    LoginData(
        email="sualsabbir@gmail.com",
        password="",
        valid=False,
        user_name="Sabbir",
        payload={"email": "sualsabbir@gmail.com"},
        expected_code=400,
        expected_message="Bad request, email or password parameter is missing in POST request.",
        expected_response_code=400
    ),
    # Both missing
    LoginData(
        email="",
        password="",
        valid=False,
        user_name="Sabbir",
        payload={},
        expected_code=400,
        expected_message="Bad request, email or password parameter is missing in POST request.",
        expected_response_code=400
    ),
]