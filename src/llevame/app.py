from flask import Flask,Blueprint
from user.user_controller import user_controller
from availableTrips.availableTripsController import availableTripsController
from position.position_controller import position_controller
from drivers.drivers_controller import drivers_controller_constructor
from drivers.drivers_service import DriversService
from path.path_controller import path_controller
from parameters.parametersController import parameters_controller
from login.login_controller import login_controller
from shared_service import shared_server_service as SharedService
from availableTrips import availableTripsService

import os
import logging


#Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'user'}


def build_app(mongo_uri = None, db = "t2"):
    if (mongo_uri == None):
        mongo_uri = "mongodb://" + os.environ['MONGO_URI']

    app = Flask(__name__)

    #TODO: Refactor de este codigo
    main_controller = Blueprint('main',__name__)
    @main_controller.route('/ht',methods=['GET'])
    def health():
        return 'UP',200

    logging.info('Iniciando aplicación',extra=log_info)
    SharedService.getToken()


    app.register_blueprint(user_controller)
    app.register_blueprint(path_controller)
    driver_service = DriversService(mongo_uri, db)
    availableTripsService.init(mongo_uri,db)
    app.register_blueprint(drivers_controller_constructor(driver_service))
    app.register_blueprint(availableTripsController)
    app.register_blueprint(position_controller)
    app.register_blueprint(login_controller)
    app.register_blueprint(main_controller)
    app.register_blueprint(parameters_controller)
    return app

# La URL de mongodb se le pasa por la variable de entorno MONGO_URI.
app = build_app()

if __name__ == "__main__":
    app.run()
