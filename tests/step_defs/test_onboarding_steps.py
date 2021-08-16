from pytest_bdd import when, then, scenarios, parsers, given

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
