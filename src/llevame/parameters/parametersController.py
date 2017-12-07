from flask import Blueprint,request,jsonify
import logging



FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'parametersController'}

def build_parameters_controller():

    #creando un controlador
    parameters_controller = Blueprint('parameters_controller',__name__)

    @parameters_controller.route('/parameters/car/model',methods=['GET'])
    def getModels():
        logging.info('Se recibio un Request GET en car/model',extra=log_info)
        response = {'parameters':['Ford Fiesta','Chevrolet S10','Toyota Hilux','Fiat Palio','Renault Scenic']}
        return jsonify(response),200


    @parameters_controller.route('/parameters/car/colour',methods=['GET'])
    def getColours():
        logging.info('Se recibio un Request GET car/colour',extra=log_info)
        response = {'parameters':['Negro','Amarillo','Azul','Rojo']}
        return jsonify(response),200


    @parameters_controller.route('/parameters/car/state',methods=['GET'])
    def getStatesAvailable():
        logging.info('Se recibio un Request GET car/state',extra=log_info)
        response = {'parameters':['Excelente','Bueno','Destartalado','PicaPiedra']}
        return jsonify(response),200


    @parameters_controller.route('/parameters/car/music',methods=['GET'])
    def getMusicOption():
        logging.info('Se recibio un Request GET car/music',extra=log_info)
        response = {'parameters':['Clasica','Jazz','Tango','Rock','Folklore','Pop']}
        return jsonify(response),200


    @parameters_controller.route('/parameters/car/air_conditioner',methods=['GET'])
    def getAirConditionerOption():
        logging.info('Se recibio un Request GET car/music',extra=log_info)
        response = {'parameters':['Sí','No']}
        return jsonify(response),200

    return parameters_controller
