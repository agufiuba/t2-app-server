import requests
import json
from . import dataTransformatorQueryParams as transformator
import logging
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'sharedService'}

id = ""
token = ''
shared_server_addr = "http://shared-server:4000"

def getToken():
    logging.info("Obteniendo el token de autenticacion",extra=log_info)
    code = 0
    while(code != 200):
        logging.info('Realizando request a ['+shared_server_addr+'/login'+']',extra=log_info)
        res = requests.get(shared_server_addr+"/login")
        code = res.status_code
    token = res.headers['Authorization']
    logging.info('El token es:'+token,extra=log_info)

def addUser(user):
    logging.info('Agregando un usuario',extra=log_info)
    stringQuery = transformator.transformate(user)
    url = shared_server_addr+'/users'+'?'+stringQuery;
    logging.info('Realizando un POST al shared server con url ['+url+']',extra=log_info)
    res = requests.post(url)
    logging.info('Se recibio un '+ str(res.status_code)+" del shared server",extra=log_info)
    return res.status_code == 200 or res.status_code == 201


def getDataFromUser(id):
    return 'getDataFromUser'


def deleteUser(self,id):
    return 'deleteUser'
