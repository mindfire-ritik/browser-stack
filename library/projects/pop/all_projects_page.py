from selenium.webdriver.common.by import By


class LocatorsHomePage(object):
    def __init__(self, context=None):
        # All Project page
        self.homeTable = (By.XPATH, "//*[@role=\"grid\"]/..")
        self.status = (By.XPATH, '((//div[@role="row"])[2]//div)[4]//span')
        self.activeBtn = (By.CSS_SELECTOR, 'button[value="active"]')
        self.selectedActiveBtn = (By.CSS_SELECTOR, 'button[value="active"][aria-pressed="true"]')
        self.completeBtn = (By.CSS_SELECTOR, 'button[value="complete"]')
        self.selectedCompleteBtn = (By.CSS_SELECTOR, 'button[value="complete"][aria-pressed="true"]')
        self.selectColumnBtn = (By.CSS_SELECTOR, '[title="Select Columns"]')
        self.selectColumnDialog = (By.CSS_SELECTOR, 'div[class*="Dialog"] h2')
        self.selectedProjectTab = (By.CSS_SELECTOR, '[id="table-tab-project"][aria-selected="true"]')
        self.selectedSiteTab = (By.CSS_SELECTOR, '#table-tab-site[aria-selected="true"]')
        self.siteTab = (By.CSS_SELECTOR, '#table-tab-site')
        self.cancelBtn = (By.CSS_SELECTOR, 'button[class*="Error"]')
        self.search = (By.CSS_SELECTOR, '[aria-label="search"]')
        self.projectName = (By.XPATH, '((//div[@role="row"])[2]//div)[1]//span')
        self.searchProjectName = (By.XPATH, '((//div[@role="row"])[3]//div)[1]//span')
        self.searchResult = (By.CSS_SELECTOR, 'a[href*="P-008258"]')
        # Project Details page
        self.header = (By.CSS_SELECTOR, '[data-testid="ExpandMoreIcon"]')
        self.collapseTab = (By.CSS_SELECTOR, 'svg[class*="Icon"][data-testid="ExpandMoreIcon"]')
        self.collapseAllBtn = (By.XPATH, '(//div[@role="group"] //button)[2]')
        self.expandTab = (By.CSS_SELECTOR, 'svg[class*="rotate"]')
        self.expandAllBtn = (By.XPATH, '(//div[@role="group"] //button)[1]')
        self.viewLogBtn = (By.XPATH, '//button[text()="View Log"]')
        self.logDialog = (By.CSS_SELECTOR, 'div[role="dialog"]')
        self.logModalCloseBtn = (By.XPATH, '//button[text()="Close"]')
        self.viewAttachmentsBtn = (By.CSS_SELECTOR, 'a[href*="attachments"]')
        self.tableHome = (By.XPATH, '//div[@role="grid"]')

        # Site Details page
        self.selectedAttachmentsTab = (By.XPATH, "//button[contains(text(), 'Attachments')]")
        self.attachmentGalleryButton = (By.XPATH, '//button[text()="Attachment Gallery"]')
        self.progressBar = (By.CSS_SELECTOR, 'span[role="progressbar"]')
        # Basic Filters
        self.filterDrawerHeading = (By.CSS_SELECTOR, 'button+h6')
        self.statusDropdown = (By.CSS_SELECTOR, '#ProjectStatus')
        self.statusOption = (By.XPATH, '//li[text()="Complete"]')
        self.statusTag = (By.XPATH, '//span[text()="Project Status : Complete"]')
        self.typeDropdown = (By.CSS_SELECTOR, '#ProjectType')
        self.typeOption = (By.XPATH, '//li[text()="New Tower Build V.3"]')
        self.typeTag = (By.XPATH, '//span[text()="Project Type : NEW TOWER BUILD V.3"]')
        self.typeColumn = (By.XPATH, '(//div[@aria-colindex="3"])[2]')
        self.statusColumn = (By.XPATH, '(//div[@aria-colindex="4"])[2]')
        self.basicTab = (By.XPATH, '//button[text()="Basic"]')
        self.moreActions = (By.XPATH, '//button[@title="More Actions"]')
        self.saveCurrentFilter = (By.XPATH, '//li[text()="Save current filter"]')
        self.clearCurrentPreference = (By.XPATH, '//li[text()="Clear current preference"]')
        self.selectFilter = (By.XPATH, '//li[text()="Select filter"]')
        self.currentFilterName = (By.XPATH, '//input[@name="name"]')
        self.currentFilterDescription = (By.XPATH, '//textarea[@name="description"]')
        self.saveButton = (By.XPATH, '//button[text()="Save"]')
        self.filterAddedPopUp = (By.XPATH, '//div[text()="New Filter saved successfully"]')
        self.filterDeletedPopUp = (By.XPATH, '//div[text()="Deleted filter successfully"]')
        self.currentFilter = "//p[text()='%s']"
        self.currentFilterButton = "//button[text()='%s']"
        self.noFiltersCheck = (By.XPATH, '//button[@title="Select Filters"]//span[text()="0"]')
        # Advanced Filters
        self.attributeDropdownOption = (By.XPATH, '//li[text()="Feeding link installed"]')
        self.siteHeight = (By.XPATH, '(//div[@aria-colindex="9"])[2]')
        self.feedlinkInstall = (By.XPATH, '(//div[@aria-colindex="10"])[2]')
        self.attributeDropdown = (By.XPATH, '//*[contains(@value,"Created by")]')
        self.siteButton = (By.XPATH, '//button[@id="table-tab-site"]')
        self.projectAccordian = (By.XPATH, '//span[text()="Project"]/following::div[1]')
        self.releasedToSalesFromAccordian = (By.XPATH, '//span[text()="Released To Sales"]')
        self.removeReleasedToSales = (By.XPATH, '//p[text()="Released To Sales"]/following::button[2]')

        #Site Details
        self.secondaryAPHeightEdit = (By.XPATH, '//h6[text()="Secondary Planned Ap Height (ft)"]/following::button[1]')
        self.secondaryAPHeightInput = (By.XPATH, "//input[@name='secondaryPlannedApHeightFtC']")
        self.updatePopup = (By.XPATH, '//div[text()="AP upgrade updated successfully in Masterdata and Sitetracker."]')
        self.userLocatorViewLog = (By.XPATH, "//tr[1]//td[3]")
        self.itemChangedViewLog = (By.XPATH, "//tr[1]//td[5]")
        self.beforeValueViewLog = (By.XPATH, "//tr[1]//td[6]")
        self.afterValueViewLog = (By.XPATH, "//tr[1]//td[7]")
