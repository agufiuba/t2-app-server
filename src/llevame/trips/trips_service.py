import sys
import logging
from notification import notification_service as notificationService

#Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'tripsService'}


this = sys.modules[__name__]
this.trips = {}


def addTrip(passengerID,driverID,fromPos,toPos):
    this.trips[passengerID] = driverID
    data = {'passengerID':passengerID,'from':fromPos,'to':toPos}
    notificationService.notificate_user(driverID,data)
    return True
