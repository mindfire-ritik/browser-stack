from selenium.webdriver.common.by import By


class AccountLocators(object):
    def __init__(self, context=None):
        self.address = (By.XPATH, "//div[contains(text(),'95 Parker Oaks Ln Weatherford')]")
        self.phone = (By.XPATH, "//div[contains(text(),'(201) 222-4413')]")
        self.email = (By.XPATH, "//div[contains(text(),'wlimjr-c@team.nxlink.com')]")
        self.edit_contact = (By.XPATH, "//span[normalize-space()='edit contact']")
        self.nextlink_account_number = (By.XPATH, "//span[normalize-space()='5055']")
        self.vw_acnt_actvty = (By.XPATH, "//div[contains(text(),'View Account Activity')]")
        self.self_srvce = (By.XPATH, "//div[contains(text(),'Service Details')]")
        self.balance = (By.XPATH, "//div[normalize-space()='Balance']")
        self.manage_billing = (By.XPATH, "//div[contains(text(),'Manage Billing')]")
        self.athrzd_usrs = (By.XPATH, "//div[normalize-space()='Authorized Users']")
        self.add_athrzd_usrs = (By.XPATH, "//div[contains(text(),'Add Authorized User')]")
        self.vw_usrs = (By.XPATH, "//div[contains(text(),'View Users')]")
        self.settings = (By.XPATH, "//div[normalize-space()='Settings']")
        self.manage_pin = (By.XPATH, "//div[contains(text(),'Manage PIN')]")
        self.notification = (By.XPATH, "//div[contains(text(),'Notifications')]")
        # Edit Contact
        self.common_modal = \
            (By.XPATH, "(//div[@class='w-full text-[20px] text-dark-black dark:text-white font-medium'])[1]")
        self.phone_number_input = (By.XPATH, "//input[@id='phoneNumber']")
        self.email_input = (By.XPATH, " //input[@id='emailAddress']")
        self.save_edit = (By.XPATH, "//button[normalize-space()='Save']")
        self.cancel_edit = (By.XPATH, "//button[normalize-space()='Cancel']")
        self.changes_svd = (By.XPATH,
                            "(//div[@class='flex-1 justify-start text-[20px] font-bold text-dark-black "
                            "dark:text-white'])[1]")
        self.clse_btn = (By.XPATH, "//button[normalize-space()='Close']")
        # Service Details
        self.edited_phone = (By.XPATH, "//div[contains(text(),'(222) 222-2222')]")
        self.srv_dtls1 = (By.XPATH, "(//div[contains(@class,'w-full text-sm text-left whitespace-normal')])[1]")
        self.srv_dtls2 = (By.XPATH, "(//div[contains(@class,'w-full text-sm text-left whitespace-normal')])[2]")
        self.pckg = (By.XPATH, "//div[normalize-space()='NEXT50']")
        self.eqpmtn = (By.XPATH, "//div[normalize-space()='Router']")
        self.service_modal = \
            (By.XPATH, "(//div[contains(@class,'flex-1 text-[20px] text-dark-black dark:text-white font-medium')])[1]")
        # Add Users
        self.firstname_fld = (By.ID, "firstName")
        self.lastname_fld = (By.ID, "lastName")
        self.phone_fld = (By.ID, "dayPhoneNumber")
        self.email_fld = (By.ID, "emailAddress")
        self.add_prmssns_btn = (By.XPATH, "//span[normalize-space()='add permissions']")
        self.sve_users_btn = (By.XPATH, "//button[normalize-space()='Save User']")
        self.manage_account_perm = (By.ID, "Manage Account0")
        self.manage_users_perm = (By.ID, "Manage Users2")
        self.manage_billing_perm = (By.ID, "Manage Billing1")
        self.save_perm_btn = (By.XPATH, "//button[normalize-space()='Save']")
        self.permission_conf_modal = \
            (By.CSS_SELECTOR, "div[class='w-full text-[20px] text-black dark:text-white tracking-wider font-medium']")
        self.cntinue_prm_conf = (By.XPATH, "//button[normalize-space()='Continue']")
        self.permission_text =(By.XPATH, "//div[@class='text-base']")
        self.changes_svd = \
            (By.CSS_SELECTOR, "div[class='flex-1 justify-start text-[20px] font-bold text-dark-black dark:text-white']")
        self.changes_svd_close = (By.XPATH, "//button[normalize-space()='Close']")
        self.user_added_conf = (By.XPATH, "//div[contains(text(),'QA Test')]")
        self.act_address = (By.XPATH, "(//div[@class='flex flex-1 w-full'])[4]")
        self.act_phone = (By.XPATH, "(//div[@class='flex flex-1 w-full'])[5]")
        self.act_email = (By.XPATH, "//div[contains(text(),'qatest')]")
        self.remove = (By.XPATH, "//span[contains(text(),'remove')]")
        self.edit_user = (By.XPATH, "//span[normalize-space()='edit user']")
        self.x_btn = (By.XPATH, "//div[@class='cursor-pointer']//*[name()='svg']")
        self.recent_actity_manage_user_btn =\
            (By.XPATH, "//div[@class='flex flex-col space-y-2 tracking-wider']//div[1]//div[3]//span[1]")
        self.new_qa_test_added = (By.XPATH, "//div[normalize-space()='A new user QA Test was added.']")
        self.service_location_section = \
            (By.XPATH, "(//div[@class='text-[14px] text-black dark:text-white tracking-widest'])[1]")
         # Edit User
        self.edit_user_btn = (By.XPATH, "//span[normalize-space()='edit user']")
        self.edited_user = (By.XPATH, "//div[contains(text(),'QAedited Testedited')]")
        self.edited_phne = (By.XPATH, "//div[contains(text(),'(111) 111-1111')]")
        # Delete user
        self.remove_btn = (By.XPATH, "//span[contains(text(),'remove')]")
        self.user_delete_conf = \
            (By.XPATH, "(//div[contains(@class,'w-full text-[20px] text-black dark:text-white font-semibold')])[1]")
        self.user_info_to_delete = (By.XPATH, "//div[@class='text-dark-gray dark:text-white font-medium']")
        self.delete_user_btn = (By.XPATH, "//button[normalize-space()='Delete User']")
        self.user_deleted_modal = \
            (By.CSS_SELECTOR, "div[class='flex-1 flex justify-start text-[20px] font-bold text-dark-black dark:text-white']")
        self.x_button = (By.XPATH, "(//*[name()='path'][@stroke-linecap='round'])[10]")
        self.closed_user = (By.XPATH,
                            "(//div[contains(text(), 'User QAedited Testedited was closed on this accoun')])[1]")
        # Manage Pin
        self.manage_pin_modal = (By.XPATH, "(//div[@class='text-[20px] text-black dark:text-white'])[1]")
        self.pin_field = (By.ID, "contactIdentifier")
        self.continue_button = (By.XPATH, "//button[normalize-space()='Continue']")
        self.wrong_pin_validaton = \
            (By.XPATH, "(//span[@class='flex-1 text-sm pt-0.5 tracking-widest text-black dark:text-white'])[1]")
        self.new_pin_field = (By.ID, "pin")
        self.new_pin_field_confirm = (By.ID, "confirmPin")
        # Manage Notifcations
        self.manage_not_screen = \
            (By.XPATH, "(//div[@class='text-[20px] font-semibold tracking-widest text-black dark:text-white'])[1]")
        self.toggle_noti = (By.XPATH, "(//button[@id='headlessui-switch-:r3:'])[1]")
        self.edit_noti = (By.XPATH, "//span[@class='tracking-widest text-dark-gray dark:text-white']")
        self.accnt_chngs = (By.XPATH, "//div[contains(text(),'Account Changes')]")
        self.user_chngs = (By.XPATH, "//div[contains(text(),'User Changes')]")
        self.billing = \
            (By.XPATH, "(//div[@class='text-base tracking-widest text-dark-silver dark:text-white'][normalize-space()='Billing'])[1]")
        self.billing_chckbx  = (By.ID, "Billing0")
        self.usr_changes_chckbx = (By.ID, "User Changes2")
        self.accnt_changes_chckbx = (By.ID, "Account Changes1")
        self.save_noti_items_btn = (By.XPATH, "//button[@aria-label='edit-notification']")




