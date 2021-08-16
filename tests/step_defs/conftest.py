import pytest
from pytest_bdd import given, then, when, parsers

from driver.appium_driver import AppiumDriver
from conf.conf import logger_test
from data.data_gen import DataGenerator
from activities.phone_number_input_activity import PhoneNumberInputActivity
from activities.otp_input_activity import OTPInputActivity


@pytest.fixture(scope='session')
def appium_driver():
    appium_driver = AppiumDriver()
    yield appium_driver
    try:
        appium_driver.quit()
    except Exception as e:
        logger_test.critical(e)
        raise


@given("the choco app is opened in a mobile", target_fixture="open_app")
def open_app(appium_driver):
    try:
        appium_driver.connect()
    except Exception as e:
        logger_test.critical(e)
        raise


@then('close the choco app', target_fixture='close_app')
def close_app(appium_driver):
    try:
        appium_driver.close_app()
    except Exception as e:
        logger_test.critical(e)
        raise


@when("I tap on country code", target_fixture="tap_on_country_code")
@when("tap on country code", target_fixture="tap_on_country_code")
def tap_on_country_code(appium_driver):
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())
    phone_number_input_activity.tap(phone_number_input_activity.country_code_select)


@when("enter valid country code in search field to filter", target_fixture="enter_text_to_filter_countries")
def enter_text_to_filter_countries(appium_driver):
    country_calling_code = DataGenerator().get_valid_country_calling_code()[1:]
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())
    phone_number_input_activity.enter_text(phone_number_input_activity.country_code_filter_input, country_calling_code)


@when('tap on valid country from the filtered search result',
      target_fixture="tap_on_country_from_filter_result")
def tap_on_country_from_filter_result(appium_driver):
    country = DataGenerator().get_valid_country()
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())
    phone_number_input_activity.tap_on_filtered_result_on_basis_of_country(country=country)


@when("enter valid phone number", target_fixture="enter_phone_number")
@when("I enter valid phone number", target_fixture="enter_phone_number")
def enter_phone_number(appium_driver):
    phone_number = DataGenerator().get_valid_phone_number()
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
        #TODO raise customer exception
        pytest.fail()

    otp_input_activity = OTPInputActivity(appium_driver.connect())
    otp_input_activity.find_elements(otp_input_activity.otp_input)






