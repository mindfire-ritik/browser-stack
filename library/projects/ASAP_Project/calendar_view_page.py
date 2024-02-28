from selenium.webdriver.common.by import By


class LocatorsCalendarViewPage(object):
    def __init__(self, context=None):
        #Calender View Home
        self.dateTab = (By.XPATH, "//div[@class='flex items-center']//p")
        self.zoneDropdownOption = (By.XPATH, "//li[contains(text(),'IA-')]")
        self.zoneDropdown = (By.XPATH, "//input[@placeholder='Select Zone(s)']")
        self.calendar_view = (By.XPATH, "//span[normalize-space()='Calendar View']")
        self.calendar_title = (By.XPATH, "// p[text() = 'Calendar']")
        self.previousButton = (By.XPATH, "//div[@class='flex items-center']//button[1]")
        self.nextButton = (By.XPATH, "//div[@class='flex items-center']//button[2]")
        self.dayButton = (By.CSS_SELECTOR, "button[value='day']")
        self.weekButton = (By.CSS_SELECTOR, "[value='week']")
        self.month = (By.CSS_SELECTOR, "[value='month']")