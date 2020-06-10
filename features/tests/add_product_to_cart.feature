# Created by Radu at 10.06.2020
Feature: Add any product to Amazon shopping cart and verify it is there

  Scenario: Verify phone was added to shopping cart
    Given Open Amazon page
    When Input smartphone into search box
    And Click on search button
    Then Search result for smartphone is shown
    When Click on first phone
    When Click on Add to cart button
    Then Phone added to cart
    When Click on shopping cart
    Then Verify phone in the cart