import pytest
from loguru import logger
from assertpy import assert_that
from pytest_bdd import given, when, then, parsers
from selenium.common.exceptions import (
    NoSuchElementException,
)

from activities.phone_number_input_activity import PhoneNumberInputActivity
from activities.otp_input_activity import OTPInputActivity
from activities.onboard_success_activity import OnboardSuccessActivity
from data.data_gen import DataGenerator



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


@given("the choco app is opened in a mobile", target_fixture="open_app")
def open_app(appium_driver):
    try:
        logger.info('Checking app state')
        state = appium_driver.get_app_state()
        if state == 0:
            logger.info('App is not in installed. installing it')
            appium_driver.install_app()
        elif state == 1 or state == 2 or state ==3:
            logger.info('Launching App')
            appium_driver.launch_app()

    except Exception as e:
        logger.critical(e)
        raise


@then('close the choco app', target_fixture='close_app')
def close_app(appium_driver):
    try:
        logger.info('Closing the app')
        appium_driver.close_app()
    except Exception as e:
        logger.critical(e)
        raise


@given("I am on OTPInputActivity", target_fixture="go_to_OTPInputActivity")
def go_to_OTPInputActivity(helper_tap_on_country_code,
                           helper_enter_text_to_filter_countries,
                           helper_tap_on_country_from_filter_result,
                           helper_enter_phone_number,
                           helper_tap_on_button_in_phone_number_input_activity,
                           context):
    helper_tap_on_country_code()

    context['country_code'] = DataGenerator().get_valid_country_calling_code()
    country_calling_code = DataGenerator().get_valid_country_calling_code()[1:]
    helper_enter_text_to_filter_countries(country_calling_code)

    country = DataGenerator().get_valid_country()
    helper_tap_on_country_from_filter_result(country)

    context['phone_number'] = phone_number = DataGenerator().get_valid_phone_number()
    helper_enter_phone_number(phone_number)

    helper_tap_on_button_in_phone_number_input_activity(PhoneNumberInputActivity.button_text)


@when("I tap on country code", target_fixture="tap_on_country_code")
@when("tap on country code", target_fixture="tap_on_country_code")
def tap_on_country_code(helper_tap_on_country_code):
    helper_tap_on_country_code()


@when("enter valid phone number", target_fixture="enter_phone_number")
@when("I enter valid phone number", target_fixture="enter_phone_number")
def enter_phone_number(helper_enter_phone_number, context):
    context['phone_number'] = DataGenerator().get_valid_phone_number()
    phone_number = DataGenerator().get_valid_phone_number()
    helper_enter_phone_number(phone_number)


@then(parsers.parse('enter valid OTP'), target_fixture="enter_otp")
@when(parsers.parse('enter valid OTP'), target_fixture="enter_otp")
def enter_otp(appium_driver, helper_enter_otp):
    otp = DataGenerator().get_valid_otp()

    helper_enter_otp(otp)

    logger.info(f"Checking if current activity is Onboard Success Activity")
    try:
        onboard_success_activity = OnboardSuccessActivity()

        appium_driver.find_element(onboard_success_activity.title)
    except NoSuchElementException as e:
        message = f"Expected activity to be {onboard_success_activity} but found {OTPInputActivity()}"
        logger.critical(message)
        raise AssertionError(f"message")


@when('tap on valid country from the filtered search result',
      target_fixture="tap_on_country_from_filter_result")
def tap_on_country_from_filter_result(helper_tap_on_country_from_filter_result):
    country = DataGenerator().get_valid_country()
    helper_tap_on_country_from_filter_result(country)


@when(parsers.parse('tap on "{button_text}" button'),
      target_fixture="tap_on_button_in_phone_number_input_activity")
def tap_on_button_in_phone_number_input_activity(helper_tap_on_button_in_phone_number_input_activity,
                                                 button_text):
    helper_tap_on_button_in_phone_number_input_activity(button_text)


@then(parsers.parse('see the message "{message}"'),
      target_fixture="check_correct_message_is_shown_in_onboard_success_activity")
def check_correct_message_is_shown_in_onboard_success_activity(appium_driver, message):
    onboard_success_activity = OnboardSuccessActivity()

    element_text = appium_driver.get_text(onboard_success_activity.title)
    logger.info(f"Checking if correct message {message} and  {message} are same")

    try:
        assert_that(element_text).is_equal_to(message)
    except AssertionError as e:
        logger.critical(e)
        raise


@when("enter valid country code in search field to filter", target_fixture="enter_text_to_filter_countries")
def enter_text_to_filter_countries(context, helper_enter_text_to_filter_countries):
    context['country_code'] = DataGenerator().get_valid_country_calling_code()
    country_calling_code = DataGenerator().get_valid_country_calling_code()[1:]
    helper_enter_text_to_filter_countries(country_calling_code)


@when(parsers.parse('enter <text> in search field to filter'),
      target_fixture='enter_text_to_filter_countries')
def enter_text_to_filter_countries(text, helper_enter_text_to_filter_countries):
    helper_enter_text_to_filter_countries(text)


@when(parsers.parse('tap on <country> from the filtered search result'),
      target_fixture="tap_on_country_from_filter_result")
def tap_on_country_from_filter_result(country, helper_tap_on_country_from_filter_result):
    helper_tap_on_country_from_filter_result(country)
