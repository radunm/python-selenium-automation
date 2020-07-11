from behave import given, when, then


@given("Open Amazon main page")
def open_amazon(context):
    context.app.page.open_page()


@when('Click Orders')
def click_orders_button(context):
    context.app.top_nav_menu.click_orders()


@then('{expected_text} page opened')
def verify_text(context, expected_text):
    context.app.sign_in_page.verify_page(expected_text)
