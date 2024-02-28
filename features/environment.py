from selenium import webdriver
from dotenv import load_dotenv
# Load env variables
load_dotenv()


def before_scenario(context, feature):
    desired_capabilities = {
        'browserName': 'chrome'
    }
    context.browser = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://localhost:4444/wd/hub"
    )

def after_scenario(context, feature):
    context.browser.quit()
