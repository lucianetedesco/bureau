from flask import request, jsonify, Blueprint

from database.connection import Connection
from repository.property_repository import PropertyRepository
from schemas.property_schema import PropertySchema

property_api = Blueprint('property_api', __name__)


@property_api.route("/property", methods=["POST"])
def add_property():
    with Connection().session() as session:
        new_property = PropertySchema().load(request.get_json(), session=session)
        PropertyRepository(session).insert(new_property)
        session.commit()

        return jsonify(PropertySchema().dump(new_property))


@property_api.route("/property", methods=["GET"])
def get_all_propertys():
    with Connection().session() as session:
        all_propertys = PropertyRepository(session).get_all()

        return jsonify(PropertySchema(many=True).dump(all_propertys))


@property_api.route("/property/<id>", methods=["GET"])
def get_id_property(id):
    with Connection().session() as session:
        property_id = PropertyRepository(session).get_id(id)

        return jsonify(PropertySchema().dump(property_id))


@property_api.route("/property/<id>", methods=["DELETE"])
def delete_id_property(id):
    with Connection().session() as session:
        property_id = PropertyRepository(session).delete_id(id)

        return jsonify(PropertySchema().dump(property_id))


@property_api.route("/property/<id>", methods=["PUT"])
def update_id_property(id):
    with Connection().session() as session:
        prop = request.get_json()
        prop['id'] = id
        property = PropertySchema().load(prop, session=session)
        property = PropertyRepository(session).update(property)

        return jsonify(PropertySchema().dump(property))


@property_api.route("/property/<id>", methods=["PATCH"])
def patch_id_property(id):
    value = request.json['value']
    description = request.json['description']
    person_id = request.json['person_id']

    with Connection().session() as session:
        property_id = PropertyRepository(session).patch_id(id, value, description, person_id)

        return jsonify(PropertySchema().dump(property_id))
