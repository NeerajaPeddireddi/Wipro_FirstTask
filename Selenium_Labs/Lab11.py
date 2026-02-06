import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Day17.Testcase3_dropdowns import dropdown


class OpenCartLocators:
    desktops_menu=(By.LINK_TEXT,"Desktops")
    mac_option=(By.LINK_TEXT,"Mac (1)")
    sort_dropdown=(By.ID,"input-sort")
    select_name_az=(By.XPATH, "//option[. = 'Name (A - Z)']")
    add_to_cart=(By.CSS_SELECTOR, ".button-group > button:nth-child(1)")
    cart_icon = (By.CSS_SELECTOR, ".fa-shopping-cart")
    #Lab4
    search_box=(By.NAME,"search")
    search_button=(By.CSS_SELECTOR,".input-group-btn > .btn")
    input_search = (By.ID, "input-search")
    description_checkbox = (By.ID, "description")
    button_search = (By.ID, "button-search")

class OpenCartActionsForLab3:
    def __init__(self,driver):
        self.driver = driver
    def click_desktop(self):
        self.driver.find_element(*OpenCartLocators.desktops_menu).click()
    def click_mac(self):
        self.driver.find_element(*OpenCartLocators.mac_option).click()
        time.sleep(2)
        #Verification: check if "Mac" text is present
        assert "Mac" in self.driver.page_source

    def click_name_az(self):
        self.driver.find_element(*OpenCartLocators.select_name_az).click()
        dropdown=self.driver.find_element(*OpenCartLocators.sort_dropdown)
        dropdown.find_element(*OpenCartLocators.select_name_az).click()
        time.sleep(2)

    def click_add_to_cart(self):
        element=self.driver.find_element(*OpenCartLocators.add_to_cart)
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        time.sleep(2)

    def hover_cart(self):
        element = self.driver.find_element(*OpenCartLocators.cart_icon)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
class OpenCartActionsForLab4(OpenCartActionsForLab3):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def search_from_header(self, text):
        self.driver.find_element(*OpenCartLocators.search_box).click()
        self.driver.find_element(*OpenCartLocators.search_box).send_keys(text)
        self.driver.find_element(*OpenCartLocators.search_button).click()
        time.sleep(2)

    def advanced_search(self, text):
        self.driver.find_element(*OpenCartLocators.input_search).click()
        self.driver.find_element(*OpenCartLocators.input_search).send_keys(text)
        self.driver.find_element(*OpenCartLocators.description_checkbox).click()
        self.driver.find_element(*OpenCartLocators.button_search).click()
        time.sleep(2)

    def verify_search_text(self, expected_text):
        assert expected_text.lower() in self.driver.page_source.lower()
