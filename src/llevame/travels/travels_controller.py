from flask import Blueprint,request,jsonify
from . import travelService
from . import travelRequestValidator
import logging


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'travelsController'}


travels_controller = Blueprint('travels_controller',__name__)




@travels_controller.route('/travels/<email>',methods=['POST'])
def addTravelAvailable(email):
    logging.info('Llegó un reques PUT en el /travels',extra=log_info)
    validate = travelRequestValidator.validate(request)
    if validate != 'ok':
        return validate,400
    if travelService.addTravel(email,request.get_json()):
        return jsonify({'message':'Se guardo exitosamente el viaje del user'+email}),200
    return jsonify({'message':'No existe pasajero registrado con email '+email}),400

@travels_controller.route('/travels/available',methods=['GET'])
def getAvailableTravels():
    return jsonify(travelService.getAvailableTravels()),200
