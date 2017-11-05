import firebase_admin
from firebase_admin import credentials

import logging
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'firebaseService'}

cred = credentials.Certificate('/as/src/main/firebase/serviceAccountKey.json')
auth = firebase_admin.initialize_app(cred)


def validate_token(id_token):
    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token['uid']
    logging.info('decoded_token'+uid,extra=log_info)
    print(uid)
    return True
