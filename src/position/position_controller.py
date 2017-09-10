from flask import Blueprint

position_controller = Blueprint('position_controller',__name__)


@position_controller.route('/position')
def root_service():
    return 'Welcome to positioning service'
