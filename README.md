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
        'nameOnCard':'xxxx',
        'number':'xxx',
        'typeCard':'xxxxx',
        'securityCode':'xxxxxx',
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



### Servicio de viaje

Este tiene 2 responsabilidades:

+ Cotizar los viajes
+ Informar los viajes disponibles


### Servicio de choferes

Se encarga de informar los choferes disponibles.


### Servicio de posicionamiento


Corrobar que está realizando el viaje, y la distancia y tiempo de manera exacta.

### Servicio de viajes

#### Agregar un viaje nuevo

+ Verbo REST: PUT
+ Body:

      {
        email:cristian@gmail.com,
        from: -36.60213444;-37.43928221,
        to: -37.343431912;49.4394329
      }

+ URL: http://uri:port/travels

+ Response :

En caso de que el usuario no exista se devuelve un 400

      {
        message: El usuario no existe.
      }

En caso de que el usuario exista

      {
        message: Nuevo viaje agregado exitosamente
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
