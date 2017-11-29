from my_firebase import firebase_service as firebaseService
from shared_service import shared_server_service as sharedService
from session import session_service as sessionService
import logging



#Configurando el loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'loginService'}



def login(request):
    logging.info('LLegó el pedido para loguear a un user',extra=log_info)
    id_token = request.headers['Authorization']
    session_token = request.headers['Session']
    logging.info('Se obtuvo el siquiente token del app android: '+id_token,extra=log_info)
    email = firebaseService.validate_token(id_token)
    userID = firebaseService.getUID(id_token)
    #Me guardo el token de session
    sessionService.addSession(userID,session_token)
    user =  sharedService.getUserFromEmail(email)
    if user != None:
        logging.info('El logueo fue exitoso para el usuario de email ['+email+']',extra=log_info)
        return convertType(int(user['type']))
    logging.info('El usuario no pudo loguearse porque no se encuentra en la db',extra=log_info)
    return None


def convertType(idType):
    if idType == 1:
        return 'passenger'
    return 'driver'
