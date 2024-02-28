import time
import os

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import *

from library.projects.ASAP_Project.home_page import LocatorsHomePage
from library.projects.ticketing.tickets_locators import TicketsLocators


use_step_matcher("re")

@when('I click on Login Button')
def click_on_login_button(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    page = LocatorsHomePage(context)
    ticketing_login = TicketsLocators(context)

    error_text = "Login button is not found/clickable"
    try:
        wait.until(EC.visibility_of_element_located(page.login_button), error_text).click()
    except TimeoutException:
        wait.until(EC.visibility_of_element_located(ticketing_login.ticketingLogin), error_text).click()


@when('I enter username')
def enter_username(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=60, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    username = os.getenv("AUTOMATION_USERNAME")

    try:
        wait.until(EC.visibility_of_element_located(page.userName)).send_keys(username)
    except TimeoutException:
        error_text = "Username is not entered"
        assert False, error_text


@when('I click on next Button')
def click_on_next_button(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=60, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    error_text = "Next button is not found/clickable"
    wait.until(EC.visibility_of_element_located(page.nextBtn), error_text).click()


@when('I enter password')
def enter_password(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=120, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    password = os.getenv("AUTOMATION_PASSWORD")

    try:
        wait.until(EC.visibility_of_element_located(page.passwd)).send_keys(password)

    except TimeoutException:
        error_text = "Password is not entered"
        assert False, error_text


@when('I click on submit button')
def click_on_submit_button(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=60, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    error_text = "SignIn button is not found/clickable"
    wait.until(EC.visibility_of_element_located(page.submitBtn), error_text).click()


@when('I click on Stay SignedIn as No')
def click_SignIn_Button_as_No(context):
    driver = context.browser
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
    page = LocatorsHomePage(context)

    # click on next button
    try:
        # Click on next button if available
        wait.until(EC.visibility_of_element_located(page.next_button)).click()
    except TimeoutException:
        # Handle the case where the next button is not found
        print("Next button is not found")

    # click on the skip button
    try:
        # Click on skip setup button
        wait.until(EC.visibility_of_element_located(page.skip_button)).click()
    except TimeoutException:
        # Handle the case where the skip setup button is not found or an unexpected error occur
        print("Skip setup button is not found")
        driver.back()
        time.sleep(1)
        driver.forward()
        try:
            wait.until(EC.visibility_of_element_located(page.skip_button)).click()
        except TimeoutException:
            # Handle the case where the skip setup button is not found or an unexpected error occur
            driver.refresh()
            wait.until(EC.visibility_of_element_located(page.skip_button)).click()


    error_text = "Stay SignIn Page is not displayed/Found"
    wait.until(EC.visibility_of_element_located(page.signedinText), error_text).is_displayed()

    error_text_signin = "Stay SignIn Page No button is not displayed/Found"
    wait.until(EC.visibility_of_element_located(page.noBtn), error_text_signin).click()
    time.sleep(10)