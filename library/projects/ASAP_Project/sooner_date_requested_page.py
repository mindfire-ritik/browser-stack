from selenium.webdriver.common.by import By


class LocatorsSoonerDateRequestedPage(object):
    def __init__(self, context=None):
        self.sooner_date_requested_page_table = (By.XPATH, "//table[contains(@class,'MuiTable-root MuiTable-stickyHeader')]")
        self.work_type_btn = (By.XPATH, "(//*[contains(text(),'Work Type')])[1]")
        self.account_number_btn = (By.XPATH, "//div[normalize-space()='Account#']")
        self.appointment_details = (By.CSS_SELECTOR,
                                    "div:nth-child(1) > main:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2)")
        self.account_type_btn = (By.XPATH, "(//div[@id='demo-multiple-checkbox'])[2]")
        self.zone_status_btn = (By.XPATH, "(//div[@id='demo-multiple-checkbox'])[3]")
        self.appointment_date_dropdown_btn = (By.XPATH, "//div[@id='panel1a-header']")
        self.end_date = (By.XPATH, "(//input[@id='outlined-basic'])[2]")
        self.scheduled_checkbox = (By.XPATH, "(//span[contains(text(),'Scheduled')])[3]")
        self.billmax_number_btn = (By.XPATH, "//div[normalize-space()='Billmax ID']")
