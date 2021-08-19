@choco
  Feature: onboard to CHOCO app

Background:
    Given the choco app is opened in a mobile
  @debug
  Scenario Outline: Onboard into choco app when valid text is entered for country code filtering
    When I tap on country code
    And  enter <text> in search field to filter
    And tap on <country> from the filtered search result
    And enter valid phone number
    And tap on "Continue" button
    And enter valid OTP
    Then see the message "Welcome to Choco!!"
    And close the choco app

    Examples:
      | text        | country    |
      | germany     | germany    |
      | 49          | germany    |
      | germ        | germany    |



  Scenario: Onboard into choco app by entering phone number and then selecting country code
    When I enter valid phone number
    And tap on country code
    And enter valid country code in search field to filter
    And tap on valid country from the filtered search result
    And tap on "Continue" button
    And enter valid OTP
    Then see the message "Welcome to Choco!!"
    And close the choco app

  Scenario: Onboard into choco app when mobile is in landscape
    Given mobile is in "landscape" orientation
    When I tap on country code
    And  enter valid country code in search field to filter
    And tap on valid country from the filtered search result
    And enter valid phone number
    And tap on "Continue" button
    And enter valid OTP
    Then see the message "Welcome to Choco!!"
    And change mobile to "portrait" orientation
    And close the choco app


    Scenario: Tapping on back button in OTP input activity will take user to phone number input activity
    Given I am on OTPInputActivity
    When I tap on back button in otp input activity
    Then am taken to phone number input activity
    And close the choco app

  @debug
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
      | ba          | bahamas    | 1620000      | That phone number isn’t valid, are you sure you entered it correctly? |
      | ba          | cuba       | !!3adfzcv    | That phone number isn’t valid, are you sure you entered it correctly? |

  Scenario: Entering wrong OTP code show error message and correcting it results successful onboard
    Given I am on OTPInputActivity
    When enter wrong OTP
    Then "Loading" text should be shown
    And error message "The code you entered was incorrect, are you sure you entered it correctly" is shown for wrong otp
    And enter valid OTP
    And see the message "Welcome to Choco!!"
    And close the choco app


  Scenario: From OTPInputActivity back button press
    Given I am on OTPInputActivity
    When tap on mobile back button
    Then in PhoneNumberInputActivity default country code "+1" should be shown
    And "Continue" button should be enabled
    And phone number input field should be cleared


  Scenario: In OTPInputActivity description phone number where otp was sent is shown
    Given I am on OTPInputActivity
    Then My phone number should show in the activity in the description
