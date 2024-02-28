from selenium.webdriver.common.by import By


class LocatorsHomePage(object):
    def __init__(self, context=None):
        # HomePage Background
        self.home = (By.XPATH, '//p[text()="Home"]')
        self.permissionRow = (By.CSS_SELECTOR, "#UpdateAPUpgradeBuildBillOfMaterials")
        self.department = (By.XPATH, "(//div[@role='button'])[1]")
        self.listBox = (By.XPATH, "//ul[@role='listbox']")
        self.dispatchOption = (By.XPATH, "//li[normalize-space()='Dispatch']")
        self.role = (By.XPATH, "(//div[@role='button'])[2]")
        self.dispatcher = (By.XPATH, "//li[normalize-space()='Dispatcher']")
        self.uncheckedCheckbox = (By.CSS_SELECTOR, 'td input+svg[data-testid="CheckBoxOutlineBlankIcon"]')
        self.checkedCheckbox = (By.CSS_SELECTOR, 'td input+svg[data-testid="CheckBoxIcon"]')
        self.accessCheckbox = (By.CSS_SELECTOR, 'th input')
