from selenium.webdriver.common.by import By


class DeviceLocators(object):
    def __init__(self, context=None):
        self.click_device = (By.XPATH, "//div[normalize-space()='MSI']")
        self.device_name = \
            (By.XPATH, "(//div[normalize-space()='MSI'])[1]")
        self.dvc_dtl_btn = (By.XPATH, "//button[@aria-label='back-button']//*[name()='svg']")
        self.device_type = (By.XPATH, "//div[normalize-space()='Other']")
        self.block_btn = (By.XPATH, "//button[normalize-space()='Block']")
        self.pause_btn = (By.XPATH, "//button[normalize-space()='Pause']")
        self.unblock_btn = (By.XPATH, "//button[normalize-space()='Unblock']")
        self.unpause_btn = (By.XPATH, "//button[normalize-space()='Unpause']")
        self.edt_dvc = (By.XPATH, "//div[contains(text(),'Edit Device')]")
        self.trblsht_dvc = (By.XPATH, "//div[contains(text(),'Troubleshoot Device')]")
        self.hstname = (By.XPATH, "//div[normalize-space()='N/A']")
        self.connectiontype = (By.XPATH, "//div[normalize-space()='Wireless']")
        self.ipaddress = (By.XPATH, "//div[normalize-space()='192.168.18.13']")
        self.mcaddress = (By.XPATH, "//div[normalize-space()='40:ec:99:a9:62:17']")
        self.data_usage = (By.XPATH, "//div[@role='region']//*[name()='svg']")
        self.download = (By.XPATH, " //span[normalize-space()='Download']")
        self.uploads = (By.XPATH, " //span[normalize-space()='Uploads']")
        self.devices_heading = (By.XPATH, "//div[normalize-space()='Devices']")
        self.edit_device_modal = (By.XPATH, "(//div[contains(text(),'Edit Device')])[2]")
        self.device_name_input = (By.XPATH, "//input[@id='deviceName']")
        self.dvc_type_drdown = (By.XPATH, "//button[@aria-label='select dropdown']")
        self.cmptr_drpdown = (By.XPATH, "(//li[@role='option'])[2]")
        self.othr_drpdown = (By.XPATH, "//div[@role='dialog']//li[1]")
        self.save_btn = (By.XPATH, "//button[normalize-space()='Save']")
        self.dvc_update_conf =(By.XPATH, "//div[contains(text(),'Your changes were successful, please note it may t')]")
        self.conf_close_btn = (By.XPATH, "//button[normalize-space()='Close']")
        self.dvc_edited = (By.XPATH, "(//div[contains(text(),'DeviceEdited')])[2]")
        self.dvc_type_edited = (By.XPATH, "(//div[normalize-space()='Computer'])[1]")
        self.trblsht_dvc_page = (By.XPATH, "//p[contains(text(),'Try moving your device closer to the router in you')]")
        self.opn_srvc_tckt = (By.XPATH, "//a[normalize-space()='Open a service ticket here']")
        self.bck_btn = (By.XPATH, " //button[@aria-label='back-button']//*[name()='svg']")






