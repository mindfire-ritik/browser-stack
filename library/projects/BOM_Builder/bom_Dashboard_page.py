from selenium.webdriver.common.by import By

class LocatorsBomDashboardPage(object):
    def __init__(self, context=None):
        # Background Locators
        self.home = (By.XPATH, '//p[text()="Home"]')
        self.login_button = (By.CSS_SELECTOR, "button[type='button']")
        self.userName = (By.CSS_SELECTOR, "input[type='email']")
        self.nextBtn = (By.XPATH, "//input[@type=\"submit\"]")
        self.passwd = (By.CSS_SELECTOR, "input[type='password']")
        self.submitBtn = (By.CSS_SELECTOR, "[data-report-event=\"Signin_Submit\"]")
        self.signedinText = (By.CSS_SELECTOR, "div[class='row text-title']")
        self.noBtn = (By.CSS_SELECTOR, "input[id*=\"Back\"]")
        #Dashboard page
        self.header = (By.XPATH, "//header[@class='flex items-center justify-between fixed w-full left-0 z-[1000] h-[4.25rem] md:h-[5rem] px-[15px] md:px-4 py-5 bg-[#212121]']")
        self.nextlink_logo = (By.XPATH, "//a[@data-automation-id='logo-cta']")
        self.create_bom = (By.XPATH, "//a[@data-automation-id='create-bom']")
        self.create_bom_model = (By.XPATH, "//div[@class='flex flex-col gap-6']")
        self.create_bom_close_btn = (By.XPATH, "//*[name()='path' and contains(@d,'M18.3 5.71')]")
        self.toggle_btn = (By.XPATH, "//label[@class='themeSwitcherTwo relative inline-flex cursor-pointer select-none items-center']")
        self.collapse_btn = (By.XPATH, "//div[@data-automation-id='desktop-side-bar']")
        self.dashboard_icon = (By.XPATH, "(//*[name()='svg'][@class='dark:hidden'])[1]")
        self.dashboard = (By.XPATH, "//p[text()='Dashboard']")
        self.profile_logo = (By.XPATH, "//div[@data-automation-id='show-profile-nav']")
        self.logout_btn = (By.XPATH, "//div[text()='Log Out']")
        self.bom_title = (By.XPATH, "//h2[contains(@class,'font-work-sans text-black dark:text-white')]")

        #BOM List Page
        self.bom_page = (By.XPATH, "//div[contains(@class,'w-full h-full flex flex-col justify-between')]//a[contains(@title,'BOMs')]")
        self.bom_list = (By.XPATH, "//button[normalize-space()='BOM List']")
        self.bom_list_search_btn = (By.XPATH, "//input[@placeholder='Search']")
        self.bom_list_table = (By.XPATH, "//div[@class='data-grid__table']")
        self.bom = (By.XPATH, "//span[contains(text(),'BOM')]")
        self.site_name = (By.XPATH, "//span[contains(text(),'Site Name')]")
        self.project_id = (By.XPATH, "//span[contains(text(),'Project ID')]")
        self.warehouse_location = (By.XPATH, "//span[contains(text(),'Warehouse Location')]")
        self.date_requested = (By.XPATH, "//span[contains(text(),'Date Requested')]")
        self.project_type = (By.XPATH, "//span[contains(text(),'Project Type')]")
        self.project_pre_deployment_start = (By.XPATH, "//span[contains(text(),'Project Pre-deployment Start')]")
        self.last_updated = (By.XPATH, "//span[contains(text(),'Last Updated')]")
        self.list_per_page = (By.XPATH, "//p[normalize-space()='Lists Per Page']")
        self.list_per_page_no = (By.XPATH, "//div[@class='flex flex-wrap justify-end gap-4']/div/button[contains(@class,'MuiMenuButton-root MuiMenuButton-variantOutlined')]")
        self.page = (By.XPATH, "//p[normalize-space()='Page']")
        self.page_no = (By.XPATH, "//div[@class='flex flex-wrap gap']/div/button[contains(@class,'MuiMenuButton-root MuiMenuButton-variantOutlined')]")
        self.create_bom_btn = (By.XPATH, "//button[normalize-space()='Create Master BOM']")
        self.master_bom_list = (By.XPATH, "//button[normalize-space()=\"Master BOM's\"]")

        #Material list
        self.material_page = (By.XPATH, "//a[contains(@data-automation-id,'side-bar-link-desktop-Material Lists')]")
        self.material_title_page = (By.XPATH, "//h2[normalize-space()='Material List']")
        self.material_page_table = (By.XPATH, "//div[contains(@class,'data-grid__table')]")
        self.variable_btn = (By.XPATH, "//button[@data-automation-id='material-list-open-variable-modal']")
        self.create_list_set = (By.XPATH, "//button[@data-automation-id='create-list-set']")
        self.close_create_list_set = (By.XPATH, "//button[contains(@class,'MuiModalClose-root MuiModalClose-variantPlain MuiModalClose')]//*[name()='svg']")
        self.name = (By.XPATH, "//span[contains(text(),'Name')]")
        self.created_by = (By.XPATH, "//span[contains(text(),'Created By')]")
        self.date_created = (By.XPATH, "//span[contains(text(),'Date Created')]")
        self.category = (By.XPATH, "//span[contains(text(),'Category')]")
        self.late_updated = (By.XPATH, "//span[contains(text(),'Last Updated')]")
        self.search_btn = (By.XPATH, "//div[@data-automation-id='material-list-search-box']")
        self.next_page_btn = (By.XPATH, "//button[@data-automation-id='material-list-next-page']")
        self.dialog_variable_box = (By.XPATH, "//div[@role='dialog']")
        self.search_vriable_btn = (By.XPATH, "//input[@id='searchVariableInput']")
        self.variable_table = (By.XPATH, "//div[@class='flex flex-col gap-1.5']//div//div[@class='data-grid__table']")
        self.variable_column = (By.XPATH, "//span[contains(text(),'Variable')]")
        self.description_column = (By.XPATH, "//span[contains(text(),'Definition')]")
        self.rows_per_page_btn = (By.XPATH, "//button[@data-automation-id='variable-modal-list-per-page-btn']")
        self.row_per_page_menu = (By.XPATH, "//ul[@role='menu']")
        self.rows_per_page_list = (By.XPATH, "//li[@data-automation-id='variable-modal-list-page-size -20']")
        self.page_btn = (By.XPATH, "//button[@data-automation-id='variable-modal-list-current-page-btn']")
        self.page_list = (By.XPATH, "//li[@data-automation-id='variable-modal-list-page-size-2']")
        self.previous_page = (By.XPATH, "//button[@data-automation-id='variable-modal-list-prev-page']")
        self.next_page = (By.XPATH, "//button[@data-automation-id='variable-modal-list-next-page']")
        self.add_variable_btn = (By.XPATH, "//button[@data-automation-id='variable-modal-list-add-new']")





