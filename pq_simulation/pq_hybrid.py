import os
import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asympadding
from cryptography.hazmat.primitives import hashes

# Simulated PQ encryption (mocked with XOR and base64)
def pq_encrypt(message, pq_key):
    return base64.b64encode(bytes([b ^ pq_key[i % len(pq_key)] for i, b in enumerate(message)]))

def pq_decrypt(ciphertext, pq_key):
    data = base64.b64decode(ciphertext)
    return bytes([b ^ pq_key[i % len(pq_key)] for i, b in enumerate(data)])

def hybrid_encrypt(message, rsa_public_key, pq_key):
    rsa_encrypted = rsa_public_key.encrypt(
        message,
        asympadding.OAEP(
            mgf=asympadding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    pq_encrypted = pq_encrypt(rsa_encrypted, pq_key)
    return pq_encrypted

def hybrid_decrypt(ciphertext, rsa_private_key, pq_key):
    rsa_encrypted = pq_decrypt(ciphertext, pq_key)
    decrypted = rsa_private_key.decrypt(
        rsa_encrypted,
        asympadding.OAEP(
            mgf=asympadding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted
