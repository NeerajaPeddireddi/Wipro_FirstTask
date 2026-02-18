from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SortProducts:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ----------- LOCATORS ------------
        self.sort_dropdown = (By.NAME, "orderby")

    def select_sort_option(self, value):
        """
        Select a sorting option from the dropdown.
        :param value: option value attribute, e.g., "popularity"
        """
        dropdown_element = self.wait.until(
            EC.visibility_of_element_located(self.sort_dropdown)
        )
        select = Select(dropdown_element)
        select.select_by_value(value)