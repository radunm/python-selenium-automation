from selenium.webdriver.common.by import By

from pages.base_page import Page


class ShoppingCart(Page):
    SHOPPING_ICON = (By.XPATH, "//a[@id='nav-cart']")
    CART_EMPTY = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty h2")

    def click_cart_icon(self):
        self.click(*self.SHOPPING_ICON)

    def verify_cart(self, expected_text: str):
        self.verify_text(expected_text, *self.CART_EMPTY)
