import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestQ1:
    def setup_method(self,method):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    def test_q1(self):
        driver = self.driver
        wait = self.wait
        # Part 1: Launch Application
        driver.get("https://tutorialsninja.com/demo")
        driver.set_window_size(1552, 832)
        # ------Verify title--------
        wait.until(EC.title_contains("Your Store"))
        expected_title = "Your Store"
        actual_title = driver.title
        print("Actual title:",actual_title)
        assert expected_title == actual_title

        # ---------Registration page open-------
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()

        # ------Verify registration title-----
        heading = driver.find_element(By.CSS_SELECTOR, "#content h1")
        assert heading.text == "Register Account"
        print("Heading is Verified successfully:",heading.text)

        # -----Click on Continue Button------
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # Wait for the alert to appear
        alert_div = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible"))
        )
        expected_alert="You must agree to the Privacy Policy!"
        assert expected_alert in alert_div.text
        print("Alert Verified Successfully:", alert_div.text)

        # Part 2: For 'Your Personal Details'



        # Part 3,4
        self.driver.find_element(By.ID, "input-firstname").click()
        self.driver.find_element(By.ID, "input-firstname").clear()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Rajan")
        self.driver.find_element(By.ID, "input-lastname").click()
        self.driver.find_element(By.ID, "input-lastname").send_keys("sir")
        self.driver.find_element(By.ID, "input-email").click()
        self.driver.find_element(By.ID, "input-email").send_keys("rajansirio1@gmail.com")
        self.driver.find_element(By.ID, "input-telephone").click()
        self.driver.find_element(By.ID, "input-telephone").send_keys("7878787878")
        self.driver.find_element(By.ID, "input-password").click()
        self.driver.find_element(By.ID, "input-password").send_keys("admin123")
        self.driver.find_element(By.ID, "input-confirm").click()
        self.driver.find_element(By.ID, "input-confirm").send_keys("admin123")
        self.driver.find_element(By.CSS_SELECTOR, ".radio-inline:nth-child(2) > input").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.LINK_TEXT, "Success").click()
        success_msg = self.driver.find_element(By.CSS_SELECTOR, "#content > h1").text
        assert success_msg == "Your Account Has Been Created!"
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # download_link = driver.find_element(By.XPATH, '//a[contains(@href, "route=account/download")]')
        # download_link.click()
