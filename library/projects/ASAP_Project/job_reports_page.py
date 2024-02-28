from selenium.webdriver.common.by import By


class LocatorsJobReportsPage(object):
    def __init__(self, context=None):
        #JobReportsHome
        self.secondDropdown = (By.XPATH, "(//div[contains(@class,'MuiInputBase-root MuiInput-root MuiInput-underline MuiInputBase-colorPrimary')]/input)[2]")
        self.meterTitle = "//h6[contains(normalize-space(),'%s')]"
        self.start_date_batch = (By.XPATH, "//label[contains(normalize-space(),'Start Date')]")
        self.end_date_batch = (By.XPATH, "//label[contains(normalize-space(),'End Date')]")
        self.jobReportsTitle = (By.XPATH, "//p[text() = 'Appointment Reports']")
        self.jobReports = (By.XPATH, "//span[normalize-space()='Appointment Reports']")
        self.dynamicDropDownOption ="//li[text()='%s']"
        self.filterByDropdown = (By.XPATH,"//div[contains(@class,'MuiFormControl-root')]//label[text()='Filter By']/following-sibling::div/div")
        self.zoneDropdownOption = (By.XPATH, "//li[contains(text(),'IA-')]")
        self.zoneDropdown = (By.XPATH, "//div[contains(@class,'MuiFormControl-root')]//label[contains(text(),'Select')]/following-sibling::div/div")