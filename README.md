[![Build Status](https://travis-ci.org/agufiuba/t2-app-server.svg?branch=master)](https://travis-ci.org/agufiuba/t2-app-server)
[![Coverage Status](https://coveralls.io/repos/github/agufiuba/t2-app-server/badge.svg?branch=master)](https://coveralls.io/github/agufiuba/t2-app-server?branch=master)

# t2-app-server

## Instalación

La aplicación requiere que exista una red de docker llamada "ubernet". Para crearla debe ejecutarse:

-   `docker network create ubernet`

Luego, para construir la aplicación:

-   `docker-compose build`

## Ejecución

Se explicita el puerto al cual se ligará el servidor al levantarlo:

-   `export PORT=<puerto>`

Por ejemplo, si se ejecuta `export PORT=3000` luego se accederá a la API a través de `localhost:3000`. Si la aplicación se usa en simultáneo con el `shared-server` deben estar ligados a puertos distintos.

Finalmente, para levantar el servidor:

-   `docker-compose up`

## Servicios disponibles

### Servicio de usuario

Este se encarga todo respecto al usuario, registro, etc.

#### Registrar Usuario

+ Verbo REST: POST

+ Body:

      {
        type: 'driver'
        name: 'xxxxx',
        last_name: 'xxxxx',
        email: 'xxxx',
      car:{
          model: 'xxxx',
          color: 'xxxx',
          patent: 'xxxxx',
          year: 'xxxxx',
          state: ['good','bad','maso'],
          air_conditioner:'hp',
          music:['radio','album']
      }
      }

      {
           type: 'passenger'
           name: 'name',
           last_name: 'apellido',
           email: 'email',
           car:{
            'number':'xxx',
            'typeCard':'xxxxx',
            'securityCode':'xxxxxx',
            'expirationYear':'xxxxx',
            'expirationMonth':'xxxxxx'
            }
      }


+ URL: http://uri:port/user/

#### Actualizar información usuario

+ Verbo REST: PUT
+ Body:
              {
                email: 'julano.casandro@gmail',
                ...
                ....
              }

Los puntos suspensivos serian los datos que se quieren actualizar

+ URL: http://uri:port/user/

#### Ver información de Usuario

+ Verbo REST: GET
+ Body:

        {}

+ URL: http://uri:port/user/{id_user}


+ Respuesta si es un pasajero
            
            {
                type: 'passenger'
                name: 'name',
                last_name: 'apellido',
                email: 'email',
                car:{
                        'number':'xxx',
                        'typeCard':'xxxxx',
                        'securityCode':'xxxxxx',
                        'expirationYear':'xxxxx',
                        'expirationMonth':'xxxxxx'
                  }
            }
         
+ Respuesta si es chofer:
            
            
         {
            type: 'driver'
            name: 'xxxxx',
            last_name: 'xxxxx',
            email: 'xxxx',
            car:{
                  model: 'xxxx',
                  color: 'xxxx',
                  patent: 'xxxxx',
                  year: 'xxxxx',
                  state: ['good','bad','maso'],
                  air_conditioner:'hp',
                  music:['radio','album']
                  }
            }
            

### Servicio de viaje

Agregar un viaje que se va a realizar

+ URL: /trips
+ Verbo REST: POST
+ Header: 
      
      {'Authorization':'xxxx'}

+ Body:
      
      {
      'driverID':'xxxx',
      'from':'xxxx',
      'to':'xxxxx'
      }


### Servicio de choferes

Obtener los choferes disponibles.

+ Verbo REST: GET
+ Header: 
       
       {'Authorization':'xxxx'}

+ URL: /drivers?pos=lat/lng: (-34.6220855,-58.3832781)
+ Response: La lista de los id de los drivers cercanos al pasajero
          
          {
          'drivers':[id1,id2,id3]
          }
          
 

Agregar un chofer disponible

+ URL: /drivers
+ Verbo REST: POST
+ Header: 
       
       {'Authorization':'xxxx'}
       
 + Response:
       
       {'message': 'Se agrego de manera correcta al chofer de xxxx'}

### Servicio de posicionamiento


Corrobar que está realizando el viaje, y la distancia y tiempo de manera exacta.

### Servicio de viajes disponibles

#### Agregar un viaje nuevo

+ Verbo REST: PUT
+ Body:
      
      {
      'Authorization':'xxxxxxx',
      'Content-Type':'application/json'
      }
      {
        'from': '-34.617952,-58.385983',
        'to': '-34.617952,-58.385983',
      }


+ URL: http://uri:port/availableTrip

+ Response :

En caso de que el usuario no exista se devuelve un 400

      {
        message: El usuario no existe.
      }

En caso de que el usuario exista

      {
        'cost':'xxx',
        'distance':'xxx km'
        'points':'xxxxxxxxxxxxxxxxxxxx',
        'time':'x hours x mins'
      }



+ Verbo REST: GET
+ Body:

          {}

+ Response:
          {
            'availableTrips':[
            {
              "email": "dasdasdads",
              "from": "casa",
              "km": "20",
              "to": "otra casa"
            },
            {
              "email": "dasdasdads",
              "from": "Avenida Santa fe",
              "km": "20",
              "to": "Avenida San Juan"
            },
            {
              "email": "dasdasdads",
              "from": "Avenida Santa Matia",
              "km": "20",
              "to": "Avenida San Cristbal"
            }
            ]
          }
### Servicio de Direccionamiento

Se utilizara para permitir conocer los caminos disponibles.



### Servicio de parametros

Se utiliza para obtener los parametros posibles

URL's:
  +  http://localhost:3000/parameters/car/state
  +  http://localhost:3000/parameters/car/music
  +  http://localhost:3000/parameters/car/model
  +  http://localhost:3000/parameters/car/colour
  + http://localhost:3000/parameters/car/air_conditioner


Response:

        {
          parameters : [......]
        }

## Uri's dispobibles


+ /user
+ /travels
+ /position
+ /drivers
+ /path
