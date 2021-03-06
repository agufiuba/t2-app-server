import logging
from my_firebase.firebase_service import FirebaseService
from shared_service.shared_server_service import SharedServerService

FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'userService'}

class UserService:

    def __init__(self, sharedService = SharedServerService(),firebaseService = FirebaseService()):
        self.sharedService = sharedService
        self.firebaseService = firebaseService

    def addUser(self, user):
        logging.info('Se va a agregar un nuevo usuario, enviando solicitud al servicio del shared service',extra=log_info)
        return self.sharedService.addUser(user)

    def getUser(self, email):
        logging.info('Se va a obtener información de un nuevo usuario de email'+email,extra=log_info)
        response  = self.sharedService.getUserFromEmail(email)
        if (response != None):
            filted_response = {}
            for field in response:
                if field != 'id':
                    if field == 'type':
                        filted_response[field] = self.convertType(response[field])
                    else:
                        filted_response[field] = response[field]
            return filted_response
        else:
            return None

    def convertType(self, idType):
        if idType == 1:
            return 'passenger'
        return 'driver'

    def getDriverFromUID(self,UID):
        email = self.firebaseService.getEmailFromUid(UID)
        car = self.sharedService.getCarInfo(email)
        return {'car':car}
