Feature: Refund Payment

  @regression
  Scenario: Refund a payment
    Given I have a completed payment id
    When I send refund request
    Then response status code should be 200
