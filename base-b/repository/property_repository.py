from core.redis_wrapper import cache
from model.property_model import Property


class PropertyRepository:

    def __init__(self, session):
        self._session = session

    def insert(self, property: Property):
        self._session.add(property)

    @cache()
    def get_id(self, id):
        return self._session.query(Property).get(id)

    @cache()
    def get_all(self):
        return self._session.query(Property).all()

    def update(self, update_property):
        self._session.add(update_property)

    def patch_id(self, id, value, description, person_id):
        update_property = self._session.query(Property).get(id)
        if value:
            update_property.value = value
        if description:
            update_property.description = description
        if person_id:
            update_property.person_id = person_id
        self._session.add(update_property)

    def delete_id(self, id):
        property_delete = self._session.query(Property).get(id)
        self._session.delete(property_delete)

    def get_property_by_person_id(self, id):
        return self._session.query(Property).filter(Property.person_id == id).all
