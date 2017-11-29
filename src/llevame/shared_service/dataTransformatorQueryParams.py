import logging

FORMAT = "%(asctime)-15s %(clientip)s %(service)-8s %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'dataTransformerQueryParams'}



def transformate(data):
    logging.info('Transformato un data a url para queryParam',extra=log_info)
    queryParam = ''
    for field in data:
        if field == 'type':
            data['type'] = transformateTypeUser(data['type'])
        logging.info('El parametro visible es'+field,extra=log_info)
        if type(data[field]) is dict:
            for sub_field in data[field]:
                queryParam = queryParam + sub_field+"="+data[field][sub_field]+"&"
        else:
            queryParam = queryParam + field+"="+data[field]+"&"

    logging.info('Se transformo a la siguiente query params'+queryParam,extra=log_info)
    return queryParam


def transformateTypeUser(type):
    if type == 'passenger':
        return '1'
    return '2'