from selenium.webdriver.common.by import By

from pages.base_page import Page


class TopNavMenu(Page):
    ORDERS_BUTTON_LOCATOR = (By.ID, 'nav-orders')
    HAMBURGER_MENU_BUTTON = (By.ID, 'nav-hamburger-menu')
    HAMBURGER_MUSIC_ITEM_LOCATOR = (By.XPATH, "//div[@id='hmenu-content']//div[contains(text(), 'Amazon Music')]")
    MUSIC_MENU_LIST = (By.CSS_SELECTOR, '.hmenu.hmenu-visible a:not(.hmenu-back-button)')

    def click_orders(self):
        self.click(*self.ORDERS_BUTTON_LOCATOR)

    def click_hamburger_menu(self):
        self.click(*self.HAMBURGER_MENU_BUTTON)

    def click_music(self):
        self.wait_for_element_click(*self.HAMBURGER_MUSIC_ITEM_LOCATOR)

    def count_items(self, expected_number: int):
        expected_number = int(expected_number)
        self.wait.until(CorrectMenuItemsPresent(self.MUSIC_MENU_LIST, expected_number))
        actual_number = self.find_elements(*self.MUSIC_MENU_LIST)
        assert len(actual_number) == expected_number, f'Expected number {expected_number}, but got {len(actual_number)}'


class CorrectMenuItemsPresent(object):
    def __init__(self, locator, amount):
        self.locator = locator
        self.amount = amount

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)  # Finding the referenced element
        if len(elements) == self.amount:
            return elements
        else:
            return False
