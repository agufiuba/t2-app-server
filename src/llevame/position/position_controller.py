from flask import Blueprint,request
from . import positionRequestValidator

def build_position_controller(interfaces):
    position_controller = Blueprint('position_controller',__name__)
    firebaseService = interfaces.get_firebase_service()
    positions_from_user = {}

    @position_controller.route('/position')
    def addPositionInTime():
        token = request.headers['Authorization']
        email = firebaseService.validate_token(token)
        validation = positionRequestValidator.validate(request.get_json())
        return 'Welcome to positioning service'
    return position_controller
