from selenium.webdriver.common.by import By


class LocatorsScheduleAppointmentPage(object):
    def __init__(self, context=None):
        self.schedule_appointment_page_table = (By.XPATH, "//table[contains(@class,'MuiTable-root MuiTable-stickyHeader')]")
        self.date_btn = (By.XPATH, "(//*[contains(text(),'Date')])[1]")
        self.type_btn = (By.XPATH, "(//*[contains(text(),'Work Type')])[1]")
        self.user_btn = (By.XPATH, "(//*[contains(text(),'User')])[1]")
        self.filter_btn = (By.CSS_SELECTOR, 'button[aria-label="Filter"]')
        self.scheduled_checkbox = (By.XPATH, "(//td[text()='Scheduled'])[5]")

