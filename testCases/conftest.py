from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser ......................")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser .....................")
    elif browser == 'Edge':
        driver = webdriver.Edge()
        print("Launching Edge browser .....................")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome browser .....................")
#    else:
#        firefox_options = FirefoxOptions()
#        firefox_options.add_argument('--headless')
#        driver = webdriver.Firefox(options=firefox_options)
#        print("Launching firefox browser in headless mode.....................")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


############################# Pytest HTML Report ############################


def pytest_metadata(metadata):
    # To Add
    metadata["Environment"] = "Test"
    metadata['Project Name'] = 'Demoblaze'
    metadata['Tester'] = 'Ruturaj Darekar'
    # Remove
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)

