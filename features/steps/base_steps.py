import time

from behave import given
from behave import *

use_step_matcher("re")


@given('I navigate to "(.*)" url')
def open_given_portal(context, portal):
    driver = context.browser
    website_url = portal
    driver.get(portal)

@then('I wait for 10 sec')
def wait_for_10_sec(context):
    time.sleep(10)
    pass




