from flask import Flask, jsonify

from controller.document_acquisition_controller import document_acquisition_api
from controller.document_consult_controller import document_consult_api
from controller.document_movement_controller import document_movement_api
from exception.invalid_request import InvalidRequest

app = Flask(__name__)


@app.errorhandler(InvalidRequest)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


app.register_blueprint(document_consult_api)
app.register_blueprint(document_movement_api)
app.register_blueprint(document_acquisition_api)

app.run(debug=True)
