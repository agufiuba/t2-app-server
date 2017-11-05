from flask import Blueprint

path_controller = Blueprint('path_controller',__name__)


@path_controller.route('/path')
def root_service():
    return 'Welcome to path service'
