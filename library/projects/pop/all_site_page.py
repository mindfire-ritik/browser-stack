from selenium.webdriver.common.by import By


class LocatorsHomePage(object):
    def __init__(self, context=None):
        # HomePage Background
        self.tableHome = (By.XPATH, '//div[@role="grid"]')
        self.home = (By.XPATH, '//p[text()="Home"]')
        self.login_button = (By.CSS_SELECTOR, "button[type='button']")
        self.userName = (By.CSS_SELECTOR, "input[type='email']")
        self.nextBtn = (By.XPATH, "//input[@type=\"submit\"]")
        self.passwd = (By.CSS_SELECTOR, "input[type='password']")
        self.submitBtn = (By.CSS_SELECTOR, "[data-report-event=\"Signin_Submit\"]")
        self.signedinText = (By.CSS_SELECTOR, "div[class='row text-title']")
        self.noBtn = (By.CSS_SELECTOR, "input[id*=\"Back\"]")
        self.header = (By.XPATH, "//div[contains(@class,'MuiToolbar-root MuiToolbar-gutters MuiToolbar-regular')]")
        self.firstRow = (By.CSS_SELECTOR, "[aria-rowindex='2']>div>a")
        # Edit All Site details

        self.homeTable = (By.XPATH, "//*[@role=\"grid\"]/..")
        self.searchInput = (By.CSS_SELECTOR, '[aria-label="search"]')
        self.row = (By.CSS_SELECTOR, "[aria-rowindex=\"3\"]>div")  # table second row first column
        self.searchSite = (By.CSS_SELECTOR, 'a[href="/allsites/3"]>span')
        self.resultSite = (By.CSS_SELECTOR, 'a[href*="/allsites"]>span')
        self.header = (By.XPATH, "//*[contains(text(), 'Site Details ')]")  # site details header
        self.accessTab = (By.XPATH, "//div[text()='Access']")
        self.selectedAccessTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Access')]")
        self.transportTab = (By.XPATH, "//div[text()='Transport']")
        self.selectedTransportTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Transport')]")
        self.selectedTabData = (By.CSS_SELECTOR, "div[class*=\"site-tab-data\"]")  # selected tab data heading
        self.cabinetTab = (By.XPATH, "//div[text()='Cabinet']")
        self.selectedCabinetTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Cabinet')]")
        self.projectTab = (By.XPATH, "//div[text()='Project']")
        self.selectedProjectTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Project')]")
        self.projectTabTable = (By.CSS_SELECTOR, '[aria-label="sticky table"]')
        self.selectedProjectTableHeading = (By.XPATH, "//th[text()='Project Name']")  # selected Project tab Table Heading
        self.attachmentsTab = (By.XPATH, "//div[text()='Attachments']")
        self.selectedAttachmentsTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Attachments')]")
        self.selectedAttachmentsButton = (By.XPATH, "//button[text()='Attachment Gallery']")  # selected Attachment Gallery button
        self.siteAcquisitionsTab = (By.XPATH, "//div[text()='Site Acquisitions']")
        self.selectedSiteAcquisitionsTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Site Acquisitions')]")
        self.siteInfo = (By.XPATH, "//*[text()='Site Info']")  # SiteAcquisitions Site info table heading
        self.leaseInfo = (By.XPATH, "//*[text()='Lease Info']")  # Site Acquisitions Lease info table heading
        self.contactNotes = (By.XPATH, "//span[text()='Contact Notes']")  # Site Acquisitions Contact Notes table heading
        self.leaseNote = (By.XPATH, "//*[text()='Lease Notes']")  # Site Acquisitions Lease Notes table heading
        self.gisTab = (By.XPATH, "//div[text()='GIS']")
        self.selectedGisTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'GIS')]")
        self.totalHhpInfo = (By.XPATH, "//*[text()='Total HHP Info']")  # GIS totalHHP info table heading
        self.cafHhpInfo = (By.XPATH, "//*[text()='CAF HHP Info']")  # GIS CAF HHP info table heading
        self.permittingTab = (By.XPATH, "//div[text()='Permitting']")
        self.selectedPermittingTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Permitting')]")
        self.permitInfo = (By.XPATH, "//*[text()='Permit Info']")  # Permitting tab Permit Info table heading
        self.milestones = (By.XPATH, "//*[text()='Milestones']")  # Permitting & engineering tab Milestones table heading
        self.permitNotes = (By.XPATH, "//span[text()='Permit Notes']")  # Permitting tab Permit Notes table heading
        self.engineeringTab = (By.XPATH, "//div[text()='Engineering']")
        self.selectedEngineeringTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Engineering')]")
        self.engineeringInfo = (By.XPATH, "//*[text()='Engineering Info']")  # Engineering tab Engineering Info table heading
        self.engineeringNotes = (By.XPATH, "//span[text()='Engineering Notes']")  # Engineering tab Engineering Notes table heading
        self.other = (By.XPATH, "//span[text()='Other']")  # Engineering tab other table heading
        self.electricalTab = (By.XPATH, "//div[text()='Electrical']")
        self.selectedElectricalTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Electrical')]")
        self.ownershipInfo = (By.XPATH, "//*[text()='Ownership Info']")  # Electrical tab Ownership Info table heading
        self.electricalStatus = (By.XPATH, "//*[text()='Electrical Status']")  # Electrical tab Electrical Status table heading
        self.cost = (By.XPATH, "//span[text()='Cost']")  # Electrical tab Cost table heading
        self.powerNotes = (By.XPATH, "//*[text()='Power Notes']")  # Electrical tab Power Notes table heading
        self.fiberTab = (By.XPATH, "//div[text()='Fiber']")
        self.selectedFiberTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Fiber')]")
        self.projectInfo = (By.XPATH, "//*[text()='Project Info']")  # Fiber tab Project Info table heading
        self.constructionTab = (By.XPATH, "//div[text()='Construction']")
        self.selectedConstructionTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Construction')]")
        self.maintenanceTab = (By.XPATH, "//div[text()='Maintenance']")
        self.selectedMaintenanceTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Maintenance')]")
        self.maintenanceInfo = (By.XPATH, "//*[text()='Maintenance Info']")  # Maintenance tab maintenance Info table heading
        self.upgradeNotes = (By.XPATH, "//span[text()='Upgrade Notes']")  # Maintenance tab Upgrade Notes table heading
        self.deploymentTab = (By.XPATH, "//div[text()='Deployment']")
        self.selectedDeploymentTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Deployment')]")
        self.deploymentInfo = (By.XPATH, "//*[text()='Deployment Info']")  # Deployment tab deployment Info table heading
        self.primary = (By.XPATH, "//span[text()='Primary']")  # Deployment tab Primary table heading
        self.secondary = (By.XPATH, "//span[text()='Secondary']")  # Deployment tab Secondary table heading
        self.bom = (By.XPATH, "//span[text()='BOM']")  # Deployment tab BOM table heading
        self.networkOperationsTab = (By.XPATH, "//div[text()='Network Operations']")
        self.selectedNetworkOperationsTab = (By.XPATH, "//div[contains(@style, ' rgb(250')][contains(text(), 'Network Operations')]")
        self.networkInfo = (By.XPATH, "//*[text()='Network Info']")  # Network Operations tab Network Info table heading
        # Basic Filter testcase
        self.selectFilterButton = (By.CSS_SELECTOR, 'button[title="Select Filters"]')
        self.filterDrawerHeading = (By.CSS_SELECTOR, 'button+h6')
        self.statusDropdown = (By.CSS_SELECTOR, '#SiteStatus')
        self.cergDropdown = (By.CSS_SELECTOR, 'div#CERG')
        self.statusOption = (By.XPATH, '//li[text()="Active"]')
        self.siteDetailsExpandButton = (By.XPATH, '//p[text()="Site Details"]')
        self.cergOption = (By.XPATH, '//li[text()="Yes"] ')
        self.statusOption = (By.XPATH, '//li[text()="Active"]')
        self.applyFilterButton = (By.XPATH, '//button[text()="Apply Filter"]')
        self.statusTag = (By.XPATH, '//span[text()="Site Status : Active"]')
        self.rdofTag = (By.XPATH, '//span[text()="Site Status : Active"]')
        self.clearAllButton = (By.XPATH, '//button[text()="Clear All"]')
        self.cergColumn = (By.XPATH, '(//div[@aria-colindex="6"])[2]')
        self.statusColumn = (By.XPATH, '(//div[@aria-colindex="12"])[2]')
        self.filterNumber = (By.CSS_SELECTOR, '[aria-label="Select Filters"]>span[class*="text"]')
        # Advance Filter testcase
        self.attributeDropdownOption = (By.XPATH, '//li[text()="Site height"]')
        self.conditionDropdownOption = (By.XPATH, '//li[text()="Is equal to"]')
        self.valueDropdownOption = (By.XPATH, '//li[text()="120"]')
        self.attributeDropdown = (By.CSS_SELECTOR, 'label+div>[role="combobox"]')
        self.conditionDropdown = (By.XPATH, '(//div//div[@aria-haspopup="listbox"])[2]')
        self.valueDropdown = (By.XPATH, '(//div//input[@aria-autocomplete="list"])[2]')
        self.advanceTab = (By.XPATH, '//button[text()="Advanced"]')
        self.selectedAdvanceTab = (By.XPATH, '//button[text()="Advanced"][contains(@class, "selected")]')
        self.plusButton = (By.CSS_SELECTOR, 'button[aria-label="Add expression"]')
        self.secondAttributeDropdown = (By.XPATH, '(//input[@aria-autocomplete="list"])[3]')
        self.secondConditionDropdown = (By.XPATH, '(//div//div[@aria-haspopup="listbox"])[3]')
        self.secondValueDropdown = (By.XPATH, '(//div[@aria-haspopup="listbox"])[4]')
        self.secondAttributeDropdownOption = (By.XPATH, '//li[text()="Cerg 2020"]')
        self.secondConditionDropdownOption = (By.XPATH, '//li[text()="Is equal to"]')
        self.secondValueDropdownOption = (By.XPATH, '//li[text()="True"]')
        self.siteHeight = (By.XPATH, '(//div[@aria-colindex="4"])[2]')

        # Select Columns
        self.selectColumns = (By.XPATH, '//button[@title="Select Columns"]')
        self.siteDetailsAccordian = (By.XPATH, '//span[text()="Site Details"]/following::div')
        self.lastFromAccordian = '//span[text()="%s"]'
        self.zipFromAccordian = (By.XPATH, '//span[text()="Zip"]')
        self.okButton = (By.XPATH, '//button[text()="OK"]')
        self.noOfDraggables = (By.XPATH, '//div[@draggable = "true"]')
        self.removeZipButton = (By.XPATH, '//p[text()="Zip"]/following::button[2]')

        # Edit Details
        self.searchSiteResultName = (By.CSS_SELECTOR, 'a[href="/allsites/295"]')
        self.searchSiteName = (By.CSS_SELECTOR, 'a[href="/allsites/3733"]')
        self.editSiteContact = (By.XPATH, '//button[text()="Edit Site Contact"]')
        self.saveButton = (By.XPATH, '//button[text()="Save"]')
        self.contactNotesTextBox = (By.XPATH, '//label[text()="Contact Notes"]/following::textarea[1]')
        self.contactNotesText = (By.XPATH, '//p[text()="Contact Notes"]/following::p[1]')
        self.commentsTextBox = (By.XPATH, '//label[text()="Comments"]/following::input[1]')
        self.commentsText = (By.XPATH, '//p[text()="Comments"]/following::p[1]')
        self.expandAccordian = "//h3[text()='%s']"
        self.editExpandedAccordian = "//h3[text() = '%s'] / following::button[1]"
        self.contactTextBox = (By.XPATH, '//label[text()="Contact"]/following::input[1]')
        self.contactText = (By.XPATH, '//p[text()="Contact"]/following::p[1]')
        self.ftthTextBox = (By.XPATH, '//label[text()="FTTH"]/following::input[1]')
        self.ftthText = (By.XPATH, '//p[text()="FTTH"]/following::p[1]')
        self.netopsStatusTextBox = (By.XPATH, '//label[text()="NetOps Status"]/following::input[1]')
        self.netopsStatusText = (By.XPATH, '//p[text()="NetOps Status"]/following::p[1]')
        self.successfullyAddedPopup = (By.XPATH, '//div[text()="Successfully updated the details"]')
        self.rowExpandedAccordian = "//h3[text()='%s']/ancestor::div[contains(@aria-expanded,'true')]/following::p[contains(text(),'%s')]"
        self.collapsedAccordian = "//h3[text()='%s']/ancestor::div[contains(@aria-expanded,'false')]"



