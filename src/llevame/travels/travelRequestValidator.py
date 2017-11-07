import logging

#Configurando loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'travelsRequestValidator'}


def validate(request):
    json = request.get_json()
    if 'km' not in json:
        logging.info('El campo km no existe',extra=log_info)
        return 'El campo km no se encuentra disponible en el request'
    logging.info('El request tiene todos los campos que corresponde',extra=log_info)
    return 'ok'
