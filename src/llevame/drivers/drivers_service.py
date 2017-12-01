import logging

# Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'driversService'}

class DriverService:
    def __init__(self, interfaces):
        self.drivers = []
        self.firebaseService = interfaces.get_firebase_service()

    def getDriversAroundFrom(self, passengerPosition):
        logging.info('getDriversAroundFrom', extra=log_info)
        return self.firebaseService.getDriversArounPosition(passengerPosition, self.drivers)

    # El ID es firebase id
    def login_driver(self, ID):
        self.drivers.append(ID)
        return True

    def delete_driver(self, ID):
        self.drivers.remove(ID)
        return True
