from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(10)

    def login(self, username="max@qlogic.io", password='N4885L'):
        self.driver.find_element(By.NAME, 'email').click()
        self.driver.find_element(By.NAME, 'email').send_keys(username)
        self.driver.find_element(By.NAME, 'password').click()
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "btn").click()      # click on login button

    def logout(self):
        self.driver.find_element(By.CLASS_NAME, "hidden-sm").click()  # click on logout button

    def open_home_page(self):
        self.driver.set_window_size(1920, 1080)
        self.driver.get('http://pilotstub.qlogic.io/#/login')

    def destroy(self):
        self.driver.quit()