from selenium.webdriver.common.by import By


class LocatorsManagePermissionsPage(object):
    def __init__(self, context=None):
        #ManagePermissionsHome
        self.permissionsTableHeader = (By.XPATH, "//th[contains(text(),'Action')]")
        self.managepermissionstitle = (By.XPATH, "// p[text() = 'Manage Permissions']")
        self.managepermissions = (By.XPATH, "//span[normalize-space()='Manage Permissions']")
        self.accessCheckBox = (By.XPATH, "(// th[text() = 'Access'] // span)[1]")
        self.allPermissionsCheckBox = (By.XPATH, "//*[local-name() = 'svg' and @data-testid='CheckBoxOutlineBlankIcon']")
        #By Role
        self.departmentDropdownOption = (By.XPATH, "//li[text()='Engineering']")
        self.departmentDropdown = (By.XPATH, "//div[contains(@class,'MuiFormControl-root')]//label[text()='Department']/following-sibling::div/div")
        self.roleDropdownOption = (By.XPATH, "//li[contains(text(),'Junior Developer')]")
        self.roleDropdown = (By.XPATH, "//div[contains(@class,'MuiFormControl-root')]//label[text()='Role']/following-sibling::div/div")
        #By Email
        self.byEmailRadioButton = (By.XPATH, "(//span[contains(@class,'Radio')])[2]")
        self.addNewEmail = (By.XPATH, "// button[text() = 'Add New Email']")
        self.addbutton = (By.XPATH, "// button[text() = 'Add']")
        self.addNewEmailTextBox = (By.XPATH, "//div[contains(@class,'MuiFormControl-root')]//label[contains(text(),'Email')]/following-sibling::div/input")
        self.cancelButton = (By.XPATH, "// button[text() = 'Cancel']")

