import pytest
from loguru import logger
from assertpy import assert_that

from activities.phone_number_input_activity import PhoneNumberInputActivity
from activities.otp_input_activity import OTPInputActivity


@pytest.fixture(scope='function')
def context():
    return {}


@pytest.fixture(scope="function")
def helper_tap_on_country_code(appium_driver):
    def _helper_tap_on_country_code():
        logger.info('Tapping on country code')
        phone_number_input_activity = PhoneNumberInputActivity()
        appium_driver.tap(phone_number_input_activity.country_code_select)

    return _helper_tap_on_country_code


@pytest.fixture(scope='function')
def helper_enter_text_to_filter_countries(appium_driver):
    def _helper_enter_text_to_filter_countries(text):
        logger.info(f'Entering {text} to filter')
        phone_number_input_activity = PhoneNumberInputActivity()
        appium_driver.enter_text(phone_number_input_activity.country_code_filter_input,
                                               text)
    return _helper_enter_text_to_filter_countries


@pytest.fixture(scope='function')
def helper_tap_on_country_from_filter_result(appium_driver):
    def _helper_tap_on_country_from_filter_result(country):
        logger.info(f'Tapping on {country} to select as country code')
        phone_number_input_activity = PhoneNumberInputActivity()
        appium_driver.tap_on_filtered_result_on_basis_of_country(phone_number_input_activity.country_code_title_text_view,
                                                                 country=country)

    return _helper_tap_on_country_from_filter_result


@pytest.fixture(scope='function')
def helper_change_mobile_orientation(appium_driver):
    def _helper_change_mobile_orientation(orientation):

        logger.info(f"Changing mobile orientation to {orientation}")
        appium_driver.change_device_orientation(orientation)
    return _helper_change_mobile_orientation


@pytest.fixture(scope='function')
def helper_enter_phone_number(appium_driver):

    def _helper_enter_phone_number(phone_number):
        logger.info(f'Entering phone number {phone_number}')
        phone_number_input_activity = PhoneNumberInputActivity()
        appium_driver.enter_text(phone_number_input_activity.phone_number_input,
                                               phone_number)
    return _helper_enter_phone_number


@pytest.fixture(scope='function')
def helper_tap_on_button_in_phone_number_input_activity(appium_driver):
    def _helper_tap_on_button_in_phone_number_input_activity(button_text):
        phone_number_input_activity = PhoneNumberInputActivity()
        text = appium_driver.get_text(phone_number_input_activity.button)

        logger.info(f"Tapping on {button_text} button")

        appium_driver.tap(phone_number_input_activity.button)

        try:
            assert_that(button_text).is_equal_to(text)
        except AssertionError as e:
            logger.critical(e)
            raise

        logger.info(f"Checking if current activity is OTP Input Activity")
        otp_input_activity = OTPInputActivity()
        appium_driver.find_elements(otp_input_activity.otp_input)
    return _helper_tap_on_button_in_phone_number_input_activity


@pytest.fixture(scope='function')
def helper_enter_otp(appium_driver):
    def _helper_enter_otp(otp):
        otp_input_activity = OTPInputActivity()
        logger.info(f"Entering otp {otp}")
        appium_driver.enter_otp(otp_input_activity.otp_input, otp=otp)
    return _helper_enter_otp