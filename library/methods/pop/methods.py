import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_element(driver, locator, locatorName):
    wait = WebDriverWait(driver, timeout=7, poll_frequency=0.5)

    text = "{} is not found/clickable"
    error_text = text.format(locatorName)
    wait.until(EC.element_to_be_clickable(locator), error_text)
    wait.until(EC.visibility_of_element_located(locator), error_text).click()

def send_keys(driver,sendText, locator, locatorName):
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.5)

    text = "{} is not entered"
    error_text = text.format(locatorName)
    wait.until(EC.element_to_be_clickable(locator), error_text)
    wait.until(EC.visibility_of_element_located(locator), error_text).send_keys(sendText)

def page_has_loaded(driver):
    page_state = driver.execute_script('return document.readyState;')
    return page_state == 'complete'

def absence_of_element(driver, time, locator, locatorName):

    text = "{} is still present"
    error_text = text.format(locatorName)
    try:
        i = 0
        while len(driver.find_elements(*locator)) > 0:
            time.sleep(1)
            i += 1
            if i == time:
               break
        else:
            return False, error_text

    except Exception:
             return True

def wait_for_visibility(driver,  time, locator, locatorName):

    wait = WebDriverWait(driver, timeout=time, poll_frequency=0.2)
    try:
        wait.until(EC.visibility_of_element_located(locator))
        return True

    except TimeoutException:
        error_text = f"{locatorName} is not visible"
        assert False, error_text


def is_displayed(driver,  time, locator):

    wait = WebDriverWait(driver, timeout=time, poll_frequency=0.2)
    try:
        wait.until(EC.visibility_of_element_located(locator))
        return True

    except TimeoutException:
        return False