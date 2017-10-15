import logging

FORMAT = "%(asctime)-15s %(clientip)s %(service)-8s %(message)s"

logging.basicConfig(format=FORMAT,level=logging.INFO)

log_info = {'clientip': '192.168.0.1', 'service': 'user'}




def validate_add_user_request(request):
    fields_of_add_user_request = ['type','name','last_name','id']
    logging.info('Validando request para agregar user',extra=log_info)
    for field in fields_of_add_user_request:
        if (request.form.get(field) == None):
            logging.info('El campo '+field+" no existe",extra=log_info)
            return 'El campo '+field+' no existe'
        else:
            logging.info('El campo '+field+' existe',extra=log_info)
            if(field == 'type' and request.form.get('type') == 'driver'):
                if (request.form.get('car') != None):
                    fields_from_driver = ['model','color','patent','year','state','air_conditioner','music']
                    for car_field in fields_from_driver:
                        if(request.form.get('car').get(car_field) == None):
                            logging.debug('El campo '+field+" no existe",extra=log_info)
                            return 'El campo [' +car_field+'] del campo [car] no existe'
                else:
                    return 'El campo car no existe'
    logging.info('Request correcto',extra=log_info)
    return 'ok'
