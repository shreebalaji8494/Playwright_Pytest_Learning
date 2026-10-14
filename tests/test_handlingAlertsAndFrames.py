from playwright.sync_api import Page, expect

def test_handling_alerts(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # Handling Mouse Hover in Playwright
    # We are using hover() method to perform mouse hover action on the "Mouse Hover" button.
    page.get_by_role("button", name="Mouse Hover").hover() # This will perform mouse hover action on the "Mouse Hover" button and display the hidden options.
    #click on the "Top" option which is visible after mouse hover action.
    page.get_by_role("link", name="Top").click() # This will click on the "Top" option which is visible after mouse hover action.
    # Handling alert popups in Playwright
    # We are using on() method to listen for the "dialog" event, which is triggered when an alert popup appears on the page.
    # The on() method takes two arguments: the event name and a callback function that will be called when the event is triggered. The callback function takes a single argument, which is the dialog object representing the alert popup.
    # We are using lambda function just to accept the alert popup when it appears. The dialog object has an accept() method that we can call to accept the alert popup.
    page.on("dialog", lambda dialog: dialog.accept()) # This will accept the alert popup
    # We are clicking the confirm button which will trigger the alert. 
    # We are doing it after the on() method so that we can listen for the dialog event and accept the alert popup when it appears.
    page.get_by_role("button", name="Confirm").click() 

    # Handling frames in Playwright
    pageFrame=page.frame_locator("#courses-iframe") # We are using frame_locator() method to locate the iframe on the page. 
    # The frame_locator() method returns a FrameLocator object that represents the iframe on the page. We are passing the CSS selector of the iframe as an argument to the frame_locator() method.
    # We are using the FrameLocator object to locate elements inside the iframe. The FrameLocator object has the same methods as the Page object, so we can use the same methods to locate elements inside the iframe. 
    # We are using get_by_role() method to locate the "All Access Plan" link inside the iframe and verify its presence.
    expect(pageFrame.get_by_role("link", name="All Access Plan")).to_be_visible() # We are using the expect() method to verify that the "All Access Plan" link is visible on the page.
    pageFrame.get_by_role("link", name="All Access Plan").click()
    # We are using the expect() method to verify that the "Happy Subscribers" text is present on the page.
    # We used loactor() method to locate the body tag of the iframe and then used to_contain_text() method to verify that the text "Happy Subscribers" is present in the body tag of the iframe.
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")     