import time
import random

def benchmark_symmetric():
    start = time.time()
    _ = [random.getrandbits(128) for _ in range(100000)]
    return time.time() - start

def benchmark_rsa():
    time.sleep(0.3)  # Simulated delay
    return 0.3

def benchmark_pq():
    time.sleep(0.5)  # Simulated PQ algorithm latency
    return 0.5

def run_threat_comparison():
    symmetric = benchmark_symmetric()
    rsa = benchmark_rsa()
    pq = benchmark_pq()

    print("🔐 Threat Model Benchmark:")
    print(f"Symmetric (AES-like) Ops Time: {symmetric:.4f}s")
    print(f"Traditional RSA Ops Time    : {rsa:.4f}s")
    print(f"Post-Quantum (PQ Sim) Time  : {pq:.4f}s")

    print("\n📉 Relative Resistance Summary:")
    print(" - RSA: Vulnerable to Shor’s Algorithm (Quantum threat)")
    print(" - PQ (Kyber/Dilithium): Resistant to known quantum attacks")
    print(" - AES: Key-length based resistance; 256-bit recommended")

if __name__ == "__main__":
    run_threat_comparison()
