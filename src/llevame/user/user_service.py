import logging
from shared_service import shared_server_service as sharedService


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'userService'}


def addUser(user):
    logging.info('Se va a agregar un nuevo usuario, enviando solicitud al servicio del shared service',extra=log_info)
    return sharedService.addUser(user)


def getUser(email):
    logging.info('Se va a obtener información de un nuevo usuario de email'+email,extra=log_info)
    response  = sharedService.getUserFromEmail(email)
    if (response != None):
        filted_response = {}
        for field in response:
            if field != 'id':
                if field == 'type':
                    filted_response[field] = convertType(response[field])
                else:
                    filted_response[field] = response[field]
        return filted_response
    else:
        return None


def convertType(idType):
    if idType == 1:
        return 'passenger'
    return 'driver'
