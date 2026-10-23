from pages.dashboardPage import DashboardPage


class LoginPage:
    def __init__(self,page):
        self.page = page


    def navigate_to_url(self,page):
        self.page.goto("https://rahulshettyacademy.com/client")   

    def login(self,userName,userPassword):
        self.page.locator("#userEmail").fill(userName)
        self.page.locator("#userPassword").fill(userPassword)
        self.page.get_by_role("button",name="Login").click()
        # As soon we click login button we know that we will be navigated to dashboard page. 
        # so we can create its class object here itself and return it 
        # so that we dont have to create class objects for each class in our test method.
        dashboardPage = DashboardPage(self.page)
        return dashboardPage

