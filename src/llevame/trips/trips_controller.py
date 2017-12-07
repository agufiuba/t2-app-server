from flask import Blueprint,request,jsonify
import logging
from my_firebase import firebase_service as firebaseService
from . import trips_request_validator as validator
from my_firebase.firebase_service import FirebaseService
from shared_service.shared_server_service import SharedServerService
from . import trips_service as tripsService


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'tripsController'}


tripsController = Blueprint('tripsController',__name__)
sharedService = SharedServerService()
firebaseService = FirebaseService()


@tripsController.route('/trips',methods=['POST'])
def add_trip():
    logging.info('Llego un request POST a /trips',extra=log_info)
    validation = validator.validate(request)
    if validation != 'ok':
        return jsonify({'message':validation}),400
    passengerToken = request.headers['Authorization']
    email = firebaseService.validate_token(passengerToken)
    if email != None:
        logging.info('El token del pasajero es valido.',extra=log_info)
        user = sharedService.getUserFromEmail(email)
        if user != None:
            logging.info('El usuario '+email+' se encuentra registrado en nuestra db.',extra=log_info)
            json = request.get_json()
            driverID = json['driverID']
            fromPos = json['from']
            toPos = json['to']
            paymethod = json["paymentMethod"]
            passengerID = firebaseService.getUID(passengerToken)
            if tripsService.addTrip(passengerID,driverID,fromPos,toPos, paymethod):
                return jsonify({'message':'Se agrego el viaje de manera correcta'}),200
            else:
                return jsonify({'message':'Hubo un error el tratar de agregar el viaje'}),400
        else:
            logging.info('El usuario no existe en nuestra db',extra=log_info)
            return jsonify({'message':'El usuario no existe en nuestra db'}),400
    else:
        return jsonify({'message':'Hubo un error con el token'}),400


@tripsController.route('/trips/driverTraveling',methods = ['PUT'])
def driverInWay():
    logging.info('Llego un request PUT /trips/driverTraveling',extra=log_info)
    token = request.headers['Authorization']
    email = firebaseService.validate_token(passengerToken)
    if email != None:
        driverID = firebaseService.getUID(token)
        tripsService.driverInWay(driverID)
        return jsonify({'message':'Se actualizo el estado del vieje'}),200
    else:
        return jsonify({'message':'Hubo un error al tratar de validar el token'}),400
