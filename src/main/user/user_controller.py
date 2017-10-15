from flask import Blueprint,request
import logging

FORMAT = "%(asctime)-15s %(clientip)s %(service)-8s %(message)s"

logging.basicConfig(format=FORMAT,level=logging.INFO)

log_info = {'clientip': '192.168.0.1', 'service': 'user'}

user_controller = Blueprint('controller',__name__)



@user_controller.route('/user',methods = ['POST'])
def add_user():
    logging.info('Se recibio un Request POST',extra=log_info)
    logging.info('User creado con nombre '+request.form['name']+' y apellido '+request.form['last_name']+'de tipo '+request.form['type'],extra = log_info)
    logging.info('Otro log', extra = log_info)
    return 'POST user OK',200


@user_controller.route('/user',methods = ['PUT'])
def update_user():
    logging.info('Se recibio un Request PUT',extra=log_info)
    return 'PUT user OK',200


@user_controller.route('/user/<id>',methods = ['GET'])
def see_user(id):
    logging.info('Se recibio un Request GET',extra=log_info)
    return 'GET user OK',200


@user_controller.route('/user/<id>',methods = ['DELETE'])
def delete_user(id):
    logging.info('Se recibio un Request DELETE',extra=log_info)
    return 'DELETE user OK',200
