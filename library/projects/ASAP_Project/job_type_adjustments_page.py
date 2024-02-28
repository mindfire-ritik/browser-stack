from selenium.webdriver.common.by import By


class LocatorsJobTypeAdjustmentsPage(object):
    def __init__(self, context=None):
        self.jobTypeAdjusmentsTitle = (By.XPATH, "// p[text() = 'Job Type Adjustments']")
        self.jobTypeAdjustments = (By.XPATH, "//span[normalize-space()='Job Type Adjustments']")
