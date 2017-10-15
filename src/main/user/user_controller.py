from flask import Blueprint
user_controller = Blueprint('controller',__name__)

@user_controller.route('/user')
def root_service():
    return 'Welcome to user service' #NOTE vuelve a como estaba antes.
