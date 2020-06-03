# Created by Radu at 02.06.2020
Feature: User can search for solutions of Cancelling an order on Amazon

  Scenario: Search for canceled orders
    Given Open Amazon main page
    When Click on Help link
    Then Help page is shown
    When Type Cancel order into search field
    And Click Go
    Then Cancel Items or Orders text is present
