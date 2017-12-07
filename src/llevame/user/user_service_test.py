import unittest
from user.user_service import UserService
from shared_service.shared_server_service import SharedServerService
from my_firebase.firebase_service import FirebaseService
from user.mock.dataMock import driver,driverIncomplet,passenger,passengerIncomplete
import mock

def addUserMock(data):
    if data == driver:
        return True
    elif data == driverIncomplet:
        return False
    elif data == passenger:
        return True
    elif data == passengerIncomplete:
        return False

def getUserFromEmailMock(email):
    if email == 'cristian3629@gmail.com':
        copy = dict(driver)
        copy.pop('car')
        copy['id'] = 'xx'
        return copy

    if email == 'cristian3629xx@gmail.com':
        copy = dict(passenger)
        copy.pop('card')
        copy['id'] = 'xx'
        return copy
    return None

sharedServerService = SharedServerService()
firebaseService = FirebaseService()

sharedServerService.addUser = mock.MagicMock(side_efect=addUserMock)
sharedServerService.getUserFromEmail =  mock.MagicMock(side_efect = getUserFromEmailMock)

userService = UserService(sharedServerService)



class TestUserService(unittest.TestCase):
    def test_the_add_user_should_return_true_when_the_data_have_correct_format(self):
        assertTrue(userService.addUser(driver))

    def test_the_add_user_should_return_false_when_the_data_have_incorrect_format_driver(self):
        assertFalse(userService.addUser(driverIncomplet))

    def test_the_add_user_should_return_true_when_the_data_have_correct_format_passenger(self):
        assertTrue(userService.add(passenger))

    def test_the_add_user_should_return_false_when_the_data_have_incorrect_format_passenger(self):
        assertTrue(userService.add(passengerIncomplete))


    def test_the_convertType_shoud_return_passenger(self):
        assertTrue(userService.convertType(1) == 'passenger')

    def test_the_convertType_shoud_return_driver(self):
        assertTrue(userService.convertType(2) == 'driver')


    def test_getUser_should_filter_from_shared_response(self):
        copy = dict(driver)
        excepted = copy.pop('car')
        assertTrue(userService.getUser('cristian3629@gmail.com') == excepted)

    def test_getUser_should_filter_from_shared_response_again(self):
        copy = dict(passenger)
        excepted = copy.pop('card')
        assertTrue(userService.getUser('cristian3629xx@gmail.com') == excepted)

    def test_getUser_should_return_None_when_shared_returns_None(self):
        assertTrue(userService.get('userNotExits@gmail.com') == None)
