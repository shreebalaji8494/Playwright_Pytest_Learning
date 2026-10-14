from playwright.sync_api import Page,expect
def test_childWindow(page : Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    #Click on the "Free Access to InterviewQues/ResumeAssistance/Material" link which opens a new child window.
    #After clicking on the link it opens a new child window. Now we have to switch to that child window to perform any actions on it. 
    # We can use the expect() method to wait for the new page to open and then use the page.context.pages property to get a list of all the pages in the current context. 
    # The last page in the list will be the newly opened child window.
    # We are using the expect_popup() method to wait for the new page to open. 
    # The expect_popup() method returns a context manager that we can use to wait for the new page to open.
    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").filter(has_text="Free Access to InterviewQues/ResumeAssistance/Material").click()
        childWindow = new_page_info.value
        #Now we can perform any actions on the new page. For example, we can get the text of the h1 element on the new page and print it to the console.
        childWindowText = childWindow.locator(".red").text_content()
        print(childWindowText)
        # We are splitting the text content and fetching the email address present in the text.
        words = childWindowText.split("at") # this will split with "at".
        email = words[1].strip().split(" ")[0] # this will split the space having the email id alone in the list.
        print(email)
        assert email == "mentor@rahulshettyacademy.com"
        


