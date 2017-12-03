import requests
import json
from shared_service import shared_server_service as sharedService
import logging
import sys

#ApiKey para pegarle a la API de google
apiKey = "AIzaSyDh9EMTub3aewSOKjv_oyrRs8sOZjUQwek";
#Url service
url = "https://maps.googleapis.com/maps/api/directions/json?"




FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'tripCostService'}


this = sys.modules[__name__]
this.cacheGooleResponses = {}



def getCostAndDistance(userEmail,fromString,toString):
    dictWithSomeParameters = getGoogleResponse(fromString,toString)
    if dictWithSomeParameters != None:
        addResponseInCache(fromString,toString.dictWithSomeParameters)
        cost = sharedService.getCostFromDistanceInKM(userEmail,dictWithSomeParameters['distance'].split('k')[0])
        dictWithSomeParameters['cost'] = cost
        return dictWithSomeParameters
    else:
        logging.info('No se pudo obtener los parametros distancia,tiempo',extra=log_info)
        return None


def getGoogleResponse(fromString,toString):
    #Si ya se realizo la busqueda alguna vez, lo obtengo
    if ifItIsInResultsCache(fromString,toString):
        dictWithSomeParameters = cacheResults[(fromString,toString)]
    else:
        dictWithSomeParameters = getDistanceInKm(fromString,toString)
    return dictWithSomeParameters


def addResponseInCache(fromString,toString,data):
    cacheResults[(fromString,toString)] = dictWithSomeParameters


def ifItIsInResultsCache(fromString,toString):
    return (fromString,toString) in cacheGooleResponses


def getDistanceInKm(fromString,toString):
    logging.info('Obteniendo distancia desde '+fromString+'hasta'+toString,extra=log_info)
    res = requests.get(url+'origin='+fromString+'&destination='+toString+'&key='+apiKey+"&alternatives=true")
    resJSON = json.loads(res.text)
    try:
        timeInMinutes = resJSON['routes'][0]['legs'][0]['duration']['text']
        distanceInMeters = resJSON['routes'][0]['legs'][0]['distance']['text']
        points = resJSON['routes'][0]['overview_polyline']['points']
    except:
        logging.info('No se pudo obtener una respuesta ok del app google',extra=log_info)
        return None
    return {'distance':distanceInMeters,'time':timeInMinutes,'points':points}
