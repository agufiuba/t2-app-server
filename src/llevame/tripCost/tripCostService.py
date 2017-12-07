import requests
import json
from shared_service import shared_server_service as sharedService
import logging
import sys
from tripCost.googleMapService import GoogleMapService
from shared_service.shared_server_service import SharedServerService

FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'tripCostService'}


class TripCostService():
    def __init__(self,googleMapService = GoogleMapService() ,sharedService = SharedServerService()):
        self.googleMapService = googleMapService
        self.sharedService = sharedService

    def getCostDistanceTimeAndCost(self,email,fromString,toString):
        response = self.googleMapService.getDistanceTimeAndPoints(fromString,toString)
        if response != None:
            logging.info('El string de distancia es el siguiente:'+response['distance'],extra=log_info)
            #Obtengo costo
            cost = self.sharedService.getCostFromDistanceInKM(email,response['distance'].split('k')[0])['costo']
            response['cost'] = cost['costo']
            logging.info('Devolviendo el tiempo,costo,distancia y puntos',extra=log_info)
            return response
        else:
            logging.info('No se pudo obtener los parametros distancia,tiempo',extra=log_info)
            return None
