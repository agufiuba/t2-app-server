import logging
from math import radians, cos, sin, asin, sqrt

#Configuracion del login
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'positionTransformer'}

class Position:
    # positionString = lat/lng: (-34.6220855,-58.3832781)
    def __init__(self, position_string):
        logging.info('Transformando el siguiente string:'+position_string,extra=log_info)
        list_of_positions = position_string.split(':')[1].replace('(','').replace(')','').split(',')
        logging.info('La posiciones son:'+list_of_positions[0]+'y:'+list_of_positions[1],extra=log_info)
        self.lat = float(list_of_positions[0])
        self.lng = float(list_of_positions[1])

    def haversine(self, lon1, lat1, lon2, lat2):
        """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)
        """
        logging.info('Calculando distancia',extra=log_info)
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        # Radius of earth in kilometers is 6371
        km = 6371* c
        logging.info('La distancia es: ' + str(km), extra=log_info)
        return km

    def distance(self, otherPosition):
        logging.info('position:'+ str(self), extra=log_info)
        logging.info('position:'+ str(otherPosition), extra=log_info)
        return self.haversine(self.lng, self.lat, otherPosition.lng, otherPosition.lat)

    def __str__(self):
        return "Lat: " + str(self.lat) + "; Long: " + str(self.lng)
