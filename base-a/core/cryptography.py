import base64

import singletons
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

from core import config


@singletons.GlobalFactory
class Cryptography:

    def __init__(self):
        self.key = bytes.fromhex(config.KEY)
        self.iv = bytes.fromhex(config.IV)

    def encrypt(self, plaintext):
        encryptor = Cipher(
            algorithms.AES(self.key),
            modes.GCM(self.iv),
            backend=default_backend()
        ).encryptor()
        ciphertext = encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize()

        ciphertext_encoded = base64.b64encode(ciphertext).decode('ascii').strip()
        tag = base64.b64encode(encryptor.tag).decode('ascii').strip()
        return "%s$%s" % (tag, ciphertext_encoded)

    def decrypt(self, ciphertext):
        if not ciphertext:
            return ciphertext
        tag, ciphertext_encoded = ciphertext.split('$', 1)
        tag = base64.b64decode(tag)
        ciphertext_encoded = base64.b64decode(ciphertext_encoded)

        decryptor = Cipher(
            algorithms.AES(self.key),
            modes.GCM(self.iv, tag),
            backend=default_backend()
        ).decryptor()

        return (decryptor.update(ciphertext_encoded) + decryptor.finalize()).decode()
