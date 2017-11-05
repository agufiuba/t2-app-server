from flask import Blueprint,request
from . import travelService
from . import travelRequestValidator
import logging


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'travelsController'}


travels_controller = Blueprint('travels_controller',__name__)





@travels_controller.route('/travels/<email>',methods=['PUT'])
def addTravelAvailable(email):
    logging.info('Llegó un reques PUT en el /travels',extra=log_info)
    validate = travelRequestValidator.validate(request)
    if validate != 'ok':
        return validate,400
    travelService.addTravel(id,request)
    return 'Welcome to travels service'
