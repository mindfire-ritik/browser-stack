from selenium.webdriver.common.by import By


class LocatorsHomePage(object):
    def __init__(self, context=None):
        # Site Audit page
        self.siteName = (By.XPATH, '((//tr)[5]//td)[1]')
        self.inProgressBtn = (By.CSS_SELECTOR, 'button[value="inprogress"]')
        self.status = (By.XPATH, '((//tr)[3]//td)[2]')
        self.selectedInProgressBtn = (By.CSS_SELECTOR, 'button[class*="selected"][value="inprogress"]')
        self.completeBtn = (By.CSS_SELECTOR, 'button[value="complete"]')
        self.search = (By.CSS_SELECTOR, 'input[aria-label="search"]')
        self.selectedCompleteBtn = (By.CSS_SELECTOR, 'button[class*="selected"][value="complete"]')
        self.searchSiteName = (By.XPATH, '((//tr)[2]//td)[1]')
        #Site details Page
        self.header = (By.XPATH, '//p[contains(text(), "Site Audit :")]')
        self.siteDetailsForm = (By.CSS_SELECTOR, 'form[class*="space"]')
        self.transportTab = (By.XPATH, '//p[text()="Transport"]')
        self.selectedTransportTab = (By.XPATH, '//div[contains(@class, "selected")] //p[text()="Transport"]')
        self.transportTabTable = (By.CSS_SELECTOR, 'table thead')
        self.cabinetTab = (By.XPATH, '//p[text()="Cabinet"]')
        self.selectedCabinetTab = (By.XPATH, '//div[contains(@class, "selected")] //p[text()="Cabinet"]')
        self.cabinetTabTable = (By.CSS_SELECTOR, 'table thead')
        self.accessTab = (By.XPATH, '//p[text()="Access"]')
        self.selectedAccessTab = (By.XPATH, '//div[contains(@class, "selected")] //p[text()="Access"]')
        self.accessTabTable = (By.CSS_SELECTOR, 'table thead')
        self.attachmentsTab = (By.XPATH, '//p[text()="Attachments"]')
        self.selectedAttachmentsTab = (By.XPATH, '//div[contains(@class, "selected")] //p[text()="Attachments"]')
        self.attachmentsTabTable = (By.CSS_SELECTOR, 'table thead')
