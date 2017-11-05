from flask import Blueprint,request
import logging
from . import user_validator
from . import user_service as userService

FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'user'}

#creando un controlador
user_controller = Blueprint('user_controller',__name__)


@user_controller.route('/user',methods=['POST'])
def add_user():
    logging.info('Se recibio un Request POST',extra=log_info)
    response = user_validator.validateAddUserRequest(request)
    if response != 'ok':
        return response,400
    if userService.addUser(request.get_json()):
        return 'POST user OK',200
    return 'POST user is not OK',400


@user_controller.route('/user', methods=['PUT'])
def update_user():
    response = user_validator.validate_update_user_request(request)
    if response != 'ok':
        return response,400
    logging.info('Se recibio un Request PUT', extra=log_info)
    return 'PUT user OK', 200


@user_controller.route('/user/<email>',methods=['GET'])
def see_user(email):
    logging.info('Se recibio un Request GET', extra=log_info)
    userService.getUser(email)
    return 'GET user OK', 200


@user_controller.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    logging.info('Se recibio un Request DELETE', extra=log_info)
    return 'DELETE user OK', 200
