from pytest_bdd import then, scenarios, parsers
from assertpy import assert_that
from loguru import logger

from activities.otp_input_activity import OTPInputActivity


scenarios('../features/otp_input_activity_title_description_phone_number.feature')


@then(parsers.parse('see title "{title}" in otp input activity'),
      target_fixture='check_otp_input_activity_title')
def check_otp_input_activity_title(appium_driver, title):
    otp_input_activity = OTPInputActivity(appium_driver.connect())

    logger.info(f"Checking if proper title {title} is shown")

    assert_that(title).is_equal_to(otp_input_activity.
                                   get_text(otp_input_activity.title))


@then(parsers.parse('see description "{description}" in otp input activity'),
      target_fixture='check_phone_number_input_activity_description')
def check_phone_number_input_activity_description(appium_driver, description):
    otp_input_activity = OTPInputActivity(appium_driver.connect())

    logger.info(f"Checking if description {description} is shown")

    assert_that(otp_input_activity.get_text(otp_input_activity.description)).contains(description)


@then(parsers.parse('see my phone number in otp input activity'),
      target_fixture='check_phone_number_input_activity_phone_number')
def check_phone_number_input_activity_phone_number(appium_driver, context):
    my_phone_number = context['country_code'] + context['phone_number']
    otp_input_activity = OTPInputActivity(appium_driver.connect())

    logger.info(f"Checking if description my phone number is shown")

    assert_that(otp_input_activity.get_text(otp_input_activity.description)).contains(my_phone_number)

