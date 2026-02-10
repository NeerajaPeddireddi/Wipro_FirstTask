import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

GRIDURL ="http://192.168.1.7:4444/wd/hub"  # paste ur url here



def get_driver(browser):
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

    elif browser == "firefox":
        options = FirefoxOptions()

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

    else:
        raise ValueError("Browser not supported")

    driver = webdriver.Remote(
        command_executor=GRIDURL,
        options=options
    )
    return driver
@pytest.mark.parametrize("browser",["chrome","firefox","edge"])
def test_getdriver(browser):
    driver=get_driver(browser)
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    caps =driver.capabilities
    print(
        f"Browser: {caps.get('browserName')}, "
        f"Platform: {caps.get('platformName')}, "
        f"Version: {caps.get('browserVersion')}"
    )
    driver.quit()

