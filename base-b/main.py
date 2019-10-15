from flask import Flask, jsonify

from controller.person_controller import person_api
from controller.property_controller import property_api
from exception.invalid_request import InvalidRequest

app = Flask(__name__)


@app.errorhandler(InvalidRequest)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


app.register_blueprint(person_api)
app.register_blueprint(property_api)

app.run(debug=True)
