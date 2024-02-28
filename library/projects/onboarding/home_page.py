from selenium.webdriver.common.by import By


class LocatorsHomePage(object):
    def __init__(self, context=None):
        # HomePage
        self.emailReference = (By.XPATH, "//label[text()='Email']/preceding-sibling::input")
        self.phoneReference = (By.XPATH, "//label[text()='Phone Number']/preceding-sibling::input")
        self.fullNameReference = (By.XPATH, "//label[text()='Full Name']/preceding-sibling::input")
        self.yourInformationTitle = (By.XPATH, "//h1[text()='Your Information']")
        self.planTotal = (By.XPATH, "//h4[text()='Cart']/following::p[4]")
        self.customiseServices = (By.XPATH, "//h1[text()='Customize Your Services']")
        self.iHaveARouter = (By.XPATH, '//span[text()="Included"]')
        self.internetEquipment = (By.XPATH, "//span[text()=' Internet Equipment']")
        self.iWantServiceProtection = (By.XPATH, "//input[@id='add-protection-plan-lg']")
        self.serviceProtectionPlan = (By.XPATH, "//p[text()='SERVICE PROTECTION PLAN']")
        self.additionalOptions = (By.XPATH, "//span[text()=' Additional Options']")
        self.continueButton = (By.XPATH, "//button[@aria-labelledby='cart-continue']")
        self.mobilePlans = (By.XPATH, "//p[contains(text(),'VoIP')]")
        self.monthToMonthToggle = (By.XPATH, "//button[@role='switch']")
        self.internetPlansAccrodian =  (By.XPATH, "//span[text()='Phone Services']")
        self.selectYourServiceTitle = (By.XPATH, "//h1[text()='Select Your Services']")
        self.internetPlans = "//p[contains(text(),'%s')]"  # remove
        self.spinner = (By.CSS_SELECTOR, 'img[alt="spinner"]')
        self.internetPlan = (By.XPATH, "//p[contains(text(),'NEXT')]")
        self.addressBarLocator = (By.XPATH, "//input[@placeholder='Enter Address']")
        self.checkAvailability = (By.XPATH, "//button[text()='Check Availability']")
        self.radiobutton = "//label[text()='%s']"
        self.notInterested = (By.XPATH, "//p[text()='NOT INTERESTED']")
        self.selectInternetPlan = "//p[contains(text(),'%s')]/parent::div/following-sibling::div[2]/button"
        self.currentSelectedPlanPrice = (By.XPATH, '//button[contains(@class,"notice bg-notice")]/following-sibling::div/p')
        self.cartTotal = (By.XPATH, "//h4[text()='Cart']/following::p[2]")
        self.addressFromOptions = "//p[text() = '%s']"
        self.monthFree = (By.XPATH,"//span[text()='1']/ancestor::div[contains(@class,'mx-auto')]/following-sibling::div/div[contains(@class,'bg-notice')]")
        self.serviceProtectionCost = (By.XPATH, "//p[text()='SERVICE PROTECTION PLAN']/following::p[text()='per month']/preceding-sibling::p")
        self.yearDOB = (By.XPATH, "//input[@id='year']")
        self.dayDOB = (By.XPATH, "//input[@id='day']")
        self.monthDOB = (By.XPATH, "//input[@id='month']")
        self.termsAndConditions = (By.CSS_SELECTOR, "input[type='checkbox']")
        self.scheduleInstallationTitle = (By.XPATH, "//h1[text()='Schedule Installation']")
        self.contactInfoDialog = (By.XPATH, '//h3[text()="Enter Your Contact Information"]')
        self.emailID = (By.XPATH, "//label[text()='Email*']/preceding-sibling::input")
        self.phoneNumber = (By.XPATH, "//label[text()='Phone Number *']/preceding-sibling::input")
        self.lastName = (By.XPATH, "//label[text()='Last Name*']/preceding-sibling::input")
        self.firstName = (By.XPATH, "//label[text()='First Name*']/preceding-sibling::input")
        self.placeOrderBtn = (By.CSS_SELECTOR, "#cart-continue")
        self.disabledPlaceOrderBtn = (By.CSS_SELECTOR, "#cart-continue[disabled]")
        self.orderSummary = (By.XPATH, "//p[text()='Order Summary']")
        self.monthlyTotal = (By.XPATH, "(//p[text()='Monthly Total']/following-sibling::p)[1]")
        self.monthlyCost = (By.XPATH, "(//p[text()='Monthly Total']/following-sibling::p)[3]")
        self.protectionCost = (By.XPATH, "(//p[text()='Monthly Total']/following-sibling::p)[5]")
        self.oneTimeInstallationCost = (By.XPATH, "(//p[text()='One Time Charges']/following-sibling::p)[1]")
        self.promoCost = (By.XPATH, "(//p[contains(text(), 'Free Install')]/following-sibling::p)[1]")
        self.dueAtInstall = (By.XPATH, "(//p[text()='Due at Install']/following-sibling::p)[1]")
        self.loader = (By.CSS_SELECTOR, 'img[loading="lazy"]')
        self.contactAM = (By.CSS_SELECTOR, 'input[name="contactAm"]')
        self.contactPM = (By.CSS_SELECTOR, 'input[name="contactPm"]')
        self.contactAfter5PM = (By.CSS_SELECTOR, 'input[name="contactAfter5Pm"]')
        self.contactMe = (By.CSS_SELECTOR, 'input[name="contactMe"]')
        self.noPlanDialog = (By.XPATH, '//p[text()="We’re Sorry!"]')
        self.showVoipPlan = (By.XPATH, '//button[text()="SHOW ME VOICE OPTIONS"]')
        self.voipInstallationCost = (By.XPATH, "//p[text()='VoIP Only Install']/following::p[1]")
        self.disableContinueBtn = (By.CSS_SELECTOR, "button[aria-labelledby='cart-continue'][disabled]")
        self.voipOneTimeInstallationCost = (By.XPATH, "(//p[text()='ONE TIME CHARGE']/following-sibling::p)[1]")
        self.submitBtn = (By.XPATH, '//button[text()="SUBMIT"]')
        #customize plan
        self.cartRouterPrice = (By.XPATH, "(//p[contains(text(),'Router')]/following::p[1])[2]")
        self.addButton = (By.CSS_SELECTOR, 'button[aria-label="Add Button"]')
        self.wifiExtender = (By.CSS_SELECTOR, 'select[title="Quantity"]')
        self.wifiExtenderOption = "//select[@title='Quantity']/option[@value='%s']"
        self.wifiExtenderCartPrice = "//p[text()='%s']/following::p[1]"
        self.hyperLink = "//p[contains(text(),'%s')]/../.. //a[@href='#']"
        self.cartRouterPriceForSelectPage = (By.XPATH, "//p[contains(text(),'Router')]/following::p[1]")
        #Hyperlink Modal
        self.hyperlinkModal = (By.CSS_SELECTOR, '[role="dialog"] [data-headlessui-state="open"]')
        self.dialogHeading = (By.CSS_SELECTOR, '[role="dialog"] .text-left.font-bold')
        self.closeButton = (By.CSS_SELECTOR, '[role="dialog"] button')
