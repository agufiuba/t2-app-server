import requests
import json
from shared_service import shared_server_service as sharedService
#ApiKey para pegarle a la API de google
apiKey = "AIzaSyDh9EMTub3aewSOKjv_oyrRs8sOZjUQwek";
#Url service
url = "https://maps.googleapis.com/maps/api/directions/json?"




def getCostAndDistance(userEmail,fromString,toString):
    dictWithSomeParameters = getDistanceInKm(fromString,toString)
    cost = sharedService.getCostFromDistanceInKM(userEmail,dictWithSomeParameters['distance'])
    dictWithSomeParameters['cost'] = cost
    return dictWithSomeParameters


def getDistanceInKm(fromString,toString):
    res = requests.get(url+'origin='+fromString+'&destination='+toString+'&key='+apiKey+"&alternatives=true")
    resJSON = json.loads(res.text)
    distanceInMeters = resJSON['routes'][0]['legs'][0]['distance']['value']
    timeInMinutes = resJSON['routes'][0]['legs'][0]['duration']['text'].split(' ')[0]
    points = resJSON['routes'][0]['overview_polyline']['points']
    return {'distance':distanceInMeters/1000,'time':timeInMinutes,'points':points}
