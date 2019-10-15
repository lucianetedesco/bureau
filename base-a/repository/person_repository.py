from model.person_model import Person


class PersonRepository:

    def __init__(self, session):
        self._session = session

    def insert(self, person: Person):
        self._session.add(person)

    def get_id(self, id):
        return self._session.query(Person).get(id)

    def get_all(self):
        return self._session.query(Person).all()

    def update(self, update_person):
        self._session.add(update_person)

    def patch_id(self, id, name, document, address):
        update_person = self._session.query(Person).get(id)
        if name:
            update_person.name = name
        if document:
            update_person.document = document
        if address:
            update_person.address = address
        self._session.add(update_person)

    def delete_id(self, id):
        person_delete = self._session.query(Person).get(id)
        self._session.delete(person_delete)
