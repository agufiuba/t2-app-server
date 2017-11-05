import requests
import json


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

    # TODO
    # def addUser(self, json):
    #
    # def getDataFromUser(self):
    #
    # def updateUser(self):
    #
    # def deleteUser(self):
