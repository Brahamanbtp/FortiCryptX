import hashlib
import time
import json
import os

BLOCKCHAIN_FILE = "/content/FortiCryptX-Colab/audit_logger/blockchain.json"

def compute_block_hash(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

def get_last_block():
    if not os.path.exists(BLOCKCHAIN_FILE) or os.stat(BLOCKCHAIN_FILE).st_size == 0:
        return None
    with open(BLOCKCHAIN_FILE, "r") as f:
        chain = json.load(f)
        return chain[-1]

def create_block(event_type, data):
    previous_block = get_last_block()
    previous_hash = compute_block_hash(previous_block) if previous_block else "0" * 64
    block = {
        "timestamp": time.time(),
        "event_type": event_type,
        "data": data,
        "previous_hash": previous_hash
    }
    block["hash"] = compute_block_hash(block)
    return block

def add_block_to_chain(event_type, data):
    block = create_block(event_type, data)
    if not os.path.exists(BLOCKCHAIN_FILE):
        chain = []
    else:
        with open(BLOCKCHAIN_FILE, "r") as f:
            try:
                chain = json.load(f)
            except json.JSONDecodeError:
                chain = []
    chain.append(block)
    with open(BLOCKCHAIN_FILE, "w") as f:
        json.dump(chain, f, indent=2)
