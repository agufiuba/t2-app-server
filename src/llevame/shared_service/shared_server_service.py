import requests
import json
from . import dataTransformatorQueryParams as transformator
import logging
import os


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'sharedService'}


token = ''
shared_server_addr = os.environ["SHARED_SERVER_ADDR"]
logging.info("La dirección del shared server es: " + shared_server_addr, extra=log_info)

def getToken():
    logging.info("Obteniendo el token de autenticacion",extra=log_info)
    code = 0
    while(code != 200):
        logging.info('Realizando request a ['+shared_server_addr+'/login'+']',extra=log_info)
        try:
            res = requests.get(shared_server_addr+"/login")
            code = res.status_code
            token = res.headers['Authorization']
        except ConnectionError:
            logging.info('Se rechazó conexion',extra=log_info)
    logging.info('El token es:'+token,extra=log_info)
    logging.info('El inicio fue OK',extra=log_info)

def addUser(user):
    logging.info('Agregando un usuario',extra=log_info)
    stringQuery = transformator.transformate(user)
    url = shared_server_addr+'/users'+'?'+stringQuery;
    logging.info('Realizando un POST al shared server con url ['+url+']',extra=log_info)
    res = requests.post(url)
    logging.info('Se recibio un '+ str(res.status_code)+" del shared server",extra=log_info)
    return res.status_code == 200 or res.status_code == 201


def getUserFromEmail(email):
    logging.info('Obteniendo información del usuario ['+email+']',extra=log_info)
    url = shared_server_addr+'/users/'+email
    logging.info('Realizando GET al shared server con url +['+url+']',extra=log_info)
    res = requests.get(url)
    code = res.status_code
    if code != 200 and code !=201 :
        logging.info('Hubo un problema al tratar de obtener información del user',extra=log_info)
        return None;
    logging.info('Se obtuvo la información de manera correcta',extra=log_info)
    return json.loads(res.text)


def deleteUser(self,id):
    return 'deleteUser'



def getCostFromDistanceInKM(userEmail,distanceInKM):
    logging.info('Calculando la el costo de viaje para '+userEmail+' y distancia '+str(distanceInKM),extra=log_info)
    url = shared_server_addr+'/cost/'+userEmail+'/'+str(distanceInKM)
    logging.info('Realizo request al shared server con el siguiente request',extra=log_info)
    res = requests.get(url)





def getPayMethods():
    logging.info('Llegó una solicitud para poder obtener los medios de pagos',extra=log_info)
    url = shared_server_addr+'/paymethods'
    logging.info('Se esta enviando un GET a la siguiente url'+url,extra=log_info)
    res = requests.get(url)
    return json.loads(res.text)
