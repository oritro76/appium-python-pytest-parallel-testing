from pytest_bdd import when, then, scenarios, parsers, given
from assertpy import assert_that
from loguru import logger

from activities.phone_number_input_activity import PhoneNumberInputActivity
from activities.otp_input_activity import OTPInputActivity
from data.data_gen import DataGenerator

scenarios('../features/onboard_to_choco_app.feature',)


@given(parsers.parse('mobile is in "{orientation}" orientation'),
       target_fixture="given_change_mobile_orientation")
def given_change_mobile_orientation(helper_change_mobile_orientation, orientation):
    helper_change_mobile_orientation(orientation)


@then(parsers.parse('change mobile to "{orientation}" orientation'),
      target_fixture="change_mobile_orientation")
def given_change_mobile_orientation(helper_change_mobile_orientation, orientation):
    helper_change_mobile_orientation(orientation)


@when(parsers.parse('enter <text> in search field to filter'),
      target_fixture='enter_text_to_filter_countries')
def enter_text_to_filter_countries(text, helper_enter_text_to_filter_countries):
    helper_enter_text_to_filter_countries(text)


@when(parsers.parse('tap on <country> from the filtered search result'),
      target_fixture="tap_on_country_from_filter_result")
def tap_on_country_from_filter_result(country, helper_tap_on_country_from_filter_result):
    helper_tap_on_country_from_filter_result(country)


@when("I tap on back button in otp input activity",
      target_fixture='tap_on_back_button_otp_input_activity')
def tap_on_back_button_otp_input_activity(appium_driver):
    otp_input_activity = OTPInputActivity(appium_driver.connect())

    logger.info(f"Tapping on OTP Input Activity back button")
    otp_input_activity.tap(otp_input_activity.back_button)


@then('am taken to phone number input activity',
      target_fixture="check_currenct_activity_is_phone_number_input_activity")
def check_current_activity_is_phone_number_input_activity(appium_driver):
    logger.info(f"Checking if current activity is Phone Number Input Activity")
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())
    phone_number_input_activity.find_element(phone_number_input_activity.phone_number_input)


@when('enter <text> in search field to filter',
      target_fixture="enter_text_to_filter_countries")
def enter_text_to_filter_countries(helper_enter_text_to_filter_countries, text):
    helper_enter_text_to_filter_countries(text)


@when(parsers.parse("enter valid/invalid phone_number <phone_number>"),
      target_fixture="enter_phone_number")
def enter_valid_or_invalid_phone_number(helper_enter_phone_number, phone_number):
    helper_enter_phone_number(phone_number)


@when('tap on valid/invalid <country> from the filtered search result',
      target_fixture="tap_on_valid_or_invalid_country_from_filter_result")
def tap_on_valid_or_invalid_country_from_filter_result(helper_tap_on_country_from_filter_result,
                                                       country):
    helper_tap_on_country_from_filter_result(country)


@then(parsers.parse('error message <err_text> is shown for wrong phone number or wrong country calling code'),
      target_fixture='check_correct_error_message_is_shown_for_wrong_country_code_wrong_phone_number')
def check_correct_error_message_is_shown_for_wrong_country_code_wrong_phone_number(appium_driver,
                                                                                   err_text):
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())

    logger.info(f"Asserting for correct error message {err_text} after entering wrong phone number ")
    error_text = phone_number_input_activity.get_text(phone_number_input_activity.error_indicator)

    assert_that(error_text).contains(err_text)

@when('enter wrong OTP', target_fixture="enter_wrong_otp")
def enter_wrong_otp(helper_enter_otp):
    otp = DataGenerator().get_random_otp()
    helper_enter_otp(otp)

@then(parsers.parse('"{loading_text}" text should be shown'),
      target_fixture="check_loading_text_is_shown")
def check_loading_text_is_shown(appium_driver, loading_text):
    otp_input_activity = OTPInputActivity(appium_driver.connect())

    logger.info(f"Checking for loading text {loading_text} after entering otp")
    text = otp_input_activity.get_text(otp_input_activity.loading)

    assert_that(text).contains(loading_text)


@then(parsers.parse('error message "{err_text}" is shown for wrong otp'),
      target_fixture='check_correct_error_message_is_shown_for_wrong_otp')
def check_correct_error_message_is_shown_for_wrong_otp(appium_driver, err_text):
    otp_input_activity = OTPInputActivity(appium_driver.connect())

    logger.info(f"Checking for correct error message {err_text} after entering wrong otp")
    error_text = otp_input_activity.get_text(otp_input_activity.error_indicator)

    assert_that(error_text).contains(err_text)