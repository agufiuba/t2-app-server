import logging
import sys

#Configuracion del loger
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'positionService'}

class PositionService:
    def __init__(self, interfaces):
        #Inicializo las posiciones de los usuarios
        self.positions_from_user = {}
        self.ifUserIsTraveling = {}

        logging.info('Se inicializa el servicio con la db',extra=log_info)
        self.db = MongoClient(interfaces.get_mongo_uri())[interfaces.get_mongo_db_name()]


    def addPositionInTimeFromUser(self, newPosition, newTime, userEmail):
        if userEmail not in self.positions_from_user:
            self.ifUserIsTraveling[email] = True
        else:
            value = self.verificateIfPassengerIsTraveling(newPosition, newTime, userEmail)
            self.ifUserIsTraveling[email] = value
        self.positions_from_user[email] = {'position':newPosition, 'time':newTime}
        self.db.user_positions.insert_one({'email':email, 'position':newPosition,' time':newTime})
        return true



    def verificateIfPassengerIsTraveling(self, newPosition, newTime, userEmail):
        oldTimeAndPosition = self.positions_from_user[userEmail]
        return oldTimeAndPosition['position'] != position
