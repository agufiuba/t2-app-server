from flask import Blueprint
from firebase import firebase_service as firebaseService
from . import positionRequestValidator
import request

position_controller = Blueprint('position_controller',__name__)


positions_from_user = {}

@position_controller.route('/position')
def addPositionInTime():
    token = request.headers['Authorization']
    email = firebaseService.validate_token(token)
    validation = positionRequestValidator.validate(request)

    return 'Welcome to positioning service'
