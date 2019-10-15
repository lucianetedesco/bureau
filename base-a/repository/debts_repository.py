from model.debts_model import Debts


class DebtsRepository:

    def __init__(self, session):
        self._session = session

    def insert(self, debts: Debts):
        self._session.add(debts)

    def get_id(self, id):
        return self._session.query(Debts).get(id)

    def get_all(self):
        return self._session.query(Debts).all()

    def update(self, update_debt):
        self._session.add(update_debt)

    def patch_id(self, id, value, description, person_id):
        update_debts = self._session.query(Debts).get(id)
        if value:
            update_debts.value = value
        if description:
            update_debts.description = description
        if person_id:
            update_debts.person_id = person_id
        self._session.add(update_debts)

    def delete_id(self, id):
        debts_delete = self._session.query(Debts).get(id)
        self._session.delete(debts_delete)

    def get_debts_by_person_id(self, id):
        return self._session.query(Debts).filter(Debts.person_id == id).all
