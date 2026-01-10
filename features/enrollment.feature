Feature: Enroll Payment Method

  @integration
  Scenario: Enroll card for customer
    Given I have a customer
    When I send enrollment request
    Then response status code should be 201
