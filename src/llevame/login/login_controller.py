from flask import Blueprint,request,jsonify
from .login_service import LoginService
import logging

# Configurando el loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'login_controller'}

def build_login_controller(interfaces):

    login_controller = Blueprint('login_controller',__name__)
    loginService = LoginService(interfaces)

    @login_controller.route('/login',methods=['POST'])
    def login_user():
        logging.info('Se recibio un POST en /login',extra=log_info)
        userType = loginService.login(request)
        if userType != None:
            logging.info('El logueo fue exitoso, devolviendo un 200',extra=log_info)
            return jsonify({'message':'El logueo fue exitoso','type':userType}),200
        logging.info('El logueo falló, devolviendo un 400',extra=log_info)
        return jsonify({'message':'El logueo no se pudo realizar, verificio que el usuario esté registrado'}),400

    return login_controller
