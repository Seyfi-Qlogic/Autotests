from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class Application:

    def __init__(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == "firefox":
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            raise ValueError("Unrecognized browser" % browser)
        self.driver.implicitly_wait(10)
        self.driver.set_window_size(1920, 1080)

    def login(self, username="max@qlogic.io", password='N4885L'):
        self.driver.find_element(By.NAME, 'email').click()
        self.driver.find_element(By.NAME, 'email').send_keys(username)
        self.driver.find_element(By.NAME, 'password').click()
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "btn").click()  # click on login button

    def logout(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Log out')]").click()  # click on logout button

    def open_home_page(self):
        self.driver.get('http://pilotstub.qlogic.io/#/login')

    def click_OK_button_when_login_error(self):
        self.driver.find_element(By.CLASS_NAME, "confirm").click()

    def login_button(self):
        self.driver.find_element(By.CLASS_NAME, "btn").click()

    def destroy(self):
        self.driver.quit()

    def clear(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
