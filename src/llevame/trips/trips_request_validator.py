import logging

#Configurando loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'tripsRequestValidator'}


def validate(request):
    logging.info('Validando request',extra=log_info)
    json = request.get_json()
    if 'driverID' not in json:
        logging.info('No se encuentra el ID del chofer',extra=log_info)
        return 'El ID del chofer no se encuentra, por favor verifique eso'
    if 'from' not in json:
        logging.info('No se encuentra el <from> ',extra=log_info)
        return 'El <from> no se encuentra, por favor verifique eso'
    if 'to' not in json:
        logging.info('No se encuentra el <to> ',extra=log_info)
        return 'El <to> no se encuentra, por favor verifique eso'
    if 'paymentMethod' not in json:
        logging.info('No se encuentra el <paymentMethod> ',extra=log_info)
        return 'El <paymentMethod> no se encuentra, por favor verifique eso'
    logging.info('El request es valido',extra=log_info)
    return 'ok'
