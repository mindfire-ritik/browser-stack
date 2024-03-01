@smoke 
Feature: ASAP Dashboard Page

    Scenario: : Navigate to ASAP dashboard page
        Given I navigate to "https://uat-asap.nxlink.com/" url
        When  I click on Login Button
        Then I wait for 10 sec