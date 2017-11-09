from flask import Blueprint,request,jsonify
from . import availableTripsService
from . import availableTripsRequestValidator
import logging
from firebase import firebase_service as firebaseService

FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'travelsController'}


availableTripsController = Blueprint('availableTripsController',__name__)




@availableTripsController.route('/availableTrip',methods=['POST'])
def addTravelAvailable():
    logging.info('Llegó un reques PUT en el /travels',extra=log_info)
    validate = availableTripsRequestValidator.validate(request)
    token = request.headers['Authorization']
    email = firebaseService.validate_token(token)
    if validate != 'ok':
        return validate,400
    response = availableTripsService.addTravel(email,request.get_json())
    if response != None:
        return jsonify(response),200
    return jsonify({'message':'Hubo un error al tratar de agregar un nuevo viaje disponible '+email}),400



@availableTripsController.route('/availableTrip',methods=['GET'])
def getAvailableTravels():
    return jsonify({'availableTrips':availableTripsService.getAvailableTravels()}),200
