from playwright.sync_api import  Page

from page_objects.home_page import HomePage
from test_data.login_data import login_data_list
from test_data.product_data import product_data_list
from test_data.payment_data import payment_data_list

'''
Test Case 24: Download Invoice after purchase order
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Add products to cart
5. Click 'Cart' button
6. Verify that cart page is displayed
7. Click Proceed To Checkout
8. Click 'Register / Login' button
9. Fill all details in Signup and create account
10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
11. Verify ' Logged in as username' at top
12.Click 'Cart' button
13. Click 'Proceed To Checkout' button
14. Verify Address Details and Review Your Order
15. Enter description in comment text area and click 'Place Order'
16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
17. Click 'Pay and Confirm Order' button
18. Verify success message 'Your order has been placed successfully!'
19. Click 'Download Invoice' button and verify invoice is downloaded successfully.
20. Click 'Continue' button
21. Click 'Delete Account' button
22. Verify 'ACCOUNT DELETED!' and click 'Continue' button
Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality
Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality'''

product_data = product_data_list[0]
login_data = login_data_list[0]
payment_data = payment_data_list[0]

def test_download_invoice_after_purchase_order(validated_homepage: HomePage):
    logged_in = False
    validated_homepage.add_feature_product_to_cart(product_data)
    cart_page = validated_homepage.goto_cart_from_modal()
    
    if logged_in:
        checkout_page = cart_page.checkout(logged_in)
    else:
        cart_page.checkout(logged_in)
        login_page = cart_page.goto_login_from_modal()
        logged_in = True
        homepage = login_page.login(login_data)
        cart_page = homepage.goto_cart()
        checkout_page = cart_page.checkout(logged_in)
    
    payment_page = checkout_page.place_order()
    confirmation_page = payment_page.make_payment(payment_data)
    assert confirmation_page.download_invoice() is not None, 'Failed to download'




