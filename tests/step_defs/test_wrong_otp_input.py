import pytest
from pytest_bdd import when, then, scenarios, parsers, given, feature
from assertpy import assert_that

from loguru import logger
from data.data_gen import DataGenerator
from activities.phone_number_input_activity import PhoneNumberInputActivity
from activities.otp_input_activity import OTPInputActivity
from activities.onboard_success_activity import OnboardSuccessActivity

scenarios('../features/wrong_otp_input.feature')


@when('enter wrong OTP', target_fixture="enter_wrong_otp")
def enter_wrong_otp(appium_driver):
    otp_input_activity = OTPInputActivity(appium_driver.connect())

    otp = DataGenerator().get_random_otp()

    logger.info(f"Entering wrong otp {otp}")

    otp_input_activity.enter_otp(otp=otp)


@then(parsers.parse('error message "{err_text}" is shown for wrong otp'),
      target_fixture='check_correct_error_message_is_shown_for_wrong_otp')
def check_correct_error_message_is_shown_for_wrong_otp(appium_driver, err_text):
    otp_input_activity = OTPInputActivity(appium_driver.connect())

    logger.info(f"Checking for correct error message {err_text} after entering wrong otp")
    error_text = otp_input_activity.get_text(otp_input_activity.error_indicator)

    assert_that(error_text).contains(err_text)
