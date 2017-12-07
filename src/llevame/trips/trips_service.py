import sys
import logging
from notification import notification_service as notificationService
from my_firebase.firebase_service import FirebaseService
from user.user_service import UserService
from tripCost.tripCostService import TripCostService
from session.session_service import SessionService
from drivers.drivers_service import DriverService
#Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'tripsService'}


this = sys.modules[__name__]
this.trips = {}
this.withUser = {}
tripCostService = TripCostService()
userService = UserService()
driverService = DriverService()
sessionService = SessionService()
firebaseService = FirebaseService()

def addTrip(passengerID,driverID,fromPos,toPos):
    logging.info('Se esta agregando un nuevo viaje',extra=log_info)
    this.trips[(passengerID,driverID)] = 'WAIT_DRIVER_CONFIRMATION'
    this.withUser[driverID] = passengerID
    this.withUser[passengerID] = driverID
    nameAndLasName = getNameAndLastNameFromUID(driverID)
    driverService.delete_driver(driverID)
    data = {
        '_passengerID':passengerID,
        '_from':fromPos,
        '_to':toPos,
        '_passengerName':nameAndLasName['name'],
        '_passengerLastName':nameAndLasName['last_name'],
        '_polyline':tripCostService.getGoogleResponse(getLatAndLngFromString(fromPos),getCostAndDistance(toPos))['points']
    }
    notificationService.notificate_user(driverID,data)
    return True


#Input : 'lat/lng: (-34.617952,-58.385983)'
#Output: '-34.617952,-58.385983'
def getLatAndLngFromString(aString):
    return aString.split(')')[0].split('(')[1]



def driverInWay(driverID):
    passengerID = this.withUser[driverID]
    data_for_passenger = {'sessionIDs':sessionService.getSessionsList(driverID)}
    notificationService.notificate_user(passengerID,data_for_passenger)
    data_for_driver = {'sessionIDs':sessionService.getSessionsList(passengerID)}
    notificationService.notificate_user(driverID,data_for_driver)
    this.trips[(passengerID,driverID)] = 'DRIVER IN WAY'


def getNameAndLastNameFromUID(UID):
    email = firebaseService.getEmailFromUid(UID)
    userInformation =  userService.getUser(email)
    return {'name':userInformation['name'],'last_name':userInformation['last_name']}
