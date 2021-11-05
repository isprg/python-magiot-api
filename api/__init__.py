from flask import Flask

from .devices import devices
from .users import users

app = Flask(__name__)
app.url_map.strict_slashes = False

# add blueprint
app.register_blueprint(devices)
app.register_blueprint(users)
