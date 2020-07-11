from behave import then, when


@when("Click on hamburger menu")
def click_hamburger_menu(context):
    context.app.top_nav_menu.click_hamburger_menu()


@when("Click on Amazon Music menu item")
def click_music_menu_item(context):
    context.app.top_nav_menu.click_music()


@then("{expected_number} menu items are present")
def verify_menu_items(context, expected_number):
    context.app.top_nav_menu.count_items(expected_number)
