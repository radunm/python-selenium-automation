# Created by Radu at 02.06.2020
Feature: Logged out user sees Sign in page when clicking Orders

  Scenario: Verify Sign in
    Given Open Amazon main page
    When Click Orders
    Then Sign in page opened
