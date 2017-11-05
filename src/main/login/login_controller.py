from flask import Blueprint
from . import login_service as loginService
login_controller = Blueprint('login_controller',__name__)


@login_controller.route('/login',methods=['POST'])
def root_service():
    loginService.login(request)
    return 'Welcome to login service',200
