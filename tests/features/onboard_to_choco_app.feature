@endtoend @successful_onboard
  Feature: Choco App Onboard
    As a user,
    I want to select country calling code
    and enter my mobile number
    and enter OTP
    So I can onboard into Choco App

  Background:
    Given the choco app is opened in a mobile

  Scenario: Onboard into choco app when filtering with country calling code
    When I tap on country code
    And  enter valid country code in search field to filter
    And tap on valid country from the filtered search result
    And enter valid phone number
    And tap on "Continue" button
    And enter valid OTP
    Then am taken to success activity and shown the message "Welcome to Choco!!"
    And close the choco app

  Scenario: Onboard into choco app when filtering with country name
    When I tap on country code
    And  enter valid country code in search field to filter
    And tap on valid country from the filtered search result
    And enter valid phone number
    And tap on "Continue" button
    And enter valid OTP
    Then am taken to success activity and shown the message "Welcome to Choco!!"
    And close the choco app

  Scenario: Onboard into choco app by entering phone number and then selecting country code
    When I enter valid phone number
    And tap on country code
    And  enter valid country code in search field to filter
    And tap on valid country from the filtered search result
    And tap on "Continue" button
    And enter valid OTP
    Then am taken to success activity and shown the message "Welcome to Choco!!"
    And close the choco app

  Scenario: Onboard into choco app when mobile is in landscape
    Given mobile is in "landscape" orientation
    When I tap on country code
    And  enter valid country code in search field to filter
    And tap on valid country from the filtered search result
    And enter valid phone number
    And tap on "Continue" button
    And enter valid OTP
    Then am taken to success activity and shown the message "Welcome to Choco!!"
    And change mobile to "portrait" orientation
    And close the choco app
