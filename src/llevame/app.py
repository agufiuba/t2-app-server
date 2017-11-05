from flask import Flask
from user.user_controller import user_controller
from travels.travels_controller import travels_controller
from position.position_controller import position_controller
from drivers.drivers_controller import drivers_controller_constructor
from drivers.drivers_service import DriversService
from path.path_controller import path_controller
from login.login_controller import login_controller
import os

def build_app(mongo_uri = None, db = "t2"):
    if (mongo_uri == None):
        mongo_uri = "mongodb://" + os.environ['MONGO_URI']

    app = Flask(__name__)

    app.register_blueprint(user_controller);
    app.register_blueprint(path_controller);
    driver_service = DriversService(mongo_uri, db);
    app.register_blueprint(drivers_controller_constructor(driver_service));
    app.register_blueprint(travels_controller);
    app.register_blueprint(position_controller);
    app.register_blueprint(login_controller);

    return app

# La URL de mongodb se le pasa por la variable de entorno MONGO_URI.
app = build_app()

if __name__ == "__main__":
    app.run()
