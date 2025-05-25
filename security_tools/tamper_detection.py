import json
import os
from .hash_integrity import compute_sha256

def save_file_hash(filepath, hash_db_path="hashes.json"):
    file_hash = compute_sha256(filepath)
    hashes = {}

    if os.path.exists(hash_db_path):
        with open(hash_db_path, "r") as f:
            hashes = json.load(f)

    hashes[os.path.basename(filepath)] = file_hash

    with open(hash_db_path, "w") as f:
        json.dump(hashes, f, indent=2)

def verify_file_before_decryption(filepath, hash_db_path="hashes.json"):
    if not os.path.exists(hash_db_path):
        raise FileNotFoundError("Hash database not found.")

    with open(hash_db_path, "r") as f:
        hashes = json.load(f)

    filename = os.path.basename(filepath)
    if filename not in hashes:
        raise ValueError(f"No hash record found for {filename}.")

    current_hash = compute_sha256(filepath)
    expected_hash = hashes[filename]

    return current_hash == expected_hash
