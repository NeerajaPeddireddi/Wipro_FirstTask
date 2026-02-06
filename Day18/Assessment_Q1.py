from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage:

    def __init__(self,driver):
        self.driver=driver
    firstname=(By.ID,"first-name")
    lastname=(By.ID,"last-name")
    jobtitle=(By.ID,"job-title")
    high_school_radiobutton=(By.ID,"radio-button-1")
    college_radiobutton = (By.ID, "radio-button-2")
    grad_school_radiobutton = (By.ID, "radio-button-3")
    male=(By.ID, "checkbox-1")
    female=(By.ID, "checkbox-2")
    prefer_not_say=(By.ID, "checkbox-3")
    experience_dropdown=(By.ID, "select-menu")
    datepicker = (By.ID, "datepicker")
    loginbutton=(By.LINK_TEXT,"Submit")

    def enter_firstname(self,firstname):
        self.driver.find_element(*self.firstname).send_keys(firstname)
    def enter_lastname(self,lastname):
        self.driver.find_element(*self.lastname).send_keys(lastname)
    def enter_jobtitle(self,jobtitle):
        self.driver.find_element(*self.jobtitle).send_keys(jobtitle)
    def select_education(self,level):
        if level.lower()=="high-school":
            self.driver.find_element(*self.high_school_radiobutton).click()
        elif level.lower()=="college":
            self.driver.find_element(*self.college_radiobutton).click()
        elif level.lower()=="grad_school":
            self.driver.find_element(*self.grad_school_radiobutton).click()
    def select_sex(self,option):
        if option.lower()=="male":
            self.driver.find_element(*self.male).click()
        elif option.lower()=="female":
            self.driver.find_element(*self.female).click()
        elif option.lower()=="prefer_not_say":
            self.driver.find_element(*self.prefer_not_say).click()

    def select_experience(self, option):
        dropdown = Select(self.driver.find_element(*self.experience_dropdown))

        if option == "0-1":
            dropdown.select_by_visible_text("0-1")
        elif option == "2-4":
            dropdown.select_by_visible_text("2-4")
        elif option == "5-9":
            dropdown.select_by_visible_text("5-9")
        elif option == "10+":
            dropdown.select_by_visible_text("10+")

    def select_date(self, date):
        date_field = self.driver.find_element(*self.datepicker)
        date_field.clear()
        date_field.send_keys(date)
    def click_login(self):
        self.driver.find_element(*self.loginbutton).click()

from pywin.dialogs import login
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



driver=webdriver.Chrome()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)
driver.get("https://formy-project.herokuapp.com/form")
loginobj=LoginPage(driver)
loginobj.enter_firstname("Ram")
loginobj.enter_lastname("s")
loginobj.enter_jobtitle("Software Engineer")
loginobj.select_education("high-school")
loginobj.select_sex("male")
loginobj.select_experience("5-9")
loginobj.select_date("02/15/2026")
loginobj.click_login()
