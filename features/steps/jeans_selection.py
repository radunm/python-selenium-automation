from selenium.webdriver.common.by import By
from behave import given, then

COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given("Open Amazon Jeans {productid} page")
def open_jeans_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@then("Verify user can select through colors")
def verify_color_selection(context):
    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for color in color_options:
        color.click()
        expected_color = color.get_attribute('alt')
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert selected_color in expected_color, f"Expected {expected_color}, but got {selected_color}"
