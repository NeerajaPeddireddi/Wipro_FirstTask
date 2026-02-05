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

        driver.get("https://demoqa.com/automation-practice-form")
        driver.set_window_size(1552, 832)

        # FIRST NAME
        first = wait.until(EC.presence_of_element_located((By.ID, "firstName")))
        driver.execute_script("arguments[0].scrollIntoView(true);", first)
        first.send_keys("Ram")

        # LAST NAME
        last = driver.find_element(By.ID, "lastName")
        last.send_keys("S")

        # EMAIL
        email = driver.find_element(By.ID, "userEmail")
        email.send_keys("Rams12@gmail.com")

        # GENDER (label click is correct)
        driver.find_element(By.XPATH, "//label[@for='gender-radio-1']").click()

        # MOBILE
        mobile = driver.find_element(By.ID, "userNumber")
        mobile.send_keys("8978787878")

        # DATE OF BIRTH (MOST IMPORTANT FIX)
        dob = driver.find_element(By.ID, "dateOfBirthInput")
        driver.execute_script("arguments[0].scrollIntoView(true);", dob)
        dob = self.wait.until(
            EC.presence_of_element_located((By.ID, "dateOfBirthInput"))
        )

        self.driver.execute_script(
            "arguments[0].value = '03 Feb 2002';", dob
        )

        # DATE OF BIRTH — FIXED
        driver.execute_script(
            "document.getElementById('dateOfBirthInput').value = '03 Feb 2002';"
        )

        dob.send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "subjectsInput").click()
        self.driver.find_element(By.ID, "subjectsInput").send_keys("Maths,Hindi")
        self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']").click()
        self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-2']").click()
        self.driver.find_element(By.ID, "uploadPicture").send_keys(r"C:\Users\Neeraja\Pictures\2011-cricket-world-cup.jpg")
        time.sleep(2)
        self.driver.find_element(By.ID, "currentAddress").click()
        self.driver.find_element(By.ID, "currentAddress").send_keys("hyderabad,India")
        state = self.driver.find_element(By.ID, "react-select-3-input")
        state.send_keys("NCR")
        state.send_keys(Keys.ENTER)
        city = self.driver.find_element(By.ID, "react-select-4-input")
        city.send_keys("Delhi")
        city.send_keys(Keys.ENTER)
        submit = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit)
        self.driver.execute_script("arguments[0].click();", submit)
        # WAIT FOR SUCCESS MODAL
        modal_title = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "example-modal-sizes-title-lg")
            )
        )

        assert modal_title.text == "Thanks for submitting the form"


