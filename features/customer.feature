Feature: Customer Creation

  @sanity
  Scenario: Create customer successfully
    Given I prepare customer payload
    When I send create customer request
    Then response status code should be 201

  @negative
  Scenario: Create customer without merchant_customer_id
    Given I prepare invalid customer payload
    When I send create customer request
    Then response status code should be 400
