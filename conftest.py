#This file is a global file where we can place any global configuration for the tests. 
#For example, we can set up fixtures, hooks, or any other configurations that should 
#be applied to all tests in the suite.

import pytest
#pytest_addoption is a pytest hook that registers a custom command-line option before the tests run
#this method is like the registration of the terminal option we are providing and making the playwright to do as per our commands lie choosing browser etc.
#Without pytest_addoption, pytest wouldn’t recognize --browser_name as a valid command-line option. One detail: your "chrome" branch launches Playwright’s Chromium browser; it doesn’t necessarily launch the branded Google Chrome browser.
def pytest_addoption(parser):
    #means you can pass --browser_name when starting pytest. action="store" saves the value you provide, and default="chrome" uses "chrome" if you leave the option out.
    # The browserInstance fixture then reads that saved value with request.config.getoption("browser_name") and chooses which Playwright browser to launch.
    parser.addoption("--browser_name", action="store",default = "chrome", help="Browser selection")

@pytest.fixture(scope='session')
def user_credentials(request):
    return request.param

# If we wanted to run tests based on which browser option we give in the terminal,
# We need to configure it to fetch from terminal.
@pytest.fixture
def browserInstance(playwright,request):
    browser_name= request.config.getoption("browser_name") # here browser_name is the config name we provide in the terminal while running a test
    if browser_name=="chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name=="firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()