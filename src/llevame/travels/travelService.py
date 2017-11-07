from shared_service import shared_server_service as sharedService
from pymongo import MongoClient
from bson.json_util import dumps
import logging


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'travelsService'}

client = None
db = None

def init(db_url,db):
    logging.info('Se inicializa el servicio con la db',extra=log_info)
    client = MongoClient(db_url)
    db = client[db]


#fromPlace porque from es reservado de python
def addTravel(email,data):
    user = sharedService.getUserFromEmail(email)
    #Si el user existe
    if user != None:
        
        db.drivers.insert_one({'email':email,'from':data['from'],'to':data['to'],'km':data['km']})
        return True
    return False

def getAvailableTravels():
    cursor = db.find({})
    response = []
    for document in cursor:
        print(document['email'])
    return document
