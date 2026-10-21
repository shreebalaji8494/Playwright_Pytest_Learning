#In this Test we are going to generate an order using api and then verify the order id in orders page 
#using web automation.
from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils

def test_e2e_webApiIntegration(playwright:Playwright):
    #Step 1:create order using api
    #for achieving this step we need to call the api methods which we have written in the utils package.
    # we will do it by creating a class object for that class and then call the method.
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright)

    #Step 2: Login to the web page using credentials
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    # page.get_by_placeholder("email@example.com").fill("shreebalajimsc@gmail.com")
    # page.get_by_placeholder("enter your passsword").fill("Dinku@2408")
    page.locator("#userEmail").fill("shreebalajimsc@gmail.com")
    page.locator("#userPassword").fill("Dinku@2408")
    page.get_by_role("button",name="Login").click()

    #Step 3 : Go to orders page and then click view button in the particular order and then assert the message
    page.get_by_role("button",name="ORDERS").click()
    #finding the view button of our order id
    row = page.locator("tr").filter(has_text=order_id)
    #now clicking view button of that particular entry 
    row.get_by_role("button",name="View").click()
    #Assert the thank you text
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")


