import logging

#Configurando loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'travelsRequestValidator'}


def validate(request):
    json = request.get_json()
    if 'from' not in json:
        logging.info('El campo <from> no existe',extra=log_info)
        return 'El campo <from> no se encuentra disponible en el request'
    if 'to' not in json:
        logging.info('El campo <to> no existe',extra=log_info)
        return 'El campo <to> no se encuentra disponible en el request'
    logging.info('El request tiene todos los campos que corresponde',extra=log_info)
    return 'ok'
