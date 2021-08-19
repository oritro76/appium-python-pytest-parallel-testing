from pytest_bdd import scenario, then, parsers, given


@scenario('../features/onboard_to_choco_app.feature',
          'Onboard into choco app when mobile is in landscape')
def test_onboard_into_choco_app_when_mobile_is_in_landscape(appium_driver):
    """Onboard into choco app when mobile is in landscape."""


@given(parsers.parse('mobile is in "{orientation}" orientation'),
       target_fixture="given_change_mobile_orientation")
def given_change_mobile_orientation(helper_change_mobile_orientation, orientation):
    helper_change_mobile_orientation(orientation)


@then(parsers.parse('change mobile to "{orientation}" orientation'),
      target_fixture="change_mobile_orientation")
def given_change_mobile_orientation(helper_change_mobile_orientation, orientation):
    helper_change_mobile_orientation(orientation)