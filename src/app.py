from flask import Flask
from .main.user.user_controller import user_controller
from .main.travels.travels_controller import travels_controller
from .main.position.position_controller import position_controller
from .main.drivers.drivers_controller import drivers_controller
from .main.path.path_controller import path_controller

app = Flask(__name__)

app.register_blueprint(user_controller);
app.register_blueprint(path_controller);
app.register_blueprint(drivers_controller);
app.register_blueprint(travels_controller);
app.register_blueprint(position_controller);


if __name__ == "__main__":
    app.run()
