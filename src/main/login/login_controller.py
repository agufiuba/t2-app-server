from flask import Blueprint,request
from . import login_service as loginService
import logging




FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'sharedService'}



#Obteniendo controller
login_controller = Blueprint('login_controller',__name__)


@login_controller.route('/login',methods=['POST'])
def login_user():
    logging.info('Se recibio un POST en /login',extra=log_info)
    loginService.login(request)
    return 'Welcome to login service',200
