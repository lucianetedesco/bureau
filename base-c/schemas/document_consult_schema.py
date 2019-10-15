from dateutil.parser import parse
from marshmallow import Schema, fields

from core.cryptography import Cryptography


class DocumentConsult(Schema):
    id = fields.UUID()
    document = fields.Str(required=True)
    company = fields.Str(required=True)
    consult_date = fields.Date(required=True)

    def __init__(self):
        super().__init__()
        self.cryp = Cryptography()

    def to_database(self, doc):
        doc['document'] = self.cryp.encrypt(doc['document'])
        doc['company'] = self.cryp.encrypt(doc['company'])
        return doc

    def from_database(self, doc):
        doc['document'] = self.cryp.decrypt(doc['document'])
        doc['company'] = self.cryp.decrypt(doc['company'])
        doc['consult_date'] = parse(doc['consult_date']).date()
        return doc
