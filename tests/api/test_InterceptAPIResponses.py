#This test is used to intercept API responses to test edge cases.
#For example, in the orders page, currently we will have orders. But if we have to test a scenario to validate when
# there is no orders in the order history page, we need not want to delete all the orders to achieve.
# Instead, we will use fulfill method to create a fake response for the order history api call and then validate it.

from playwright.sync_api import Page, expect

fakeJSONResponse={"data":[], "message":"No orders"}

#This method is the event handler in the route method which is used to create a fake response when the api call happens.
def intercept_response(route):
    route.fulfill(
        json= fakeJSONResponse
    )

def test_InterceptAPIResponses(page: Page):
    #We will perform the same operations of logging into the page and clicking on orders button.
    # we will just add one step where it will listen to the API call when it gets triggered.
    page.goto("https://rahulshettyacademy.com/client")
    # route method 
    #Routing provides the capability to modify network requests that are made by a page.
    #Once routing is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or aborted.
    #this url will get triggered once we click on the orders button and 
    # hence we ask playwright to listen to this event using route method.
    #Here we are giving /* in the url because the user id is always dynamic and we are not user which user will be testing this test.
    #Users are different users of that webpage who has a valid account. Each account will have an account id which will be sent with the url.
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.locator("#userEmail").fill("shreebalajimsc@gmail.com")
    page.locator("#userPassword").fill("Dinku@2408")
    page.get_by_role("button",name="Login").click()

    page.get_by_role("button",name="ORDERS").click()

    #The below line is the place which has the no orders message when actually there are no orders for that particular user.
    order_page_message = page.locator(".mt-4").text_content()
    print(order_page_message)
    expect(page.locator(".mt-4")).to_contain_text("You have No Orders to show at this time")




