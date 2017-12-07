import unittest
from user.user_service import UserService
from shared_service.shared_server_service import SharedServerService
from my_firebase.firebase_service import FirebaseService
from user.mock.dataMock import driver,driverIncomplet,passenger,passengerIncomplete

def addUserMock(data):
    if data == driver:
        return True
    elif data == driverIncomplet:
        return False
    elif data == passenger:
        return True
    elif data == passengerIncomplete:
        return False

sharedServerService = SharedServerService()
firebaseService = FirebaseService()

sharedServerService.addUser = MagicMock(side_efect=addUserMock)


userService = UserService(sharedServerService)



class TestUserService(unittest.TestCase):
    def the_add_user_should_return_true_when_the_data_have_correct_format(self):
        assertTrue(userService.addUser(driver))

    def the_add_user_should_return_false_when_the_data_have_incorrect_format_driver(self):
        assertFalse(userService.addUser(driverIncomplet))

    def the_add_user_should_return_true_when_the_data_have_correct_format_passenger(self):
        assertTrue(userService.add(passenger))

    def the_add_user_should_return_false_when_the_data_have_incorrect_format_passenger(self):
        assertTrue(userService.add(passengerIncomplete))
