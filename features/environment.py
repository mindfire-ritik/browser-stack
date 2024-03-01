from selenium import webdriver
from dotenv import load_dotenv
# Load env variables
load_dotenv()

# ./SBSecureTunnel --username "wlimjr-c@team.nxlink.com" --authkey 9euUw8V33Q9XyufqIogGYMhKmVhu0YwB

def before_scenario(context, scenario):
    capabilities = {
        'platformName': 'Linux',
        'browserName': 'firefox',
        'browserVersion': '122',
        'bitbar:options': {
            'project': 'local_desktop',
            'testrun': 'local_test_run',
            'apiKey': '9euUw8V33Q9XyufqIogGYMhKmVhu0YwB',
            'osVersion': '18.04',
            'resolution': '1920x1080',
            'seleniumVersion': '4',
	    }
    }
    context.browser = webdriver.Remote(command_executor='https://us-west-desktop-hub.bitbar.com/wd/hub', desired_capabilities=capabilities)
    context.browser.maximize_window()
    context.browser.delete_all_cookies()

    print(context.browser.session_id)


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    context.browser.quit()

# def before_scenario(context, feature):
#     desired_capabilities = {
#         'browserName': 'chrome'
#     }
#     context.browser = webdriver.Remote(
#         desired_capabilities=desired_capabilities,
#         command_executor="http://localhost:4444/wd/hub"
#     )

# def after_scenario(context, feature):
#     context.browser.quit()
