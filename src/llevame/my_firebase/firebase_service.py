import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db

import logging
from math import radians, cos, sin, asin, sqrt
from utils import positionTransformer
import os


#Configuracion del login
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'firebaseService'}



#Configuracion de firebase
logging.info('Obteniendo credenciales',extra=log_info)
filename = os.path.join(os.path.dirname(__file__), 'serviceAccountKey.json')
cred = credentials.Certificate(filename)
logging.info('Levantanto la app de firebase',extra=log_info)
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://t2t2-9753f.firebaseio.com'
})



def validate_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        logging.info('decoded_token'+uid,extra=log_info)
        email = getEmailFromUid(uid)
        logging.info('el user es:'+email+"",extra=log_info)
    except ValueError:
        logging.info('Hubo un error al tratar de iniciar la sesión',extra=log_info)
        return None
    return email


def getUID(token):
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']
    logging.info('Obtenido UID'+uid,extra=log_info)
    user = auth.get_user(uid)
    logging.info('Se obtuvo el UID del usuario:'+str(user.email)+"",extra=log_info)
    return uid



def haversine(lon1, lat1, lon2, lat2):
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
    logging.info('La distancia es:'+str(km),extra=log_info)
    return km


def calculateDistance(position,otherPosition):
    logging.info('position:'+str(position),extra=log_info)
    logging.info('position:'+str(otherPosition),extra=log_info)
    return haversine(position['lng'],position['lat'],otherPosition['lng'],otherPosition['lat'])


def getDriversArounPosition(passengerPosition,driversListID):
    nearbyDriverIDsList = []
    logging.info('Se esta calculando las posiciones cercanas al pasajero',extra=log_info)
    for driverID in driversListID:
        ref = db.reference(driverID)
        # TODO es necesario o siquiera razonable hacer dos res.get? no es mejor guardarlo?
        driverPositionString = str(ref.get())
        logging.info('Se obtuvo la siguiente respuesta de firebase:'+driverPositionString,extra=log_info)
        driverPosition = positionTransformer.parserStringToPosition(str(ref.get()))
        if calculateDistance(passengerPosition,driverPosition) <= 100 :
            nearbyDriverIDsList.append({'id':driverID,'pos':driverPosition})
    return nearbyDriverIDsList



def getEmailFromUid(uid):
        logging.info('Se esta pidiendo obtener el email del UID: '+uid,extra=log_info)
        user = auth.get_user(uid)
        logging.info('el user es:'+str(user.email)+"",extra=log_info)
        return str(user.email)
