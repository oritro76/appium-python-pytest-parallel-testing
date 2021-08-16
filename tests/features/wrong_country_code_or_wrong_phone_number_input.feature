@endtoend
Feature: Entering wrong county calling code or phone number will show error message
  As a user,
  If I enter wrong phone number or invalid phone number
  or select wrong country code
  then error message is shown

Background:
    Given the choco app is opened in a mobile

  Scenario Outline: Wrong country_code, wrong and invalid phone number input shows error message
    When I tap on country code
    And  enter <text> in search field to filter
    And tap on valid/invalid <country> from the filtered search result
    And enter valid/invalid phone_number <phone_number>
    And tap on "Continue" button
    Then error message <err_text> is shown for wrong phone number or wrong country calling code
    And close the choco app

    Examples:
      | text        | country    | phone_number | err_text                                                              |
      | bangladesh  | bangladesh | 01521105241  | That phone number isn’t valid, are you sure you entered it correctly? |
      | 91          | india      | 16200000001  | That phone number isn’t valid, are you sure you entered it correctly? |
      | ba          | bahamas    | 1620000      | That phone number isn’t valid, are you sure you entered it correctly?     |
      | ba          | cuba       | !!3adfzcv    | That phone number isn’t valid, are you sure you entered it correctly?     |
