# Created by Radu at 09.06.2020
Feature: User can click on the Shopping cart icon and verifies it is empty

  Scenario: Verify the Shopping cart is empty

    Given Open Amazon page
    When Click on cart icon
    Then Verify Your Amazon Cart is empty text present