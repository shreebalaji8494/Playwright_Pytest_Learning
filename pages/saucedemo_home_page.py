from playwright.sync_api import Page

class SaucedemoHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_fleece_jacket_button = page.locator("#add-to-cart-sauce-labs-fleece-jacket")
        self.add_to_cart_bike_light_button = page.locator("#add-to-cart-sauce-labs-bike-light")
        self.add_to_cart_bolt_tshirt_button = page.locator("#add-to-cart-sauce-labs-bolt-t-shirt")
        self.shopping_cart_link = page.locator("[data-test='shopping-cart-badge']")
        self.shopping_page_title = page.get_by_label("Products")

    def get_title(self):
        return self.page.title()

    def add_to_cart_operation(self):
        self.add_to_cart_fleece_jacket_button.click()
        self.add_to_cart_bike_light_button.click()
        self.add_to_cart_bolt_tshirt_button.click()

    def go_to_shopping_cart(self):
        self.shopping_cart_link.click() 

    def validate_shopping_page_title(self):
        return self.shopping_page_title.is_visible()    

    def perform_adding_items_to_cart_and_click_shopping_cart(self):
        self.validate_shopping_page_title()
        self.add_to_cart_operation()
        self.go_to_shopping_cart()        