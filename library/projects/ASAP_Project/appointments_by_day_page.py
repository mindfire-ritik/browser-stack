from selenium.webdriver.common.by import By


class LocatorsAppointmentsByDayPage(object):
    def __init__(self, context=None):
        self.appointments_by_day = (By.XPATH, "//span[normalize-space()='Appointments By Day']")
        self.appointment_by_day_table  = (By.XPATH, "//div[contains(@class,'mt-16')]")
        self.all_btn = (By.XPATH, "//button[normalize-space()='All']")
        self.fiber_btn = (By.XPATH, "//button[normalize-space()='Fiber']")
        self.fiber_bury_btn = (By.XPATH, "//button[normalize-space()='Fiber Bury']")
        self.contractor_btn = (By.XPATH, "//button[normalize-space()='Contractor']")
        self.los_btn = (By.XPATH, "//button[normalize-space()='LOS']")
        self.zone_dropdown = (By.XPATH, "//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputSizeSmall')]")
        self.zoneDropdownOption = (By.XPATH, "//li[contains(text(),'TX-1')]")
        self.tx_option = (By.XPATH, "(//div[@id='panel1a-header'])[5]")
        self.table = (By.CSS_SELECTOR, "[aria-expanded='true']+div tr>th+td:nth-of-type(1)")
        self.technician = (By.XPATH, "//table[@aria-label='purchases']")
        self.edit_proposed_tech = (By.XPATH, "//tr[@class='MuiTableRow-root css-1eg2zxr']//img[@alt='edit']")
        self.edit_technician_dialog_box = (By.XPATH, "//div[@role='dialog']")
        self.editproposed_tech = (By.XPATH, "//h2[normalize-space()='Edit Proposed Technician(s)']")
        self.proposed_techs = (By.XPATH, "//div[@class='grid grid-cols-2 mb-1']")
        self.select_proposed_tech = (By.XPATH, "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input MuiInputBase')])[2]")
        self.proposed_name = (By.XPATH, "//li[@role='option']")
        self.proposed_two_tech = (By.XPATH, "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input MuiInputBase')])[3]")
        self.cancel_btn = (By.XPATH, "//button[normalize-space()='Cancel']")
        self.update_btn = (By.XPATH, "//button[normalize-space()='Update']")
        self.zone_table = (By.XPATH, "(//table[@aria-label='collapsible table'])[5]")
        self.toast_mssgs = (By.XPATH, "//div[contains(text(),'Proposed technician updated successfully')]")
        self.confirm_dialog_box = (By.XPATH, "//div[@aria-describedby='alert-dialog-slide-description']")
        self.yes_button = (By.XPATH, "//button[normalize-space()='Yes']")