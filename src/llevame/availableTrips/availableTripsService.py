from tripCost.tripCostService import TripCostService
from pymongo import MongoClient
from bson.json_util import dumps
import logging
import sys
from shared_service.shared_server_service import SharedServerService
from tripCost.tripCostService import TripCostService


# Configuración de Log
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'availableTripsService'}

class AvailableTripService:

    def __init__(self, interfaces):
        logging.info('Se inicializa el servicio con la db',extra=log_info)
        logging.info('URL de DB: ' + str(interfaces.get_mongo_uri()),extra=log_info)
        self.sharedService = SharedServerService()
        self.tripCostService = TripCostService()

    # fromPlace porque from es reservado de python
    def addTravel(self, email, data):
        # Si el user existe
        if user != None:
            logging.info('El usuario '+email+' sí se encuentra registrado',extra=log_info)
            response = self.tripCostService.getCostDistanceTimeAndCost(email,data['from'],data['to'])
            if response != None:
                logging.info('Se agrego correctamente el viaje',extra=log_info)
                return response
            else:
                return None
        logging.info('El usuario no se encuentra registrado, no se agrega viaje',extra=log_info)
        return None
