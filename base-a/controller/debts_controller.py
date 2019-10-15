from flask import request, jsonify, Blueprint

from database.connection import Connection
from repository.debts_repository import DebtsRepository
from schemas.debts_schema import DebtsSchema

debts_api = Blueprint('debts_api', __name__)


@debts_api.route("/debts", methods=["POST"])
def add_debt():
    with Connection().session() as session:
        new_debt = DebtsSchema().load(request.get_json(), session=session)
        DebtsRepository(session).insert(new_debt)
        session.commit()

        return jsonify(DebtsSchema().dump(new_debt))


@debts_api.route("/debts", methods=["GET"])
def get_all_debts():
    with Connection().session() as session:
        all_debts = DebtsRepository(session).get_all()

        return jsonify(DebtsSchema(many=True).dump(all_debts))


@debts_api.route("/debts/<id>", methods=["GET"])
def get_id_debt(id):
    with Connection().session() as session:
        debt_id = DebtsRepository(session).get_id(id)

        return jsonify(DebtsSchema().dump(debt_id))


@debts_api.route("/debts/<id>", methods=["DELETE"])
def delete_id_debt(id):
    with Connection().session() as session:
        debt_id = DebtsRepository(session).delete_id(id)

        return jsonify(DebtsSchema().dump(debt_id))


@debts_api.route("/debts/<id>", methods=["PUT"])
def update_id_debt(id):
    with Connection().session() as session:
        debt = request.get_json()
        debt['id'] = id
        update_debt = DebtsSchema().load(debt, session=session)
        debt_id = DebtsRepository(session).update(update_debt)

        return jsonify(DebtsSchema().dump(debt_id))


@debts_api.route("/debts/<id>", methods=["PATCH"])
def patch_id_debt(id):
    value = request.json['value']
    description = request.json['description']
    person_id = request.json['person_id']

    with Connection().session() as session:
        debt_id = DebtsRepository(session).patch_id(id, value, description, person_id)

        return jsonify(DebtsSchema().dump(debt_id))
