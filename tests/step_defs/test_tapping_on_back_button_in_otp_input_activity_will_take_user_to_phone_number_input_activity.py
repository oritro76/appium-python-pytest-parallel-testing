from pytest_bdd import scenario, when, then
from loguru import logger

from activities.otp_input_activity import OTPInputActivity
from activities.phone_number_input_activity import PhoneNumberInputActivity


@scenario('../features/onboard_to_choco_app.feature', 'Tapping on back button in OTP input activity will take user to phone number input activity')
def test_tapping_on_back_button_in_otp_input_activity_will_take_user_to_phone_number_input_activity(appium_driver):
    """Tapping on back button in OTP input activity will take user to phone number input activity."""


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
