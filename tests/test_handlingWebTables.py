from playwright.sync_api import Page as page, expect

def test_handling_webTables(page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    # Handling web tables in Playwright
    # our aim here is to assert the price of the "Rice" product in the web table. 
    # We are using the locator() method to locate the web table on the page. 
    # The locator() method returns a Locator object that represents the web table on the page. 
    # We are passing the CSS selector of the web table as an argument to the locator() method.
    # Since the web table has multiple rows and columns, we are using the nth() method to locate the specific row and column that contains the "Rice" product.
    # The nth() method takes an index as an argument and returns a Locator object that represents the specific row or column at that index.
    # We are using for loop to iterate through the column headers to find the price column and from that we will get the price of rice 
    for i in range(page.locator("th").count()):
        #We are using if loop to check if the text content of column header is price and if it is then we will get the index of that column header and break the loop.
        if page.locator("th").nth(i).text_content() == "Price": 
            priceColumnIndex = i
            break

    # Now we will find the row index of the "Rice" product
    riceRow = page.locator("tr").filter(has_text="Rice")

    # Now we will get the price of the "Rice" product using the row index and column index
    ricePrice = riceRow.locator("td").nth(priceColumnIndex).text_content()

    #Asserting the price of the "Rice" product to be 37
    expect(riceRow.locator("td").nth(priceColumnIndex)).to_have_text("37")
    
