from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CHANGE_LOCATION_BUTTON = (By.CSS_SELECTOR, '.nav-a.nav-a-2.a-popover-trigger')
SET_LOCATION_INPUT = (By.ID, 'GLUXZipUpdateInput')
APPLY_LOCATION_BUTTON = (By.XPATH, "//span[@id='GLUXZipUpdate']")
CONTINUE_BUTTON = (By.ID, 'GLUXConfirmClose')
HELP_LINK = (By.XPATH, "//div[@class='navFooterVerticalRow navAccessibility']//a[contains(text(),'Help')]")
HELP_TEXT_LOCATOR = (By.CSS_SELECTOR, '.a-section h1')
SEARCH_INPUT_LOCATOR = (By.ID, 'helpsearch')
GO_BUTTON = (By.CSS_SELECTOR, '.a-button-input')
CANCEL_LABEL_LOCATOR = (By.XPATH, "//h1[text()='Cancel Items or Orders']")


@given('Open Amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

    # Set Amazon location to Portland, OR
    context.driver.find_element(*CHANGE_LOCATION_BUTTON).click()
    search = context.driver.find_element(*SET_LOCATION_INPUT)
    search.clear()
    search.send_keys('97266')
    context.driver.find_element(*APPLY_LOCATION_BUTTON).click()
    sleep(2)
    con = context.driver.find_element(*CONTINUE_BUTTON)
    context.driver.execute_script("arguments[0].click();", con)
    sleep(2)


@when('Click on Help link')
def click_help_link(context):
    context.driver.find_element(*HELP_LINK).click()
    sleep(2)


@then('Help page is shown')
def verify_help_page(context):
    actual_text = context.driver.find_element(*HELP_TEXT_LOCATOR).text
    assert "help" in actual_text, "Expected word '{}' in message, but got '{}'".format('help', actual_text)


@when('Type Cancel order into search field')
def input_search(context):
    search = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    search.clear()
    search.send_keys('Cancel order')


@when('Click Go')
def click_go(context):
    context.driver.find_element(*GO_BUTTON).click()
    sleep(2)


@then('Cancel Items or Orders text is present')
def verify_text(context):
    actual_text = context.driver.find_element(*CANCEL_LABEL_LOCATOR).text
    assert "Cancel" in actual_text, "Expected word '{}' in message, but got '{}'".format('Cancel', actual_text)
