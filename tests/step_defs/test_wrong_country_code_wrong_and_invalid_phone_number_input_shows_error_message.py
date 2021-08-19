from pytest_bdd import scenario, when, then, parsers
from loguru import logger
from assertpy import assert_that

from activities.phone_number_input_activity import PhoneNumberInputActivity


@scenario('../features/onboard_to_choco_app.feature',
          'Wrong country_code, wrong and invalid phone number input shows error message')
def test_wrong_country_code_wrong_and_invalid_phone_number_input_shows_error_message(appium_driver):
    """Wrong country_code, wrong and invalid phone number input shows error message."""


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