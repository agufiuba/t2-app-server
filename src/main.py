from flask import Flask
from .user.user_controller import user_controller
from .travels.travels_controller import travels_controller
from .position.position_controller import position_controller
from .drivers.drivers_controller import drivers_controller
from .path.path_controller import path_controller


app = Flask(__name__)

app.register_blueprint(user_controller);
app.register_blueprint(path_controller);
app.register_blueprint(drivers_controller);
app.register_blueprint(travels_controller);
app.register_blueprint(position_controller);

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
