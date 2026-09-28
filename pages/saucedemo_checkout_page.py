from playwright.sync_api import Page


class SaucedemoCheckoutPage:
    """Page object for the checkout workflow on SauceDemo."""

    def __init__(self, page: Page):
        # Keep the page instance and locate the checkout form and action buttons.
        self.page = page
        self.checkout_button = page.locator("[data-test=\"checkout\"]")
        self.first_name_input = page.locator("[data-test=\"firstName\"]")
        self.last_name_input = page.locator("[data-test=\"lastName\"]")
        self.postal_code_input = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.finish_button = page.locator("[data-test=\"finish\"]")
        self.back_to_products_button = page.locator("[data-test=\"back-to-products\"]")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_sidebar_link = page.locator("[data-test=\"logout-sidebar-link\"]")

    def click_checkout(self):
        """Start the checkout process from the cart page."""
        self.checkout_button.click()

    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        """Enter the details needed to complete the buyer information form."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def click_continue(self):
        """Move from the customer information step to the review page."""
        self.continue_button.click()

    def click_finish(self):
        """Submit the order once the review step is reached."""
        self.finish_button.click()

    def click_back_to_products(self):
        """Return to the products page after a completed order."""
        self.back_to_products_button.click()

    def click_menu(self):
        """Open the burger menu in the header for navigation options."""
        self.menu_button.click()

    def click_logout(self):
        """Log out from the side menu after the purchase flow is complete."""
        self.logout_sidebar_link.click()

    def perform_checkout(self, first_name: str, last_name: str, postal_code: str):
        """Complete the standard checkout, order confirmation, and logout flow."""
        self.click_checkout()
        self.fill_checkout_information(first_name, last_name, postal_code)
        self.click_continue()
        self.click_finish()
        self.click_back_to_products()
        self.click_menu()
        self.click_logout()