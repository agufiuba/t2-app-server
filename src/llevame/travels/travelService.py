from shared_service import shared_server_service as sharedService
from pymongo import MongoClient
from bson.json_util import dumps
import logging
import sys

this = sys.modules[__name__]
this.db = None


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'travelsService'}


def init(db_url,db="t2"):
    logging.info('Se inicializa el servicio con la db',extra=log_info)
    this.db = MongoClient(db_url)[db]


#fromPlace porque from es reservado de python
def addTravel(email,data):
    user = sharedService.getUserFromEmail(email)
    #Si el user existe
    if user != None:
        this.db.trips.insert_one({'email':email,'from':data['from'],'to':data['to'],'km':data['km']})
        return True
    return False

def getAvailableTravels():
    cursor = this.db.trips.find({})
    response = []
    for document in cursor:
        travel = {}
        logging.info(document['from'],extra=log_info)
        response.append({'email':document['email'],'from':document['from'],'to':document['to'],'km':document['km']})
    return response
