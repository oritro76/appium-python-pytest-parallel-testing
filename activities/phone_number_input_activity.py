from appium.webdriver.common.mobileby import MobileBy

from activities.app import App


class PhoneNumberInputActivity(App):
    """
    phone number input activity locators
    """
    title = (MobileBy.ID, 'app.choco.dummyqa:id/title')
    description = (MobileBy.ID, 'app.choco.dummyqa:id/description')
    country_code_select = (MobileBy.ID, 'app.choco.dummyqa:id/countryCode')
    phone_number_input = (MobileBy.ID, 'app.choco.dummyqa:id/phone')
    country_code_filter_input = (MobileBy.ID, 'app.choco.dummyqa:id/filterEditText')
    country_code_title = (MobileBy.ID, 'app.choco.dummyqa:id/title')
    button = (MobileBy.ID, 'app.choco.dummyqa:id/button')
    error_indicator = (MobileBy.ID, 'app.choco.dummyqa:id/errorIndicator')
    country_code_title_text_view = (MobileBy.CLASS_NAME, 'android.widget.TextView')

    title_text = 'What’s your cell phone number?'
    description_text = 'We need this to create your account or help you log you back in.'
    default_country_code = '+1'
    button_text = 'Continue'
    error_text = 'That phone number isn’t valid, are you sure you entered it correctly?'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def tap_on_filtered_result_on_basis_of_country(self, country):
        filtered_results = self.find_elements(self.country_code_title_text_view)
        limit = len(filtered_results)

        for temp in range(limit):
            if country.lower() == filtered_results[temp].text.lower():
                filtered_results[temp].click()
                return

