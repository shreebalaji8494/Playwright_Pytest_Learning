import pytest
from playwright.sync_api import expect

def test_google_search(page):
    page.goto("https://www.google.com")
    search_box = page.locator("#ti6dpd")
    search_box.fill("Playwright Python")
    search_box.press("Enter")
    expect(page).to_have_title("Playwright Python - Google Search")