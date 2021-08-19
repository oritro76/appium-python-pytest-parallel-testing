from pytest_bdd import scenario, then, parsers
from loguru import logger
from assertpy import assert_that

from activities.otp_input_activity import OTPInputActivity


@scenario('../features/onboard_to_choco_app.feature',
          'In OTPInputActivity description phone number where otp was sent is shown')
def test_in_otpinputactivity_description_phone_number_where_otp_was_sent_is_shown(appium_driver):
    """In OTPInputActivity description phone number where otp was sent is shown."""


@then(parsers.parse('My phone number should show in the activity in the description'),
      target_fixture='check_phone_number_is_shown_where_otp_was_sent')
def check_phone_number_is_shown_where_otp_was_sent(appium_driver, context):
    otp_input_activity = OTPInputActivity()

    phone_number = context['country_code'] + context['phone_number']
    text = appium_driver.get_text(otp_input_activity.description)
    logger.info(f"My phone number {phone_number}")
    logger.info(f"OTPInputActivity description {text}")

    try:
        assert_that(text).contains(phone_number)
    except AssertionError as e:
        logger.critical(e)
        raise
