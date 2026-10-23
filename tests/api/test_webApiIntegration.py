#In this Test we are going to generate an order using api and then verify the order id in orders page 
#using web automation.
import json
from playwright.sync_api import Playwright, expect
import pytest
from pages.loginPage import LoginPage
from utils.apiBase import APIUtils

#fetching the credentials from external data file for login
with open("test_data/credentials.json") as f:
    data= json.load(f)
    user_credentials_list = data['user_credentials']

#We are using pytest parameterize fixture to get the list of user credentials
@pytest.mark.parametrize('user_credentials',user_credentials_list) 
def test_e2e_webApiIntegration(playwright:Playwright, user_credentials): 
    userName = user_credentials['user_email']
    userPassword = user_credentials['user_password']
    #Step 1:create order using api
    #for achieving this step we need to call the api methods which we have written in the utils package.
    # we will do it by creating a class object for that class and then call the method.
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright,user_credentials)

    #Step 2: Login to the web page using credentials
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    loginPage = LoginPage(page)
    loginPage.navigate_to_url(page)
    dashboardPage=loginPage.login(userName,userPassword)
    
    #Step 3 : Go to orders page and then click view button in the particular order and then assert the message
    orderHistoryPage = dashboardPage.selectOrdersNavigationLink()
    #finding the view button of our order id
    orderDetailsPage = orderHistoryPage.selectOrder(order_id)
    
    #Assert the thank you text
    orderDetailsPage.verifyOrder()

    #Closing the context
    context.close()

