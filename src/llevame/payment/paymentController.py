from flask import Blueprint,request,jsonify
import logging
from . import paymentService

FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'paymentController'}

def build_payment_controller(interfaces):
    payment_controller = Blueprint('paymentController',__name__)
    shared_service = interfaces.get_shared_server_service()
    firebaseService = interfaces.get_firebase_service()

    @payment_controller.route('/payment/methods',methods=['GET'])
    def getPaymentMethods():
        token = request.headers['Authorization']
        email = firebaseService.validate_token(token)
        if email != None:
            user = sharedService.getUserFromEmail(email)
            if user != None:
                payMethodsList = paymentService.getPaymentMethods()
                if payMethodsList != None:
                    return jsonify({'methods':payMethodsList}),200
                else:
                    return jsonify({'message':'No se pudo obtener los medios de pagos'}),400
            else:
                return jsonify({'message':'El usuario no se encuentra registrado'}),400
        else:
            return jsonify({'message':'El token esta expirado'}),400

    return payment_controller
