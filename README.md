[![Build Status](https://travis-ci.org/agufiuba/t2-app-server.svg?branch=master)](https://travis-ci.org/agufiuba/t2-app-server)
[![Coverage Status](https://coveralls.io/repos/github/agufiuba/t2-app-server/badge.svg?branch=master)](https://coveralls.io/github/agufiuba/t2-app-server?branch=master)

# t2-app-server

App Server para Taller de Programación II (7552 - FIUBA). Existe una versión desplegada en heroku (`http://t2-appserver.herokuapp.com`), pero en este repositorio se encuentran todas las herramientas necesarias para ejecutarlo localmente utilizando Docker.

## Prerrequisitos

-   Instalación de [Docker](https://docs.docker.com/engine/installation/).
-   Este documento describe el uso en consolas estilo bash o zsh (típicamente encontradas en linux o mac). No ha sido probado en Windows.

## Instalación

1.  Descargar este repositorio.

    ```bash
    git clone https://github.com/agufiuba/t2-app-server
    ```

2.  La aplicación requiere que exista una red de docker llamada "ubernet". Si esta no está creada (verificable con `docker network ls`) debe ejecutarse:

    ```
    docker network create ubernet
    ```

3.  Luego, si no se desean configuraciones adicionales, para construir la aplicación se utiliza:

    ```
    docker-compose build
    ```

## Configuración

Las variables obligatorias a las que no se les de valor toman sus valores por defecto, especificados en el archivo `.env`.

La única configuración obligatoria en el App Server es la variable de entorno `PORT`, que explicita el puerto al cual se ligará el servidor cuando sea levantado. Su valor por defecto es `3000`.

Por ejemplo, si se ejecuta `export PORT=5000` luego se accederá a la API a través de `localhost:5000`. Si la aplicación se usa en simultáneo con el [Shared Server](https://github.com/agufiuba/t2-shared-server) deben estar ligados a puertos distintos.

<!-- TODO agregar variables no obligatorias  -->

## Ejecución

Finalmente, para levantar el servidor:

```
docker-compose up
```

## Servicios disponibles

_Nota sobre las direcciones:_ la dirección base (de ahora en adelante `app_uri`) dependerá de si se accede a un App Server local en Docker o al desplegado en heroku, así como desde dónde se accede.

-   **Docker**:
    -   Para android, `<ip_pc>:<PORT>` donde `<ip_pc>` es la dirección IP de la computadora ejecutando el container del App Server en la red local.
    -   Si se accede desde otro container en Docker en la Ubernet, como un Shared Server, se puede utilizar la dirección `app-server:<PORT>`, ya que Docker resuelve las ips de sus servicios con sus nombres.
-   **Heroku**: `t2-appserver.herokuapp.com`.

El valor por defecto de `PORT`, como es explicado más arriba, es 3000.

### Servicio de usuarios (`/user` y `/driver`)

Este se encarga todo respecto al usuario, registro, etc.

#### Registrar Usuario

+   Verbo REST: POST

+   Body:

    _Para Choferes_

    ```
    {
      type: 'driver'
      name: 'xxxxx',
      last_name: 'xxxxx',
      email: 'xxxx',
      car: {
        model: 'xxxx',
        color: 'xxxx',
        patent: 'xxxxx',
        year: 'xxxxx',
        state: ['good','bad','maso'],
        air_conditioner:'hp',
        music: ['radio','album']
      }
    }
    ```

    _Para Pasajeros_

    ```
    {
      type: 'passenger'
      name: 'name',
      last_name: 'apellido',
      email: 'email',
      card: {
        'number':'xxx',
        'typeCard':'xxxxx',
        'securityCode':'xxxxxx',
        'expirationYear':'xxxxx',
        'expirationMonth':'xxxxxx'
      }
    }
    ```

+   URL: `http://app_uri:port/user/`

#### Actualizar información usuario

+   Verbo REST: PUT
+   Body:

    ```
    {
      email: 'julano.casandro@gmail',
      ...
      ....
    }
    ```

Los puntos suspensivos serian los datos que se quieren actualizar.
<!-- TODO Mejorar esto.  -->

+   URL: `http://app_uri:port/user/`

#### Ver información de Usuario

+   Verbo REST: GET
+   Body:
    ```
    {}
    ```
+   URL: `http://app_uri:port/user/{id_user}`


+   Respuesta si es un pasajero

    ```
    {
        type: 'passenger'
        name: 'name',
        last_name: 'apellido',
        email: 'email',
    }
    ```

#### Obtener información del auto de un usuario

+   URL: `http://app_uri:port/user/driver/<uid>`
+   verbo REST: GET

+   Respuesta:

    ```
    {
      "car": {
          "air_conditioner": "Sí",
          "color": "Azul",
          "model": "Toyota Hilux",
          "music": "Clasica",
          "patent": "12345678",
          "state": "Excelente",
          "year": "2010"
      }
    }
    ```

### Servicio de viajes (`/trips`)

#### Agregar un viaje que se va a realizar

+   URL: `/trips`
+   Verbo REST: POST
+   Header:

    ```
    {'Authorization':'xxxx'}
    ```

+   Body:
    ```
    {
      'driverID':'xxxx',
      'from':'xxxx',
      'to':'xxxxx'
    }
    ```

#### Avisar que el chofer esta viajando

+   URL: `/trips/driverTraveling`
+   Verbo REST: PUT
+   Header :

    ```
    {'Authorization':'xxxx'}
    ```

+   Response:

    ```
    {'message':'Se actualizo el estado del vieje'}
    ```

Cuando se realiza el request, se manda notificacion tanto al chofer como el pasajero, y en data se le manda el sessionList


La notificacion tiene como data el siguiente formato:
<!-- TODO verificar -->
    ```
    {'sessionIDs':[1,2,3,4,5]}
    ```

### Servicio de choferes

#### Obtener los choferes disponibles.

+   Verbo REST: GET
+   Header:

    ```
    {'Authorization':'xxxx'}
    ```

+   URL: /drivers?pos=lat/lng: (-34.6220855,-58.3832781)
+   Response: La lista de los id de los drivers cercanos al pasajero
    <!--  TODO verificar -->

    ```
    { 'drivers': [id1,id2,id3] }
    ```

#### Agregar un chofer disponible.

+   URL: `/drivers`
+   Verbo REST: POST
+   Header:

    ```
    {'Authorization':'xxxx'}
    ```

+   Response:

    ```
    {'message': 'Se agrego de manera correcta al chofer de xxxx'}
    ```

### Servicio de posicionamiento

Corrobar que está realizando el viaje, y la distancia y tiempo de manera exacta.

### Servicio de viajes disponibles

#### Agregar un viaje nuevo

+   Verbo REST: PUT
+   Body:
    <!-- TODO verificar -->
    ```
      {
        'Authorization':'xxxxxxx',
        'Content-Type':'application/json'
      }
      {
        'from': '-34.617952,-58.385983',
        'to': '-34.617952,-58.385983',
      }
    ```

+   URL: `http://app_uri:port/availableTrip`

+   Response:

    En caso de que el usuario no exista se devuelve un `400` con el siguiente body:

    ```
    {
      message: 'El usuario no existe'.
    }
    ```

    En caso de que el usuario exista

    ```
    {
      'cost':'xxx',
      'distance':'xxx km'
      'points':'xxxxxxxxxxxxxxxxxxxx',
      'time':'x hours x mins'
    }
    ```

+   Verbo REST: GET
+   Body:

    ```
    {}
    ```

+   Response:

    ```
    {
      'availableTrips': [
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
    ```

### Servicio de Direccionamiento

Se utilizará para permitir conocer los caminos disponibles.

### Servicio de parametros

Se utiliza para obtener los parametros posibles

URL's:
+   `http://localhost:3000/parameters/car/state`
+   `http://localhost:3000/parameters/car/music`
+   `http://localhost:3000/parameters/car/model`
+   `http://localhost:3000/parameters/car/colour`
+   `http://localhost:3000/parameters/car/air_conditioner`

Response:

    ```
    { parameters : [......] }
    ```

## Uri's disponibles

+   `/user`
+   `/travels`
+   `/position`
+   `/drivers`
+   `/path`
