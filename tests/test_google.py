import pytest
from playwright.sync_api import expect

# This small smoke test demonstrates a simple browser search flow in Playwright.
# It verifies that entering a search query on Google leads to the expected page title.


def test_google_search(page):
    # Navigate to the Google homepage before running the search action.
    page.goto("https://www.google.com")

    # Locate the search box and enter the query text.
    search_box = page.locator("#ti6dpd")
    search_box.fill("Playwright Python")
    search_box.press("Enter")

    # Confirm the result page title matches the expected query result.
    expect(page).to_have_title("Playwright Python - Google Search")