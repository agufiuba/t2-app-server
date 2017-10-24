from flask import Blueprint,request
import logging
from .  import user_validator
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"

logging.basicConfig(format=FORMAT,level=logging.INFO)

log_info = {'clientip': '192.168.0.1', 'service': 'user'}

user_controller = Blueprint('controller',__name__)



@user_controller.route('/user',methods=['POST'])
def add_user():
    logging.info('Se recibio un Request POST',extra=log_info)
    response = user_validator.validate_add_user_request(request)
    if response != 'ok':
        return response,400
    return 'POST user OK',200


@user_controller.route('/user', methods=['PUT'])
def update_user():
    response = user_validator.validate_update_user_request(request)
    if response != 'ok':
        return response,400
    logging.info('Se recibio un Request PUT', extra=log_info)
    return 'PUT user OK', 200


@user_controller.route('/user/<id>',methods=['GET'])
def see_user(id):
    logging.info('Se recibio un Request GET', extra=log_info)
    return 'GET user OK', 200


@user_controller.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    logging.info('Se recibio un Request DELETE', extra=log_info)
    return 'DELETE user OK', 200
