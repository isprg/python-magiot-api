from flask import Flask, jsonify

from .devices import devices
from .users import users

app = Flask(__name__)
app.url_map.strict_slashes = False

# add blueprint
app.register_blueprint(devices)
app.register_blueprint(users)

# error hundler


@app.errorhandler(400)
@app.errorhandler(403)
@app.errorhandler(404)
def error_handler(error):
    return jsonify({'error': {
        'code': error.description['code'],
        'message': error.description['message']
    }}), error.code
