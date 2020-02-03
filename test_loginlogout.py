# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


class TestLoginlogout():
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, ".login_btn").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".login_btn")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

    def open_home_page(self):
        self.driver.set_window_size(1920, 1080)
        self.driver.get("https://eznotes.ubcorp.pro/")

    def logout(self):
        self.driver.find_element(By.XPATH, "//div[@title='admin']").click()
        self.driver.find_element(By.LINK_TEXT, "Log Out").click()

    def test_loginlogout(self):
        self.open_home_page()
        self.login(username="admin", password="111")
        self.logout()

    def test_login_with_empty_credentials(self):
        self.open_home_page()
        self.login(username="", password="")
        time.sleep(5)

    def test_open_free_card_and_buy(self):
        self.open_home_page()
        self.driver.find_element(By.XPATH, "//a [@href='/category/simchas']").click()
        self.driver.find_element(By.XPATH, "//a [@href='/product/pidyan-haben']").click()