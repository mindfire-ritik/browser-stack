from selenium.webdriver.common.by import By


class LocatorsHomePage(object):
    def __init__(self, context=None):
        # Login functionality
        self.signIn = (By.XPATH, "//div[text()='Sign In']")
        self.emailInput = (By.CSS_SELECTOR, "input#email")
        self.emailLabel = (By.CSS_SELECTOR, "label[for='email']")
        self.passwordInput = (By.CSS_SELECTOR, "input#password")
        self.invalidEmailMessage = (By.XPATH, "//span[text()='Invalid Email Address']")
        self.incorrectPasswordMessage = (By.CSS_SELECTOR, "div>svg+span")
        self.signInBtn = (By.CSS_SELECTOR, "button[type='submit']")
        self.unregisterEmailMessage = (By.CSS_SELECTOR, "div>svg+span")
        self.loader = (By.CSS_SELECTOR, 'img[alt="animated-gif"]')
        self.successfullyLogInToast = (By.XPATH, "//div[text()='Successfully logged In']")
        self.homeBtn = (By.CSS_SELECTOR, 'a[href = "/home"]')


        # Forget Password functionality
        self.forgetPasswordBtn = (By.CSS_SELECTOR, "a[href*='forgot-password']")
        self.resetPasswordText = (By.XPATH, "//div[text()='Reset your Password']")
        self.continueBtn = (By.XPATH, "//button[text()='Continue']")
        self.successfullyCodeSentMsg = (By.XPATH, "//span[text()='Code resent successfully.']")
        self.resetPasswordBtn = (By.XPATH, "//button[text()='Reset Password']")
        self.resetCode = (By.CSS_SELECTOR, 'input[name="resetCode"]')
        self.sendNewCodeBtn = (By.XPATH, "//span[text()='Send a new code']")
        self.resetPageSignInBtn = (By.CSS_SELECTOR, 'a[href="/"]')
        self.quickLink = (By.XPATH, "//div[text()='Quick Links']")
        self.option = "//a[text()='%s']"
        self.pageHeading = "//div[text()='%s']"
        self.logout = (By.XPATH, "//p[text()='Logout']")
        self.switch = (By.CSS_SELECTOR, "button[role='switch']")
        self.light = (By.CSS_SELECTOR, "button[class*='light.png']")
        self.dark = (By.CSS_SELECTOR, "button[class*='dark.png']")
        self.logoutToast = (By.XPATH, "//div[text()='Successfully logged out']")
        self.online_network_status = (By.XPATH, "//div[text()='Your network is online']")
        self.offline_network_status = (By.XPATH, "//div[text()='Your network is offline']")
        self.alert_message = (By.XPATH, "//div[@role='alert']")
        self.login_page = (By.XPATH, "//div[contains(@class,'flex flex-col space-y-6 p-6 w-auto md:w-[480px] bg-white')]")
        self.google_signIn = (By.XPATH, "//span[contains(@class,'flex items-center justify-center float-right w-10 h-10 p-2 text-sm')]")
        self.enter_email = (By.XPATH, "//input[@type='email']")
        self.next_btn = (By.XPATH, "//button[contains(@class,'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf')]")
        self.pwd = (By.XPATH, "//input[@type='password']")
        self.manage_billing_quicklinks = (By.XPATH, "//div[contains(text(),'Manage Billing')]")
        self.share_wifi_quicklinks = (By.XPATH, "//div[text()='Share Wi-Fi']")
        self.devices_quicklinks = (By.XPATH, "//div[text()='Devices']")
        self.billing_page = (By.XPATH, "//div[@class='xl:w-[864px] w-full flex flex-col space-y-6']")
        self.billing_back_btn = (By.XPATH, "//button[@aria-label='back-button']")
        self.share_wifi_model = (By.XPATH, "//div[@id='headlessui-dialog-panel-:r2:']")
        self.share_wifi_close_model = (By.XPATH, "//button[@aria-label='close-modal']")
        self.devices_page_list = (By.XPATH, "//div[@class='flex flex-col space-y-5']")
        self.loginfail_toast = (By.XPATH, "//div[@class='Toastify__toast-body']")
        self.autopay = (By.XPATH, "//div[contains(text(),'Autopay scheduled')]")
        self.acct_suspended = (By.XPATH, "//div[text()='Account Suspended']")
        self.overdue = (By.XPATH, "//div[contains(text(), 'days overdue')]")
        self.upcoming_bill = (By.XPATH, "//div[contains(text(), 'Upcoming bill on')]")
        self.suspended_failed_attempt = (By.XPATH, "//div[contains(text(),'There’s a problem processing your payment. Please review the payment')]")
        self.apple_store = (By.XPATH, "//a[@aria-label='apple-store-link']")
        self.google_play_store = (By.XPATH, "//a[@aria-label='google-store-link']")

        # View Invoive Testcase
        self.viewInvoice = (By.XPATH, "//div[text()='view invoice']")
        self.invoiceCloseBtn = (By.CSS_SELECTOR, 'div[class*="outline-gold"]')
        self.downloadInvoice = (By.CSS_SELECTOR, 'svg[class*="outline-gold"]')
        self.invoicePopup = (By.XPATH, "//div[@data-headlessui-state='open'] //div[text()='Invoice']")

        # billing testcases
        self.manage_billing_btn = (By.XPATH, "//span[normalize-space()='Manage Billing']")
        self.edit_payment_method_btn = (By.XPATH, "//button[@aria-label='edit-payment']")
        self.payment_Dialog_box = (By.XPATH, "//div[contains(@class,'flex flex-col space-y-4 tracking-widest text-black')]")
        self.cancel_btn = (By.XPATH, "//button[normalize-space()='Cancel']")
        self.make_payment_btn = (By.XPATH, "//button[normalize-space()='Make a Payment']")
        self.statement_block = (By.CSS_SELECTOR,"main:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)")
        self.statement_history_btn = (By.XPATH, "//div[text()='Statement History']")
        self.statement_history_dialog_box = (By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)")
        self.latest_year = (By.XPATH, "//div[contains(@class,'flex flex-row place-items-center w-full')]")
        self.latest_month_list = (By.XPATH, "//div[@id='headlessui-disclosure-panel-:ra:']")
        self.latest_month = (By.XPATH, "(//div[contains(@class,'flex flex-row py-2 cursor-pointer place-items-center')])[1]")
        self.monthly_bill = (By.XPATH, "//div[@class='table_scrollbar___LLMg table_scrollbar-primary__vnv4W overflow-auto flex flex-col']")
        self.bill_download_btn = (By.XPATH, "//div[@class='w-full items-start justify-start cursor-default']//*[name()='svg']")
        self.bill_close_btn = (By.XPATH, "//div[@class='flex flex-row cursor-default']//div[@class='cursor-pointer outline-gold']")
        self.statement_history_close_btn = (By.XPATH, "//div[@class='cursor-pointer outline-gold']")
        self.recentpayment = (By.XPATH, "//div[normalize-space()='Recent Payments']")
        self.payment_list = (By.XPATH, "//div[contains(@class,'flex flex-col w-full border-t border-light-gray dark:border-dark-silver')]")
        self.balance_billing = (By.XPATH, "//div[@class='flex-1 text-xl text-left']")
        self.balance = (By.XPATH, "//div[@class='text-xl']")
        self.show_more_btn = (By.XPATH, "//div[contains(text(),'Show More')]")
        self.balance_heading = (By.XPATH, "(//div[@class='font-medium text-[20px] text-center'])[1]")

        # Device Page
        self.devices_btn = (By.XPATH, "//a[normalize-space()='Devices']")
        self.device_page = (By.XPATH, "//div[@class='flex flex-col space-y-5']")
        self.connected_devices = (By.XPATH, "//div[text()='Connected to your Wi-Fi ']")
        self.disconnected_devices = (By.XPATH, "//div[text()='Disconnected ']")
        self.blocked_devices = (By.XPATH, "//div[text()='Blocked ']")
        self.disconnected_devices_list = (By.XPATH, "(//div[@class='flex flex-row space-x-8 place-items-center p-4 cursor-pointer sm:px-6'])[1]")
        self.device_details_page = (By.XPATH, "//div[@class='flex flex-col space-y-4']")

        #Header and footer
        self.support = (By.XPATH, "//div[text()='Support']")
        self.nextlinkLogo = (By.CSS_SELECTOR, "svg[tabindex='0']")
        self.footer = (By.CSS_SELECTOR, "footer>p")
        self.supportModal = (By.CSS_SELECTOR, "div[id*='headlessui-dialog-panel']")
        self.faq = (By.CSS_SELECTOR, "a[href*='/support-center']")
        self.faqPageHeading = (By.XPATH, "//h3[text()='Internet Service FAQs']")
        self.contactUs = (By.CSS_SELECTOR, "a[href*='/support-center/contact-us']")
        self.contactPageHeading = (By.XPATH, "//h1[text()='CONTACT NEXTLINK']")
        self.serviceTicket = (By.CSS_SELECTOR, "a[href*='/support-center/report-trouble']")
        self.reportTroublePageHeading = (By.XPATH, "//h1[text()='Report a service issue']")
        self.outage = (By.CSS_SELECTOR, "a[href*='/support-center/network-status']")
        self.billingPageHeading = (By.XPATH, "//h1[text()='OPEN A BILLING TICKET']")
        self.billingTicket = (By.CSS_SELECTOR, "a[href*='open-a-billing-ticket/']")
        self.networkStatusPageHeading = (By.XPATH, "//h1[text()='network status']")
        self.supportChatButton = (By.CSS_SELECTOR, 'button[aria-label="reboot-device"]')
        self.supportMessageModal = (By.CSS_SELECTOR, 'div[aria-label="messages"]')
        self.supportModalIframe = (By.CSS_SELECTOR, 'iframe[allow="picture-in-picture"]')





