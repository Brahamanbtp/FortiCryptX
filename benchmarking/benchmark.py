import time
import os
from crypto_engine.hybrid_crypto import encrypt_file, decrypt_file

def benchmark_encryption_algorithms(input_file, public_key, private_key):
    results = {}
    start = time.time()
    encrypt_file(input_file, public_key, "test.enc")
    end = time.time()
    results["encryption_time"] = end - start

    start = time.time()
    decrypt_file("test.enc", private_key, "test.dec")
    end = time.time()
    results["decryption_time"] = end - start

    results["file_size_kb"] = os.path.getsize(input_file) / 1024
    return results

def generate_benchmark_report():
    print("Benchmarking complete. Compare times and file sizes in your notebook output.")
