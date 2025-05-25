import os
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def ecies_encrypt(public_key, data):
    ephemeral_key = ec.generate_private_key(ec.SECP384R1())
    shared_secret = ephemeral_key.exchange(ec.ECDH(), public_key)

    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"ecies"
    ).derive(shared_secret)

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    padding_len = 16 - len(data) % 16
    data += bytes([padding_len]) * padding_len
    ciphertext = encryptor.update(data) + encryptor.finalize()

    return ephemeral_key.public_key(), iv, ciphertext

def ecies_decrypt(private_key, peer_public_key, iv, ciphertext):
    shared_secret = private_key.exchange(ec.ECDH(), peer_public_key)

    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"ecies"
    ).derive(shared_secret)

    cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    padding_len = padded_data[-1]
    return padded_data[:-padding_len]
