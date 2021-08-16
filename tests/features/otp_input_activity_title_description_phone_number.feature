@endtoend
Feature: Choco App OTP Input Activity Title, Description and Phone Number
    As a user,
    I will see title
    and description
    and my phone number
    after entering phone number and tapping on continue button

Background:
    Given the choco app is opened in a mobile

  Scenario: Title, description, my phone number are shown in the otp input activity
    When I tap on country code
    And enter valid country code in search field to filter
    And tap on valid country from the filtered search result
    And enter valid phone number
    And tap on "Continue" button
    Then see title "We just sent you an SMS with a code. Please type it below!" in otp input activity
    And see description "We sent the code to " in otp input activity
    And see my phone number in otp input activity