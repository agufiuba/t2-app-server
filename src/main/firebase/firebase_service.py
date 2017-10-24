import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('/as/src/main/firebase/serviceAccountKey.json')
auth = firebase_admin.initialize_app(cred)




def validate_token(id_token):
    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token['uid']
    print(decoded_token)
    print(uid)
    return True
