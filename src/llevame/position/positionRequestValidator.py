import logging

#Configurando loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'positionRequestValidator'}





def validate(request):
    data = request.get_json()
    if 'position' not in data:
        logging.info('El campo <position> no se encuentra en el request',extra=log_info)
        return 'El campo <position> no se encuentra en el request'
    if 'time' not in data:
        logging.info('El campo <time> no se encuentra en el request',extra=log_info)
        return 'El campo <time> no se encuentra en el request'
    logging.info('El request es valido',extra=log_info)
    return 'ok'
