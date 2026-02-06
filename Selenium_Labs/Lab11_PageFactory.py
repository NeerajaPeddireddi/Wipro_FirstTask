import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Day17.Testcase3_dropdowns import dropdown


class OpenCartLocators:
    def __init__(self,driver):
        self.driver = driver
    @property
    def desktops(self):
        return self.driver.find_element(By.LINK_TEXT,"Desktops")
    @property
    def mac_option(self):
        return self.driver.find_element(By.LINK_TEXT,"Mac (1)")
    @property
    def sort_dropdown(self):
        return self.driver.find_element(By.ID,"input-sort")
    @property
    def select_name_az(self):
        return self.driver.find_element(By.XPATH, "//option[. = 'Name (A - Z)']")

    @property
    def add_to_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".button-group > button:nth-child(1)")
    @property
    def cart_icon(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".fa-shopping-cart")

    #Lab4
    @property
    def search_box(self):
        return self.driver.find_element(By.NAME,"search")
    @property
    def search_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,".input-group-btn > .btn")
    @property
    def input_search(self):
        return self.driver.find_element(By.ID, "input-search")
    @property
    def description_checkbox(self):
        return self.driver.find_element(By.ID, "description")
    @property
    @property
    def button_search(self):
        return self.driver.find_element(By.ID, "button-search")


class OpenCartActionsForLab3:
    def __init__(self,driver):
        self.driver = driver
        self.page = OpenCartLocators(driver)
    def click_desktop(self):
        self.page.desktops.click()
    def click_mac(self):
        self.page.mac_option.click()
        time.sleep(2)
        #Verification: check if "Mac" text is present
        assert "Mac" in self.driver.page_source

    def click_name_az(self):
        self.page.sort_dropdown.click()
        self.page.select_name_az.click()
        time.sleep(2)

    def click_add_to_cart(self):
        element=self.page.add_to_cart
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        time.sleep(2)

    def hover_cart(self):
        element = self.page.cart_icon
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
class OpenCartActionsForLab4(OpenCartActionsForLab3):
    def __init__(self, driver):
        super().__init__(driver)

    def search_from_header(self, text):
        self.page.search_box.click()
        self.page.search_box.send_keys(text)
        self.page.search_button.click()
        time.sleep(2)

    def advanced_search(self, text):
        self.page.input_search.click()
        self.page.input_search.send_keys(text)
        self.page.description_checkbox.click()
        self.page.button_search.click()
        time.sleep(2)

    def verify_search_text(self, expected_text):
        assert expected_text.lower() in self.driver.page_source.lower()
