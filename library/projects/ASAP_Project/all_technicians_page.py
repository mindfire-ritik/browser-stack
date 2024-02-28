from selenium.webdriver.common.by import By


class LocatorsAllTechniciansPage(object):
    def __init__(self, context=None):
        #home
        self.noDataInAvailability = "//p[text()='%s']"
        self.firstTechHome = (By.XPATH, "//td[1]")
        self.searchButton = (By.XPATH, "//input[@placeholder='Search…']")
        #Add Technician
        self.submitButtonDeactivation = (By.XPATH, "//button[text()='Submit']/span")
        self.techNameDropdown = (By.XPATH, "//p[text()='Technician Name']/following-sibling::div//button[@title='Open']")
        self.techDeactivationSuccessful = (By.XPATH, "//div[text()='Technician Deactivation Successful']")
        self.dateTechDeactivation = (By.XPATH, "//input[@type='date']")
        self.addTechnicianDeactivation = (By.XPATH, "//button[@aria-label='Add Technician Deactivation']")
        self.zoneAvailabilityOption = "//h5[text()='Availability']/parent::div/following-sibling::div//p[text()='%s']"
        self.nextAvailability = (By.XPATH, "//h5[text()='Availability']/following::*[@data-testid='ArrowForwardIosIcon']")
        self.techAddedSuccessfully = (By.XPATH, "//div[text()='Technician was created successfully']")
        self.addPMPoint = "//p[text()='%s']/following::button[4]"
        self.saveButtonJobTypes = (By.XPATH, "//p[text()='Job types']/following::button[text()='Save']")
        self.checkBoxBody = (By.XPATH, "//ul[@role='listbox']//li")
        self.addSelectJobType = (By.XPATH, "//button[text()='Add']")
        self.startDate = (By.XPATH, "//input[@placeholder='Start Date']")
        self.firstAutofill = (By.XPATH, "//button[text()='Mon - Fri']")
        self.zonesDropdown = (By.XPATH, "//p[text()='Zone(s)']/following::input[1]")
        self.addTechnicianTitle = (By.XPATH, "//p[text()='Add Technician']")
        self.addTechnician = (By.XPATH, "//button[text()='Add a Technician']")
        self.firstTechnician = (By.XPATH, "//li[1]")
        #Temporary Move Zone/JobType/Adjust Points popup
        self.jobTypeHeading = (By.CSS_SELECTOR, 'ul[aria-labelledby="demo-simple-select-label"]')
        self.jobMovedPopup = (By.XPATH, "//div[text()='Technician Job(s) Moved Successfully']")
        self.primaryServiceCheck = "// p[contains(text(), '%s')]"
        self.submitButton = (By.XPATH, "//button[text()='Submit']")
        self.saveButton = (By.XPATH, "//button[text()='Save']")
        self.checkBoxSelection = (By.CSS_SELECTOR, 'tr input[class*="Base-input"]')
        # self.secondaryDropdownOption = (By.XPATH, '(//ul/li)[5]')
        self.secondaryServiceDropdown = (By.CSS_SELECTOR, '[aria-labelledby="demo-simple-select-label"]')
        self.primaryServiceDropdown = (By.XPATH, "//label[text()='Primary Service Type']/following-sibling::div/div")
        self.addJobTypeButton = (By.XPATH, "//button[text()='Add Job Types']")
        self.jobType = (By.XPATH, "//button[text()='Job Type']")
        self.end_date_batch = (By.XPATH, "//label[contains(normalize-space(),'Date To')]/following-sibling::div/input")
        self.start_date_batch = (By.XPATH, "//label[contains(normalize-space(),'Date From')]")
        self.jobTypeButton = (By.XPATH, "//button[@aria-label='Temporary Move Zone/JobType/Adjust Points']")
        self.allTechniciansTitle = (By.XPATH, "//p[text()='All Technicians']")
        self.technicianManagement = (By.XPATH, "//span[normalize-space()='Technician Management']")
        self.allTechnicians = (By.XPATH, "//span[normalize-space()='All Technicians']")
        self.dynamicDropDownOption ="//li[text()='%s']"
        self.technicianNameDropdown = (By.XPATH,"//p[contains(text(),'Technician Name')]/parent::div/div/div/div")
        #Filter
        self.multipleCheckBoxBody = (By.CSS_SELECTOR, "ul[aria-labelledby='demo-multiple-checkbox-label']")
        self.filterButton = (By.XPATH, "//*[@data-testid='FilterAltIcon']")
        self.zoneDropdown = (By.XPATH, "//label[text()='Zone']/following::div")
        self.paylocityStatusDropdown = (By.XPATH, "//label[text()='Paylocity Status']/following::div")
        self.dropdownChip = "(//span[text()='%s'])[2]"
        self.applyButton = (By.XPATH, "//button[text()='Apply']")
        self.zoneFirstTechnician = (By.XPATH, "//tr[@role='checkbox'][1]//td[7]")
        self.paylocityFirstTechnician = (By.XPATH, "//tr[@role='checkbox'][1]//td[4]")
        self.filterBy = (By.XPATH, "//p[text()='Filter By']")
        self.filterDropDownOption = "//li//span[text()='%s']"