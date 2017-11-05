from shared_service import shared_server_service as sharedService
from pymongo import MongoClient
from bson.json_util import dumps

client = None
db = None

def init(db_url,db):
    client = MongoClient(db_url)
    db = client[db]


#fromPlace porque from es reservado de python
def addTravel(email,fromPlace,to):
    user = sharedService.getUserFromEmail(email)
    #Si el user existe
    if user != None:
        db.drivers.insert_one({'email':email,'from':fromPlace,'to':to})
        return True
    return False

def getAvailableTravels():
    cursor = db.find({})
    response = []
    for document in cursor:
        print(document['email'])
