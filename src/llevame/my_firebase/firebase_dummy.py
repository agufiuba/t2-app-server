from .firebase_service import haversine
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

    def add_user(self, token, user):
        self.datos_segun_token[token] = user
        self.addEmailAndUid(user["mail"], user["id"])

    def getUID(self, token):
        return self.datos_segun_token[token]["id"]

    def calculateDistance(self, position,otherPosition):
        return self.haversine(position['lng'],position['lat'],otherPosition['lng'],otherPosition['lat'])

    def getDriversArounPosition(self, passengerPosition,driversListID):
        # TODO esto le corresponde más al servicio de drivers que al de firebase.
        nearbyDriverIDsList = []
        for driverID in driversListID:
            driverPosition = positionTransformer.parserStringToPosition(str(ref.get()))
            if self.calculateDistance(passengerPosition,driverPosition) <= 100 :
                nearbyDriverIDsList.append({'id':driverID,'pos':driverPosition})
        return nearbyDriverIDsList

    def addEmailAndUid(self, email, UID):
        self.emails[UID] = email

    def getEmailFromUid(self, UID):
        return self.emails[UID]
