@WEB @SMOKE @SPORTY-TEST
Feature: [WEB] Sporty Group - Twitch

  Scenario: Sporty Group Acceptance Test
    Given Tom goes to "Twitch" Web APP login page
    And Tom should see the Twitch logo present
    And Tom clicks on search
    When Tom searches for "StarCraft II"
    And Tom selects the first result
    And Tom scrolls down 2 times
    And Tom selects a streamer in view
    Then Tom takes an snapshot