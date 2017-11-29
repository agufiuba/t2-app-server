import logging
import sys


this = sys.modules[__name__]
#Inicializo las posiciones de los usuarios
this.positions_from_user = {}
this.ifUserIsTraveling = {}


#Configuracion del loger
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'travelsService'}



def init(db_url,db="t2"):
    logging.info('Se inicializa el servicio con la db',extra=log_info)
    this.db = MongoClient(db_url)[db]


def addPositionInTimeFromUser(newPosition,newTime,userEmail):
    if userEmail not in positions_from_user:
        this.ifUserIsTraveling[email] = True
    else:
        value = verificateIfPassengerIsTraveling(newPosition,newTime,userEmail)
        this.ifUserIsTraveling[email] = value
    this.positions_from_user[email] = {'position':newPosition,'time':newTime}
    this.db.user_positions.insert_one({'email':email,'position':newPosition,'time':newTime})
    return true



def verificateIfPassengerIsTraveling(newPosition,newTime,userEmail):
    oldTimeAndPosition = positions_from_user[userEmail]
    return oldTimeAndPosition['position'] != position
