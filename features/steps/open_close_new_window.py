from selenium.webdriver.common.by import By
from behave import when, then
from selenium.webdriver.support import expected_conditions as EC

BLOG_LINK_LOCATOR = (By.CSS_SELECTOR, "#desktop-btf-grid-6 .a-cardui-footer a")
BLOG_TEXT = (By.CSS_SELECTOR, ".ArticlePage-headerLinks li:first-child")
OPEN_HAMBURGER_MENU = (By.CSS_SELECTOR, ".ArticlePage-header-menuToggle")
CLOSE_HAMBURGER_MENU = (By.CSS_SELECTOR, ".ArticlePage-header-menuClose")
HAMBURGER_MENU_LIST = (By.CSS_SELECTOR, ".ArticlePage-navigation .Navigation-items > li")


@when("Store original windows")
def store_original(context):
    context.original_window = context.driver.current_window_handle


@when("Click on blog link “See daily updates at blog.aboutamazon.com”")
def click_blog_link(context):
    context.driver.find_element(*BLOG_LINK_LOCATOR).click()
    context.driver.wait.until(EC.new_window_is_opened)
    context.new_window = context.driver.window_handles[1]


@when("Switch to the newly opened window")
def switch_to_window(context):
    context.driver.switch_to_window(context.new_window)


@then("Amazon Blog is opened")
def verify_blog(context):
    actual_text = context.driver.find_element(*BLOG_TEXT).text
    assert "Amazon's COVID-19 blog" in actual_text, f"Expected 'Amazon's COVID-19 blog', but got {actual_text}"


@then("User can open and close Blog menu")
def verify_blog_menu(context):
    context.driver.find_element(*OPEN_HAMBURGER_MENU).click()
    menu_list = context.driver.find_elements(*HAMBURGER_MENU_LIST)
    assert len(menu_list) == 8, f"Expected 8, but got {len(menu_list)} menu list items"
    context.driver.find_element(*CLOSE_HAMBURGER_MENU).click()


@then("User can close new window and switch back to original")
def switch_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)
