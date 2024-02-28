from selenium.webdriver.common.by import By


class LocatorsOnCallTechniciansPage(object):
    def __init__(self, context=None):
        #HomePage
        self.deleteButton = (By.XPATH, "//td[contains(text(),'Ashish Rajpoot')]/following::button")
        self.yesButton = (By.XPATH, "//button[text()='Yes']")
        self.onCallTechDeleted = (By.XPATH, "//div[text()='On call tech was deleted successfully']")
        self.supPhoneLocator = (By.XPATH, "//td[contains(text(),'Ashish Rajpoot')]/preceding::td[1]")
        self.techPhoneLocator = (By.XPATH, "//td[contains(text(),'Ashish Rajpoot')]/preceding::td[3]")
        self.technicianLocator = (By.XPATH, "//td[contains(text(),'Ashish Rajpoot')]/preceding::td[4]")
        self.dateCalender = "//button[contains(text(),'%s')]"
        self.zoneLocator = (By.XPATH, "//td[contains(text(),'Ashish Rajpoot')]/preceding::td[5]")
        self.nextWeekend = (By.XPATH, "//p[contains(text(),'Week Of')]")
        self.onCallTechAdded = (By.XPATH, "//div[text()='On call tech was added successfully']")
        #NewOnCall
        self.onCallTechPopup = (By.XPATH, "//h2[text()='New On Call Tech']")
        self.subPhoneButton = (By.XPATH, "//input[@name='supPhone']")
        self.techPhoneButton = (By.XPATH, "//input[@name='techPhone']")
        self.selectZoneDropdown = (By.XPATH, "//label[text()='Select Zone(s)']/following-sibling::div")
        self.date_batch = (By.XPATH, "//button[contains(@aria-label,'Choose date')]")
        self.createButton = (By.XPATH, "//button[text()='Create']")
        self.dynamicDropDownOption = "//li[text()='%s']"
        self.technicianNameDropdown = (By.XPATH, "//label[contains(text(),'Select Technician')]/following::div")
        self.newOnCall = (By.XPATH, "//button[text()='New On Call']")
        self.onCallTechniciansTitle = (By.XPATH, "//p[text()='On Call Technicians']")
        self.onCallTechnicians = (By.XPATH, "//span[normalize-space()='On Call Technicians']")