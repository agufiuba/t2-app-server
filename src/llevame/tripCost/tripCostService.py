from . import position
import requests
import json

#ApiKey para pegarle a la API de google
apiKey = "AIzaSyDh9EMTub3aewSOKjv_oyrRs8sOZjUQwek";
#Url service
url = "https://maps.googleapis.com/maps/api/directions/json?"

def gestCostOfKm(fromString,toString):
    res = requests.get(url+'origin='+fromString+'&destination='+toString+'&key='+apiKey+"&alternatives=true")
    resJSON = json.loads(res.text)
    distanceInMeters = resJSON['routes'][0]['legs'][0]['distance']['value']
    return distanceInMeters/1000
    
