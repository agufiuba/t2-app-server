from pymongo import MongoClient
from bson.json_util import dumps

class DriversService():
    def __init__(self, db_url, db = "t2"):
        self.client = MongoClient(db_url)
        self.db = self.client[db] # TODO añadir opción de cambio de BDD.

    # Devuelve un BSON con los choferes disponibles.
    def get_drivers(self):
        return dumps([doc for doc in self.db.drivers.find()])

    # Añade a la BDD un chofer.
    def login_driver(self, id):
        self.db.drivers.insert_one({ "id": int(id) })

    # TODO Lo quita de la base de datos.
    # def logout_driver(self, id):
