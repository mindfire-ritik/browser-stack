@smoke 
Feature: POP Dashboard Page

    Scenario: : Navigate to pop dashboard page
        Given I navigate to "https://uat-popapp.nxlink.com/" url
        When  I click on Login Button
        Then I wait for 10 sec