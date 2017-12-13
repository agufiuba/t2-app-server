from flask import Blueprint,request,jsonify
from .drivers_service import DriverService
import logging
from . import drivers_request_validator as validator
from my_firebase.firebase_service import FirebaseService
from utils.position import Position

# Configuracion del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'driversController'}

def build_drivers_controller(interfaces):
    drivers_controller = Blueprint('drivers_controller',__name__)
    firebaseService = FirebaseService()
    driverService = DriverService()

    # Obtengo todos los choferes que esten cerca del pasajero que quiere viajar
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
                passengerPosition = Position(request.args.get('pos'))
                drivers = driverService.getDriversAroundFrom(passengerPosition)
                return jsonify({'drivers':drivers}),200
        return jsonify({'message':'El token pasado no es valido'}),400


    @drivers_controller.route('/drivers', methods=["POST"])
    def login_driver():
        logging.info('Llegó una solicitud POST',extra=log_info)
        token = request.headers['Authorization']
        email = firebaseService.validate_token(token)
        ID = firebaseService.getUID(token)
        driverService.login_driver(ID)
        logging.info('Se devuelvo un 200, se agrego al usuario de manera correcta',extra=log_info)
        return jsonify({'message':'Se agrego de manera correcta al chofer de email'+email}),200


    @drivers_controller.route('/drivers',methods=['DELETE'])
    def delete_driver():
        logging.info('Llegó una solicitud DELETE',extra=log_info)
        token = request.headers['Authorization']
        email = firebaseService.validate_token(token)
        if email != None:
            logging.info('El usuario existe, procediendo a eliminar el usuario de choferes disponibles',extra=log_info)
            ID = firebaseService.getUID(token)
            driverService.delete_driver(ID)
            return jsonify({'message':'Se eliminó de manera correcta al chofer de email'+email}),200
        else:
            logging.info('El usuario no existe',extra=log_info)
            return jsonify({'message':'El usuario no existe en la base de datos'}),400

    return drivers_controller
