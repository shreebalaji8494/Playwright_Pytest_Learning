from playwright.sync_api import Playwright

#Our aim here is to hit login api, create an order using create_order api and fetch the order id from response and 
#use that order id to verify it in the order details page using the playwrights web automation. 
# We will be using playwrights request context to hit the api and get the response.
login_payload = {"userEmail": "shreebalajimsc@gmail.com", "userPassword": "Dinku@2408"}
create_order_payload = {"orders":[{"country":"India","productOrderedId":"6960ea76c941646b7a8b3dd5"}]}
class APIUtils:
    #getToken method will hit the login api and return the token from the response.
    def getToken(self, playwright:Playwright):
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_context.post("api/ecom/auth/login", data=login_payload)
        #The return statement will return the token as the response of the 
        # method will be in JSON format which in python is a dictionary. 
        # So we will retrieve the token from the dictionary using the key "token" and return it.
        print(response.json())
        return response.json()["token"]

    def createOrder(self, playwright:Playwright):
        #createOrder method will hit the create_order api and return the response.
        #For creating an order we need to pass the token in the header of the request, 
        # which we will get from the getToken method.
        token = self.getToken(playwright)
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_context.post("api/ecom/order/create-order", data=create_order_payload,
                                     headers={"Authorization":token,
                                              "Content-Type":"application/json"})

        print(response.json())
        order_id=response.json()["orders"][0]
        return order_id