# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestOpenProfessionalSupportSession():
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def open_home_page(self):
        self.driver.set_window_size(1920, 1080)
        self.driver.get("http://qlogic.io/index.html")

    def open_professional_support_section(self):
        self.driver.set_window_size(1920, 1080)
        self.driver.get("http://qlogic.io/profesional.php")

    def test_open_professional_support_section(self):
        self.open_home_page()
        self.driver.find_element(By.XPATH, "//a[@href='profesional.php']").click()

    def test_send_quick_contact(self):
        self.open_professional_support_section()
        self.driver.find_element(By.NAME, "name").send_keys("Qlogic")
        self.driver.find_element(By.NAME, "email").send_keys("seyfi@qlogic.io")
        self.driver.find_element(By.NAME, "subject").send_keys("Testing")
        self.driver.find_element(By.NAME, "phone").send_keys("8888")
        self.driver.find_element(By.NAME, "message").send_keys("TEST TEXT FFFFFFFFFFFFF")
        time.sleep(60)
        self.driver.find_element(By.NAME, "submit").click()


    def test_quick_contact_empty_name_field(self):
        self.open_professional_support_section()
        self.driver.find_element(By.NAME, "name").send_keys("")
        self.driver.find_element(By.NAME, "email").send_keys("seyfi@qlogic.io")
        self.driver.find_element(By.NAME, "subject").send_keys("Testing")
        self.driver.find_element(By.NAME, "phone").send_keys("8888")
        self.driver.find_element(By.NAME, "message").send_keys("TEST TEXT FFFFFFFFFFFFF")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(5)

    def test_quick_contact_fill_numbers_in_name_field(self):
        self.open_professional_support_section()
        self.driver.find_element(By.NAME, "name").send_keys("12345")
        self.driver.find_element(By.NAME, "email").send_keys("seyfi@qlogic.io")
        self.driver.find_element(By.NAME, "subject").send_keys("Testing")
        self.driver.find_element(By.NAME, "phone").send_keys("8888")
        self.driver.find_element(By.NAME, "message").send_keys("TEST TEXT FFFFFFFFFFFFF")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(5)


    def test_quick_contact_empty_email_field(self):
        self.open_professional_support_section()
        self.driver.find_element(By.NAME, "name").send_keys("Test")
        self.driver.find_element(By.NAME, "email").send_keys("")
        self.driver.find_element(By.NAME, "subject").send_keys("Testing")
        self.driver.find_element(By.NAME, "phone").send_keys("8888")
        self.driver.find_element(By.NAME, "message").send_keys("TEST TEXT FFFFFFFFFFFFF")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(5)


    def test_quick_contact_empty_subject_field(self):
        self.open_professional_support_section()
        self.driver.find_element(By.NAME, "name").send_keys("Test")
        self.driver.find_element(By.NAME, "email").send_keys("seyfi@qlogic.io")
        self.driver.find_element(By.NAME, "subject").send_keys("")
        self.driver.find_element(By.NAME, "phone").send_keys("8888")
        self.driver.find_element(By.NAME, "message").send_keys("TEST TEXT FFFFFFFFFFFFF")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(5)


    def test_quick_contact_empty_phone_field(self):
        self.open_professional_support_section()
        self.driver.find_element(By.NAME, "name").send_keys("Test")
        self.driver.find_element(By.NAME, "email").send_keys("seyfi@qlogic.io")
        self.driver.find_element(By.NAME, "subject").send_keys("gdfdgkj")
        self.driver.find_element(By.NAME, "phone").send_keys("")
        self.driver.find_element(By.NAME, "message").send_keys("TEST TEXT FFFFFFFFFFFFF")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(5)


    def test_quick_contact_empty_description_field(self):
        self.open_professional_support_section()
        self.driver.find_element(By.NAME, "name").send_keys("Test")
        self.driver.find_element(By.NAME, "email").send_keys("seyfi@qlogic.io")
        self.driver.find_element(By.NAME, "subject").send_keys("gdfdgkj")
        self.driver.find_element(By.NAME, "phone").send_keys("88888")
        self.driver.find_element(By.NAME, "message").send_keys("")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(5)