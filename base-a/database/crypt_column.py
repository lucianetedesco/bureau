from sqlalchemy.types import TypeDecorator, String

from core.cryptography import Cryptography


class CryptColumn(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        if value:
            return Cryptography().encrypt(value)
        return None

    def process_result_value(self, value, dialect):
        if value:
            if isinstance(value, (bytes, bytearray)):
                value = value.decode()
            return Cryptography().decrypt(value)
        return None
