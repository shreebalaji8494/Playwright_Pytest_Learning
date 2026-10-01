from playwright.sync_api import Page


class DemoQAPracticePage:

    def __init__(self, page: Page):
        # Keep the browser page instance and define the locators for the practice page elements.
        self.page = page
        self.first_name_input = page.locator("#firstName")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.email_input = page.locator("#userEmail")
        self.male_gender_radio_button = page.locator("input[name='gender'][value='Male']")
        self.female_gender_radio_button = page.locator("input[name='gender'][id='gender-radio-2']")
        self.other_gender_radio_button = page.locator("input[name='gender'][value='Other']")
        self.mobile_number_input = page.locator("#userNumber")
        self.date_of_birth_input = page.locator("input[type='text'][id='dateOfBirthInput']")
        self.subjects_input = page.locator("#subjectsInput")
        self.sports_hobbies_checkbox = page.locator("#hobbies-checkbox-1")
        self.reading_hobbies_checkbox = page.locator("#hobbies-checkbox-2")
        self.music_hobbies_checkbox = page.locator("#hobbies-checkbox-3")
        self.upload_picture_button = page.locator("#uploadPicture")
        self.current_address_textarea = page.locator("#currentAddress")
        self.state_dropdown = page.locator("#state")
        self.city_dropdown = page.locator("#city")
        self.submit_button = page.locator("#submit")

    def fill_name_email_mobileNumber(self,first_name:str,last_name:str,email:str,mobile_number:str):
        """Fill in the first name, last name, email, and mobile number fields."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.email_input.fill(email)
        self.mobile_number_input.fill(mobile_number)    

    def fill_date_of_birth(self, date_of_birth: str):
            """Fill in the date of birth field."""
            self.date_of_birth_input.fill(date_of_birth)      

    def select_gender(self, gender: str):
        """Select the gender radio button based on the provided gender string."""
        if gender.lower() == "male":
            self.male_gender_radio_button.check()
        elif gender.lower() == "female":
            self.female_gender_radio_button.check()
        elif gender.lower() == "other":
            self.other_gender_radio_button.check()
        else:
            raise ValueError("Invalid gender. Please choose 'Male', 'Female', or 'Other'.")    

    def select_hobbies(self, hobbies: list):
        """Select the hobbies checkboxes based on the provided list of hobbies."""
        assert isinstance(hobbies, list), "Hobbies should be provided as a list."
        assert self.sports_hobbies_checkbox.is_enabled(), "Sports checkbox is not enabled."
        assert self.reading_hobbies_checkbox.is_enabled(), "Reading checkbox is not enabled."
        assert self.music_hobbies_checkbox.is_enabled(), "Music checkbox is not enabled."
        
        for hobby in hobbies:
            if hobby.lower() == "sports":
                self.sports_hobbies_checkbox.check()
            elif hobby.lower() == "reading":
                self.reading_hobbies_checkbox.check()
            elif hobby.lower() == "music":
                self.music_hobbies_checkbox.check()
            else:
                raise ValueError("Invalid hobby. Please choose 'Sports', 'Reading', or 'Music'.")    

    def fill_current_address(self, address: str):
        """Fill in the current address textarea."""
        self.current_address_textarea.fill(address)

    def select_state_city(self, state: str, city: str):
        """Select the state and city from the dropdowns."""
        assert self.state_dropdown.is_enabled(), "State dropdown is not enabled."
        assert self.city_dropdown.is_enabled(), "City dropdown is not enabled."
        self.state_dropdown.click()
        self.page.get_by_role("option", name=state, exact=True).click()
        self.city_dropdown.click()
        self.page.get_by_role("option", name=city, exact=True).click()

    def submit_form(self):
        """Click the submit button to submit the form."""
        assert self.submit_button.is_visible(), "Submit button is not enabled."
        self.submit_button.click()

    def fill_details_and_submit(self, first_name: str, last_name: str, email: str, mobile_number: str, date_of_birth: str, gender: str, hobbies: list, address: str, state: str, city: str):
        """Fill in all the required details and submit the form."""
        self.fill_name_email_mobileNumber(first_name, last_name, email, mobile_number)
        self.fill_date_of_birth(date_of_birth)
        self.select_gender(gender)
        self.select_hobbies(hobbies)
        self.fill_current_address(address)
        self.select_state_city(state, city)
        self.submit_form()    

             
