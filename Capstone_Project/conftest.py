import pytest
import configparser
import os

from Capstone_Project.utilities.driver_factory import get_driver


@pytest.fixture(scope="function")
def setup():

    driver = get_driver()

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config/config.ini"))
    base_url = config["DEFAULT"]["base_url"]

    driver.get(base_url)

    yield driver

    driver.quit()
