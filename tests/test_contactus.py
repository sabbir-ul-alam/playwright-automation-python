from playwright.sync_api import Page
from page_objects.home_page import HomePage
from test_data.contactus_data import contactus_data_list

contact_data = contactus_data_list[0]

def test_contactus_form(validated_homepage: HomePage):
    contactus_page = validated_homepage.goto_contactus()
    assert contactus_page.is_loaded()

    # page.on("dialog", lambda dialog: dialog.accept())
    contactus_page.submit_feedback(contact_data)

    assert contactus_page.is_submitted(), 'Failed to submit contact form'

    homepage = contactus_page.goback_to_homepage()
    assert homepage.is_loaded(), 'Failed to load homepage'
