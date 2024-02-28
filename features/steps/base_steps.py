import time

from behave import given
from behave import *

use_step_matcher("re")


@given('I navigate to "(.*)" url')
def open_given_portal(context, portal):
    driver = context.browser
    website_url = portal
    driver.get(portal)




