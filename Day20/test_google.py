import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Day20.driverfactory import getdriver

@pytest.mark.parametrize("browser",["chrome","firefox","edge"])
def test_google_title(browser):
    driver=getdriver(browser)
    driver.get("https://www.google.com")
    driver.maximize_window()
    assert "Google" in driver.title
    driver.quit()

@pytest.mark.parametrize("browser", ["chrome","firefox", "edge"])
def test_google_search(browser):
    driver = getdriver(browser)
    driver.get("https://www.google.com")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("selenium grid")
    search_box.submit()
    WebDriverWait(driver, 10).until(
        lambda d: "google" in d.current_url.lower()
    )

    assert "google" in driver.current_url.lower()
    driver.quit()