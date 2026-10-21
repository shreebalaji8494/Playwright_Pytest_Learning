#This test is to intercept a particular API request.
#For example, in the same order history page, consider if we are viewing an order which was placed by a different user.
#i.e the user who is viewing the order is not the one who placed the order. Ideally it will be throwing an error.
from playwright.sync_api import Page,expect

#We are using the continue method which will replace the endpoint url from what we have given in the route method
#This will help us to test negative scenarios which can be used in security testing.
def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6ad833a893b084c41f5d8c10")


def test_InterceptAPIRequests(page : Page):
    #We will perform the same operations of logging into the page and clicking on orders button.
    # we will just add one step where it will listen to the API call when it gets triggered.
    page.goto("https://rahulshettyacademy.com/client")
    # route method 
    #Routing provides the capability to modify network requests that are made by a page.
    #Once routing is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or aborted.
    #this url will get triggered once we click on the view button and 
    # hence we ask playwright to listen to this event using route method.
    #Here we are giving /* in the url because the user id is always dynamic and we are not sure which user will be testing this test.
    #Users are different users of that webpage who has a valid account. Each account will have an account id which will be sent with the url.
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.locator("#userEmail").fill("shreebalajimsc@gmail.com")
    page.locator("#userPassword").fill("Dinku@2408")
    page.get_by_role("button",name="Login").click()
    
    page.get_by_role("button",name="ORDERS").click()

    #Click on the view button of the first order in the list.
    
    page.get_by_role("button",name="View").first.click()

    #We will be validating the error message and asserting it.
    order_error_message = page.locator(".blink_me").text_content()
    print(order_error_message)

    expect(page.locator(".blink_me")).to_have_text("You are not authorize to view this order")

