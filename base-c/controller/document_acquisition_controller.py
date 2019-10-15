from flask import request, jsonify, Blueprint
from marshmallow import ValidationError

from database.elasticsearch_client import ElasticsearchClient
from exception.invalid_request import InvalidRequest
from schemas.document_acquisition import DocumentAcquisition

document_acquisition_api = Blueprint('document_acquisition_api', __name__)
document = DocumentAcquisition()
index = 'document_acquisition'


@document_acquisition_api.route("/document/acquisition", methods=["POST"])
def add_acquisition():
    try:
        new_acquisition = document.load(request.get_json())
    except ValidationError as err:
        raise InvalidRequest(err.messages)

    id = ElasticsearchClient().insert(index, document.to_database(new_acquisition))
    new_acquisition['id'] = id

    return jsonify(document.dump(document.from_database(new_acquisition)))


@document_acquisition_api.route("/document/acquisition/<id>", methods=["GET"])
def get_acquisition_by_id(id):
    id_acquisition = ElasticsearchClient().get_id(index, id)
    if id_acquisition:
        return jsonify(document.dump(document.from_database(id_acquisition['_source'])))
    else:
        raise InvalidRequest('Aquisition not found', 404)


@document_acquisition_api.route("/document/acquisition", methods=["GET"])
def get_all_acquisitions():
    acquisitions = ElasticsearchClient().get_all(index)
    result = list()
    for hit in acquisitions:
        result.append(document.dump(document.from_database(hit['_source'])))

    return jsonify(result)
