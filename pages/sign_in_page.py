from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignIn(Page):
    SIGN_IN_LABEL_LOCATOR = (By.CSS_SELECTOR, 'h1')

    def verify_page(self, expected_text: str):
        self.verify_text(expected_text, *self.SIGN_IN_LABEL_LOCATOR)
