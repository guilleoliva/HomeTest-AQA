@API @SMOKE @SPORTY-TEST
Feature: [API] Get fact by its ID

  Background:
    Given The fact exists with the following data
    """
    fact:
      _id: 591f98803b90f7150a19c229
      text: "In an average year, cat owners in the United States spend over $2 billion on cat food."
      type: cat
      status:
        verified: true
        sentCount: 1
    """

  Scenario: Retrieve fact by its ID
    Given Tom wants to get a fact for his ID "591f98803b90f7150a19c229"
    When Tom is told the get fact by its ID request was successful
    Then Tom verifies that all the fact information is correct
