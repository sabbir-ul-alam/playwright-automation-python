from playwright.sync_api import Page
from page_objects.home_page import HomePage
from test_data.registration_data import user_registration_data_list


registration_data = user_registration_data_list[0]


'''
Test Case 1: Register User
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and email address
7. Click 'Signup' button
8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
9. Fill details: Title, Name, Email, Password, Date of birth
10. Select checkbox 'Sign up for our newsletter!'
11. Select checkbox 'Receive special offers from our partners!'
12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
13. Click 'Create Account button'
14. Verify that 'ACCOUNT CREATED!' is visible
15. Click 'Continue' button
16. Verify that 'Logged in as username' is visible
17. Click 'Delete Account' button
18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button

'''
def test_case_1_register_user(validated_homepage: HomePage):
    login_page = validated_homepage.goto_login_or_signup()
    signup_page = login_page.signup(registration_data.name,registration_data.email)
    confirmation_page = signup_page.create_account(registration_data)
    assert confirmation_page.is_account_created(), 'Failed to create Account'
    
    homepage = confirmation_page.goback_to_homepage()
    assert homepage.is_loaded(), 'Failed to load homepage'
    #verify logged is as user name visible
    assert homepage.is_user_logged_in(registration_data.name), 'Failed to logged in user after signup'
    
    confirmation_page = homepage.delete_account()
    assert confirmation_page.is_account_deleted(), 'Failed to delete account'
    
    homepage = confirmation_page.goback_to_homepage()
    assert homepage.is_loaded()


