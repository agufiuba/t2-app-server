import requests
import json
from shared_service.dataTransformatorQueryParams import BodyTransformatorQueryParam
import logging
import os


FORMAT = "%(asctime)-15s    %(service)-8s     %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)
log_info = {'clientip': '192.168.0.1', 'service': 'sharedService'}




class SharedServerService:

    token = ''

    def __init__(self,transformator = BodyTransformatorQueryParam()):
        self.shared_server_addr = os.environ["SHARED_SERVER_ADDR"]
        logging.info("La dirección del shared server es: "+self.shared_server_addr, extra=log_info)
        self.transformator = transformator

    def getToken(self):
        logging.info("Obteniendo el token de autenticacion",extra=log_info)
        code = 0
        if SharedServerService.token == '':
            while(code != 200):
                logging.info('Realizando request a ['+self.shared_server_addr+'/login'+']',extra=log_info)
                try:
                    res = requests.get(self.shared_server_addr+"/login")
                    code = res.status_code
                    SharedServerService.token = res.headers['Authorization']
                except ConnectionError:
                    logging.info('Se rechazó conexion',extra=log_info)
        logging.info('El token es: ' + SharedServerService.token,extra=log_info)
        logging.info('El inicio fue OK',extra=log_info)

    def addUser(self,user):
        logging.info('Agregando un usuario',extra=log_info)
        #Setup
        stringQuery = self.transformator.transformate(user)
        url = self.shared_server_addr+'/users'+'?'+stringQuery;
        logging.info('Realizando un POST al shared server con url ['+url+']',extra=log_info)
        #Realizando request
        logging.info('El token es:'+SharedServerService.token,extra=log_info)
        res = requests.post(url,headers = {'Authorization':SharedServerService.token})
        logging.info('Se recibio un '+ str(res.status_code)+" del shared server",extra=log_info)
        return res.status_code == 200 or res.status_code == 201


    def getUserFromEmail(self,email):
        logging.info('Obteniendo información del usuario ['+email+']',extra=log_info)
        #Setup
        url = self.shared_server_addr+'/users/'+email
        logging.info('Realizando GET al shared server con url +['+url+']',extra=log_info)
        #Realizando request
        res = requests.get(url,headers = {'Authorization':SharedServerService.token})
        code = res.status_code
        if code != 200 and code !=201 :
            logging.info('Hubo un problema al tratar de obtener información del user',extra=log_info)
            return None;
        logging.info('Se obtuvo la información de manera correcta',extra=log_info)
        return json.loads(res.text)


    def deleteUser(self,id):
        return 'deleteUser'

    def getCostFromDistanceInKM(self,userEmail,distanceInKM):
        logging.info('Calculando la el costo de viaje para '+userEmail+' y distancia '+str(distanceInKM),extra=log_info)
        url = self.shared_server_addr+'/costos/'+userEmail+'/'+str(distanceInKM)
        logging.info('Realizo request al shared server con el siguiente request'+url,extra=log_info)
        #Realizando request
        res = requests.get(url,headers = {'Authorization':SharedServerService.token})
        return json.loads(res.text)

    def getPayMethods(self):
        logging.info('Llegó una solicitud para poder obtener los medios de pagos',extra=log_info)
        url = self.shared_server_addr+'/paymethods'
        logging.info('Se esta enviando un GET a la siguiente url'+url,extra=log_info)
        res = requests.get(url,headers = {'Authorization':SharedServerService.token})
        return json.loads(res.text)


    def getCarInfo(self,email):
        logging.info('Llegó una solicitud para poder obtener información de un auto de:'+email,extra=log_info)
        url = self.shared_server_addr+'/cars/'+email
        logging.info('Realizo request al shared server con el siguiente request'+url,extra=log_info)
        #Realizando request
        res = requests.get(url,headers = {'Authorization':SharedServerService.token})
        return json.loads(res.text)

    # POST al sharedServer/trips.
    def addTrip(self, userEmail, driverEmail, distance, paymethod):
        logging.info("Enviándole al shared-server un viaje para agregar.", extra=log_info)
        url = self.shared_server_addr+'/trips/'+ userEmail + "/" + driverEmail \
            + "/" + distance.split(" ")[0] + "?" + "metodo=" + paymethod
        logging.info("POST a la siguiente url: "+ url, extra=log_info)
        res = requests.post(url,headers = {'Authorization': SharedServerService.token})
        return res.status_code == 200 or res.status_code == 201
