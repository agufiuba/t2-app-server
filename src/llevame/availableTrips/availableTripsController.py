from flask import Blueprint,request,jsonify
from .availableTripsService import AvailableTripService
from . import availableTripsRequestValidator
import logging


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'travelsController'}


def build_available_trips_controller(interfaces):

    availableTripsController = Blueprint('availableTripsController',__name__)
    firebaseService = interfaces.get_firebase_service()
    availableTripsService = AvailableTripService(interfaces)

    @availableTripsController.route('/availableTrip',methods=['POST'])
    def addTravelAvailable():
        logging.info('Llegó un reques POST en el /availableTrip',extra=log_info)
        validate = availableTripsRequestValidator.validate(request)
        token = request.headers['Authorization']
        email = firebaseService.validate_token(token)
        if validate != 'ok':
            logging.info('La validacion del request no fue ok',extra=log_info)
            return validate,400
        response = availableTripsService.addTravel(email,request.get_json())
        if response != None:
            logging.info('Se agregó de manera exitosa el viaje disponible del usuario:'+email,extra=log_info)
            return jsonify(response),200
        return jsonify({'message':'Hubo un error al tratar de agregar un nuevo viaje disponible '+email}),400

    @availableTripsController.route('/availableTrip',methods=['GET'])
    def getAvailableTravels():
        return jsonify({'availableTrips':availableTripsService.getAvailableTravels()}),200

    return availableTripsController
