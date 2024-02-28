from selenium.webdriver.common.by import By


class LocatorsZoneGroupingsPage(object):
    def __init__(self, context=None):
        #Home Page
        self.yesButton = (By.XPATH, "//button[text() = 'Yes']")
        self.deleteButton = "//th[text()='%s']/following::*[@data-testid='DeleteForeverIcon']"
        self.zoneNameHome = "//th[text()='%s']"
        self.editZoneGroupingButton = "//th[text()='%s']/following::img"
        self.zonesHome = "//th[text()='%s']/following-sibling::th[1]"
        self.rdoNameHome = "//th[text()='%s']/following-sibling::th[2]"
        self.zoneUpdatedPopup = (By.XPATH, "//div[text()='Zone Grouping Updated Successfully']")
        self.zoneDeletedPopup = (By.XPATH, "//div[text()='Zone Grouping Deleted Successfully']")
        self.newZoneAddedPopup = (By.XPATH, "//div[text()='New Zone Grouping Added Successfully']")
        self.addZoneGrouping = (By.XPATH, "//button[text() = 'Add Zone Grouping']")
        self.zoneGroupingsTitle = (By.XPATH, "//p[text() = 'Zone Groupings']")
        self.zoneGroupings = (By.XPATH, "//span[normalize-space()='Zone Groupings']")
        #Add/Update Zone Grouping
        self.updateButton = (By.XPATH, "//button[text()='Update']")
        self.dialogHeading = (By.CSS_SELECTOR, "[role='dialog']>h2")
        self.addButton = (By.XPATH, "//button[text()='Add']")
        self.selectZoneDropdown = (By.XPATH, "//label[text()='Select Zone(s)']/following-sibling::div")
        self.dynamicDropDownOption = "//li[text()='%s']"
        self.rdoDropdown = (By.XPATH, "//label[text()='RDO']/following-sibling::div")
        self.zoneGroupingName = (By.XPATH, "//input[@id = 'zoneGroupName']")
        self.removeFirstChip = (By.XPATH, "(//*[contains(@class,'MuiChip-deleteIcon')])[1]")