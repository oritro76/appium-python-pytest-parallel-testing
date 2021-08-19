from pytest_bdd import scenario, when, then, parsers
from loguru import logger
from data.data_gen import DataGenerator
from assertpy import assert_that

from activities.otp_input_activity import OTPInputActivity



@scenario('../features/onboard_to_choco_app.feature', 'Entering wrong OTP code show error message and correcting it results successful onboard')
def test_entering_wrong_otp_code_show_error_message_and_correcting_it_results_successful_onboard(appium_driver):
    """Entering wrong OTP code show error message and correcting it results successful onboard."""


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
