from selenium.webdriver.common.by import By


class NetworkLocators(object):
    def __init__(self, context=None):
        self.network_btn_menu = (By.XPATH, "//a[normalize-space()='Network']")
        self.cnctd_ntwrk_hdng = (By.XPATH, "//div[normalize-space()='Connected to your Network']")
        self.wifi_hdng = (By.XPATH, "//div[normalize-space()='Wi-Fi Details']")
        self.advnce_sttngs = (By.XPATH, "//div[contains(text(),'Advanced Settings')]")
        self.wifi = (By.XPATH, "//div[normalize-space()='Zyxel_2.4 (2.4GHz)']")
        self.edit_wifi = (By.XPATH, "//div[normalize-space()='Edit Wi-Fi']")
        self.wifi_name = (By.XPATH, "//input[@id='ssid']")
        self.network_type = (By.CSS_SELECTOR, "label[for='networkType']")
        self.password = (By.CSS_SELECTOR, "label[for='passphrase']")
        self.security_type = (By.CSS_SELECTOR, "label[for='securityType']")
        self.hide_ssd = (By.CSS_SELECTOR, "input[name='hideSsid']")
        self.auto_channel = (By.XPATH, "//input[@name='autoChannel']")
        self.ntwork_value = (By.XPATH, "//span[normalize-space()='wifi_24G']")
        self.name_value = (By.CSS_SELECTOR, "input[value='Zyxel_2.4']")
        self.pass_value = (By.CSS_SELECTOR, "input[value='112222288']")
        self.sec_value = (By.XPATH, "//span[normalize-space()='WPA2']")
        self.wifi_updt_cnf = (By.XPATH, "//div[@class='text-sm text-dark-black dark:text-white tracking-wider']")
        self.close_modal = (By.CSS_SELECTOR, "button[aria-label='close-modal']")
        self.save_wifi = (By.CSS_SELECTOR, " button[aria-label='ssid-edit']")
        self.edited_wifi = (By.XPATH, "//div[normalize-space()='WifiEdited (2.4GHz)']")
        #Router
        self.router = (By.XPATH, "//div[normalize-space()='Online']")
        self.rbt_rtr = (By.CSS_SELECTOR, "button[aria-label='reboot-device']")
        self.speed_test = (By.XPATH, "//div[contains(text(),'Speed Test')]")
        self.cnnctd_dvc = (By.XPATH, "//div[contains(text(),'Connected Devices')]")
        self.rtr_dtls = (By.XPATH, "//div[contains(text(),'Router Details')]")
        self.cncl = (By.XPATH, " //button[normalize-space()='Cancel']")
        self.cncl_speed = (By.XPATH, "//button[@aria-label='cancel-speed']")
        self.test_cmpltd = \
            (By.XPATH, "(//div[@class='flex-1 w-full flex justify-start text-[20px] font-bold text-dark-black dark:text-white'])[1]")
        self.rtr_dtls_modal = \
            (By.XPATH, "(//div[@class='w-full text-[20px] text-black dark:text-white font-semibold tracking-widest'])[1]")
        self.animated_loading = (By.XPATH, "//img[@alt='animated-gif']")
        self.rbt_cmpltd =\
            (By.CSS_SELECTOR, "div[class='flex-1 justify-start text-[20px] font-bold text-dark-black dark:text-white']")
        #Advance settings
        self.set_up_port = (By.XPATH, "//div[normalize-space()='Set Up Port Forwarding']")
        self.dmz = (By.XPATH, "//div[normalize-space()='DMZ']")
        self.wan = (By.XPATH, "//div[normalize-space()='WAN Settings']")
        self.lan = (By.XPATH, "//div[normalize-space()='LAN Settings']")
        self.dns = (By.XPATH, "//div[normalize-space()='DNS Settings']")
        self.back_btn = (By.XPATH, "//button[@aria-label='back-button']//*[name()='svg']")












