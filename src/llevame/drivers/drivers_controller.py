from flask import Blueprint

def drivers_controller_constructor(driver_service):

    drivers_controller = Blueprint('drivers_controller',__name__)

    @drivers_controller.route('/drivers', methods=["GET"])
    def get_drivers():
        # Conversión de BSON a JSON.
        return driver_service.get_drivers(), 200

    @drivers_controller.route('/drivers/<id>', methods=["PUT"])
    def login_driver(id):
        # client = MongoClient("mongodb://mdb")
        # TODO chequear que existe ese id en el shared server?
        # TODO chequear que no está dado de alta.
        # TODO chequear que id sea un número? Son numéricos
        # Por ahora lo doy de alta así nomás.
        return driver_service.login_driver(id)
        return 'PUT driver OK', 200

    return drivers_controller
