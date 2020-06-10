from selenium.webdriver.common.by import By
from behave import given, then, when
from time import sleep

SHOPPING_ICON = (By.XPATH, "//a[@id='nav-cart']")
CART_EMPTY = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty h2")


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*SHOPPING_ICON).click()
    sleep(2)


@then('Empty shopping cart label shown')
def empty_shopping_cart(context):
    assert 'Your Amazon Cart is empty' in context.driver.find_element(*CART_EMPTY).text
