Feature: Verify Payment

  @sanity
  Scenario: Verify card payment
    Given I prepare verify payment payload
    When I send verify request
    Then response status code should be 200
