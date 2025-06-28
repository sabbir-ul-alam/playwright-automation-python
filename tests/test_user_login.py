import pytest
from playwright.sync_api import Page
from page_objects.home_page import HomePage
from test_data.login_data import LoginData, login_data_list

'''
Test Case 2: Login User with correct email and password
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter correct email address and password
7. Click 'login' button
8. Verify that 'Logged in as username' is visible
-------------------------------------------------------------
Test Case 3: Login User with incorrect email and password
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'Login to your account' is visible
6. Enter incorrect email address and password
7. Click 'login' button
8. Verify error 'Your email or password is incorrect!' is visible
'''

@pytest.mark.parametrize("login_data", login_data_list)
def test_user_login(validated_homepage: HomePage, login_data: LoginData):
    login_page = validated_homepage.goto_login_or_signup()
    assert login_page.is_loaded()

    if login_data.valid:
        homepage = login_page.login(login_data)
        #will call api to get the user_name in future
        assert homepage.is_user_logged_in(login_data.user_name), 'Failed to log in properly'
    else:
        login_page.login(login_data)
        assert login_page.invalid_login(), 'Login error message is not showing for invalid login'


def test_user_logout(validated_homepage: HomePage):
    login_page = validated_homepage.goto_login_or_signup()
    assert login_page.is_loaded()
    homepage = login_page.login(login_data_list[0])
    login_page = homepage.logout()
    assert login_page.is_loaded(), 'Failed to logout properly'












