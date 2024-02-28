from selenium.webdriver.common.by import By


class LocatorsMaterialListPage(object):
    def __init__(self, context=None):
        self.variable_btn = (By.XPATH, "//button[@data-automation-id='material-list-open-variable-modal']")
        self.variable_dialog_box = (By.XPATH, "//div[@role='dialog']")
        self.add_variable_btn = (By.XPATH, "//button[@data-automation-id='variable-modal-list-add-new']")
        self.create_variable_dialog_box = (By.XPATH, "(//div[@role='dialog'])[2]")
        self.name_label = (By.XPATH, "//label[normalize-space()='Name']")
        self.name_variable = (By.XPATH, "//input[@name='variableName']")
        self.description_label = (By.XPATH, "//label[normalize-space()='Description']")
        self.description_text = (By.XPATH, "//textarea[@name='description']")
        self.input_label = (
        By.XPATH, "//p[contains(@class,'font-work-sans text-black dark:text-white uppercase text')]")
        self.formula_value = (By.XPATH, "//label[normalize-space()='Formula Value']")
        self.formula_value_text = (By.XPATH, "//textarea[@name='variableValue']")
        self.cancel_btn = (By.XPATH, "//button[@id='CancelBtn']")
        self.save_btn = (By.XPATH, "//button[@id='SaveBtn']")
        self.input_search_btn = (
        By.XPATH, "//div[contains(@class,'my-react-select__value-container my-react-select__value-container')]")
        self.input_model = (
        By.XPATH, "//div[@class='my-react-select__menu-list my-react-select__menu-list--is-multi joy-qr46ko']")
        self.bh_type = (By.XPATH, "//div[@id='react-select-2-option-1']")
        self.bh_frequenzy = (By.XPATH, "//div[@id='react-select-2-option-6']")
        self.pre_deployment_start_date = (By.XPATH, "//div[@id='react-select-2-option-18']")
        self.input_option_block = (By.XPATH, "//div[@class='grid grid-cols-3 items-center']")
        self.operation_listbox = (By.XPATH, "//div[@id='react-select-3-listbox']")
        self.equal_operation = (By.XPATH, "//div[@id='react-select-3-option-2']")
        self.input_field = (By.XPATH, "(//div[contains(@class,'p-3 h-full border-r-[1px] border-solid border')])[1]")
        self.operation_field = (By.XPATH, "(//div[contains(@class,'p-3 h-full border-r-[1px] border-solid border')])[2]")
        self.operation_block = (By.XPATH, "(//div[@class='my-react-select-container joy-b62m3t-container'])[2]")
        self.definiation_listbox = (By.XPATH, "(//div[@id='react-select-9-listbox'])")
        self.bh_type_option = (By.XPATH, "//div[@id='react-select-4-placeholder']")
        self.defination = (By.XPATH, "(//div[@class='w-full flex flex-col'])[3]")
        self.between_option = (By.XPATH, "(//div[@class='my-react-select__option joy-ss6f6h-option'])")
        self.operation_bh_listbox = (By.XPATH, "//div[@id='react-select-7-listbox']")
        self.operation_listbox_block = (By.XPATH, "(//div[@class='my-react-select-container joy-b62m3t-container'])[4]")
        self.definiation_field = (By.XPATH, "//div[@class='p-3 h-full']")
        self.bh_type_input = (By.XPATH, "//p[normalize-space()='BH Type']")
        self.bh_frequenzy_input = (By.XPATH, "//p[normalize-space()='BH Frequency TX.']")
        self.pre_deployment_start_date_input = (By.XPATH, "//p[normalize-space()='Pre Deployment Start Date']")
        self.bh_frequenzy_input_value = (By.XPATH, "//input[@name='inputs.0.inputValue1']")
        self.pre_deployment_start_date_input_value = (By.XPATH, "//div[contains(@class,'MuiInput-root MuiInput-variantPlain')]//input[@type='date']")
        self.alert_mssgs = (By.XPATH, "//div[contains(@class,'animate-enter bg-white dark:bg-dark-bgsub rounded max-w')]")
        self.dismiss_btn = (By.XPATH, "//button[normalize-space()='Dismiss']")
        self.search_btn = (By.XPATH, "//input[@id='searchVariableInput']")
        self.search_grid = (By.XPATH, "//div[@class='flex flex-col gap-1.5']//div//div[@role='grid']")
        self.edit_variable_btn = (By.XPATH, "(//p[@class='hover:underline cursor-pointer'])[2]")
        self.edit_variable_dialog_box = (By.XPATH, "(//div[@role='dialog'])[2]")
        self.delete_btn = (By.XPATH, "//button[@id='deleteVariableBtn']")


