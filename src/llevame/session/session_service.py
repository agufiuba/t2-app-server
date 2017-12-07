import sys
import logging

#Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'sessionService'}


class SessionService:
    def __init__(self):
        self.sessions = {}

    def addSession(self,userID,sessionToken):
        logging.info('Guardando una session',extra=log_info)
        session_list = []
        if userID in self.sessions.keys():
            session_list = self.sessions[userID]
        session_list.append(sessionToken)
        self.sessions[userID] = session_list

    def getSessionsList(self,userID):
        if userID not in self.sessions.keys():
            return []
        return self.sessions[userID]
