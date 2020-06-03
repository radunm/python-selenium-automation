from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ORDERS_LABEL_LOCATOR = (By.ID, 'nav-orders')
SIGN_IN_LABEL_LOCATOR = (By.CSS_SELECTOR, 'h1')


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(*ORDERS_LABEL_LOCATOR).click()
    sleep(2)


@then('Sign in page opened')
def verify_text(context):
    actual_text = context.driver.find_element(*SIGN_IN_LABEL_LOCATOR).text
    assert "Sign-In" in actual_text, "Expected word '{}' in message, but got '{}'".format('Sign-In', actual_text)
