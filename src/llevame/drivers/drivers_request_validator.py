import logging

#Configurando loggin
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'driversRequestValidator'}




def validate(request):
    logging.info('Validando request',extra=log_info)
    from_string = request.args.get('pos')
    logging.info('Se obtuvo la siguiente posicion:'+from_string,extra=log_info)
    return 'ok'
