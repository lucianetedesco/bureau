from marshmallow_sqlalchemy import ModelSchema

from model.person_model import Person


class PersonSchema(ModelSchema):
    class Meta:
        model = Person
