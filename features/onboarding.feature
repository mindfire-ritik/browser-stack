@smoke 
Feature: Onboarding Dashboard Page

    Scenario: : Navigate to onboarding app dashboard page
        Given I navigate to "https://uat-onboarding.nextlinkinternet.com/" url
        When  I click on Login Button
        And   I enter username
        And   I click on next Button
        And   I enter password
        And   I click on submit button
        And   I click on Stay SignedIn as No