[![Build Status](https://travis-ci.org/agufiuba/t2-app-server.svg?branch=master)](https://travis-ci.org/agufiuba/t2-app-server)
[![Coverage Status](https://coveralls.io/repos/github/agufiuba/t2-app-server/badge.svg?branch=master)](https://coveralls.io/github/agufiuba/t2-app-server?branch=master)

# t2-app-server

App Server para Taller de Programación II (7552 - FIUBA). Existe una versión desplegada en heroku (`http://t2-appserver.herokuapp.com`), pero en este repositorio se encuentran todas las herramientas necesarias para ejecutarlo localmente utilizando Docker.

## Prerrequisitos

-   Instalación de [Docker](https://docs.docker.com/engine/installation/).
-   Instalación de [Docker Compose](https://docs.docker.com/compose/install/).
-   Instalación de [Shared Server](https://github.com/agufiuba/t2-shared-server). Además, para la correcta ejecución de este servidor, el Shared Server debe estar levanado en Docker.
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

### Servicio de usuarios (`/user`)

Este se encarga todo respecto al usuario, registro, etc.

#### Registrar Usuario

+   URL: `http://app_uri:port/user/`

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

+   Response: `200` si fue exitoso el registro, `400` si hubo algún problema.

#### Actualizar información usuario

+   URL: `http://app_uri:port/user/`

+   Verbo REST: PUT

+   Body:

    ```
    {
      email: 'julano.casandro@gmail',
      [name: 'xxxxx'],
      [last_name: 'xxxxx'],
      [email: 'xxxx'],
      [...]
    }
    ```

    Se utiliza el mail como identificador. El resto de los campos serán los que se quieran actualizar. Son opcionales y son los mismos que al efectuar el registro.

+   Response: `200` si fue exitoso el registro, `400` si hubo algún problema.


#### Ver información de Usuario

+   URL: `http://app_uri:port/user/{id_user}`

+   Verbo REST: GET

+   Body:
    ```
    {}
    ```

+   Response: `200` con los datos de usuario si es encontrado, `400` si hubo un problema o el usuario no está registrado. Ejemplo para un pasajero:

    ```
    {
        "id": 1,
        "name": "Armando",
        "last_name": "Gales",
        "mail": "agales@gmail.com",
        "type": "passenger",
        "saldo": "2500.0"
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

### Servicio de login (`/login`)

#### Loguear un usuario

+   URL: `http://app_uri/login`

+   Verbo REST: POST

+   Header:

    ```
    {
      'Authorization':'xxxxxxx',
      'Session': 'xxxxx',
      'Content-Type':'application/json'
    }
    ```

    Es importante notar que se envía, además del token de Firebase en Authorization, el SessionID (también de Firebase), que será utilizado más adelante para enviar mensajes particulares por FCM.

+   Response: `200` en caso de éxito, `400` en caso de que el usuario no esté registrado en el Shared Server.

### Servicio de viajes (`/trips`)

#### Agregar un viaje que se va a realizar

Además de agregarlo notifica al chofer mediante el sistema de notificaciones de Firebase (FCM) con los datos del viaje.

+   URL: `http://app_uri/trips`
+   Verbo REST: POST
+   Header:

    ```
    {
      'Authorization':'xxxxxxx',
      'Content-Type':'application/json'
    }
    ```

+   Body:
    ```
    {
      'driverID':'xxxx',
      'from': 'lat/lng: (-34.6220855,-58.3832781)',
    	'to': 'lat/lng: (-35.6220855,-58.3832781)',
      'paymentMethod': ['cash', 'card']
    }
    ```

Advertencia: en plataformas como android el campo `from` y el `to` deben escribir el espacio entre el ":" y el "(" como un "%20".

+   Response: `200` si el viaje se agregó correctamente, `400` si hubo un error al tratar de agregarlo o si hubo un error de autenticación.

#### Avisar que el chofer esta viajando

+   URL: `http://app_uri/trips/driverTraveling`
+   Verbo REST: PUT
+   Header :

    ```
    {
      'Authorization':'xxxxxxx',
      'Content-Type':'application/json'
    }
    ```

+   Response: `200` en caso de éxito. `400` si hubo error de autenticación.

    ```
    {'message':'Se actualizo el estado del vieje'}
    ```

+   Notificaciones:
    Le envía por FCM los Session ID del chofer al pasajero y del pasajero al chofer para que puedan interactuar, por ejemplo, con el chat.

    La notificacion tiene como "data" el siguiente formato:

    ```
    {'sessionIDs': [session_id_1, session_id_2, session_id_3]}
    ```

### Servicio de choferes (`/driver`)

#### Obtener los choferes disponibles.

+   URL: `/drivers?pos=lat/lng: (-34.6220855,-58.3832781)`. Se mantiene la recomendación de agregar `%20` en lugar de espacio para plataformas como Android.

+   Verbo REST: GET

+   Header:

    ```
    {
      'Authorization':'xxxxxxx',
      'Content-Type':'application/json'
    }
    ```

+   Response: en caso de éxito, código `200` y la lista de los id de los drivers cercanos al pasajero. De estos en particular se obtiene el ID y la posición (en formato "lat;long"):

    ```
    {
      'drivers': [
        {'id': id1, 'pos': lat;long},
        {'id': id2, 'pos': lat;long},
        {'id': id3, 'pos': 34;50}
      ]
    }
    ```

    En caso de falla (request inválido o error de autenticación), se devuelve un `400`.

#### Agregar un chofer disponible.

+   URL: `http://app_uri/drivers`
+   Verbo REST: POST
+   Header:

    ```
    {
      'Authorization':'xxxxxxx',
      'Content-Type':'application/json'
    }
    ```

+   Response: `200`

    ```
    {'message': 'Se agrego de manera correcta al chofer de xxxx'}
    ```

<!-- ### Servicio de posicionamiento

Corrobar que está realizando el viaje, y la distancia y tiempo de manera exacta. -->

### Servicio de viajes disponibles (`/availableTrip`)

#### Agregar un viaje nuevo

Se obtienen los datos de un viaje nuevo dados el origen y el destino.

+   URL: `http://app_uri:port/availableTrip`

+   Verbo REST: PUT

+   Headers:

    ```
    {
      'Authorization':'xxxxxxx',
      'Content-Type':'application/json'
    }
    ```

+   Body:

    ```
      {
        'from': '-34.617952,-58.385983',
        'to': '-34.617952,-58.385983',
      }
    ```


+   Response:

    En caso de que el usuario no exista se devuelve un `400` con el siguiente body:

    ```
    { message: 'El usuario no existe'. }
    ```

    En caso de que el usuario exista, un `200` con:

    ```
    {
      'cost':'xxx',
      'distance':'xxx km'
      'points':'xxxxxxxxxxxxxxxxxxxx',
      'time':'x hours x mins'
    }
    ```

<!--
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
    ``` -->

### Servicio de Parámetros

Se utiliza para obtener los valores posibles para elegir sobre los parámetros de un auto.

+   URL's:

    +   `http://app_uri/parameters/car/state`
    +   `http://app_uri/parameters/car/music`
    +   `http://app_uri/parameters/car/model`
    +   `http://app_uri/parameters/car/colour`
    +   `http://app_uri/parameters/car/air_conditioner`

+   Verbo REST: GET

+   Response: `200` y los datos pedidos. Ejemplo para "model":

    ```
    {
      'parameters': [
        'Ford Fiesta',
        'Chevrolet S10',
        'Toyota Hilux',
        'Fiat Palio',
        'Renault Scenic'
      ]
    }
    ```

## Tests

Para ejecutar las pruebas automatizadas de forma local, debe primero levantarse el servidor en docker, y luego ejecutarse:

```
docker-compose exec -ti t2appserver_app-server_1 sh /as/src/test.sh
```
