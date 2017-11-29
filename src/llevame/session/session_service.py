import sys
import logging

#Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'sessionService'}


this = sys.modules[__name__]
this.sessions = {}


def addSession(userID,sessionToken):
    logging.info('Guardando un session',extra=log_info)
    session_list = sessions[userID]
    if session_list == None:
        session_list = []
    session_list.append(sessionToken)
    sessions[userID] = session_list
    return True;



def getSessionsList(userID):
    return sessions[userID]