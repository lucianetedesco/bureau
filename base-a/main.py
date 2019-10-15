from flask import Flask, jsonify

from controller.debts_controller import debts_api
from controller.person_controller import person_api
from exception.invalid_request import InvalidRequest

app = Flask(__name__)


@app.errorhandler(InvalidRequest)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


app.register_blueprint(person_api)
app.register_blueprint(debts_api)

app.run(debug=True)
