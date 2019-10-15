from marshmallow import Schema, fields

from core.cryptography import Cryptography


class DocumentMovement(Schema):
    id = fields.UUID()
    document = fields.Str(required=True)
    value = fields.Float(required=True)
    input_type = fields.String(required=True)

    def __init__(self):
        super().__init__()
        self.cryp = Cryptography()

    def to_database(self, doc):
        doc['document'] = self.cryp.encrypt(doc['document'])

        return doc

    def from_database(self, doc):
        doc['document'] = self.cryp.decrypt(doc['document'])
        return doc
