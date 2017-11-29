from pymongo import MongoClient
from bson.json_util import dumps
import sys
import logging
from my_firebase import firebase_service as firebaseService


#Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'driversService'}


this = sys.modules[__name__]
this.drivers = []



def getDriversAroundFrom(passengerPosition):
    logging.info('getDriversAroundFrom',extra=log_info)
    return firebaseService.getDriversArounPosition(passengerPosition,this.drivers)

    

# El ID es firebase id
def login_driver(ID):
    this.drivers.append(ID)
    return True
