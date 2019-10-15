from marshmallow import Schema, fields

from core.cryptography import Cryptography


class DocumentAcquisition(Schema):
    id = fields.UUID()
    document = fields.Str(required=True)
    value = fields.Float(required=True)
    store = fields.Str(required=True)

    def __init__(self):
        super().__init__()
        self.cryp = Cryptography()

    def to_database(self, doc):
        doc['document'] = self.cryp.encrypt(doc['document'])
        doc['store'] = self.cryp.encrypt(doc['store'])

        return doc

    def from_database(self, doc):
        doc['document'] = self.cryp.decrypt(doc['document'])
        doc['store'] = self.cryp.decrypt(doc['store'])
        return doc
