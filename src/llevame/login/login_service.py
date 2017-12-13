from shared_service import shared_server_service as sharedService
from session.session_service import SessionService
import logging

from my_firebase.firebase_service import FirebaseService
from shared_service.shared_server_service import SharedServerService

#Configurando el loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'loginService'}

class LoginService:

    def __init__(self, firebaseService = FirebaseService(), sharedService = SharedServerService(),sessionService = SessionService()):
        self.firebaseService = firebaseService
        self.sharedService = sharedService
        self.sessionService = sessionService

    def login(self, request):
        logging.info('LLegó el pedido para loguear a un user',extra=log_info)
        id_token = request.headers['Authorization']
        session_token = request.headers['Session']
        logging.info('Se obtuvo el siquiente token del app android: '+id_token,extra=log_info)
        logging.info('Se obtuvo el siquiente token de session: '+session_token,extra=log_info)
        email = self.firebaseService.validate_token(id_token)
        userID = self.firebaseService.getUID(id_token)
        #Me guardo el token de session
        self.sessionService.addSession(userID,session_token)
        user =  self.sharedService.getUserFromEmail(email)
        if user != None:
            logging.info('El logueo fue exitoso para el usuario de email ['+email+']',extra=log_info)
            return self.convertType(int(user['type']))
        logging.info('El usuario no pudo loguearse porque no se encuentra en la db',extra=log_info)
        return None

    def convertType(self, idType):
        if idType == 1:
            return 'passenger'
        return 'driver'
