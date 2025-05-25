import os
import shutil

PERSIST_DIR = "/content/drive/MyDrive/FortiCryptX-Persist"

def save_file_session(local_path):
    if not os.path.exists(local_path):
        raise FileNotFoundError(f"{local_path} does not exist.")

    os.makedirs(PERSIST_DIR, exist_ok=True)
    filename = os.path.basename(local_path)
    destination = os.path.join(PERSIST_DIR, filename)
    shutil.copy2(local_path, destination)
    print(f"Persisted {filename} to Drive.")

def load_file_session(filename):
    filepath = os.path.join(PERSIST_DIR, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filename} not found in persistent storage.")

    local_copy = os.path.join("/content", filename)
    shutil.copy2(filepath, local_copy)
    print(f"Loaded {filename} from persistent storage.")
    return local_copy

def list_persisted_files():
    if not os.path.exists(PERSIST_DIR):
        return []

    return os.listdir(PERSIST_DIR)
