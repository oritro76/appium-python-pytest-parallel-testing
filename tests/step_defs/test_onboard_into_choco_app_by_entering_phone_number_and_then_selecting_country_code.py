from pytest_bdd import scenario


@scenario('../features/onboard_to_choco_app.feature',
          'Onboard into choco app by entering phone number and then selecting country code')
def test_onboard_into_choco_app_by_entering_phone_number_and_then_selecting_country_code(appium_driver):
    """Onboard into choco app by entering phone number and then selecting country code."""