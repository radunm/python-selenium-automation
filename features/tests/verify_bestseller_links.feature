# Created by Radu at 15.06.2020
Feature: Count and verify bestseller menu items

  Scenario: Click on bestseller menu item and verify new page
    Given Open Amazon page
    When Click on Best Sellers link
    Then Amazon Best Sellers page is shown
    Then Count Best Sellers menu items
    When Click on each top menu item and verify page