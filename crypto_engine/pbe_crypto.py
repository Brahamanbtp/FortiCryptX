import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def derive_key_pbkdf2(password: str, salt: bytes = None, iterations: int = 100_000):
    if salt is None:
        salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )

    key = kdf.derive(password.encode())
    return key, salt

def verify_key_pbkdf2(password: str, salt: bytes, key: bytes, iterations: int = 100_000):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    try:
        kdf.verify(password.encode(), key)
        return True
    except Exception:
        return False
