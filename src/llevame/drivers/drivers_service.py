import logging
from my_firebase.firebase_service import FirebaseService

# Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'driversService'}

class DriverService:
    def __init__(self,firebaseService = FirebaseService()):
        self.drivers = []
        self.firebaseService = firebaseService

    def getDriversAroundFrom(self, passengerPosition):
        logging.info('getDriversAroundFrom', extra=log_info)
        return self.firebaseService.getDriversArounPosition(passengerPosition, self.drivers)

    # El ID es firebase id
    def login_driver(self, ID):
        self.drivers.append(ID)
        return True

    def delete_driver(self, ID):
        if ID in self.drivers:
            self.drivers.remove(ID)
        return True
