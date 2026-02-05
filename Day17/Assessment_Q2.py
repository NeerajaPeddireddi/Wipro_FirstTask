import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAlerts:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    def test_alerts(self):
        driver = self.driver
        wait = self.wait

        driver.get("https://demoqa.com/alerts")
        driver.maximize_window()

        # -------------------------
        # SIMPLE ALERT
        # -------------------------
        driver.find_element(By.ID, "alertButton").click()

        alert = wait.until(EC.alert_is_present())
        print("Alert message:", alert.text)

        alert.accept()   # Accept alert

        # -------------------------
        # CONFIRMATION ALERT (Dismiss)
        # -------------------------
        driver.find_element(By.ID, "confirmButton").click()

        alert = wait.until(EC.alert_is_present())
        print("Confirm alert message:", alert.text)

        alert.dismiss()  # Click Cancel

        # Verify result text
        confirm_result = driver.find_element(By.ID, "confirmResult").text
        assert "Cancel" in confirm_result

        # -------------------------
        #PROMPT ALERT
        # -------------------------
        driver.find_element(By.ID, "promtButton").click()

        alert = wait.until(EC.alert_is_present())
        alert.send_keys("Ram")
        alert.accept()

        # Verify prompt result
        prompt_result = driver.find_element(By.ID, "promptResult").text
        assert "Ram" in prompt_result
