import requests
import json
from shared_service import shared_server_service as sharedService
import logging
import sys
from tripCost import googleMapService


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'tripCostService'}


class tripCostService():
    def __init__(self,googleMapService,sharedService):
        self.googleMapService = googleMapService
        self.sharedService = sharedService

    def getCostDistanceTimeAndCost(self,email,fromString,toString):
        response = self.googleMapService(fromString,toString)
        if googleResponse != None:
            logging.info('El string de distancia es el siguiente:'+googleResponse['distance'],extra=log_info)
            #Obtengo costo
            cost = self.sharedService.getCostFromDistanceInKM(email,googleResponse['distance'].split('k')[0])['costo']
            response['cost'] = cost
            logging.info('Devolviendo el tiempo,costo,distancia y puntos',extra=log_info)
            return response
        else:
            logging.info('No se pudo obtener los parametros distancia,tiempo',extra=log_info)
            return None
    
