from selenium.webdriver.common.by import By
from behave import given, then

PRODUCT_LIST = (By.CSS_SELECTOR, "#wfm-pmd_deals_section .s-result-list.s-col-2 li > div > div:not(.a-text-center)")
NAME_LOCATOR = (By.CSS_SELECTOR, ".wfm-sales-item-card__product-name")
PRICE_LOCATOR = (By.CSS_SELECTOR, ".wfm-sales-item-card__regular-price")


@given("Open Amazon deals page")
def open_deals_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then("Verify every product has {expected_price_tag} and product name")
def verify_price_and_name(context, expected_price_tag):
    product_list = context.driver.find_elements(*PRODUCT_LIST)
    for product in product_list:
        print(product.find_element(*NAME_LOCATOR).text)
        assert expected_price_tag in product.find_element(*PRICE_LOCATOR).text, f"Expected {expected_price_tag}, but " \
                                                                                f"got {product.find_element(*PRICE_LOCATOR).text}"

