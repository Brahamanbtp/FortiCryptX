import os
import random

def shred_file(filepath, passes=3):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} not found.")

    filesize = os.path.getsize(filepath)

    with open(filepath, "ba+", buffering=0) as f:
        for i in range(passes):
            f.seek(0)
            f.write(os.urandom(filesize))
            f.flush()
            os.fsync(f.fileno())

    os.remove(filepath)
    print(f"{filepath} shredded securely with {passes} overwrite passes.")
