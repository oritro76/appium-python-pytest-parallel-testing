@endtoend
Feature: Wrong OTP input will show error message
  As a user,
  If I select correct country code and enter correct phone number
  and enter wrong otp
  then error message is shown

Background:
    Given the choco app is opened in a mobile

  Scenario: Wrong otp input shows error message
    When I tap on country code
    And  enter valid country code in search field to filter
    And tap on valid country from the filtered search result
    And enter valid phone number
    And tap on "Continue" button
    And enter wrong OTP
    Then error message "The code you entered was incorrect, are you sure you entered it correctly" is shown for wrong otp
    And close the choco app