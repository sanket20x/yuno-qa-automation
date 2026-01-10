Feature: Capture Payment

  @regression
  Scenario: Capture authorized payment
    Given I have an authorized payment id
    When I send capture request
    Then response status code should be 200
