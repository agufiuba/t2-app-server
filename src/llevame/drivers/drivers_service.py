import logging
from my_firebase.firebase_service import FirebaseService

# Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'driversService'}

class DriverService:
    def __init__(self,firebaseService = FirebaseService()):
        # Lista de Ids de conductores.
        self.drivers = []
        self.firebaseService = firebaseService

    def getDriversAroundFrom(self, passengerPosition):
        nearbyDriverIDsList = []
        logging.info('Se están calculando las posiciones cercanas al pasajero', extra=log_info)

        for driverID in self.drivers:
            driverPosition = self.firebaseService.getPositionFromId(driverID)
            if driverPosition.distance(passengerPosition) <= 100:
                nearbyDriverIDsList.append({'id':driverID, 'pos':driverPosition})

        logging.info('Devolviendo los choferes cercanos:'+ str(nearbyDriverIDsList), extra=log_info)
        return nearbyDriverIDsList

    # El ID es firebase id
    def login_driver(self, ID):
        self.drivers.append(ID)
        return True

    def delete_driver(self, ID):
        try:
            self.drivers.remove(ID)
            return True
        except ValueError:
            return False
