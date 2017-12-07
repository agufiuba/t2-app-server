import sys
import logging

#Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'sessionService'}


this = sys.modules[__name__]
this.sessions = {}

class SessionService:
    def addSession(self,userID,sessionToken):
        logging.info('Guardando una session',extra=log_info)
        session_list = []
        if userID in sessions.keys():
            session_list = sessions[userID]
        session_list.append(sessionToken)
        sessions[userID] = session_list

        def getSessionsList(self,userID):
            if userID not in sessions.keys():
                return []
            return sessions[userID]
