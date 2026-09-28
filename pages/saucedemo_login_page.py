from playwright.sync_api import Page
import pytest


class SaucedemoLoginPage:
    """Page object for the SauceDemo login screen."""

    def __init__(self, page: Page):
        # Keep the browser page instance and define the login form elements.
        self.page = page
        self.username_input = page.locator("[data-test=\"username\"]")
        self.password_input = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")

    def login(self, username: str, password: str):
        """Sign in using the provided username and password."""
        # Fill the credentials and submit the form to access the application.
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()