from selenium.webdriver.common.by import By


class TechAppLocators(object):

    def __init__(self, context=None):
        self.techappMenuButton = (By.XPATH, "//span[normalize-space()='Technician App']")
        self.dashboardMenuButton = (By.XPATH, "//span[normalize-space()='Dashboard']")
        self.HeadingText = (By.CSS_SELECTOR, 'h6[class*="MuiTypography-root MuiTypography-h6 "]')
        self.MyAppointmentsButton = (By.CSS_SELECTOR, "#techapp-dash-myapp-btn")
        self.map = (By.XPATH, "//div[@role='application']//canvas")
        self.appointmentsHeadline = (By.XPATH, "//h6[normalize-space()='Appointments']")
        self.vehicleNumber = (By.CSS_SELECTOR, 'svg[data-testid="ToysOutlinedIcon"]')
        self.techAppointmentdate=(By.CSS_SELECTOR,'p[id="date-click_1"]')
        self.techAppointment = (By.CSS_SELECTOR, " div[class*='tech-app-card-shadow']")
        self.customerName = (By.CSS_SELECTOR, 'h5[ class *="MuiTypography-root MuiTypography-h5"]')
        self.customerPhoneNumber= (By.CSS_SELECTOR, 'svg[data-testid="PhoneEnabledOutlinedIcon"]')
        self.customerAddress= (By.CSS_SELECTOR, 'svg[data-testid="LocationOnOutlinedIcon"]')
        self.customerEmail= (By. CSS_SELECTOR, 'svg[data-testid="EmailOutlinedIcon"]')
        self.customerTenure = (By.CSS_SELECTOR, "p > em ")