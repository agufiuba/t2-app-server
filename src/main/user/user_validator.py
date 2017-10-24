import logging

FORMAT = "%(asctime)-15s %(clientip)s %(service)-8s %(message)s"

logging.basicConfig(format=FORMAT,level=logging.INFO)

log_info = {'clientip': '192.168.0.1', 'service': 'user'}


def validate_add_user_request(request):
    fields_of_add_user_request = ['type','name','last_name','id']
    logging.info('Validando request para agregar user',extra=log_info)
    fields_from_driver = ['model','color','patent','year','state','air_conditioner','music']
    data = request.get_json()
    for field in fields_of_add_user_request:
        if field not in data:
            logging.info('Falta el campo '+field+' en el request, devolviendo un 400',extra=log_info)
            return 'Falta el campo '+field+' en el request'
    if data['type'] == 'driver':
        logging.info('Se está registrando a un conductor',extra=log_info)
        if 'car' not in data:
            logging.info('Falta el campo '+field+' en el request, devolviendo un 400',extra=log_info)
            return 'Falta el campo car en el request'
        for field_driver in fields_from_driver:
            if field_driver not in data['car']:
                logging.info('Falta el campo '+field_driver+' dentro de car, devolviendo un 400',extra=log_info)
                return 'Falta el campo '+field_driver+' dentro de car'
    return 'ok'



def validate_update_user_request(request):
    logging.info('Validando un request para actualizar informacion de un user',extra=log_info)
    if (request.form.get('id') == None):
        logging.info('El campo id no existe')
        return 'Falta el campo id'
    return 'ok'
