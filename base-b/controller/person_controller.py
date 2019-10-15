from flask import request, jsonify, Blueprint

from database.connection import Connection
from exception.invalid_request import InvalidRequest
from repository.person_repository import PersonRepository
from repository.property_repository import PropertyRepository
from schemas.person_schema import PersonSchema

person_api = Blueprint('person_api', __name__)


@person_api.route("/person", methods=["POST"])
def add_person():
    with Connection().session() as session:
        new_person = PersonSchema().load(request.get_json(), session=session)
        PersonRepository(session).insert(new_person)
        session.commit()

        return jsonify(PersonSchema().dump(new_person))


@person_api.route("/person", methods=["GET"])
def get_all_person():
    with Connection().session() as session:
        all_person = PersonRepository(session).get_all()

        return jsonify(PersonSchema(many=True).dump(all_person))


@person_api.route("/person/<id>", methods=["GET"])
def get_id_person(id):
    with Connection().session() as session:
        id_person = PersonRepository(session).get_id(id)
        if id_person:
            return jsonify(PersonSchema().dump(id_person))
        else:
            raise InvalidRequest('Person not found', 404)


@person_api.route("/person/<id>", methods=["DELETE"])
def delete_id_person(id):
    with Connection().session() as session:
        property_person = PropertyRepository(session).get_property_by_person_id(id)
        if property_person:
            raise InvalidRequest('This person has property.')

        id_person = PersonRepository(session).delete_id(id)
        return jsonify(PersonSchema().dump(id_person))


@person_api.route("/person/<id>", methods=["PUT"])
def update_id_person(id):
    with Connection().session() as session:
        update_person = request.get_json()
        update_person['id'] = id
        update_person = PersonSchema().load(update_person, session=session)

        update_person = PersonRepository(session).update(update_person)

        return jsonify(PersonSchema().dump(update_person))


@person_api.route("/person/<id>", methods=["PATCH"])
def patch_id_person(id):
    name = request.json['name']
    birth = request.json['birth']
    document = request.json['document']
    wage = request.json['wage']
    address = request.json['address']

    with Connection().session() as session:
        id_person = PersonRepository(session).patch_id(id, name, birth, document, wage, address)

        return jsonify(PersonSchema().dump(id_person))
