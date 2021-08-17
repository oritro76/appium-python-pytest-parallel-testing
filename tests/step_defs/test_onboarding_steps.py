from pytest_bdd import when, then, scenarios, parsers, given

from loguru import logger

from activities.phone_number_input_activity import PhoneNumberInputActivity

scenarios('../features/onboard_to_choco_app.feature',)


@given(parsers.parse('mobile is in "{orientation}" orientation'),
       target_fixture="given_change_mobile_orientation")
def given_change_mobile_orientation(helper_change_mobile_orientation, orientation):
    helper_change_mobile_orientation(orientation)


@then(parsers.parse('change mobile to "{orientation}" orientation'),
      target_fixture="change_mobile_orientation")
def given_change_mobile_orientation(helper_change_mobile_orientation, orientation):
    helper_change_mobile_orientation(orientation)


@when(parsers.parse('enter <text> in search field to filter'),
      target_fixture='enter_text_to_filter_countries')
def enter_text_to_filter_countries(text, helper_enter_text_to_filter_countries):
    helper_enter_text_to_filter_countries(text)


@when(parsers.parse('tap on <country> from the filtered search result'),
      target_fixture="tap_on_country_from_filter_result")
def tap_on_country_from_filter_result(country, helper_tap_on_country_from_filter_result):
    helper_tap_on_country_from_filter_result(country)