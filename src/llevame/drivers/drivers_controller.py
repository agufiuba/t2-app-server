from flask import Blueprint,request,jsonify
from my_firebase import firebase_service as firebaseService
from . import drivers_service as driverService
from availableTrips import availableTripsService
import logging
from . import drivers_request_validator as validator
from utils import positionTransformer


drivers_controller = Blueprint('drivers_controller',__name__)

#Configuracion del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'driversController'}

#Obtengo todos los choferes que esten cerca del pasajero que quiere viajar
@drivers_controller.route('/drivers', methods=["GET"])
def get_drivers():
    logging.info('Llego un solicitud GET para obtener',extra=log_info)
    token = request.headers['Authorization']
    email = firebaseService.validate_token(token)
    if (email != None):
        logging.info('El token es valido',extra=log_info)
        validation =  validator.validate(request)
        if validation != 'ok':
            return jsonify({'message':validation}),400
        else:
            passengerPosition = positionTransformer.parserStringToPosition(request.args.get('pos'))
            drivers = driverService.getDriversAroundFrom(passengerPosition)
            return jsonify({'drivers':drivers}),200
    return jsonify({'message':'El token pasado no es valido'}),400


@drivers_controller.route('/drivers', methods=["POST"])
def login_driver():
    token = request.headers['Authorization']
    email = firebaseService.validate_token(token)
    ID = firebaseService.getUID(token)
    driverService.login_driver(ID)
    return jsonify({'message':'Se agrego de manera correcta al chofer de email'+email}),200
