import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://formy-project.herokuapp.com/form")

    yield driver

    driver.quit()
