from marshmallow_sqlalchemy import ModelSchema

from model.property_model import Property


class PropertySchema(ModelSchema):
    class Meta:
        model = Property
