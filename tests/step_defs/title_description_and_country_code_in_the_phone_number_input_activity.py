from pytest_bdd import then, scenarios, parsers
from assertpy import assert_that
from loguru import logger

from activities.phone_number_input_activity import PhoneNumberInputActivity

scenarios('../features/phone_number_input_activity_title_description_and_default_country_calling_code.feature')


@then(parsers.parse('I see title "{title}"'),
      target_fixture='check_phone_number_input_activity_title')
def check_phone_number_input_activity_title(appium_driver, title):
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())

    logger.info(f"Checking if proper title {title} is shown")

    assert_that(title).is_equal_to(phone_number_input_activity.
                                   get_text(phone_number_input_activity.title))


@then(parsers.parse('see description "{description}"'),
      target_fixture='check_phone_number_input_activity_title')
def check_phone_number_input_activity_title(appium_driver, description):
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())

    logger.info(f"Checking if proper description {description} is shown")

    assert_that(description).is_equal_to(phone_number_input_activity.
                                   get_text(phone_number_input_activity.description))


@then(parsers.parse('see default country code "{country_code}"'),
      target_fixture='check_phone_number_input_activity_title')
def check_phone_number_input_activity_title(appium_driver, country_code):
    phone_number_input_activity = PhoneNumberInputActivity(appium_driver.connect())

    logger.info(f"Checking if default {country_code} is shown")

    assert_that(country_code).is_equal_to(phone_number_input_activity.
                                         get_text(phone_number_input_activity.country_code_select))

