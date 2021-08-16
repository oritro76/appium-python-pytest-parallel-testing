import pytest
from pytest_bdd import when, then, scenarios, parsers, given, feature
from assertpy import assert_that

from loguru import logger
from data.data_gen import DataGenerator
from activities.phone_number_input_activity import PhoneNumberInputActivity
from activities.otp_input_activity import OTPInputActivity
from activities.onboard_success_activity import OnboardSuccessActivity

scenarios('../features/wrong_country_code_or_wrong_phone_number_input.feature')



@when('enter <text> in search field to filter',
      target_fixture="enter_text_to_filter_countries")
def enter_text_to_filter_countries(appium_driver, text):
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())

    logger.info(f"Entering text {text} for filtering country")

    phone_number_input_activity.enter_text(phone_number_input_activity.country_code_filter_input,
                                           text)


@when(parsers.parse("enter valid/invalid phone_number <phone_number>"),
      target_fixture="enter_phone_number")
def enter_valid_or_invalid_phone_number(appium_driver, phone_number):
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())

    logger.info(f"Entering phone number {phone_number}")

    phone_number_input_activity.enter_text(phone_number_input_activity.phone_number_input,
                                           phone_number)


@when('tap on valid/invalid <country> from the filtered search result',
      target_fixture="tap_on_valid_or_invalid_country_from_filter_result")
def tap_on_valid_or_invalid_country_from_filter_result(appium_driver, country):
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())

    logger.info(f"Tapping on country {country}")

    phone_number_input_activity.tap_on_filtered_result_on_basis_of_country(country=country)


@then(parsers.parse('error message <err_text> is shown for wrong phone number or wrong country calling code'),
      target_fixture='check_correct_error_message_is_shown_for_wrong_country_code_wrong_phone_number')
def check_correct_error_message_is_shown_for_wrong_country_code_wrong_phone_number(appium_driver,
                                                                                   err_text):
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())

    logger.info(f"Asserting for correct error message {err_text} after entering wrong phone number ")
    error_text = phone_number_input_activity.get_text(phone_number_input_activity.error_indicator)

    assert_that(error_text).contains(err_text)
