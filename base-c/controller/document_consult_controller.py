from flask import request, jsonify, Blueprint
from marshmallow import ValidationError

from database.elasticsearch_client import ElasticsearchClient
from exception.invalid_request import InvalidRequest
from schemas.document_consult_schema import DocumentConsult

document_consult_api = Blueprint('document_consult_api', __name__)
document = DocumentConsult()
index = 'document_consult'


@document_consult_api.route("/document/consult", methods=["POST"])
def add_consult():
    try:
        new_consult = document.load(request.get_json())
    except ValidationError as err:
        raise InvalidRequest(err.messages)

    id = ElasticsearchClient().insert(index, document.to_database(new_consult))
    new_consult['id'] = id

    return jsonify(document.dump(document.from_database(new_consult)))


@document_consult_api.route("/document/consult/<id>", methods=["GET"])
def get_consult_by_id(id):
    id_consult = ElasticsearchClient().get_id(index, id)
    if id_consult:
        return jsonify(document.dump(document.from_database(id_consult['_source'])))
    else:
        raise InvalidRequest('Consult not found', 404)


@document_consult_api.route("/document/consult", methods=["GET"])
def get_all_consults():
    consults = ElasticsearchClient().get_all(index)
    result = list()
    for hit in consults:
        result.append(document.dump(document.from_database(hit['_source'])))

    return jsonify(result)
