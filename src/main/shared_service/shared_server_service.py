import requests
import json
from . import data_transformator_query_params as transformator
import logging
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'sharedService'}

token = ""
shared_server_addr = "http://localhost:4000"
def getToken():
    logging.info("Obteniendo el token de autenticacion",extra=log_info)
    code = 0
    while(code != 200):
        r = request.get(shared_server_addr+"/login")
        code = r.status_code
    data  = json.loads(r.text)
    token = data["id"]

def addUser(data):
    stringQuery = transformator.transformate(data)
    response = requests.post(self.shared_server_addr+'?'+stringQuery)
    return r.status_code


def getDataFromUser(id):
    return 'getDataFromUser'


def deleteUser(self,id):
    return 'deleteUser'
