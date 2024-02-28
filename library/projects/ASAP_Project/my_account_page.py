from selenium.webdriver.common.by import By


class LocatorsMyAccountPage(object):
    def __init__(self, context=None):
        self.currentFilter = (By.XPATH, "//p[contains(text(),'Current Filters')]/following::div[contains(@class,'MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1')]")
        self.department = (By.XPATH, "//p[contains(text(),'Department:')]/following-sibling::p")
        self.supervisor = (By.XPATH, "//p[contains(text(),'Supervisor:')]/following-sibling::p")
        self.role = (By.XPATH, "//p[contains(text(),'Role:')]/following-sibling::p")
        self.userName = (By.XPATH, "//p[contains(text(),'User:')]/following-sibling::p")
        self.myAccountTitle = (By.XPATH, "//p[text() = 'My Account']")
        self.myAccount = (By.XPATH, "//span[normalize-space()='My Account']")

