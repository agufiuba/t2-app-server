from flask import Blueprint
from pymongo import MongoClient


user_controller = Blueprint('controller',__name__)


@user_controller.route('/user')
def root_service():
    # ingreso a alguien.
    client = MongoClient("mongodb://mdb") # Esto anda en el docker. Y en heroku?
    db = client.t2
    result = db.users.find()

    return "{" + str([str(doc) for doc in db.users.find()]) + "}"
