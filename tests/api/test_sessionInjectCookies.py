#This test class is for injecting session cookies to save time during automation.
#For example, we are logging into the url all the time which makes it a bit time taking process.
#What if we can bypass that step by accessing the browser's local storage which stores key elements of a session.
#We know that placing order using api will need a token. Have you imagined how the token is fetched if we placed an order using the webpage itself?
#The answer is the token is getting generated during the login page itself when we click login button using our credentials.
#We are going to use that browser's local storage and bypass the login step by passing the token and directly performing our test case.
# For that we will be using our getToken method which we used in our API utils class to create order using API.
from playwright.sync_api import Playwright,expect

from utils.apiBase import APIUtils

def test_injectSessionCookies(playwright: Playwright):
    #Step 1 - Get the token from the APIUtils class.
    apiUtils = APIUtils()
    token= apiUtils.getToken(playwright)

    #Step 2 - Inject the token to the browser's local storage.
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # We are using add_init_script method to get to the local storage using javascript command.
    page.add_init_script(f"""localStorage.setItem('token','{token}')""")

    #Step 3 - go to the orders page and verify if it has "Your orders" text visible
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button",name="ORDERS").click()
    #Verify the text content
    expect(page.get_by_text("Your Orders")).to_be_visible()
