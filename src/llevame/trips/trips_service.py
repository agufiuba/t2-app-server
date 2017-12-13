import sys
import logging
from notification import notification_service as notificationService
from my_firebase.firebase_service import FirebaseService
from user.user_service import UserService
from tripCost.tripCostService import TripCostService
from session.session_service import SessionService
from drivers.drivers_service import DriverService
from shared_service.shared_server_service import SharedServerService

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
shared_service = SharedServerService()

def addTrip(passengerID,driverID,fromPos,toPos, payMethod):
    logging.info('Se esta agregando un nuevo viaje',extra=log_info)
    this.trips[(passengerID,driverID)] = 'WAIT_DRIVER_CONFIRMATION'
    this.withUser[driverID] = passengerID
    this.withUser[passengerID] = driverID
    nameAndLasName = getNameAndLastNameFromUID(driverID)
    driverService.delete_driver(driverID)

    # Datos para mandarle el pago al shared_server.
    user_email = firebaseService.getEmailFromUid(passengerID)
    driver_email = firebaseService.getEmailFromUid(driverID)
    viaje = tripCostService.getCostDistanceTimeAndCost(user_email, getLatAndLngFromString(fromPos),getLatAndLngFromString(toPos))
    distancia = viaje["distance"]
    shared_service.addTrip(user_email, driver_email, distancia, payMethod)

    # Datos para notificarle al conductor que tiene un viaje.
    data = {
        '_passengerID':passengerID,
        '_from':fromPos,
        '_to':toPos,
        '_passengerName':nameAndLasName['name'],
        '_passengerLastName':nameAndLasName['last_name'],
        '_polyline': viaje['points']
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
