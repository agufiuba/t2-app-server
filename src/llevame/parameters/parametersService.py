import logging

FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'parametersService'}

class ParametersService:
    def __init__(self, interfaces):
        self.firebase_service = interfaces.get_firebase_service()
        self.shared_service = interfaces.get_firebase_service()
