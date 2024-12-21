from behave import given, when, then, step

from features.pages.login_page import LoginPage
from features.pages.product_page import ProductPage

@given(u'User navigates to the Login Page "{url}"')
def step_impl(context, url):
    page = LoginPage(context)
    page.visit(url)

@when(u'User types user "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    page = LoginPage(context)
    page.type_user(user)
    page.type_password(pwd)

@when(u'Clicks the Login Button')
def step_impl(context):
    page = LoginPage(context)
    page.click_login()
@then(u'User should be able to view "{title}" page')
def step_impl(context, title):
    page = ProductPage(context)
    page.verify_product_title(title)