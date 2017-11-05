from flask import Blueprint,request,jsonify
from . import login_service as loginService
import logging



#Configurando el loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'sharedService'}



#Obteniendo controller
login_controller = Blueprint('login_controller',__name__)


@login_controller.route('/login',methods=['POST'])
def login_user():
    logging.info('Se recibio un POST en /login',extra=log_info)
    if loginService.login(request):
        logging.info('El logue fue exitoso, devolviendo un 200',extra=log_info)
        return jsonify({'message':'El logueo fue exitoso'}),200
    logging.info('El logue falló, devolviendo un 400',extra=log_info)
    return jsonify({'message':'El logueo no se pudo realizar, verificio que el usuario esté registrado'}),400
