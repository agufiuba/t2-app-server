from flask import Blueprint

drivers_controller = Blueprint('drivers_controller',__name__)


@drivers_controller.route('/drivers')
def root_service():
    return 'Welcome to driver service'
