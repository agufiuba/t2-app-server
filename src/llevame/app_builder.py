from flask import Flask,Blueprint

from user.user_controller import build_user_controller
from availableTrips.availableTripsController import build_available_trips_controller
from drivers.drivers_controller import build_drivers_controller
from position.position_controller import build_position_controller
from login.login_controller import build_login_controller
from parameters.parametersController import build_parameters_controller
from payment.paymentController import build_payment_controller
from trips.trips_controller import tripsController
from interfaces import Interfaces

from shared_service.shared_server_service import SharedServerService
from my_firebase.firebase_service import FirebaseService

import os
import logging

# Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'main'}

def build_app(interfaces = None):
    if (interfaces == None):
        interfaces = Interfaces(\
            mongo_uri = os.environ['MONGO_URI'], \
            mongo_db_name = "t2", \
            shared_server_service = SharedServerService())

    app = Flask(__name__)

    #TODO: Refactor de este codigo
    main_controller = Blueprint('main',__name__)
    @main_controller.route('/ht',methods=['GET'])
    def health():
        return 'UP',200

    logging.info('Iniciando aplicación',extra=log_info)
    SharedServerService().getToken()
    FirebaseService().initService()
    app.register_blueprint(build_user_controller(interfaces))
    app.register_blueprint(build_available_trips_controller(interfaces))
    app.register_blueprint(build_drivers_controller(interfaces))
    app.register_blueprint(build_position_controller())
    app.register_blueprint(build_login_controller(interfaces))
    app.register_blueprint(main_controller)
    app.register_blueprint(build_parameters_controller())
    app.register_blueprint(build_payment_controller())
    app.register_blueprint(tripsController)
    return app
