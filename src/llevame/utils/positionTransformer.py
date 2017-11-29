import logging


#Configuracion del login
FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'positionTransformer'}

def parserStringToPosition(positionString):
    logging.info('Transformando el siguiente string:'+positionString,extra=log_info)
    #positionString = lat/lng: (-34.6220855,-58.3832781)
    list_of_positions = positionString.split(':')[1].replace('(','').replace(')','').split(',')
    logging.info('La posiciones son:'+list_of_positions[0]+'y:'+list_of_positions[1],extra=log_info)
    return {'lat':float(list_of_positions[0]),'lng':float(list_of_positions[1])}
