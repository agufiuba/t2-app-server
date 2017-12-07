import unittest
from user.user_service import UserService
from shared_service.shared_server_service import SharedServerService

from user.mock.dataMock import driver,driverIncomplet,passenger,passengerIncomplete

def addUserMock(data):
    if data == driver:
        return True
    else if data == driverIncomplet:
        return False
    else if data == passenger:
        return True
    else if data == passengerIncomplete:
        return False

sharedServerService = SharedServerService()


sharedServerService.addUser = MagicMock(side_efect=addUserMock)


userService = UserService(sharedServerService)



class TestUserService(unittest.TestCase):
    def the_add_user_should_return_true_when_the_data_have_correct_format(self):
        assertTrue(True)
