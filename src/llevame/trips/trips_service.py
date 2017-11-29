import sys
import logging

#Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'tripsService'}


this = sys.modules[__name__]
this.trips = {}


def addTrip(passengerID,driverID):
    this.trips[passengerID] = driverID
    return True
