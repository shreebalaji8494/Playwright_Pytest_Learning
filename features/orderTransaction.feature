Feature: Order Transaction
    Tests related to Order Transactions

    Scenario Outline: Verify Order success message shown in details page
        Given Place an order and fetch the orderId using <username> and <password>
        And The user is on landing page
        When I login to the page using <username> and <password>
        And Navigate to the orders page
        And Select the fetched orderId
        Then Order message is successfully verified

        Examples:
        |username                |password  |
        |shreebalajimsc@gmail.com|Dinku@2408|
        |sahamonu11@gmail.com    |Dinku@2408|

