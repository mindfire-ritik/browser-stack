from selenium.webdriver.common.by import By


class LocatorsHomePage(object):
    def __init__(self, context=None):
        # HomePage Background
        self.home = (By.XPATH, '//p[text()="Home"]')
        self.login_button = (By.CSS_SELECTOR, "button[type='button']")
        self.userName = (By.CSS_SELECTOR, "input[type='email']")
        self.nextBtn = (By.XPATH, "//input[@type=\"submit\"]")
        self.passwd = (By.CSS_SELECTOR, "input[type='password']")
        self.submitBtn = (By.CSS_SELECTOR, "[data-report-event=\"Signin_Submit\"]")
        self.signedinText = (By.CSS_SELECTOR, "div[class='row text-title']")
        self.noBtn = (By.CSS_SELECTOR, "input[id*=\"Back\"]")
        self.header = (By.XPATH, "//div[contains(@class,'MuiToolbar-root MuiToolbar-gutters MuiToolbar-regular')]")

        # Login test
        self.supportRequestButton = (By.CSS_SELECTOR,"[form=\"attachment-form\"]")
        self.hamburger_button = (By.CSS_SELECTOR, '[data-testid="MenuIcon"]')
        self.hamburger_menulist = (By.CSS_SELECTOR, "[data-testid=\"sentinelStart\"]+div")
        self.logoutAccount = (By.CSS_SELECTOR, "[aria-label*=\"Sign out\"] div.table-cell")
        self.logoutOption = (By.XPATH, "//span[text()=\"Logout\"]")
        self.optionList = (By.CSS_SELECTOR, "div[class*=\"MuiListItemButton\"]>div")
        self.pickAccountHeading = (By.CSS_SELECTOR, "div[role=\"heading\"]")

        # My Account Page
        self.myAccountOption = (By.XPATH, "//span[text()=\"My Account\"]")
        self.myAccountHeading = (By.XPATH, '//p[text()="My Account"]')
        self.accountUserName = (By.XPATH, '//p[contains(text(),"User:")]')
        self.role = (By.XPATH, '//p[contains(text(),"Role")]')
        self.department = (By.XPATH, '//p[contains(text(),"Department")]')
        self.supervisor = (By.XPATH, '//p[contains(text(),"Supervisor")]')
        self.currentAccess = (By.XPATH, '//h6[contains(text(),"Current Access")]/..')
        self.currentFilter = (By.XPATH, '//h6[contains(text(),"Current Filters")]/..')

        # Navigate to All pages
        self.pageHeading = (By.CSS_SELECTOR, "header~div")
        self.managePermissionHeading = (By.XPATH, "//p[text()=\"Manage Permissions\"]")
        self.allPopDashboardHeading = (By.XPATH, "//p[text()=\"All POPs Dashboard\"]")
        self.siteAuditHeading = (By.XPATH, "//p[text()=\"Site Audits\"]")
        self.siteAuditTable = (By.CSS_SELECTOR, '[aria-labelledby="tableTitle"]')
        self.allProjectHeading = (By.XPATH, "//p[text()=\"All Projects\"]")
        self.myAccountHeading = (By.XPATH, "//p[text()=\"My Account\"]")
        self.homeTable = (By.XPATH, '//*[@role="grid"]/..')
        self.allSitesOption = (By.XPATH, '//span[text()="All Sites"]')
        self.allProjectOption = (By.XPATH, "//span[text()=\"All Projects\"]")
        self.allJhaOption = (By.XPATH, '//span[text()="All JHA"]')
        self.allJhaHeading = (By.XPATH, '//p[text()="All JHA"]')
        self.siteAuditOption = (By.XPATH, "//span[text()=\"Site Audits\"]")
        self.managePermissionOption = (By.XPATH, "//span[text()=\"Manage Permissions\"]")
        self.allProjectTable = (By.XPATH, '//div[@class="h-1"]//..')
        self.allJhaTable = (By.XPATH, '//div[@class="h-1"]//..')
        # Create Support Request Button testcase
        self.supportRequestPopupHeading = (By.CSS_SELECTOR, 'div>h6')
        self.issueTitle = (By.CSS_SELECTOR, '#issue')
        self.descriptionInput = (By.CSS_SELECTOR, 'textarea[name="description"]')
        self.resetButton = (By.CSS_SELECTOR, 'button[type="reset"]')
















