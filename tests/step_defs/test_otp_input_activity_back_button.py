import pytest
from pytest_bdd import when, then, scenarios, parsers, given, feature
from assertpy import assert_that

from conf.conf import logger_test
from data.data_gen import DataGenerator
from activities.phone_number_input_activity import PhoneNumberInputActivity
from activities.otp_input_activity import OTPInputActivity
from activities.onboard_success_activity import OnboardSuccessActivity

scenarios('../features/otp_input_activity_back_button.feature')


@when("tap on back button in otp input activity",
      target_fixture='tap_on_back_button_otp_input_activity')
def tap_on_back_button_otp_input_activity(appium_driver):
    otp_input_activity = OTPInputActivity(appium_driver.connect())

    otp_input_activity.tap(otp_input_activity.back_button)


@then('am taken to phone number input activity',
      target_fixture="check_currenct_activity_is_phone_number_input_activity")
def check_current_activity_is_phone_number_input_activity(appium_driver):
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())
    phone_number_input_activity.find_element(phone_number_input_activity.phone_number_input)

    #TODO: raise custom exception