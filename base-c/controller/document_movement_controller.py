from flask import request, jsonify, Blueprint
from marshmallow import ValidationError

from database.elasticsearch_client import ElasticsearchClient
from exception.invalid_request import InvalidRequest
from schemas.document_movement import DocumentMovement

document_movement_api = Blueprint('document_movement_api', __name__)
document = DocumentMovement()
index = 'document_movement'


@document_movement_api.route("/document/movement", methods=["POST"])
def add_movement():
    try:
        new_movement = document.load(request.get_json())
    except ValidationError as err:
        raise InvalidRequest(err.messages)

    id = ElasticsearchClient().insert(index, document.to_database(new_movement))
    new_movement['id'] = id

    return jsonify(document.dump(document.from_database(new_movement)))


@document_movement_api.route("/document/movement/<id>", methods=["GET"])
def get_movement_by_id(id):
    id_movement = ElasticsearchClient().get_id(index, id)
    if id_movement:
        return jsonify(document.dump(document.from_database(id_movement['_source'])))
    else:
        raise InvalidRequest('Movement not found', 404)


@document_movement_api.route("/document/movement", methods=["GET"])
def get_all_movements():
    movements = ElasticsearchClient().get_all(index)
    result = list()
    for hit in movements:
        result.append(document.dump(document.from_database(hit['_source'])))

    return jsonify(result)
