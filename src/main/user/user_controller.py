from flask import Blueprint
from pymongo import MongoClient


user_controller = Blueprint('controller',__name__)


@user_controller.route('/user')
def root_service():
    # ingreso a alguien.
    client = MongoClient()
    db = client.t2
    result = db.users.insert_one({"name": "tomas", "age": 24})

    return 'Welcome to user service'
