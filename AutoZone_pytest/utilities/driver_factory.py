from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
import os


def get_driver():

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "../config/config.ini"))

    browser = config["DEFAULT"]["browser"]

    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    driver.implicitly_wait(int(config["DEFAULT"]["implicit_wait"]))

    return driver
