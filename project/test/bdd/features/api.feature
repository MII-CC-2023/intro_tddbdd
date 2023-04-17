Feature: test myapi v2



  Scenario Outline: convert fahrenheit to centigrados
    Given myapi version v2
    When user invokes GET /f2c/<f>
    Then for <f>, api returns json with result: <c>
  
    Examples: 
        | f | c |
        | 32  | 0.0 |
        | 50  | 10.0 |