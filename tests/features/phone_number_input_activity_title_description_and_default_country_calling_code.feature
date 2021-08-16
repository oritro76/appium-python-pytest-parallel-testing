@endtoend
Feature: Choco App Phone Number Input Activity Title, Description and Default Country Code
    As a user,
    I will see title
    and description
    and default country code
    after opening the app

  Background:
    Given the choco app is opened in a mobile

  Scenario: Title, description, default country code are shown in the phone number input activity
    Then I see title "What’s your cell phone number?"
    And  see description "We need this to create your account or help you log you back in."
    And see default country code "+1"
    And close the choco app