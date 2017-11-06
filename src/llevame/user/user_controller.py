from flask import Blueprint,request,jsonify
import logging
from . import user_validator
from . import user_service as userService


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'userController'}


#creando un controlador
user_controller = Blueprint('user_controller',__name__)


@user_controller.route('/user',methods=['POST'])
def add_user():
    logging.info('Se recibio un Request POST',extra=log_info)
    response = user_validator.validateAddUserRequest(request)
    if response != 'ok':
        return jsonify({'message':response}),400
    if userService.addUser(request.get_json()):
        return jsonify({'message':'El registro del usuario fue exitoso'}),200
    return jsonify({'message':'hubo un error al tratar de agregar el usuario'}),400


@user_controller.route('/user', methods=['PUT'])
def update_user():
    response = user_validator.validate_update_user_request(request)
    if response != 'ok':
        return response,400
    logging.info('Se recibio un Request PUT', extra=log_info)
    return jsonify({'message':'Se actualizo la información del usuario de manera correcta'}), 200


@user_controller.route('/user/<email>',methods=['GET'])
def see_user(email):
    logging.info('Se recibio un Request GET', extra=log_info)
    user = userService.getUser(email)
    if (user != None):
        return jsonify(user),200
    return jsonify({'message':'Hubo un error al tratar de obtener la información de usuario'+email}),400

@user_controller.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    logging.info('Se recibio un Request DELETE', extra=log_info)
    return jsonify({'message':'Se pudo eliminar el usuario de manera correcta'}), 200
