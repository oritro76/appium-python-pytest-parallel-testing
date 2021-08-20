from pytest_bdd import scenario, when, then, parsers
from loguru import logger
from assertpy import assert_that

from activities.phone_number_input_activity import PhoneNumberInputActivity


@scenario('../features/onboard_to_choco_app.feature',
          'From OTPInputActivity device back button press')
def test_from_otpinputactivity_back_button_press(appium_driver):
    """From OTPInputActivity back button press."""


@when("tap on mobile back button", target_fixture="press_android_back_button")
def press_android_back_button(appium_driver):
    appium_driver.press_android_back_button()


@then(parsers.parse('in PhoneNumberInputActivity default country code "{default_country_code}" should be shown'),
      target_fixture='check_phone_number_input_default_country_code')
def check_phone_number_input_default_country_code(appium_driver, default_country_code):
    phone_number_input_activity = PhoneNumberInputActivity()

    logger.info(f"Checking if default {default_country_code} is shown")
    country_code = appium_driver.get_text(phone_number_input_activity.country_code_select)
    logger.info(f"default country code text {country_code}")
    try:
        assert_that(country_code).is_equal_to(default_country_code)
    except AssertionError as e:
        appium_driver.save_screenshot(str(e))
        logger.critical(e)
        raise


@then(parsers.parse('"{button_text}" button should be enabled'),
      target_fixture='check_button_is_enabled')
def check_button_is_enabled(appium_driver, button_text):
    phone_number_input_activity = PhoneNumberInputActivity()

    logger.info(f"Checking if {button_text} button is enable")

    is_enabled = appium_driver.is_element_enabled(phone_number_input_activity.button)
    logger.info(f"{button_text} button's current status {is_enabled}")
    try:
        assert_that(is_enabled).is_true()
    except AssertionError as e:
        appium_driver.save_screenshot(str(e))
        logger.critical(e)
        raise


@then('phone number input field should be cleared',
      target_fixture='check_phone_number_input_field_cleared')
def check_phone_number_input_field_cleared(appium_driver):
    phone_number_input_activity = PhoneNumberInputActivity()

    logger.info(f"Checking if phone_number input field is cleared")

    text = appium_driver.get_text(phone_number_input_activity.phone_number_input)
    logger.info(f"value of phone number input field {text}")

    try:
        assert_that(text).is_equal_to("")
    except AssertionError as e:
        appium_driver.save_screenshot(str(e))
        logger.critical(e)
        raise
