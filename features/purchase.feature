Feature: Purchase Payment

  @sanity
  Scenario: Purchase with minimal fields
    Given I prepare minimal purchase payload
    When I send purchase request
    Then response status code should be 200

  @negative
  Scenario: Purchase with insufficient funds
    Given I prepare insufficient funds payload
    When I send purchase request
    Then response status code should be 400
