from pytest_bdd import when, then, scenarios, parsers, given
from assertpy import assert_that
from loguru import logger

from data.data_gen import DataGenerator

from activities.otp_input_activity import OTPInputActivity
from activities.onboard_success_activity import OnboardSuccessActivity

scenarios('../features/onboard_to_choco_app.feature',)


@given(parsers.parse('mobile is in "{orientation}" orientation'),
       target_fixture="given_change_mobile_orientation")
def given_change_mobile_orientation(appium_driver, orientation):
    appium_driver.connect()
    logger.info(f"Changing mobile orientation to {orientation}")
    appium_driver.change_device_orientation(orientation)


@then(parsers.parse('change mobile to "{orientation}" orientation'),
      target_fixture="change_mobile_orientation")
def given_change_mobile_orientation(appium_driver, orientation):
    appium_driver.connect()
    logger.info(f"Changing mobile orientation to {orientation}")
    appium_driver.change_device_orientation(orientation)


@when(parsers.parse('enter valid OTP'), target_fixture="enter_otp")
def enter_otp(appium_driver):
    otp = DataGenerator().get_valid_otp()

    otp_input_activity = OTPInputActivity(appium_driver.connect())

    logger.info(f"Entering otp {otp}")

    otp_input_activity.enter_otp(otp=otp)

    logger.info(f"Checking if current activity is Onboard Success Activity")
    onboard_success_activity = OnboardSuccessActivity(appium_driver.connect())

    onboard_success_activity.find_element(onboard_success_activity.title)


@then(parsers.parse('am taken to success activity and shown the message "{message}"'),
      target_fixture="check_correct_message_is_shown_in_onboard_success_activity")
def check_correct_message_is_shown_in_onboard_success_activity(appium_driver, message):
    onboard_success_activity = OnboardSuccessActivity(appium_driver.connect())

    element_text = onboard_success_activity.get_text(onboard_success_activity.title)
    logger.info(f"Checking if correct message is shown in  {message}")
    assert_that(element_text).is_equal_to(message)
