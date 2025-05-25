import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sympadding
from cryptography.hazmat.primitives.asymmetric import padding as asympadding
from cryptography.hazmat.primitives import hashes

def encrypt_file(file_path, public_key, output_path):
    aes_key = os.urandom(32)
    iv = os.urandom(16)

    with open(file_path, "rb") as f:
        data = f.read()

    padder = sympadding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_key = public_key.encrypt(
        aes_key,
        asympadding.OAEP(
            mgf=asympadding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(output_path, "wb") as f:
        f.write(len(encrypted_key).to_bytes(4, 'big'))
        f.write(encrypted_key)
        f.write(iv)
        f.write(encrypted_data)

def decrypt_file(enc_file_path, private_key, output_path):
    with open(enc_file_path, "rb") as f:
        key_len = int.from_bytes(f.read(4), 'big')
        encrypted_key = f.read(key_len)
        iv = f.read(16)
        encrypted_data = f.read()

    aes_key = private_key.decrypt(
        encrypted_key,
        asympadding.OAEP(
            mgf=asympadding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = sympadding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    with open(output_path, "wb") as f:
        f.write(data)
