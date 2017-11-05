import logging
from ..shared_service import shared_server_service as sharedService


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'userService'}


def addUser(user):
    logging.info('Se va a agregar un nuevo usuario, enviando solicitud al servicio del shared service',extra=log_info)
    return sharedService.addUser(user)
