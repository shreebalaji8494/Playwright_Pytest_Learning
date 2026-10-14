from playwright.sync_api import Page, expect

def test_playwrightBasics(playwright): # playwright is a fixture provided by the pytest-playwright plugin that allows you to interact with the Playwright API in your tests.
    # Launch a browser instance for playwright
    browser = playwright.chromium.launch(headless=False)  # Set headless=True to run in the background without a UI. By default it runs in headless mode.
    # Create a new browser context
    context = browser.new_context()
    # create a new page in the browser context
    page = context.new_page()
    # Navigate to a website
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")


def test_playwrightUsingPageFixture(page: Page): # page is a fixture provided by the pytest-playwright plugin that allows you to interact with a single page in the browser.
    # Using Page fixture directly, we don't need to launch a browser or create a context manually. Everything is handled by the fixture.
    # If we want page fixture to give suggestions of all the methods available for page, we need to import Page from playwright.sync_api and use it as a type hint for the page parameter in the test function.
    # But this page fixture will always run with Chromium engine and in headless mode. If we want to run the test with a different browser engine or in headed mode, we need to use the playwright fixture instead of the page fixture.
    # Navigate to a website
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

def test_playwrightlocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    #get_by_label() method is used to locate an element by its label text. It is a more human-readable way to locate elements compared to using CSS selectors or XPath. It is especially useful for locating form fields, as it allows you to locate the input field associated with a specific label.
    page.get_by_label("UserName").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    #get_by_role() method is used to locate an element by its ARIA role. It is a more semantic way to locate elements compared to using CSS selectors or XPath. It is especially useful for locating interactive elements, such as buttons, links, and form fields, as it allows you to locate elements based on their intended purpose rather than their visual appearance.
    page.get_by_role("combobox").select_option("teach")
    #csv_selector() method is used to locate an element by its CSS selector. It is a more traditional way to locate elements compared to using label text or ARIA roles. It is especially useful for locating elements that do not have a label or role associated with them, such as divs, spans, and images.
    #checkbox
    page.locator("#terms").check()
    #radio button
    page.get_by_role("radio", name="user").check()
    page.get_by_role("button", name="Sign In").click()
    #wait for the page to load after clicking the Sign In button and do an assertion to verify that the login was successful by checking for the presence of a specific element on the page.
    expect(page.get_by_text('Old password "learning" is no longer valid. Please use the new password "Learning@830$3mK2".')).to_be_visible()
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("button", name="Sign In").click()
    #We are using the locator() method to locate the "Iphone X" card on the page. The locator() method returns a Locator object that represents the element on the page. We are then using the filter() method to filter the locator by its text content. The has_text parameter is used to specify the text content that we want to filter by. In this case, we are filtering by the text "Iphone X". The resulting locator will only match elements that have the text "Iphone X" in them.
    #Since the app-card tag name has multiple elements on the page, we are using the filter() method to narrow down the locator to only match the element that has the text "Iphone X". This is a more efficient way to locate elements on the page, as it reduces the number of elements that need to be searched through.
    iphoneLocator = page.locator("app-card").filter(has_text="iphone X")
    # We are narrowing the search of the add to cart button to only iphone X since there are multiple add to cart buttons on the page.
    # We are using the get_by_role() method to locate the button by its ARIA role, which is "button". 
    # This is a more semantic way to locate elements compared to using CSS selectors or XPath. 
    # It is especially useful for locating interactive elements, such as buttons, links, and form fields, as it allows you to locate elements based on their intended purpose rather than their visual appearance.
    # We are not giving any other name or text to the get_by_role() method since there is only one button in the iphone X card. If there were multiple buttons in the card, we would have to use the name parameter to specify which button we want to click.
    iphoneLocator.get_by_role("button").click()
    nokiaLocator = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaLocator.get_by_role("button").click()
    #After adding the products to the cart , we are going to verify in the cart whether those products are added or not.
    page.get_by_text("Checkout").click()
    #We are using the expect() method to verify that the products are added to the cart by counting the number of rows in the cart.
    #We are using to_have_count() method to verify that the number of rows in the cart is equal to 2, which means that both products are added to the cart.
    expect(page.locator(".media-body")).to_have_count(2)
    

