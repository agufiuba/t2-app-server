import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import logging

#Configuracion del login
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'firebaseService'}


logging.info('Obteniendo credenciales',extra=log_info)
cred = credentials.Certificate('/as/src/llevame/firebase/serviceAccountKey.json')
logging.info('Levantanto la app de firebase',extra=log_info)
default_app = firebase_admin.initialize_app(cred)


def validate_token(id_token):
    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token['uid']
    logging.info('decoded_token'+uid,extra=log_info)
    user = auth.get_user(uid)
    logging.info('el user es:'+str(user.email)+"",extra=log_info)
    return str(user.email)


def getUID(token):
    decoded_token = auth.verify_id_token(token)
    uid = decoded_token['uid']
    logging.info('Obtenido UID'+uid,extra=log_info)
    user = auth.get_user(uid)
    logging.info('Se obtuvo el UID del usuario:'+str(user.email)+"",extra=log_info)
    return uid
