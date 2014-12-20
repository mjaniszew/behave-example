from behave import given, when, then
from zonzatest.feature.login import lookup as login


@given(u'I am on the login page')
def step_impl(context):
    context.selenium.login.navigate_to_login_page()


@when(u'I submit correct login credentials')
def step_impl(context):
    context.selenium.login.complete_and_submit_login_form(
        username=login.admin_user['username'],
        password=login.admin_user['password'],
    )


@then(u'I am logged in as the user')
def step_impl(context):
    # It is hard to check whether we are logged in, but if we are now on
    # the search page we can assume we are
    assert context.selenium.login.is_on_search_page()


@when(u'I submit a bad username')
def step_impl(context):
    context.selenium.login.complete_and_submit_login_form(
        username=login.admin_user['bad_username'],
        password=login.admin_user['password'],
    )


@when(u'I submit a bad password')
def step_impl(context):
    context.selenium.login.complete_and_submit_login_form(
        username=login.admin_user['username'],
        password=login.admin_user['bad_password']
    )


@then(u'I am shown a bad login credentials message')
def step_impl(context):
    assert login.bad_credentials == (
        context.selenium.login.login_error_message())


@then(u'I am not logged in')
def step_impl(context):
    # It is hard to check whether we are logged in, but if we aren't we
    # will still be on the login page
    assert context.selenium.login.is_on_login_page()
