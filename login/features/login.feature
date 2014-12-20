Feature: Login

  Scenario: Successful login
    Given I am on the login page
    When I submit correct login credentials
    Then I am logged in as the user

  Scenario Outline: Unsuccessful login
    Given I am on the login page
    When I submit <bad credentials>
    Then I am shown a bad login credentials message
    And I am not logged in

  Examples: Bad credentials
    | bad credentials |
    | a bad password  |
    | a bad username  |
