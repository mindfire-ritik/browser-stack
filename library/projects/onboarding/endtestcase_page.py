from selenium.webdriver.common.by import By


class LocatorsHomePage(object):
    def __init__(self, context=None):

        # HomePage
        self.first = (By.XPATH,"//span[text() = '1']")
        self.pmonthFree = (By.XPATH,"//span[contains(text(),'Free Install')]")
        self.applyPromoCode = (By.XPATH, "//p[contains(text(), 'Free Install')]")
        self.monthFree = (By.XPATH,"//span[text()='1']/ancestor::div[contains(@class,'mx-auto')]/following-sibling::div/div[contains(@class,'bg-notice')]")
        self.termAndConditionLink = (By.CSS_SELECTOR, 'a[href*="terms-and-conditions"]')
        self.privacyPolicyLink = (By.CSS_SELECTOR, 'a[href*="privacy-policy"]')
        self.openInternetLink = (By.CSS_SELECTOR, 'a[href*="open-internet"]')
        self.termAndConditionHeading = (By.XPATH, "//h2[text()='Terms and Conditions']")
        self.privacyPolicyHeading = (By.XPATH, "//h3[text()='Privacy Policy']")
        self.openInternetHeading = (By.XPATH, "//h2[text()='Open Internet Transparency Statement']")



