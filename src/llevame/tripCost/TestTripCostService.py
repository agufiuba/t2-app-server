import unittest
from tripsCost.googleMapService import GoogleMapService
from shared_service.shared_server_service import SharedServerService

def MockgetDistanceTimeAndPoints(fromString,toString):
    if fromString == '-34.617952,-58.385983' and toString == '-34.617952,-58.385923':
        return {'distance':'1.6km','time':'5.5 hs','points':'xxx'}
    if fromString == '-33.617952,-58.385983' and toString == '-34.617952,-57.385923':
        return {'distance':'2.7km','time':'9 hs','points':'xxx'}
    return None

def MockgetCostFromDistanceInKM(email,fromString,toString):
    if email == 'user@gmail.com' and fromString == '-34.617952,-58.385983' and toString = '-34.617952,-58.385923':
        return '120'
    if email == 'user2@gmail.com' and fromString == '-33.617952,-58.385983' and toString = '-34.617952,-57.385923':
        return '100'
    return None

class testTripCostService(unittest.TestCase):
    def __init__(self):
        googleMapService = GoogleMapService()
        googleMapService.getDistanceTimeAndPoints = MagicMock(side_efect = MockgetDistanceTimeAndPoints)
        sharedServerService = SharedServerService()
        sharedServerService.getCostFromDistanceInKM = MagicMock(side_efect = MockgetCostFromDistanceInKM)
        self.tripCostService = TripCostService(googleMapService,sharedServerService)

    def the_value_should_be_equal(self):
        actual = self.tripCostService.getCostDistanceTimeAndCost('user@gmail.com','-34.617952,-58.385983','-34.617952,-58.385923')
        assertTrue(actual == {'distance':'1.6km','time':'5.5 hs','points':'xxx','cost':'120'})

    def the_value_should_be_equal_again(self):
        actual = self.tripCostService.getCostDistanceTimeAndCost('user@gmail.com','-34.617952,-58.385983','-34.617952,-58.385923')
        assertTrue(actual == {'distance':'2.7km','time':'9 hs','points':'xxx','cost':'100'})


    def the_value_shoud_be_None(self):
        actual = self.tripsCostService.getCostDistanceTimeAndCost('user_no_exist@gmail.com','xxx','xxx')
        assertTrue(actual == None)
