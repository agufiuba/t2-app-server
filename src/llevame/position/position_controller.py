from flask import Blueprint,request
from . import positionRequestValidator
from my_firebase.firebase_service import FirebaseService

def build_position_controller():
    position_controller = Blueprint('position_controller',__name__)
    firebaseService = FirebaseService()
    positions_from_user = {}

    @position_controller.route('/position')
    def addPositionInTime():
        token = request.headers['Authorization']
        email = firebaseService.validate_token(token)
        validation = positionRequestValidator.validate(request.get_json())
        return 'Welcome to positioning service'
    return position_controller
