from pytest_bdd import scenario, when, parsers



@scenario('../features/onboard_to_choco_app.feature',
          'Onboard into choco app when valid text is entered for country code filtering')
def test_onboard_into_choco_app_when_valid_text_is_entered_for_country_code_filtering(appium_driver):
    """Onboard into choco app when valid text is entered for country code filtering."""

