import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db
import logging
from utils.position import Position
import os


#Configuracion del login
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'firebaseService'}



#Configuracion de firebase
logging.info('Obteniendo credenciales',extra=log_info)
logging.info('Levantanto la app de firebase',extra=log_info)

class FirebaseService:

    def initService(self):
        filename = os.path.join(os.path.dirname(__file__), 'serviceAccountKey.json')
        cred = credentials.Certificate(filename)
        self.default_app = firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://t2t2-9753f.firebaseio.com'
        })
        self.cacheUIDEmail = {}
        self.cacheEmailUID = {}

    def validate_token(self,id_token):
        logging.info('Validando token',extra=log_info)
        try:
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']
            logging.info('UID:'+uid,extra=log_info)
            email = self.getEmailFromUid(uid)
            logging.info('el user es:'+email+"",extra=log_info)
        except:
            logging.info('Hubo un error al tratar de iniciar la sesión',extra=log_info)
            return None
        return email


    def getUID(self,token):
        logging.info('Tratando de obtener el uid...',extra=log_info)
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        logging.info('Obtenido UID: '+uid,extra=log_info)
        user = auth.get_user(uid)
        logging.info('Se obtuvo el UID del usuario:'+str(user.email)+"",extra=log_info)
        return uid

    def getPositionFromId(self, driverID):
        ref = db.reference('localizations/'+driverID)
        driverPositionString = str(ref.get())
        logging.info('Se obtuvo la siguiente string de posición de firebase: ' + driverPositionString, extra=log_info)
        return Position(driverPositionString)

    def getEmailFromUid(self,uid):
        logging.info('Se esta pidiendo obtener el email del UID: '+uid,extra=log_info)
        user = auth.get_user(uid)
        logging.info('el user es:'+str(user.email)+"",extra=log_info)
        return str(user.email)
