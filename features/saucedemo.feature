Feature: Saucelabs demo End to end

  Background: 
    Given I am on the Saucelabs portal
    And I have provided my credentials
    When I click on the Login button
    Then I am successfully logged in and the inventory page is opened

  Scenario: Buy a few articles from the inventory page
    When I add the first two elements to the cart
    And I go to the cart and check out the added items
    And I enter my payment information
    When I finish the checkout process
    Then I receive a confirmation message thanking me for my purchase

  Scenario: Log out of the system
    When I click on the hamburger menu and select the log out link
    Then I am logged out of the system
