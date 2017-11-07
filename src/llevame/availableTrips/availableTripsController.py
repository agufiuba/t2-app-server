from flask import Blueprint,request,jsonify
from . import availableTripsService
from . import availableTripsRequestValidator
import logging


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'travelsController'}


availableTripsController = Blueprint('availableTripsController',__name__)




@availableTripsController.route('/availableTrip/<email>',methods=['POST'])
def addTravelAvailable(email):
    logging.info('Llegó un reques PUT en el /travels',extra=log_info)
    validate = availableTripsRequestValidator.validate(request)
    if validate != 'ok':
        return validate,400
    if availableTripsService.addTravel(email,request.get_json()):
        return jsonify({'message':'Se guardo exitosamente el viaje del user'+email}),200
    return jsonify({'message':'No existe pasajero registrado con email '+email}),400

@availableTripsController.route('/availableTrip',methods=['GET'])
def getAvailableTravels():
    return jsonify({'availableTrips':availableTripsService.getAvailableTravels()}),200
