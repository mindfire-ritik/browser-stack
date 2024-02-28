from selenium.webdriver.common.by import By


class LocatorsHomePage(object):
    def __init__(self, context=None):
        # HomePage
        self.newAccountHeading = (By.CSS_SELECTOR, 'div h1')
        self.signinBtn = (By.XPATH, '//button[text()="SIGN IN"]')
        self.submitBtn = (By.CSS_SELECTOR, 'button[type="submit"]')
        self.lastName = (By.CSS_SELECTOR, "#lastNameInput")
