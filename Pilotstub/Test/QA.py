from selenium.webdriver.common.by import By
from Pilotstub.Fixture.application import Application
import time
import pytest


@pytest.fixture(scope="function ")
def app(request):
    fixture = Application()
    fixture.open_home_page()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login_and_logout(app):
    app.login()
    app.logout()
    time.sleep(2)


def test_login_with_wrong_username(app):  # add expected result to the test
    app.login(username='test')
    time.sleep(5)


def test_login_with_wrong_password(app):
    app.login(password='test')
    app.click_OK_button_when_login_error()
    time.sleep(2)


def test_fill_switched_username_and_password(app):
    app.login(username='N4885L', password='max@qlogic.io')
    time.sleep(5)


def test_login_with_empty_fields(app):
    app.login(username="", password="")


def test_open_aircraft_listing(app):
    app.login()
    app.driver.find_element(By.XPATH, "//a [@href='#/app/aircraftListing']").click()
    app.logout()


def test_open_aircraft_listing_and_choose_aircraft(app):
    app.login()
    app.driver.find_element(By.XPATH, "//a [@href='#/app/aircraftListing']").click()
    app.driver.find_element(By.CLASS_NAME, "input").click()
    app.driver.find_element(By.CLASS_NAME, "input").send_keys("t")
    app.driver.find_element(By.XPATH, "//a [@href='javascript:void(0)']").click()
    app.logout()


def test_open_reservations(app):
    app.login()
    app.driver.find_element(By.CLASS_NAME, "nav-label").click()
    time.sleep(2)
    app.logout()

def test_add_new_reservation(app):
    app.login()
    app.driver.find_element(By.CLASS_NAME, "add-new-button").click()
    time.sleep(1)
    app.driver.find_element(By.NAME, "activity").click()
    app.driver.find_element(By.XPATH, "//option[contains(text(),'Dual Training')]").click()
    app.driver.find_element(By.ID, 'EndTime').click()
    app.driver.find_element(By.XPATH, "//option[contains(text(),'11:30 PM')]").click()
    app.driver.find_element(By.NAME, 'displayname').send_keys("Display here")
    app.driver.find_element(By.CLASS_NAME, "chosen-single").click()
    app.driver.find_element(By.XPATH, "//li[contains(text(), 'Seyfi')]").click()
    app.driver.find_element(By.XPATH, "//div[@class='col-lg-12 reccuringArea']//div[@class='col-lg-4 controlTopMargin ng-scope']//select[@id='Registration/Tail']").click()
    app.driver.find_element(By.XPATH, "//div[@class='col-lg-12 reccuringArea']//div[@class='col-lg-4 controlTopMargin ng-scope']//option[contains(text(),'Test Test - Test')]").click()
    app.driver.find_element(By.ID, "location").click()
    app.driver.find_element(By.XPATH, "//option[contains(text(),'Loca tion')]").click()
    # app.driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]").click()
    time.sleep(3)
    app.logout()
