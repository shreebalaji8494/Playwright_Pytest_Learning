import pytest
from playwright.sync_api import Page, expect

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

    # Verify that the form submission was successful by checking the modal dialog for the expected values.
    results_table = page.locator(".table-responsive")
    expected_values = {
        "Student Name": "John Doe",
        "Student Email": "john.doe@example.com",
        "Gender": "Male",
        "Mobile": "1234567890",
        "Hobbies": "Sports, Reading",
        "Address": "123 Main St, Anytown, USA",
        "State and City": "Haryana Karnal",
    }

    expect(results_table).to_be_visible()
    for label, value in expected_values.items():
        row = results_table.get_by_role("row").filter(has_text=label)
        expect(row).to_contain_text(value)

    date_row = results_table.get_by_role("row").filter(has_text="Date of Birth")
    expect(date_row).to_contain_text("01")
    expect(date_row).to_contain_text("January")
    expect(date_row).to_contain_text("1990")

    hobbies_row = results_table.get_by_role("row").filter(has_text="Hobbies")
    expect(hobbies_row).to_contain_text("Sports, Reading")

    practice_page.close_modal()
