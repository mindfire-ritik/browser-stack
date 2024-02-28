from selenium.webdriver.common.by import By


class LocatorsHomePage(object):
    def __init__(self, context=None):
        # All Project page
        self.uploadJhaBtn = (By.CSS_SELECTOR, '[data-testid="CloudUploadIcon"]')
        self.uploadJhaModalHeading = (By.CSS_SELECTOR, '[role="dialog"]>h2')
        self.uploadJhaModal = (By.CSS_SELECTOR, '[role="dialog"]>h2')
        self.uploadJhaModaCloseBtn = (By.XPATH, '//button[text()="Cancel"]')
