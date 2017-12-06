import requests
import json


class googleMapService:
    def __init__(self):
        self.urlService = "https://maps.googleapis.com/maps/api/directions/json?"
        self.apiKey = "AIzaSyDh9EMTub3aewSOKjv_oyrRs8sOZjUQwek"
        this.cache = {}

    def getDistanceTimeAndPoints(self,fromString,toString):
        logging.info('Obteniendo distancia desde '+fromString+'hasta'+toString,extra=log_info)
        if (fromString,toString) in cache.keys():
            return cache[(fromString,toString)]
        else:
            response = json.loads(requests.get(url+'origin='+fromString+'&destination='+toString+'&key='+apiKey+"&alternatives=true"))
            parsedResponse = parseResponse(response)
            if (parsedResponse != None):
                cache[(fromString,toString)] = parsedResponse
                return parsedResponse
            return None


    def parseResponse(response):
        try:
            timeInMinutes = response['routes'][0]['legs'][0]['duration']['text']
            distanceInMeters = response['routes'][0]['legs'][0]['distance']['text']
            points = response['routes'][0]['overview_polyline']['points']
        except:
            logging.info('No se pudo obtener una respuesta ok del app google',extra=log_info)
            return None
        return {'distance':distanceInMeters,'time':timeInMinutes,'points':points}
