import requests
import pytest


@pytest.fixture(scope="session")
def get_token():
    response = requests.post("http://pilotstub.qlogic.io/api/api/users/auth", data={"Email":"max@qlogic.io","Password":"TjQ4ODVM"})
    token = response.json()["token"]
    return {"Authorization": token}


def test_get_schedules(get_token):
    response = requests.post("http://pilotstub.qlogic.io/api/api/reservation/getSchedules", headers=get_token,
                             json={"memberID":0,"ManufacturerKey":"","AircraftKey":"","isAdmin":True,"userKey":544,"instructorID":0,"SelectedDate":"02/22/2020","FlightSchoolID":1,"onlyPeople":False,"calendarView":"agendaTwoDay","StartDateRange":"2020-02-22T15:16:24.454Z","EndDateRange":"2020-02-22T15:16:24.454Z"})
    print(response.status_code)
    print(response.json())


def test_save_schedule(get_token):
    response = requests.post("http://pilotstub.qlogic.io/api/api/reservation/save", headers=get_token,
                             json=[{"ActivityName":"Dual Training",
                                     "StartDate":"03/01/2020",
                                     "StartTime":"12:00 AM",
                                     "EndDate":"03/01/2020",
                                     "EndTime":"02:00 AM",
                                     "isRecurring":False,
                                     "color":"#1E90FF",
                                     "ManufacturerKey":"5FF8BCDC-C66B-4672-9122-30AC541F49AB",
                                     "AircraftKey":"D7A45083-D8EF-4E03-AED2-41563F6D5962",
                                     "Notification":{"Type":"","Email":"","People":[]},
                                     "InstructorId":"",
                                     "Member1":"",
                                     "Member2":"",
                                     "enterNameManual":False,
                                     "FirstName":"",
                                     "LastName":"",
                                     "Email":"",
                                     "CellPhone":"",
                                     "SendEmailNotification":True,
                                     "InstructorComment":"",
                                     "AdditionalEmail":"",
                                     "LocationID":24,
                                     "DisplayName":"Autotest",
                                     "EstimateFlightHours":"",
                                     "FlightType":"",
                                     "FlightRules":"",
                                     "FlightRoute":"",
                                     "FlightSchoolID":1,
                                     "allowBooking":True,
                                     "isMainModel":True,
                                     "aircraftConflict":None,
                                     "Location":"Location-A",
                                     "InstructorConflict":None,
                                     "FirstMemberConflict":None,
                                     "SecondMemberConflict":None,
                                     "DatetoAdd":["2020-02-22T00:00:00"],
                                     "InstructorNonAvailability":None,
                                     "RentalNonAvailability":None,
                                     "dates":"02/22/2020","aircraftconflict":"",
                                     "instructorconflict":"",
                                     "fmemberconflict":"",
                                     "smemberconflict":"",
                                     "instructornonavailability":"",
                                     "rentalnonavailability":"",
                                     "Member1Name":None,
                                     "Member2Name":None,
                                     "Instructor":None,
                                     "Manufacturer":"Test Test",
                                     "Registration":"Test",
                                     "RegistrationKey":"D7A45083-D8EF-4E03-AED2-41563F6D5962",
                                     "DatesToAdd":["2020-02-22T00:00:00"],
                                     "Notify":True,
                                     "UserID":544}])

    assert response.status_code == 200
    assert response.json() == {'Message': 'Reservation added successfully'}