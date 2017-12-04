from .firebase_service import haversine
from utils import positionTransformer
import logging

#Configuracion del login
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'firebase_dummy'}

class FirebaseDummy:
    def __init__(self, posiciones = {}, datos_segun_token = {}):
        self.datos_segun_token = datos_segun_token
        self.posiciones_segun_driver_id = posiciones
        self.emails = {}

    def validate_token(self, id_token):
        if id_token in self.datos_segun_token:
            return self.datos_segun_token[id_token]["mail"]
        else:
            return None

    # (Método para tests) El token es una string y el usuario es un diccionario.
    def add_user(self, token, user, pos):
        self.datos_segun_token[token] = user
        self.posiciones_segun_driver_id[user["id"]] = pos
        self.addEmailAndUid(user["mail"], user["id"])

    # (Método para tests) Se asume que la lista tiene duplas (token, usuario).
    def add_user_list(self, users):
        for user in users:
            self.add_user(user[0], user[1], user[2])

    def getUID(self, token):
        return self.datos_segun_token[token]["id"]

    def calculateDistance(self, position,otherPosition):
        return haversine(position['lng'],position['lat'],otherPosition['lng'],otherPosition['lat'])

    def getDriversArounPosition(self, passengerPosition,driversListID):
        # TODO esto le corresponde más al servicio de drivers que al de firebase.
        nearbyDriverIDsList = []
        for driverID in driversListID:
            driverPosition = positionTransformer.parserStringToPosition(self.posiciones_segun_driver_id[driverID])
            if self.calculateDistance(passengerPosition,driverPosition) <= 100 :
                nearbyDriverIDsList.append({'id':driverID,'pos':driverPosition})
        return nearbyDriverIDsList

    def addEmailAndUid(self, email, UID):
        self.emails[UID] = email

    def getEmailFromUid(self, UID):
        return self.emails.get(UID, None)
