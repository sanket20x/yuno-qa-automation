Feature: Authorization

  @sanity
  Scenario: Authorization only payment
    Given I prepare authorization payload
    When I send authorization request
    Then response status code should be 200
