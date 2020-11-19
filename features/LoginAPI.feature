

Feature:  Validates login user api

  Scenario:  Verify login user authentication
    Given I have login auth credentials
    When  I hit login POST request
    Then  status code of response should be 200
    And   token type should be bearer

  Scenario:  Validate schema type of login response
    Given I have login auth credentials
    When  I hit login POST request
    Then  validate schema type access_token
    And   validate schema type of token_type
    And   validate schema type of expires_in

  Scenario:  Validate headers of login response
    Given I have login auth credentials
    When  I hit login POST request
    Then  validate header Content-Type
    And   validate header Transfer-Encoding
    And   validate header Content-Encoding
