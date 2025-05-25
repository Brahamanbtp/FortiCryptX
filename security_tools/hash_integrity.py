import hashlib
import os

def compute_sha256(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def verify_file_integrity(original_file, decrypted_file):
    return compute_sha256(original_file) == compute_sha256(decrypted_file)
