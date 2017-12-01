from session import session_service as sessionService
import requests
import logging


keyServer = 'AAAAa-B0L4s:APA91bFGGWPnw2nHxvM7xaVN-S9sSKAajA7KAfwH2u65ytDxHkZ1n9uGeIfWvBK6PYmtfNwjSOeKC-AKUeJCV_PmaBzDYtwCa96pK5PEi2tU4GQs6Qbd0kftRyf1QzmppNVezKuqgbN6'

FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'sharedService'}

def notificate_user(userID,data):
    logging.info('Se esta notificando al usuario:'+userID,extra=log_info)
    session_list = sessionService.getSessionsList(userID)
    for session in session_list:
        notificate(session)
    return True

def notificate(sessionID,data):

    data_to_active_listener = {
    'to':sessionID,
    'android':{
	   'ttl':'86400s',
		    'notification' : {
    		  'data':data
		     }
	 }
    }

    date_to_notification = {
        'to':sessionID,
    	'notification' : {
            'title': 'Nuevo Viaje',
            'body': 'Un usuario a elegido viajar con vos',
         }
    }
    requests.post('https://fcm.googleapis.com/fcm/send',headers={'Content-Type':'application/json','Authorization':'key='+keyServer},data=data_to_active_listener)
    requests.post('https://fcm.googleapis.com/fcm/send',headers={'Content-Type':'application/json','Authorization':'key='+keyServer},data=date_to_notification)
    return True
