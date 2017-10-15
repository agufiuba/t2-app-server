from flask import Blueprint
from pymongo import MongoClient
from bson.json_util import dumps

drivers_controller = Blueprint('drivers_controller',__name__)

@drivers_controller.route('/drivers')
def root_service():
    # Esto anda en el docker. Y en heroku?
    client = MongoClient("mongodb://mdb")
    db = client.t2
    # Conversión de BSON a JSON.
    return dumps([doc for doc in db.drivers.find()])
