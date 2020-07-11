from behave import then, when


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.shopping_cart_page.click_cart_icon()


@then('Verify {expected_text} text present')
def empty_shopping_cart(context, expected_text):
    context.app.shopping_cart_page.verify_cart(expected_text)
