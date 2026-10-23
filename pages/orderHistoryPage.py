from pages.orderDetailsPage import OrderDetailsPage


class OrderHistoryPage:
    def __init__(self,page):
        self.page = page

    def selectOrder(self,orderID):
        row = self.page.locator("tr").filter(has_text=orderID)
        #now clicking view button of that particular entry 
        row.get_by_role("button",name="View").click()
        orderDetailsPage = OrderDetailsPage(self.page)
        return orderDetailsPage
