from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# ------------------------------
# Setup WebDriver
# ------------------------------
driver = webdriver.Chrome()
driver.maximize_window()

# ------------------------------
# 1. Implicit Wait
# ------------------------------
driver.implicitly_wait(10)  # Wait up to 10 seconds for all elements
print("Implicit wait set to 10 seconds")

# ------------------------------
# Open OrangeHRM login page
# ------------------------------
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

# ------------------------------
# 2. Explicit Wait
# ------------------------------
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
print("Username field is clickable - explicit wait succeeded")
username_field.send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print("Logged in successfully")

# ------------------------------
# 3. Fluent Wait
# ------------------------------
def fluent_wait(driver, locator, timeout=20, poll_frequency=2):
    """
    Custom fluent wait: waits for an element to be present with polling intervals
    """
    end_time = time.time() + timeout
    while True:
        try:
            element = driver.find_element(*locator)
            print(f"Element {locator} found using fluent wait")
            return element
        except NoSuchElementException:
            pass
        time.sleep(poll_frequency)
        if time.time() > end_time:
            print(f"Fluent wait timed out for {locator}")
            break
    return None

# Example: wait for the "Admin" menu on dashboard to be visible
fluent_element = fluent_wait(driver, (By.XPATH, "//span[text()='Admin']"))

# ------------------------------
# 4. Message when element is ready
# ------------------------------
if fluent_element:
    print("Element is available for interaction!")

# ------------------------------
# Cleanup
# ------------------------------
time.sleep(3)  # Just to see the result before closing
driver.quit()
