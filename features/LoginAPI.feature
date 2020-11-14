

Feature:  Validates login user

  Scenario:  Verify login user authentication
    Given I have login auth credentials
    When  I hit login POST request
    Then  status code of response should be 200
    And   token type should be bearer
    And   I must fetch the access token
