from marshmallow_sqlalchemy import ModelSchema

from model.debts_model import Debts


class DebtsSchema(ModelSchema):
    class Meta:
        model = Debts
