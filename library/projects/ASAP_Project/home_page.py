from selenium.webdriver.common.by import By


class LocatorsHomePage(object):
    def __init__(self, context=None):
        # HomePage Background
        self.home = (By.XPATH, '//p[text()="Home"]')
        self.login_button = (By.CSS_SELECTOR, "button[type='button']")
        self.next_button = (By.CSS_SELECTOR, "#idSubmit_ProofUp_Redirect")
        self.skip_button = (By.CSS_SELECTOR, 'button + a[role="link"]')
        self.userName = (By.CSS_SELECTOR, "input[type='email']")
        self.nextBtn = (By.XPATH, "//input[@type=\"submit\"]")
        self.passwd = (By.CSS_SELECTOR, "input[type='password']")
        self.submitBtn = (By.CSS_SELECTOR, "[data-report-event=\"Signin_Submit\"]")
        self.signedinText = (By.CSS_SELECTOR, "div[class='row text-title']")
        self.noBtn = (By.CSS_SELECTOR, "input[id*=\"Back\"]")
        self.header = (By.XPATH, "//div[contains(@class,'MuiToolbar-root MuiToolbar-gutters MuiToolbar-regular')]")
        self.error = (By.XPATH, "/html/body/div/div/div[2]/main/div/div")


        # HomePage Smoke test
        self.logo_button = (By.CSS_SELECTOR, "img[alt='Logo']")
        self.holiday_ASAP_Help = (By.XPATH, '//div[contains(@class,"bg-background text-primary rounded-2xl w-full")]')
        self.support_request = (By.XPATH, '//button[normalize-space()="Create Support Request"]')
        self.pinned_pages = (By.XPATH, '//div[contains(@class,"text-primary rounded-2xl w-full  md:w-3/5")]')
        self.techs_call = (By.XPATH, '//button[normalize-space()="On Call Techs"]')
        self.employee_data_logs = (By.XPATH, '//div[@role="alert"]')
        self.hamburger_button = (By.XPATH, '//button[@aria-label="menu"]')
        self.hamburger_menulist = (By.CSS_SELECTOR, "[role='presentation']>ul")
        self.appointments_menulist = (By.XPATH, "//span[normalize-space()='Appointments']")
        self.all_appointment_page_btn = (By.XPATH, "//span[text()='All Appointments']")
        self.all_appointment_page_table = (By.XPATH, "//table[contains(@class,'MuiTable-root MuiTable-stickyHeader')]")
        self.toggle_btn = (By.XPATH, "//div[@class='relative']//div[2]")
        self.toggle_dark_theme = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium h-5 "
                                            "w-5 css-vubbuv'])[2]")
        self.toggle_light_theme = (By.XPATH, "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium "
                                             "h-5 w-5 css-vubbuv'])[1]")
        self.schedule_appointment_page_btn = (By.XPATH, "//span[text()='Scheduled/Routed Appointments']")
        self.schedule_appointment_page_table = (By.XPATH, "//table[contains(@class,'MuiTable-root MuiTable-stickyHeader')]")
        self.sooner_date_requested_page_btn = (By.XPATH, "//span[normalize-space()='Sooner Date Requested']")
        self.sooner_date_requested_page_table = (By.XPATH, "//table[contains(@class,'MuiTable-root MuiTable-stickyHeader')]")
        self.sooner_date_requested_pinned_btn = (By.XPATH, "//button[@aria-label='Pin Page']")
        self.pinned_sooner_Requested_Page_on_homePage = (By.XPATH, "(//div[contains(@class,'MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation1')])[6]")
        self.no_pinned_pages = (By.XPATH, "//span[contains(@class,'MuiTypography-root MuiTypography-caption "
                                          "MuiTypography-alignCenter items-center flex')]")
        self.appointment_creation_link = (By.XPATH, "//span[normalize-space()='Appointment Creation']")
        self.batching_routing_link = (By.XPATH, "//span[normalize-space()='Batch Routing']")
        self.technicians_link = (By.XPATH, "//span[normalize-space()='Technicians']")
        self.zone_views_Link = (By.XPATH, "//span[normalize-space()='Zone Views']")
        self.faq_link = (By.XPATH, "//span[normalize-space()='FAQs']")
        self.home_page = (By.XPATH, '//p[text()="Home"]')
        self.create_request_support_page = (By.XPATH, "//form[@class='mt-2']")
        self.on_calls_techs_btn = (By.XPATH, "//button[normalize-space()='On Call Techs']")
        self.on_calls_techs_page = (By.XPATH, "//div[@class='mt-16 ']")
        self.employee_data = (By.XPATH, "//div[@role='alert']")
        self.refresh_employee_data = (By.XPATH, "//button[normalize-space()='Refresh Employee Data']")
        self.logs_btn = (By.XPATH, "//button[normalize-space()='Logs']")
        self.logs_dialog_box = (By.CSS_SELECTOR, "div[role='dialog']")
        self.log_close_btn = (By.XPATH, "//button[contains(@class,'MuiButtonBase-root MuiIconButton-root "
                                        "MuiIconButton-sizeMedium')]")
        self.employee_recheck_btn = (By.XPATH, "//button[normalize-space()='Recheck']")
        self.refresh_roles = (By.XPATH, "//button[normalize-space()='Refresh Roles']")
        self.refresh_roles_toast_message = (By.XPATH, "//div[contains(text(),'Role refreshed successfully.')]")

        self.nextPage = (By.XPATH, '//button[@aria-label="Go to next page"]')
        self.inProgressCeck = (By.XPATH, "//div[text()='In Progress...']")
        self.paginationArrow = (By.XPATH, '//p[text()="Rows per page:"]/following-sibling::div/*[@data-testid="ArrowDropDownIcon"]')
        self.pagination = "//li[text()='%s']"
        self.currentPagination = (By.XPATH, '//p[text()="Rows per page:"]/following-sibling::div/div')
        self.currentTotalRows = (By.XPATH, '//tbody/tr')
        self.totalRows = (By.XPATH, "//p[contains(text(), 'of')]")






