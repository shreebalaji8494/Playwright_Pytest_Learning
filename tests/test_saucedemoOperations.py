from playwright.sync_api import Page
#Using Page Object Model, we are performing the tasks instead of providing locators here, we are using the methods from the page classes to perform the tasks.
from pages.saucedemo_login_page import SaucedemoLoginPage
from pages.saucedemo_home_page import SaucedemoHomePage
from pages.saucedemo_checkout_page import SaucedemoCheckoutPage


def test_runSaucedemoOperations(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")

    #Creating objects of the page classes to use their methods for performing the tasks.
    login_page = SaucedemoLoginPage(page)
    home_page = SaucedemoHomePage(page)
    checkout_page = SaucedemoCheckoutPage(page)

    #Using the methods from the page classes to perform the tasks instead of providing locators here.
    login_page.login("standard_user", "secret_sauce")
    home_page.perform_adding_items_to_cart_and_click_shopping_cart()
    checkout_page.perform_checkout("Captain", "Jack", "62458")

