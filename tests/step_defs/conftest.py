import pytest
from pytest_bdd import given, then, when, parsers

from driver.appium_driver import AppiumDriver
from conf.conf import logger_test
from data.data_gen import DataGenerator
from activities.phone_number_input_activity import PhoneNumberInputActivity
from activities.otp_input_activity import OTPInputActivity
from custom_excepitons.appium_exceptions import AppiumConnectionFailException
from custom_excepitons.choco_app_exception import ButtonTextMismatchException


@pytest.fixture(scope='session')
def appium_driver():
    appium_driver = AppiumDriver()

    yield appium_driver
    logger_test.info('Quiting Appium server connection')
    appium_driver.quit()


@given("the choco app is opened in a mobile", target_fixture="open_app")
def open_app(appium_driver):
    try:
        logger_test.info('Connecting to appium server and opening the app')
        appium_driver.connect()
    except AppiumConnectionFailException as e:
        logger_test.critical(e)


@then('close the choco app', target_fixture='close_app')
def close_app(appium_driver):
    try:
        logger_test.info('Closing the app')
        appium_driver.close_app()
    except Exception as e:
        logger_test.critical(e)
        raise


@when("I tap on country code", target_fixture="tap_on_country_code")
@when("tap on country code", target_fixture="tap_on_country_code")
def tap_on_country_code(appium_driver):
    logger_test.info('Tapping on country code')
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())
    phone_number_input_activity.tap(phone_number_input_activity.country_code_select)


@when("enter valid country code in search field to filter", target_fixture="enter_text_to_filter_countries")
def enter_text_to_filter_countries(appium_driver):
    country_calling_code = DataGenerator().get_valid_country_calling_code()[1:]
    logger_test.info(f'Entering valid country code {country_calling_code} to filter')
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())
    phone_number_input_activity.enter_text(phone_number_input_activity.country_code_filter_input, country_calling_code)


@when('tap on valid country from the filtered search result',
      target_fixture="tap_on_country_from_filter_result")
def tap_on_country_from_filter_result(appium_driver):
    country = DataGenerator().get_valid_country()
    logger_test.info(f'Entering valid country {country} to filter')
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())
    phone_number_input_activity.tap_on_filtered_result_on_basis_of_country(country=country)


@when("enter valid phone number", target_fixture="enter_phone_number")
@when("I enter valid phone number", target_fixture="enter_phone_number")
def enter_phone_number(appium_driver):
    phone_number = DataGenerator().get_valid_phone_number()
    logger_test.info(f'Entering valid phone number {phone_number}')
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())
    phone_number_input_activity.enter_text(phone_number_input_activity.phone_number_input, phone_number)


@when(parsers.parse('tap on "{button_text}" button'),
      target_fixture="tap_on_button_in_phone_number_input_activity")
def tap_on_button_in_phone_number_input_activity(appium_driver, button_text):
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())
    text = phone_number_input_activity.get_text(phone_number_input_activity.button)

    if text == button_text:
        phone_number_input_activity.tap(phone_number_input_activity.button)
    else:
        logger_test.critical(f"Button text mismatch. Expected {button_text} but found {text}")
        raise ButtonTextMismatchException(f"Button text mismatch. Expected {button_text} but found {text}")

    logger_test.info(f"Checking if current activity is OTP Input Activity")
    otp_input_activity = OTPInputActivity(appium_driver.connect())
    otp_input_activity.find_elements(otp_input_activity.otp_input)
