import pytest
from pytest_bdd import given, when, then, scenarios, parsers

from pages.loginPage import LoginPage
from utils.apiBaseFrameworkLevel import APIUtils

# We are connecting the feature file with step definition file
scenarios("../features/orderTransaction.feature")
#We are creating this fixture since we have multiple variables that are passed in next methods and
# so we are trying to save those in this dictionary so we can retrieve it.
# We are returning empty dictionary so that we can add the values as per requirement to use it in different methods.similar to global variable concept.
@pytest.fixture
def shared_data():
    return {}

# we are using parsers to make the playwright understand that the variables are being used inside the step.Else it will consider as string
@given(parsers.parse("Place an order and fetch the orderId using {username} and {password}"))
def place_an_order_using_api(playwright,username,password,shared_data):
    user_credentials = {"user_email":username,"user_password":password}
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright,user_credentials)
    shared_data["order_id"] = order_id # we are storing the orderid to the dictionary to use it whenever needed.

@given("The user is on landing page")
def the_user_is_on_the_landing_page(browserInstance,shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigate_to_url(browserInstance)
    shared_data["login_page"] = loginPage #storing in the fixture dictionary

@when(parsers.parse("I login to the page using {username} and {password}"))
def login_to_the_landing_page(browserInstance,username,password,shared_data):
    loginPage = shared_data["login_page"] #retrieving from the fixture since fixtures are the first to get executed even before the code executes
    loginPage.navigate_to_url(browserInstance)
    dashboardPage = loginPage.login(username, password)
    shared_data["dashboardPage"] = dashboardPage

@when("Navigate to the orders page")
def navigate_to_orders_page(shared_data):
    dashboardPage = shared_data["dashboardPage"]
    orderHistoryPage = dashboardPage.selectOrdersNavigationLink()
    shared_data["orderHistoryPage"] = orderHistoryPage

@when("Select the fetched orderId")
def select_the_selected_order(shared_data):
    orderHistoryPage=shared_data["orderHistoryPage"]
    order_id = shared_data["order_id"]
    orderDetailsPage = orderHistoryPage.selectOrder(order_id)
    shared_data["orderDetailsPage"] = orderDetailsPage

@then("Order message is successfully verified")
def verify_order_message(shared_data):
    orderDetailsPage = shared_data["orderDetailsPage"]
    orderDetailsPage.verifyOrder()