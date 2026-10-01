from playwright.sync_api import Page
import pytest

# This test follows the Page Object Model (POM), where each page has a dedicated
# class that encapsulates the locators and user actions for that screen.
from pages.saucedemo_login_page import SaucedemoLoginPage
from pages.saucedemo_home_page import SaucedemoHomePage
from pages.saucedemo_checkout_page import SaucedemoCheckoutPage

# The parametrization can happen in 3 ways: pass the value in @pytest.mark.parametrize, pass the csv file in the @pytest.mark.parametrize or using JSON file having data we can parametrize the test.
#Using CSV file to parametrize the test
def get_csv_data():
    """Read test data from a CSV file and return it as a list of tuples."""
    import csv
    data = []
    with open('./test_data/data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # kip the header row
        for row in reader:
            data.append((row[0], row[1]))  # Assuming username is in column 0 and password in column 1
    return data

#Using JSON file to parametrize the test
def get_json_data():
    """Read test data from a JSON file and return it as a list of tuples."""
    import json
    with open('./test_data/data.json') as jsonfile:
        data = json.load(jsonfile)
        return [(item['username'], item['password']) for item in data]  # Assuming the JSON structure has 'username' and 'password' keys

# The test below is parameterized to run with multiple sets of credentials, allowing
# us to verify the login and checkout flow for different user types in a single test function.
@pytest.mark.parametrize("username, user_password", get_json_data())

def test_runSaucedemoOperations(page: Page, username: str, user_password: str) -> None:
    """Exercise the main SauceDemo shopping and checkout flow end to end."""
    # Open the login page for the application under test.
    page.goto("https://www.saucedemo.com/")

    # Create page-object instances to keep the test readable and reusable.
    login_page = SaucedemoLoginPage(page)
    home_page = SaucedemoHomePage(page)
    checkout_page = SaucedemoCheckoutPage(page)

    # Log in, add products to the cart, and complete the checkout flow.
    login_page.login(username, user_password)
    home_page.perform_adding_items_to_cart_and_click_shopping_cart()
    checkout_page.perform_checkout("Captain", "Jack", "62458")

