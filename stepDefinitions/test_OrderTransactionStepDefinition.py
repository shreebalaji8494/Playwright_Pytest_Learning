from pytest_bdd import given,when,then,And

from utils.apiBaseFrameworkLevel import APIUtils

@given("Place an order and fetch the orderId using {username} and {password}")
def place_an_order_using_API(playwright,username,password):
    user_credentials = {"user_email":username,"user_password":password}
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright,user_credentials)