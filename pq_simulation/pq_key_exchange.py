import os
import hashlib

# Simulate Kyber-style key encapsulation (using shared random keys)
def generate_pq_keys():
    private_key = os.urandom(32)
    public_key = hashlib.sha256(private_key).digest()
    return public_key, private_key

def encapsulate_key(public_key):
    shared_secret = os.urandom(32)
    encrypted_secret = bytes([b ^ public_key[i % len(public_key)] for i, b in enumerate(shared_secret)])
    return shared_secret, encrypted_secret

def decapsulate_key(encrypted_secret, private_key):
    public_key = hashlib.sha256(private_key).digest()
    shared_secret = bytes([b ^ public_key[i % len(public_key)] for i, b in enumerate(encrypted_secret)])
    return shared_secret
