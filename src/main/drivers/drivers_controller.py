from flask import Blueprint
from pymongo import MongoClient
from bson.json_util import dumps

drivers_controller = Blueprint('drivers_controller',__name__)

@drivers_controller.route('/drivers', methods=["GET"])
def get_drivers():
    # Esto anda en el docker. Y en heroku?
    client = MongoClient("mongodb://mdb")
    db = client.t2
    # Conversión de BSON a JSON.
    return dumps([doc for doc in db.drivers.find()]), 200

@drivers_controller.route('/drivers/<id>', methods=["PUT"])
def login_driver(id):
    client = MongoClient("mongodb://mdb")
    db = client.t2
    # TODO chequear que existe ese id en el shared server?
    # TODO chequear que no está dado de alta.
    # TODO chequear que id sea un número? Son numéricos
    # Por ahora lo doy de alta así nomás.
    db.drivers.insert_one({ "id": int(id) })
    return 'PUT driver OK', 200
