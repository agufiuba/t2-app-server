from flask import Flask
from .main.user.user_controller import user_controller
from .main.travels.travels_controller import travels_controller
from .main.position.position_controller import position_controller
from .main.drivers.drivers_controller import drivers_controller
from .main.path.path_controller import path_controller
from .main.login.login_controller import login_controller
import logging
from .main.shared_service import shared_server_service

app = Flask(__name__)


#Agregando todos los controladores
app.register_blueprint(user_controller);
app.register_blueprint(path_controller);
app.register_blueprint(drivers_controller);
app.register_blueprint(travels_controller);
app.register_blueprint(position_controller);
app.register_blueprint(login_controller);


#Configuración del loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'user'}


sharedService = shared_server_service.SharedServerService()

if __name__ == "__main__":
    logging.info('Iniciando aplicación',extra=log_info)
    app.run()
    sharedService.getToken()
