from playwright.sync_api import expect,sync_playwright
import pytest
def test_handling_elements(page):
    page.goto("https://shop.qaautomationlabs.com/index.php")
    page.fill("[id='email']","demo@demo.com")
    expect(page.locator("#email")).to_have_value("demo@demo.com")
    page.get_by_placeholder("Password").fill("demo")
    expect(page.locator("#rememberMe")).to_be_visible()
    page.get_by_role("checkbox", name="Remember Me").check()
    expect(page.locator("#rememberMe")).to_be_checked()
    page.screenshot(path="login_page.png")
    page.click("#loginBtn")
    page.screenshot(path="after_login.png")
    page.wait_for_load_state("domcontentloaded")
    page.get_by_label("Shop Men Fashion").click()
    page.screenshot(path="mens_wear_page.png")
    page.wait_for_load_state("domcontentloaded")
    page.locator('label[for="gender-1"]').check()
    expect(page.locator('label[for="gender-1"]')).to_be_checked()
    page.locator('label[for="gender-2"]').check()
    expect(page.locator('label[for="gender-2"]')).to_be_checked()
    page.screenshot(path="after_selecting_gender.png")
    page.get_by_label("Add Black Sport Shoes to cart").click()
    page.screenshot(path="after_adding_shoes_to_cart.png")


