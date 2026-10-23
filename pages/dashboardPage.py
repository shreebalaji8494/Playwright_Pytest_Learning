from pages.orderHistoryPage import OrderHistoryPage


class DashboardPage:
    def __init__(self,page):
        self.page = page

    def selectOrdersNavigationLink(self):
        self.page.get_by_role("button",name="ORDERS").click()
        #We will be navigated to orders history page as soon as we click orders button
        orderHistoryPage = OrderHistoryPage(self.page)
        return orderHistoryPage
            