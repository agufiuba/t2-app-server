from ..firebase import firebase_service as firebaseService


import logging
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'loginService'}


def login(request):
    logging.info('LLegó el pedido para loguear a un user',extra=log_info)
    id_token = request.headers['Authorization']
    logging.info('Se obtuvo el siquiente token del app android'+id_token,extra=log_info)
    if firebaseService.validate_token(id_token):
        return 'Login correct',200
    else:
        return 'Login is not correct',400
