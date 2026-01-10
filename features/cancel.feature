Feature: Cancel Payment

  @regression
  Scenario: Cancel authorized payment
    Given I have an authorization id
    When I send cancel request
    Then response status code should be 200
