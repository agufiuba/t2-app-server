import logging
from my_firebase.firebase_service import FirebaseService
from shared_service.shared_server_service import SharedServerService

FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'parametersService'}

class ParametersService:
    def __init__(self,firebaseService = FirebaseService(),sharedService = SharedServerService()):
        self.firebase_service = firebaseService
        self.shared_service = sharedService
