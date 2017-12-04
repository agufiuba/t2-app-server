import sys
import logging
from notification import notification_service as notificationService
from my_firebase import firebase_service as firebaseService
from user import user_service as userService
from trips import tripCostService

#Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'tripsService'}


this = sys.modules[__name__]
this.trips = {}


def addTrip(passengerID,driverID,fromPos,toPos):
    logging.info('Se esta agregando un nuevo viaje',extra=log_info)
    this.trips[passengerID] = driverID
    nameAndLasName = getNameAndLastNameFromUID(driverID)
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



def getNameAndLastNameFromUID(UID):
    email = firebaseService.getEmailFromUid(UID)
    userInformation =  userService.getUser(email)
    return {'name':userInformation['name'],'last_name':userInformation['last_name']}
