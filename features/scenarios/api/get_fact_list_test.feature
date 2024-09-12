@API @SMOKE @SPORTY-TEST
Feature: [API] Get Facts list

  Scenario: Retrieve one or more Facts
    Given Tom wants to get a "3" facts filtered by "cat"
    When Tom is told the get facts list request was successful
    Then Tom verifies that he received the correct amount of facts
    And Tom verifies that the facts received are of type cat

  Scenario: Empty array when zero facts are requested
    Given Tom wants to get a "0" facts filtered by "cat"
    When Tom is told the get facts list request was successful
    Then Tom verifies that he received an empty array