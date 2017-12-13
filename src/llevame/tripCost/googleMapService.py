import requests
import json
import logging




FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'googleMapService'}

class GoogleMapService:
    def __init__(self):
        self.urlService = "https://maps.googleapis.com/maps/api/directions/json?"
        self.apiKey = "AIzaSyDh9EMTub3aewSOKjv_oyrRs8sOZjUQwek"
        self.cache = {}

    def getDistanceTimeAndPoints(self,fromString,toString):
        logging.info('Obteniendo distancia desde '+fromString+'hasta'+toString,extra=log_info)
        if (fromString,toString) in self.cache.keys():
            return self.cache[(fromString,toString)]
        else:
            response = json.loads(requests.get(self.urlService+'origin='+fromString+'&destination='+toString+'&key='+self.apiKey+"&alternatives=true").text)
            parsedResponse = self.parseResponse(response)
            if (parsedResponse != None):
                self.cache[(fromString,toString)] = parsedResponse
                return parsedResponse
            return None


    def parseResponse(self,response):
        try:
            timeInMinutes = response['routes'][0]['legs'][0]['duration']['text']
            distanceInMeters = response['routes'][0]['legs'][0]['distance']['text']
            points = response['routes'][0]['overview_polyline']['points']
        except:
            logging.info('No se pudo obtener una respuesta ok del app google',extra=log_info)
            return None
        return {'distance':distanceInMeters,'time':timeInMinutes,'points':points}
