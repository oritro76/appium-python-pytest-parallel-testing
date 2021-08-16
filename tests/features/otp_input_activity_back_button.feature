@endtoend
Feature: Otp input activity back button tap
  As a user
  If I select correct country code and enter correct phone number
  and after landing on otp input activity
  tap on back button
  then I am taken to phone number input activity

  Background:
    Given the choco app is opened in a mobile

  Scenario: Tapping on back button in OTP input activity will take user to phone number input activity
    When I tap on country code
    And enter valid country code in search field to filter
    And tap on valid country from the filtered search result
    And enter valid phone number
    And tap on "Continue" button
    And tap on back button in otp input activity
    Then am taken to phone number input activity
    And close the choco app