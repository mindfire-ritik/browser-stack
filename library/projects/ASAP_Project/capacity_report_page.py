from selenium.webdriver.common.by import By


class LocatorsCapacityReportPage(object):
    def __init__(self, context=None):
        self.capacity_report = (By.XPATH, "//span[normalize-space()='Capacity Report']")
        self.capacity_report_table = (By.CSS_SELECTOR, "div[class='MuiTableContainer-root max-h-[calc(100vh-9rem)] css-kge0eu']")
        self.download_csv = (By.XPATH, "//button[@aria-label='Download csv']")
        self.start_date_btn = (By.XPATH, "(//div[contains(@class,'MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary')])[1]")
        self.end_date_btn = (By.XPATH, "(//div[contains(@class,'MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary')])[2]")
        self.reset_btn = (By.XPATH, "//button[normalize-space()='Reset']")
        self.start_date_batch = (By.XPATH, "//label[normalize-space()='Start Date']")
        self.end_date_batch = (By.XPATH, "//label[normalize-space()='End Date']")