import requests
import json
from . import data_transformator_query_params as transformator

class SharedServerService:
    def __init__(self):
        self.shared_server_addr = "http://localhost:3000" # NOTE esto es solo local.
        # NOTE se llamaría a getToken acá?

    def getToken(self):
        code = 0
        while(code != 200):
            r = requests.get(self.shared_server_addr + "/login")
            code = r.status_code
        data = json.loads(r.text)
        self.token = data["id"]

    #Pre: recibo un dict con todo los parametros
    #Post: devuelvo el codigo de respuesta del shared: 200,400
    def addUser(self, data):
        stringQuery = transformator.transformate(data)
        response = requests.post(self.shared_server_addr+'?'+stringQuery)
        return r.status_code

    def getDataFromUser(self,id):
        return 'getDataFromUser'

    def updateUser(self,id,data):
        return 'updateUser'

    def deleteUser(self,id):
        return 'deleteUser'
