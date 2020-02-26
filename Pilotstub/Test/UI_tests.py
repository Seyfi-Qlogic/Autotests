from selenium.webdriver.common.by import By
from Pilotstub.Fixture.application import Application
import time
import pytest
import requests


@pytest.fixture(scope="session")
def init_fixture():
    return Application()


@pytest.fixture(scope="function")
def app(init_fixture):
    init_fixture.open_home_page()
    yield init_fixture
    init_fixture.clear()


def test_login_and_logout(app):
    app.login()
    app.logout()
    time.sleep(1)
    assert "Login" in app.driver.title


def test_login_and_refresh(app):
    app.login()
    time.sleep(1)
    app.driver.refresh()
    userdisplay = app.driver.find_element(By.XPATH, "//strong[@class='font-bold ng-binding']")
    assert userdisplay.is_displayed()


def test_login_with_wrong_username_format(app):
    app.login(username='test')
    redframe = app.driver.find_element(By.CLASS_NAME, 'ng-dirty')
    assert redframe.is_displayed()


def test_login_with_wrong_username(app):
    app.login(username='test@mail.com')
    loginerror = app.driver.find_element(By.CLASS_NAME, 'confirm')
    assert loginerror.is_displayed()


def test_login_with_wrong_password(app):
    app.login(password='test')
    app.click_OK_button_when_login_error()
    loginerror = app.driver.find_element(By.CLASS_NAME, 'confirm')
    assert loginerror.is_displayed()


def test_fill_switched_username_and_password(app):
    app.login(username='N4885L', password='max@qlogic.io')
    redframe = app.driver.find_element(By.CLASS_NAME, 'ng-dirty')
    assert redframe.is_displayed()


def test_login_with_correct_password_but_different_register(app):
    app.login(password='n4885L')
    loginerror = app.driver.find_element(By.CLASS_NAME, 'confirm')
    assert loginerror.is_displayed()


def test_login_with_correct_username_but_different_register(app):
    app.login(username='MAX@QloGic.io')
    userdisplay = app.driver.find_element(By.XPATH, "//strong[@class='font-bold ng-binding']")
    assert userdisplay.is_displayed()


def test_login_with_empty_fields(app):
    app.login(username="", password="")
    redframe = app.driver.find_element(By.CLASS_NAME, 'has-error')
    assert redframe.is_displayed()


def test_click_login_button_multiple_times(app):
    for _ in range(11):
        app.login_button()
        assert "Login" in app.driver.title


def test_login_with_empty_password(app):
    app.login(password="")
    redframe = app.driver.find_element(By.CLASS_NAME, 'ng-dirty')
    assert redframe.is_displayed()


def test_login_with_empty_username(app):
    app.login(username="")
    redframe = app.driver.find_element(By.CLASS_NAME, 'ng-dirty')
    assert redframe.is_displayed()


def test_login_with_space_before_and_after_username(app):
    app.login(username=" max@qlogic.io ")
    userdisplay = app.driver.find_element(By.XPATH, "//strong[@class='font-bold ng-binding']")
    assert userdisplay.is_displayed()


def test_open_aircraft_listing(app):
    app.login()
    app.driver.find_element(By.XPATH, "//a [@href='#/app/aircraftListing']").click()
    time.sleep(1)
    airlisting = app.driver.find_element(By.XPATH, "//h5[contains(text(),'Aircraft Listing')]")
    assert airlisting.is_displayed()


def test_open_aircraft_listing_and_choose_aircraft(app):
    app.login()
    app.driver.find_element(By.XPATH, "//a [@href='#/app/aircraftListing']").click()
    app.driver.find_element(By.CLASS_NAME, "input").click()
    app.driver.find_element(By.CLASS_NAME, "input").send_keys("t")
    app.driver.find_element(By.XPATH, "//div[@class='ibox-content']//div[2]//div[1]//a[1]//img[1]").click()
    url = app.driver.current_url
    assert "http://pilotstub.qlogic.io/#/app/viewaircraft/D7A45083-D8EF-4E03-AED2-41563F6D5962" in url


def test_open_reservations(app):
    app.login()
    app.driver.find_element(By.CLASS_NAME, "nav-label").click()
    schedule = app.driver.find_element(By.XPATH, "//h5[contains(text(),'Schedule Time Table')]")
    assert schedule.is_displayed()


def test_add_new_reservation(app):  # test is not finished
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
    app.driver.find_element(By.XPATH,
                            "//div[@class='col-lg-12 reccuringArea']//div[@class='col-lg-4 controlTopMargin "
                            "ng-scope']//select[@id='Registration/Tail']").click()
    app.driver.find_element(By.XPATH,
                            "//div[@class='col-lg-12 reccuringArea']//div[@class='col-lg-4 controlTopMargin "
                            "ng-scope']//option[contains(text(),'Test Test - Test')]").click()
    app.driver.find_element(By.ID, "location").click()
    # app.driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]").click()


def test_enter_end_time_lower_than_start_time(app):
    app.login()
    app.driver.find_element(By.CLASS_NAME, "add-new-button").click()
    time.sleep(1)
    # choose activity
    app.driver.find_element(By.NAME, "activity").click()
    app.driver.find_element(By.XPATH, "//option[contains(text(),'Dual Training')]").click()
    # choose start time
    app.driver.find_element(By.ID, 'StartTime').click()
    app.driver.find_element(By.XPATH, "//select[@id='StartTime']//option[contains(text(),'11:30 AM')]").click()
    # choose end time
    app.driver.find_element(By.ID, 'EndTime').click()
    app.driver.find_element(By.XPATH, "//select[@id='EndTime']//option[contains(text(),'12:00 AM')]").click()
    # enter displayName
    app.driver.find_element(By.NAME, 'displayname').send_keys("Display here")
    # choose aircraft
    app.driver.find_element(By.XPATH,
                            "//div[@class='col-lg-12 reccuringArea']//div[@class='col-lg-4 controlTopMargin "
                            "ng-scope']//select[@id='Registration/Tail']").click()
    app.driver.find_element(By.XPATH,
                            "//div[@class='col-lg-12 reccuringArea']//div[@class='col-lg-4 controlTopMargin "
                            "ng-scope']//option[contains(text(),'Test Test - Test')]").click()
    # click Save button
    app.driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]").click()
    alert = app.driver.find_element(By.XPATH,
                                    "//p[contains(text(),'End date & time must be greater than start date &')]")
    assert alert.is_displayed()


def test_enter_end_date_lower_than_start_date_with_recurring_schedule(app):
    app.login()
    app.driver.find_element(By.CLASS_NAME, "add-new-button").click()
    time.sleep(1)
    # click on checkbox "recurring schedule"
    app.driver.find_element(By.XPATH,
                            "//div[@class='col-lg-3 recurring-checkbox']//ins[@class='iCheck-helper']").click()
    # choose start date and end date
    app.driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
    app.driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']").click()
    app.driver.find_element(By.XPATH, "//option[contains(text(),'2025')]").click()
    app.driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']").click()
    app.driver.find_element(By.XPATH, "//option[contains(text(),'Dec')]").click()
    app.driver.find_element(By.XPATH, "//a[@class='ui-state-default'][contains(text(),'31')]").click()
    # choose activity
    app.driver.find_element(By.NAME, "activity").click()
    app.driver.find_element(By.XPATH, "//option[contains(text(),'Dual Training')]").click()
    # choose start time
    app.driver.find_element(By.ID, 'StartTime').click()
    app.driver.find_element(By.XPATH, "//select[@id='StartTime']//option[contains(text(),'11:30 AM')]").click()
    # choose end time
    app.driver.find_element(By.ID, 'EndTime').click()
    app.driver.find_element(By.XPATH, "//select[@id='EndTime']//option[contains(text(),'12:00 AM')]").click()
    # enter displayName
    app.driver.find_element(By.NAME, 'displayname').send_keys("Autotest")
    # choose aircraft
    app.driver.find_element(By.XPATH,
                            "//div[@class='col-lg-12 reccuringArea']//div[@class='col-lg-4 controlTopMargin "
                            "ng-scope']//select[@id='Registration/Tail']").click()
    app.driver.find_element(By.XPATH,
                            "//div[@class='col-lg-12 reccuringArea']//div[@class='col-lg-4 controlTopMargin "
                            "ng-scope']//option[contains(text(),'Test Test - Test')]").click()
    # click Save button
    app.driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]").click()
    alert = app.driver.find_element(By.XPATH,
                                    "//p[contains(text(),'End date & time must be greater than start date &')]")
    assert alert.is_displayed()

def test_enter_end_date_lower_than_start_date(app):
    app.login()
    app.driver.find_element(By.CLASS_NAME, "add-new-button").click()
    time.sleep(1)
    # choose start date
    app.driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
    app.driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']").click()
    app.driver.find_element(By.XPATH, "//option[contains(text(),'2025')]").click()
    app.driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']").click()
    app.driver.find_element(By.XPATH, "//option[contains(text(),'Dec')]").click()
    app.driver.find_element(By.XPATH, "//a[@class='ui-state-default'][contains(text(),'31')]").click()
    # choose end date
    app.driver.find_element(By.NAME, "enddate").click()
    app.driver.find_element(By.CLASS_NAME, "ui-datepicker-year").click()
    app.driver.find_element(By.XPATH, "//option[contains(text(),'2020')]").click()
    app.driver.find_element(By.CLASS_NAME, "ui-datepicker-month").click()
    app.driver.find_element(By.XPATH, "//option[contains(text(),'Dec')]").click()
    app.driver.find_element(By.XPATH, "//a[@class='ui-state-default'][contains(text(),'31')]").click()
    # choose activity
    app.driver.find_element(By.NAME, "activity").click()
    app.driver.find_element(By.XPATH, "//option[contains(text(),'Dual Training')]").click()
    # enter displayName
    app.driver.find_element(By.NAME, 'displayname').send_keys("Autotest")
    # choose aircraft
    app.driver.find_element(By.XPATH,
                            "//div[@class='col-lg-12 reccuringArea']//div[@class='col-lg-4 controlTopMargin "
                            "ng-scope']//select[@id='Registration/Tail']").click()
    app.driver.find_element(By.XPATH,
                            "//div[@class='col-lg-12 reccuringArea']//div[@class='col-lg-4 controlTopMargin "
                            "ng-scope']//option[contains(text(),'Test Test - Test')]").click()
    # click Save button
    app.driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]").click()
    alert = app.driver.find_element(By.XPATH,
                                    "//p[contains(text(),'End date & time must be greater than start date &')]")
    assert alert.is_displayed()


def test_add_new_student_and_delete(app):
    app.login()
    time.sleep(3)
    # used longer href because the short one is flaky
    app.driver.find_element(By.XPATH, "//body[@id='page-top']/div[@class='ng-scope']/div[@id='wrapper']/div["
                                      "@class='ng-scope']/nav[@class='navbar-default navbar-static-side "
                                      "ng-scope']/div[@class='sidebar-collapse']/ul[@id='side-menu']/li[4]").click()
    time.sleep(1)
    app.driver.find_element(By.XPATH, "//span[contains(text(),'Students')]").click()
    time.sleep(1)
    app.driver.find_element(By.XPATH, "//span[contains(text(),'Add New')]").click()
    app.driver.find_element(By. NAME, "FirstName").send_keys("Auto")
    app.driver.find_element(By.NAME, "LastName").send_keys("Test")
    app.driver.find_element(By.NAME, "phone").send_keys("444444")

    #app.driver.find_element(By.XPATH, "//button[contains(text(),'Save')]").click()

