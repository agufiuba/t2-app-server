import sys
import logging

#Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'sessionService'}


class SessionService:
    sessions = {}

    def addSession(self,userID,sessionToken):
        logging.info('Guardando una session (userID: ' + userID + ', sessionToken: ' + sessionToken + ').', extra=log_info)
        session_list = []
        if userID in SessionService.sessions.keys():
            session_list = SessionService.sessions[userID]
        session_list.append(sessionToken)
        SessionService.sessions[userID] = session_list

    def getSessionsList(self,userID):
        if userID not in SessionService.sessions.keys():
            return []
        return SessionService.sessions[userID]
