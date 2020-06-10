from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD_LOCATOR = (By.ID, "twotabsearchtextbox")
SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".nav-search-submit .nav-input")
PRODUCT_LABEL_LOCATOR = (By.CSS_SELECTOR, ".a-color-state.a-text-bold")
PHONE_IMAGE_LOCATOR = (By.XPATH, "//div[@data-index='1']//span[@class='rush-component']/a")
ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
ADDED_LABEL_LOCATOR = (By.CSS_SELECTOR, "h1")
SHOPPING_CART_LINK = (By.ID, "nav-cart")
TOTAL_ITEMS_IN_CART = (By.ID, "sc-subtotal-label-buybox")


@when('Input {product} into search box')
def input_search(context, product):
    search = context.driver.find_element(*SEARCH_FIELD_LOCATOR)
    search.clear()
    search.send_keys(product)
    sleep(2)


@when('Click on search button')
def click_search_logo(context):
    context.driver.find_element(*SEARCH_BUTTON_LOCATOR).click()
    sleep(1)


@then('Search result for {product} is shown')
def search_result_shown(context, product):
    actual_text = context.driver.find_element(*PRODUCT_LABEL_LOCATOR).text
    assert product in actual_text, f"Expected word {product}, but got {actual_text}"


@when('Click on first phone')
def product_click(context):
    context.driver.find_element(*PHONE_IMAGE_LOCATOR).click()
    sleep(1)


@when('Click on Add to cart button')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    sleep(1)


@then('Phone added to cart')
def verify_phone(context):
    actual_text = context.driver.find_element(*ADDED_LABEL_LOCATOR).text
    assert "Added to Cart" in actual_text, f"Expected word Added to Cart, but got {actual_text}"


@when('Click on shopping cart')
def shopping_cart_click(context):
    context.driver.find_element(*SHOPPING_CART_LINK).click()
    sleep(1)


@then('Verify phone in the cart')
def verify_phone(context):
    actual_text = context.driver.find_element(*TOTAL_ITEMS_IN_CART).text
    assert "Subtotal (1 item)" in actual_text, f"Expected word 'Subtotal (1 item)', but got {actual_text}"
