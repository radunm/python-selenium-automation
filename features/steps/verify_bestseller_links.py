from selenium.webdriver.common.by import By
from behave import then, when

BEST_SELLER_LINK_LOCATOR = (By.XPATH, "//div[@id='nav-xshop']/a[1]")
BEST_SELLER_LABEL = (By.ID, "zg_banner_text_wrapper")
MENU_ITEMS_LIST = (By.CSS_SELECTOR, "#zg_tabs li")
MENU_ITEM = (By.CSS_SELECTOR, "#zg_tabs a")
PAGE_LABEL = (By.ID, "zg_banner_text_wrapper")


@when("Click on Best Sellers link")
def click_best_seller_link(context):
    context.driver.find_element(*BEST_SELLER_LINK_LOCATOR).click()


@then("{expected_text} page is shown")
def verify_best_seller(context, expected_text):
    actual_text = context.driver.find_element(*BEST_SELLER_LABEL).text
    assert actual_text in expected_text, f"Expected {expected_text}, but got {actual_text}"


@then("Count Best Sellers menu items")
def count_best_seller_link(context):
    context.driver.menu_items_list = context.driver.find_elements(*MENU_ITEMS_LIST)
    assert len(context.driver.menu_items_list) == 5, f"Expected 8, but got {len(context.driver.menu_items_list)} menu list items"


@when("Click on each top menu item and verify page")
def click_menu_item(context):
    counter = 0

    while counter < len(context.driver.menu_items_list):
        expected_text = context.driver.find_elements(*MENU_ITEM)[counter].text
        context.driver.find_elements(*MENU_ITEM)[counter].click()
        actual_text = context.driver.find_element(*PAGE_LABEL).text
        assert expected_text in actual_text, f"Expected {expected_text}, but got {actual_text}"
        context.driver.back()
        counter += 1
