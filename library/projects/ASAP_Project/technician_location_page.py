from selenium.webdriver.common.by import By


class LocatorsTechnicianLocationPage(object):
    def __init__(self, context=None):
        #EditTechnician
        self.deleteZonesDropdownOption = "//span[text()='%s']/following::*[1]"
        self.technicianUpdatedPopup = (By.XPATH, "//div[text()='Technician was updated successfully']")
        self.addPoint = "//p[text()='%s']/following::button[2]"
        self.saturdayDropdown = (By.XPATH, "//p[text()='AM']/following::button[11]")
        self.filterDropDownOption = "//li[text()='%s']"
        self.zoneDropdown = (By.XPATH, "//p[text()='Zone(s)']/following::input[1]")
        self.saveButton = (By.XPATH, "//button[text()='Save']")
        self.editTechnicianLocationTitle = (By.XPATH, "//p[text()='Edit Technician']")
        #TechnicianDetails
        self.editTechnician = (By.XPATH, "//button[@aria-label='Edit Technician']")
        self.zoneTechDetails = (By.XPATH, "//div[text()='Zone(s)']/following::div")
        self.technicianName = (By.XPATH, "//div[text()='Name']/following::div")
        # HomePage
        self.firstTechName = (By.XPATH, "//tr[2]/td[1]")
        self.firstActions = (By.XPATH, "//*[@data-testid='VisibilityIcon']")
        self.firstEntryZone = (By.XPATH, "//tr[2]/td[2]")
        self.technicianLocationTable = (By.XPATH, "//th[text()='Employee']")
        self.zoneLocator = "//th[text()='%s']"
        self.technicianLocationTitle = (By.XPATH, "//p[text()='Technician Location']")
        self.technicianLocation = (By.XPATH, "//span[normalize-space()='Technician Location']")