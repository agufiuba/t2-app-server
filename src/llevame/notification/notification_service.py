from session import session_service as sessionService
import requests
import logging


keyServer = 'AAAAa-B0L4s:APA91bEFBz2dBB9GtVYrR-L6YFccRgU7UmnlCnklcAQ41YsZNRthG06IwR_oQUT2BQbJ81ItHXpbZkbSbRJRmJS_jwy-aXdusvZ85gLlowE92Cx3oDRtxlmOzQ1RvxCl_L4KDSWpD9Ub'

FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'sharedService'}

def notificate_user(userID):
    logging.info('Se esta notificando al usuario:'+userID,extra=log_info)
    session_list = sessionService.getSessionsList(userID)
    for session in session_list:
        notificate(session)
    return True

def notificate(sessionID):
    data_to_send = {'to':sessionID,'data':'aaaaaaaaaaaaa'}
    requests.post('https://fcm.googleapis.com/fcm/send',headers={'Content-Type':'application/json','Authorization':'key='+keyServer},data=data_to_send)
    return True
