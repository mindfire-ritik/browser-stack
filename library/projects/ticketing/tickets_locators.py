from selenium.webdriver.common.by import By


class TicketsLocators(object):
    def __init__(self, context=None):
        self.createTicket = (By.XPATH, "//button[normalize-space()='Create Ticket']")
        self.ticketsButton = (By.XPATH, "//p[contains(text(),'Tickets')]")
        self.nextButton = (By.XPATH, "//button[@aria-label='next-page']//*[name()='svg']")
        self.prevButton = (By.XPATH, "//button[@aria-label='prev-page']//*[name()='svg']")
        self.viewTicketsList = (By.CSS_SELECTOR,
                                "tbody tr:nth-child(1) td:nth-child(2) span:nth-child(1) span:nth-child(1)")
        self.viewSearchResult = (By.XPATH,
                                 "(//td[@class='w-auto px-2 text-left border border-t-0 border-l-0 lg:border-none border-light-gray'][normalize-space()='test'])[1]")
        self.nextPagination = (By.XPATH, "//span[normalize-space()='21-']")
        self.prevPagination = (By.XPATH, "//span[normalize-space()='1-']")
        self.createTicketModal = (By.XPATH, "//h1[normalize-space()='New Ticket']")
        self.ticketingLogin = (By.XPATH, "//button[normalize-space()='SIGN IN']")
        self.searchField = (By.XPATH, "//input[@placeholder='Search']")
        self.ticket = (By.CSS_SELECTOR,
                       "tbody tr:nth-child(1) td:nth-child(3) a:nth-child(1) span:nth-child(1)")
        # create master ticket
        self.validation_message = (By.XPATH, "//span[normalize-space()='Department is required']")
        self.department_field = (By.XPATH, "(//input[@id='headlessui-combobox-input-:r6:'])[1]")
        self.ticket_type_field = (By.XPATH, "(//input[@id='headlessui-combobox-input-:r8:'])[1]")
        self.employee_field = (By.XPATH, "(//input[@id='employee'])[1]")
        self.issue_field = (By.XPATH, "//input[@id='issueType']")
        self.subject_field = (By.XPATH, "(//input[@id='subject'])[1]")
        self.desc_field = (By.XPATH, "//div[@class='ql-editor ql-blank']//p")
        self.cncl_btn = (By.XPATH, "//button[normalize-space()='Cancel']")
        self.employee_select = (By.XPATH, "(//div[@class='pb-0.5'])[1]")
        self.submit_btn = (By.XPATH, "//button[@type='submit']")

        # ticket detail
        self.issue_field_detail = (By.XPATH, "//input[@id='issueType']")
        self.dept_field_detail = (By.XPATH, "//input[@id='department']")
        self.desc_detail = (By.CSS_SELECTOR, "div[class='ql-editor'] p")
        self.subject_detail = \
            (By.XPATH,
             "/html[1]/body[1]/main[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]")

        self.emply_detail = \
            (By.CSS_SELECTOR,
             "h3[class='font-semibold text-black font-work-sans xl:text-2xl text-large dark:text-white']")


        # Edit ticket
        self.priority_field_drpdwn = (By.XPATH, "//input[@id='priority']")
        self.tags_field_drpdwn = (By.XPATH, "//button[@id='tagList']")
        self.status_field_drpdwn = (By.XPATH, "//input[@id='status']")
        self.dept_drpdwn = (By.XPATH, "//input[@id='department']")
        self.previous_tix = (By.CSS_SELECTOR,
                             "div[class='w-full text-sm font-medium text-center xl:h-auto'] span:nth-child(1)")
        self.status_label = (By.XPATH, "//label[normalize-space()='Status']")
        self.tags_label = (By.XPATH, "//label[normalize-space()='Tags']")
        self.priority_label = (By.XPATH, "//label[normalize-space()='Priority']")
        self.department_label = (By.XPATH, "//label[normalize-space()='Department']")
        self.description_label = (By.XPATH, "//label[normalize-space()='Description']")
        self.current_issue_label = (By.XPATH, "//label[normalize-space()='Current Issue']")
        self.edit_button = (By.XPATH, "//span[@class='mr-2']")
        self.save_button = (By.XPATH, "//button[normalize-space()='Save Changes']")
        self.cancel_btn = (By.XPATH, "//span[normalize-space()='Cancel']")
        self.toast_message = (By.XPATH, "//p[@class='text-base dark:text-white ']")
        self.change_assignee = (By.ID, "change-assignee")
        self.close_assingee_modal = (By.ID, "cancel-assignee-modal")
        self.search_assignee = (By.ID, "searchAssignee")
        self.assigned = \
            (By.XPATH, "(//div[@class='text-base font-normal leading-4 dark:text-white font-work-sans'])[1]")


