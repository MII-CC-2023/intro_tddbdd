Feature: test myapi v2

  Scenario: convert fahrenheit to centigrados
    Given myapi version v2
    When user invokes GET /f2c/f
    Then api returns json with result: c