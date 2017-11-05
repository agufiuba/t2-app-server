import firebase_admin
from firebase_admin import credentials

import logging
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'firebaseService'}



def validate_token(id_token):
    logging.info('Obteniendo credenciales',extra=log_info)
    cred = credentials.Certificate('/as/src/main/firebase/serviceAccountKey.json')
    logging.info('Levantanto la app de firebase',extra=log_info)
    auth = firebase_admin.initialize_app(cred)


    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token['uid']
    logging.info('decoded_token'+uid,extra=log_info)
    user = auth.get_user(uid)
    logging.info('el user es:'+user,extra=log_info)
    return True
