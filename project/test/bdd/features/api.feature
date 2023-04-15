Feature: test myapi v2

  Scenario: convert fahrenheit to centigrados
    Given myapi version v2
    When user invokes GET /f2c/32
    Then api returns json with result: 0.0