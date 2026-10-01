import pytest
from playwright.sync_api import Page

from pages.demoQA_practice_page import DemoQAPracticePage

def test_fill_form(page: Page):
    """Test filling out the form on the DemoQA practice page."""
    # Navigate to the practice page.
    page.goto("https://demoqa.com/automation-practice-form")

    # Create an instance of the page object for the practice page.
    practice_page = DemoQAPracticePage(page)

    # Fill in the form fields with test data.
    practice_page.fill_name_email_mobileNumber(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        mobile_number="1234567890"
    )
    practice_page.fill_date_of_birth(date_of_birth="01 Jan 1990")
    practice_page.select_gender(gender="Male")
    practice_page.select_hobbies(hobbies=["Sports", "Reading"])    
    practice_page.fill_current_address(address="123 Main St, Anytown, USA")
    practice_page.select_state_city(state="Haryana", city="Karnal")
    practice_page.submit_form()
