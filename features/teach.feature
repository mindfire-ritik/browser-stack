@smoke 
Feature: Technician App Dashboard Page

    Scenario: : Navigate to technician app dashboard page
        Given I navigate to "https://test-asap.nxlink.com/" url
        When  I click on Login Button
        And   I enter username
        And   I click on next Button
        And   I enter password
        And   I click on submit button
        And   I click on Stay SignedIn as No