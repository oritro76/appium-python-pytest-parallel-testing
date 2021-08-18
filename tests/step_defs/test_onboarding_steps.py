from pytest_bdd import when, then, scenario, parsers, given
from assertpy import assert_that
from loguru import logger
import pytest

from activities.phone_number_input_activity import PhoneNumberInputActivity
from activities.otp_input_activity import OTPInputActivity
from activities.onboard_success_activity import OnboardSuccessActivity
from data.data_gen import DataGenerator
from custom_excepitons.appium_exceptions import AppiumConnectionFailException



@scenario('../features/onboard_to_choco_app.feature', 'Entering wrong OTP code show error message and correcting it results successful onboard')
def test_entering_wrong_otp_code_show_error_message_and_correcting_it_results_successful_onboard(appium_driver):
    """Entering wrong OTP code show error message and correcting it results successful onboard."""


@scenario('../features/onboard_to_choco_app.feature', 'From OTPInputActivity back button press')
def test_from_otpinputactivity_back_button_press(appium_driver):
    """From OTPInputActivity back button press."""


@scenario('../features/onboard_to_choco_app.feature', 'In OTPInputActivity description phone number where otp was sent is shown')
def test_in_otpinputactivity_description_phone_number_where_otp_was_sent_is_shown(appium_driver):
    """In OTPInputActivity description phone number where otp was sent is shown."""


@scenario('../features/onboard_to_choco_app.feature', 'Onboard into choco app by entering phone number and then selecting country code')
def test_onboard_into_choco_app_by_entering_phone_number_and_then_selecting_country_code(appium_driver):
    """Onboard into choco app by entering phone number and then selecting country code."""


@scenario('../features/onboard_to_choco_app.feature', 'Onboard into choco app when mobile is in landscape')
def test_onboard_into_choco_app_when_mobile_is_in_landscape(appium_driver):
    """Onboard into choco app when mobile is in landscape."""


@scenario('../features/onboard_to_choco_app.feature', 'Onboard into choco app when valid text is entered for country code filtering')
def test_onboard_into_choco_app_when_valid_text_is_entered_for_country_code_filtering(appium_driver):
    """Onboard into choco app when valid text is entered for country code filtering."""


@scenario('../features/onboard_to_choco_app.feature', 'Tapping on back button in OTP input activity will take user to phone number input activity')
def test_tapping_on_back_button_in_otp_input_activity_will_take_user_to_phone_number_input_activity(appium_driver):
    """Tapping on back button in OTP input activity will take user to phone number input activity."""


@scenario('../features/onboard_to_choco_app.feature', 'Wrong country_code, wrong and invalid phone number input shows error message')
def test_wrong_country_code_wrong_and_invalid_phone_number_input_shows_error_message(appium_driver):
    """Wrong country_code, wrong and invalid phone number input shows error message."""







@given("the choco app is opened in a mobile", target_fixture="open_app")
def open_app(appium_driver):
    try:
        logger.info('Connecting to appium server and opening the app')
        appium_driver.connect()
    except AppiumConnectionFailException as e:
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


@when("enter valid country code in search field to filter", target_fixture="enter_text_to_filter_countries")
def enter_text_to_filter_countries(context, helper_enter_text_to_filter_countries):
    context['country_code'] = DataGenerator().get_valid_country_calling_code()
    country_calling_code = DataGenerator().get_valid_country_calling_code()[1:]
    helper_enter_text_to_filter_countries(country_calling_code)


@when('tap on valid country from the filtered search result',
      target_fixture="tap_on_country_from_filter_result")
def tap_on_country_from_filter_result(helper_tap_on_country_from_filter_result):
    country = DataGenerator().get_valid_country()
    helper_tap_on_country_from_filter_result(country)


@when("enter valid phone number", target_fixture="enter_phone_number")
@when("I enter valid phone number", target_fixture="enter_phone_number")
def enter_phone_number(helper_enter_phone_number, context):
    context['phone_number'] = DataGenerator().get_valid_phone_number()
    phone_number = DataGenerator().get_valid_phone_number()
    helper_enter_phone_number(phone_number)


@when(parsers.parse('tap on "{button_text}" button'),
      target_fixture="tap_on_button_in_phone_number_input_activity")
def tap_on_button_in_phone_number_input_activity(helper_tap_on_button_in_phone_number_input_activity,
                                                 button_text):
    helper_tap_on_button_in_phone_number_input_activity(button_text)


@then(parsers.parse('enter valid OTP'), target_fixture="enter_otp")
@when(parsers.parse('enter valid OTP'), target_fixture="enter_otp")
def enter_otp(appium_driver, helper_enter_otp):
    otp = DataGenerator().get_valid_otp()

    helper_enter_otp(otp)

    logger.info(f"Checking if current activity is Onboard Success Activity")
    onboard_success_activity = OnboardSuccessActivity()

    appium_driver.find_element(onboard_success_activity.title)


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
    otp_input_activity = OTPInputActivity()

    logger.info(f"Tapping on OTP Input Activity back button")
    appium_driver.tap(otp_input_activity.back_button)


@then('am taken to phone number input activity',
      target_fixture="check_currenct_activity_is_phone_number_input_activity")
def check_current_activity_is_phone_number_input_activity(appium_driver):
    logger.info(f"Checking if current activity is Phone Number Input Activity")
    phone_number_input_activity = PhoneNumberInputActivity()
    appium_driver.find_element(phone_number_input_activity.phone_number_input)


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
    phone_number_input_activity = PhoneNumberInputActivity()

    logger.info(f"expected error message {err_text}")
    text = appium_driver.get_text(phone_number_input_activity.error_indicator)
    logger.info(f"error message {text} after entering wrong phone number ")
    
    try:
        assert_that(text).contains(err_text)
    except AssertionError as e:
        logger.critical(e)
        raise 


@when('enter wrong OTP', target_fixture="enter_wrong_otp")
def enter_wrong_otp(helper_enter_otp):
    otp = DataGenerator().get_random_otp()
    helper_enter_otp(otp)


@then(parsers.parse('"{loading_text}" text should be shown'),
      target_fixture="check_loading_text_is_shown")
def check_loading_text_is_shown(appium_driver, loading_text):
    otp_input_activity = OTPInputActivity()

    logger.info(f"Checking for loading text {loading_text} after entering otp")
    text = appium_driver.get_text(otp_input_activity.loading)

    logger.info(f"Loading text {loading_text}")
    try:
        assert_that(text).contains(loading_text)
    except AssertionError as e:
        logger.critical(e)
        raise 


@then(parsers.parse('error message "{err_text}" is shown for wrong otp'),
      target_fixture='check_correct_error_message_is_shown_for_wrong_otp')
def check_correct_error_message_is_shown_for_wrong_otp(appium_driver, err_text):
    otp_input_activity = OTPInputActivity()

    logger.info(f"Checking for correct error message {err_text} after entering wrong otp")
    error_text = appium_driver.get_text(otp_input_activity.error_indicator)
    try:
        assert_that(error_text).contains(err_text)
    except AssertionError as e:
        logger.critical(e)
        raise 


@when("tap on mobile back button", target_fixture="press_android_back_button")
def press_android_back_button(appium_driver):
    appium_driver.press_android_back_button()


@then(parsers.parse('in PhoneNumberInputActivity default country code "{default_country_code}" should be shown'),
      target_fixture='check_phone_number_input_default_country_code')
def check_phone_number_input_default_country_code(appium_driver, default_country_code):
    phone_number_input_activity = PhoneNumberInputActivity()

    logger.info(f"Checking if default {default_country_code} is shown")
    country_code = appium_driver.get_text(phone_number_input_activity.country_code_select)
    logger.info(f"default country code text {country_code}")
    try:
        assert_that(country_code).is_equal_to(default_country_code)
    except AssertionError as e:
        logger.critical(e)
        raise 


@then(parsers.parse('"{button_text}" button should be enabled'),
      target_fixture='check_button_is_enabled')
def check_button_is_enabled(appium_driver, button_text):
    phone_number_input_activity = PhoneNumberInputActivity()

    logger.info(f"Checking if {button_text} button is enable")

    is_enabled = appium_driver.is_element_enabled(phone_number_input_activity.button)
    logger.info(f"{button_text} button's current status {is_enabled}")
    try:
        assert_that(is_enabled).is_true()
    except AssertionError as e:
        logger.critical(e)
        raise 


@then('phone number input field should be cleared',
      target_fixture='check_phone_number_input_field_cleared')
def check_phone_number_input_field_cleared(appium_driver):
    phone_number_input_activity = PhoneNumberInputActivity()

    logger.info(f"Checking if phone_number input field is cleared")

    text = appium_driver.get_text(phone_number_input_activity.phone_number_input)
    logger.info(f"value of phone number input field {text}")
    
    try:
        assert_that(text).is_equal_to("")
    except AssertionError as e:
        logger.critical(e)
        raise


@then(parsers.parse('My phone number should show in the activity in the description'),
      target_fixture='check_phone_number_is_shown_where_otp_was_sent')
def check_phone_number_is_shown_where_otp_was_sent(appium_driver, context):
    otp_input_activity = OTPInputActivity()

    phone_number = context['country_code'] + context['phone_number']
    text = appium_driver.get_text(otp_input_activity.description)
    logger.info(f"My phone nunber {phone_number}")
    logger.info(f"OTPInputActivity descriptin {text}")
    
    try:
        assert_that(text).contains(phone_number)
    except AssertionError as e:
        logger.critical(e)
        raise
