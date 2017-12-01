from flask import Flask,Blueprint
from user.user_controller import build_user_controller
from availableTrips.availableTripsController import build_available_trips_controller
from position.position_controller import position_controller
from drivers.drivers_controller import build_drivers_controller
from path.path_controller import path_controller
from parameters.parametersController import parameters_controller
from login.login_controller import build_login_controller
from shared_service import shared_server_service as SharedService
from payment.paymentController import payment_controller
from availableTrips import availableTripsService
from interfaces import Interfaces
from my_firebase import firebase_service

import os
import logging


#Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'user'}


def build_app(interfaces = None):
    if (interfaces == None):
        interfaces = Interfaces(\
            firebase_service = firebase_service, \
            mongo_uri = os.environ['MONGO_URI'], \
            mongo_db_name = "t2", \
            shared_server_service = SharedService)

    app = Flask(__name__)

    #TODO: Refactor de este codigo
    main_controller = Blueprint('main',__name__)
    @main_controller.route('/ht',methods=['GET'])
    def health():
        return 'UP',200

    logging.info('Iniciando aplicación',extra=log_info)
    interfaces.get_shared_server_service().getToken()

    app.register_blueprint(build_user_controller(interfaces))
    app.register_blueprint(path_controller)
    app.register_blueprint(build_available_trips_controller(interfaces))
    app.register_blueprint(build_drivers_controller(interfaces))
    app.register_blueprint(position_controller)
    app.register_blueprint(build_login_controller(interfaces))
    app.register_blueprint(main_controller)
    app.register_blueprint(parameters_controller)
    app.register_blueprint(payment_controller)
    return app

# La URL de mongodb se le pasa por la variable de entorno MONGO_URI.
app = build_app()

if __name__ == "__main__":
    app.run()
