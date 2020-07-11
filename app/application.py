from pages.base_page import Page
from pages.top_nav_menu import TopNavMenu
from pages.sign_in_page import SignIn
from pages.shopping_cart_page import ShoppingCart


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(self.driver)
        self.top_nav_menu = TopNavMenu(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.shopping_cart_page = ShoppingCart(self.driver)
