[![Coverage Status](https://coveralls.io/repos/github/agufiuba/t2-app-server/badge.svg?branch=master)](https://coveralls.io/github/agufiuba/t2-app-server?branch=master)

# t2-app-server

## Servicios disponibles

### Servicio de usuario

Este se encarga todo respecto al usuario, registro, etc.

#### Registrar Usuario

+ Verbo REST: POST

+ Body:

      {
        type: ['passenger','driver']
        name: 'name',
        last_name: 'apellido',
        email: 'email',
        facebook_acount:facebook_acount,
      car:{
          model: 'model',
          color: 'color',
          patent: 'patent',
          year: '2010',
          state: ['good','bad','maso'],
          air_conditioner:'hp',
          music:['radio','album']
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

### Servicio de choferes

Proveera una lista de choferes disponibles.


### Servicio de Direccionamiento

Se utilizara para permitir conocer los caminos disponibles.



## Uri's dispobibles


+ /user
+ /travels
+ /position
+ /drivers
+ /path
