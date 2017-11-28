from flask import Blueprint,request,jsonify
from firebase import firebase_service as firebaseService
from . import driver_service as driverService

drivers_controller = Blueprint('drivers_controller',__name__)




#Obtengo todos los choferes que esten cerca del pasajero que quiere viajar
@drivers_controller.route('/drivers', methods=["GET"])
def get_drivers():
    token = request.headers['Authorization']
    email = firebaseService.validate_token(token)
    body = request.get_json()
    drivers = driverService.getDriversFrom(body['from'])
    return jsonify({'drivers':drivers}),200



@drivers_controller.route('/drivers/', methods=["POST"])
def login_driver():
    token = request.headers['Authorization']
    email = firebaseService.validate_token(token)
    ID = firebaseService.getUID(token)
    driverSrvice.login_driver(ID)
    return jsonify({'message':'Se agrego de manera correcta al chofer de email'+email}),200
