# Created by Radu at 30.06.2020
Feature: Open, switch and close new window on Amazon Blog

  Scenario: User can open and close Amazon Blog
 Given Open Amazon page
 When Store original windows
 And Click on blog link “See daily updates at blog.aboutamazon.com”
 And Switch to the newly opened window
 Then Amazon Blog is opened
 And User can open and close Blog menu
 And User can close new window and switch back to original
