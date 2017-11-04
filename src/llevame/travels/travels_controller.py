from flask import Blueprint

travels_controller = Blueprint('travels_controller',__name__)


@travels_controller.route('/travels')
def root_service():
    return 'Welcome to travels service'
