from pytest_bdd import when, then, scenarios

from loguru import logger

from activities.phone_number_input_activity import PhoneNumberInputActivity
from activities.otp_input_activity import OTPInputActivity


#scenarios('../features/otp_input_activity_back_button.feature')



@when("tap on back button in otp input activity",
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


