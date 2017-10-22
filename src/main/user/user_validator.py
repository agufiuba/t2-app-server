import logging

FORMAT = "%(asctime)-15s %(clientip)s %(service)-8s %(message)s"

logging.basicConfig(format=FORMAT,level=logging.INFO)

log_info = {'clientip': '192.168.0.1', 'service': 'user'}


def validate_add_user_request(request):
    fields_of_add_user_request = ['type','name','last_name','id']
    logging.info('Validando request para agregar user',extra=log_info)
    fields_from_driver = ['model','color','patent','year','state','air_conditioner','music']
    data = request.get_json()
    for x in data:
        logging.info('x:'+x,extra=log_info)
        logging.info('data:'+data[x],extra=log_info)
    return 'ok'



def validate_update_user_request(request):
    logging.info('Validando un request para actualizar informacion de un user',extra=log_info)
    if (request.form.get('id') == None):
        logging.info('El campo id no existe')
        return 'Falta el campo id'
    return 'ok'
